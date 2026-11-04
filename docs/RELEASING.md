# Publishing Paneltime

## First GitHub upload

Create an empty public repository named `paneltime` in your GitHub account. Do not initialize it with a README or license: both are already present here. Then, from this project directory:

```sh
git init -b main
git add .
git commit -m "Prepare Paneltime 1.0.0"
git remote add origin https://github.com/YOUR_USERNAME/paneltime.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username. If you prefer the web interface, upload the source files and directories, including `.github/`, without `dist/`. Git is preferable because it preserves the full tree reliably.

Suggested repository description: `A compact Windows-inspired panel clock for KDE Plasma.`

Suggested topics: `kde`, `plasma6`, `plasmoid`, `qml`, `clock`, `linux`.

## Build and verify

```sh
python3 scripts/build.py
cd dist
sha256sum -c SHA256SUMS
```

The `.plasmoid` contains widget files and license notices. The source ZIP contains the full source tree and build scripts. `dist/` is intentionally ignored by Git: publish its contents as release attachments. GitHub Actions also builds these files for each push and pull request; workflow artifacts are not a public GitHub Release.

## Publish release 1.0.0

On GitHub open Releases → Draft a new release. Create tag `v1.0.0` from `main`, use the title **Paneltime 1.0.0**, and paste the matching changelog entry. Mention that Plasma 6.8.2 was tested and older versions are unverified. Attach:

- `dist/paneltime-1.0.0.plasmoid`
- `dist/paneltime-1.0.0-source.zip`
- `dist/SHA256SUMS`

Publish the release. Visitors can now download the `.plasmoid` directly and follow the README.

## Next release

Update `KPlugin.Version` in `package/metadata.json`, add a changelog entry, regenerate the preview if the design changes, and update example filenames in the READMEs. Build again and test installation from the `.plasmoid`, configuration, date rollover, seconds, calendar click, font settings, and the horizontal panel layout on the Plasma versions you intend to claim support for. Publish under a matching `vX.Y.Z` tag.

The historical plugin ID is intentionally stable. Changing it installs a separate widget and does not migrate panel entries or settings.
