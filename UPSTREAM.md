# Upstream provenance

Paneltime is derived from KDE Plasma Workspace's Digital Clock applet.

- Repository: https://github.com/KDE/plasma-workspace
- Commit: `6296a73f4e4a821d5419b5a243b58b1b6cf1f9c4`
- Source: https://github.com/KDE/plasma-workspace/tree/6296a73f4e4a821d5419b5a243b58b1b6cf1f9c4/applets/digital-clock

The QML and configuration files were downloaded from this pinned revision. They are not a clean-room implementation. Original copyright and SPDX license notices are retained. Texts for the declared licenses are included in `LICENSES/`; `LICENSE` is GPL-2.0-or-later.

## Local changes

- Separate installable QML widget package, displayed as Paneltime; historical ID `local.windows11.clock` retained for upgrades.
- `ClockFace.qml`: two compact lines, Noto Sans Regular at 15 px, optical right alignment using glyph bounds, theme-aware text.
- `DigitalClock.qml`: use the new face on horizontal panels with the date below the time; retain upstream interactions and alternate layouts.
- `main.qml`: request panel area filling.
- Default date position is below the time; locale formats and seconds preferences retain KDE defaults.
- Appearance page explains the Paneltime font preset; manual font weight and italic settings are forwarded to the face.
- Added documentation, preview renderer, reproducible package builder, and CI packaging.

No Microsoft fonts, Windows assets, or KDE compiled plugins are redistributed. Runtime clock/calendar plugins are provided by the user's Plasma installation. Interface translations depend on KDE's runtime environment; a separate Paneltime translation catalog is not shipped.
