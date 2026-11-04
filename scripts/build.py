#!/usr/bin/env python3
"""Build an installable Plasma package and a source archive (Python stdlib only)."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
PACKAGE = ROOT / "package"
OUT = ROOT / "dist"


def write_zip(path, entries):
    with zipfile.ZipFile(path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for source, name in sorted(entries, key=lambda entry: entry[1]):
            info = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, source.read_bytes())
    with zipfile.ZipFile(path) as archive:
        assert archive.testzip() is None, "Corrupt ZIP archive"


def main():
    metadata = json.loads((PACKAGE / "metadata.json").read_text())
    assert metadata["KPackageStructure"] == "Plasma/Applet"
    version = metadata["KPlugin"]["Version"]
    assert re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", version), "Use a numeric x.y.z version"
    for name in ["contents/ui/main.qml", "contents/ui/DigitalClock.qml", "contents/ui/ClockFace.qml", "contents/config/main.xml", "contents/config/config.qml"]:
        assert (PACKAGE / name).is_file(), f"Missing {name}"
    ET.parse(PACKAGE / "contents/config/main.xml")
    OUT.mkdir(exist_ok=True)
    widget = OUT / f"paneltime-{version}.plasmoid"
    # License notices travel with the installable package as well as the sources.
    entries = [(f, f.relative_to(PACKAGE).as_posix()) for f in PACKAGE.rglob("*") if f.is_file()]
    entries += [(ROOT / "LICENSE", "LICENSE"), (ROOT / "UPSTREAM.md", "UPSTREAM.md")]
    entries += [(f, f.relative_to(ROOT).as_posix()) for f in (ROOT / "LICENSES").glob("*.txt")]
    write_zip(widget, entries)
    sources = OUT / f"paneltime-{version}-source.zip"
    source_entries = []
    for f in ROOT.rglob("*"):
        rel = f.relative_to(ROOT)
        if not f.is_file() or any(part in {".git", "dist", "__pycache__", ".idea", ".vscode"} for part in rel.parts) or f.suffix == ".pyc":
            continue
        source_entries.append((f, f"paneltime-{version}/" + rel.as_posix()))
    write_zip(sources, source_entries)
    checksum = OUT / "SHA256SUMS"
    checksum.write_text("".join(f"{hashlib.sha256(f.read_bytes()).hexdigest()}  {f.name}\n" for f in [widget, sources]))
    for f in [widget, sources, checksum]:
        print(f.relative_to(ROOT))


if __name__ == "__main__":
    main()
