#!/usr/bin/env python3
"""Render the actual clock face. Requires PySide6 and Noto Sans."""
import os
os.environ.setdefault("QT_QPA_PLATFORM", "offscreen")
from pathlib import Path
from PySide6.QtCore import QTimer, QUrl
from PySide6.QtGui import QColor, QGuiApplication
from PySide6.QtQuick import QQuickView

root = Path(__file__).resolve().parents[1]
app = QGuiApplication([])
view = QQuickView()
view.setSource(QUrl.fromLocalFile(str(root / "package/contents/ui/ClockFace.qml")))
if view.errors():
    raise RuntimeError(view.errors())
view.setResizeMode(QQuickView.SizeRootObjectToView)
view.resize(120, 48)
view.setColor(QColor("#272333"))
face = view.rootObject()
face.setProperty("timeText", "9:10:02 PM")
face.setProperty("dateText", "10/11/2023")
face.setProperty("textColor", QColor("#eeeaf4"))
view.show()

def capture():
    image = view.grabWindow()
    target = root / "docs/preview.png"
    if not image.save(str(target)):
        raise RuntimeError("Could not save preview")
    # Validate the visible right edges of the two rendered lines.
    edges = []
    for start, end in [(0, 24), (24, 48)]:
        xs = [x for y in range(start, end) for x in range(image.width()) if image.pixelColor(x, y).red() > 100]
        if not xs:
            raise RuntimeError("A clock line is missing")
        edges.append(max(xs))
    print(f"Saved {target}; visible right edges: {edges}")
    if abs(edges[0] - edges[1]) > 1:
        raise RuntimeError("Clock lines are misaligned")
    app.quit()

QTimer.singleShot(500, capture)
app.exec()
