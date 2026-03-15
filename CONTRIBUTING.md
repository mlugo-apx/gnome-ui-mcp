# Contributing

## Local setup

```bash
sudo apt update
sudo apt install -y python3.12 python3.12-venv python3-gi gir1.2-atspi-2.0 gir1.2-gtk-3.0 gnome-screenshot
./scripts/bootstrap.sh
```

## Development loop

```bash
uv run --active gnome-ui-mcp
```

## Quality checks

```bash
./scripts/check.sh
```

## Pull requests

1. Create a focused branch.
2. Keep changes scoped and documented.
3. Update the README when the public MCP surface changes.
4. Run `./scripts/check.sh` before opening the PR.

## Releasing

1. Update `version` in `pyproject.toml`.
2. Run `./scripts/check.sh`.
3. Commit the release, for example:

```bash
git add pyproject.toml uv.lock
git commit -m "Release version 0.1.1"
```

4. Create an annotated tag that matches the package version:

```bash
git tag -a v0.1.1 -m "Release v0.1.1"
```

5. Push the branch and the tag:

```bash
git push origin main
git push origin v0.1.1
```

6. Optionally publish a GitHub Release for the same tag.

Pushing a `v*` tag triggers CI and publishes versioned GHCR image tags.
Pushing `main` updates the `latest` image tag.
