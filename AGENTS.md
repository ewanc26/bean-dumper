# AGENTS.md

Guidance for agents working on Bean Dumper, an intentionally small, unmaintained Windows Python learning project.

## Scope and current behavior

The implementation is the single top-level `bean-windows.py` script. Despite the older README description, the current source does not download anything and does not check for an existing marker file: it resolves the bundled `beans.jpg` beside the script, enumerates every logical drive returned by `win32api.GetLogicalDriveStrings()`, and attempts to copy the image to `<drive>\beans.jpg`, overwriting an existing file through `shutil.copyfile`.

## Safety rules

- Treat every filesystem write and overwrite as potentially destructive. Before expanding or running the script, add or preserve an explicit opt-in/confirmation boundary; the current implementation has none.
- Never broaden the script into removable-drive propagation, background persistence, autorun behavior, or silent execution.
- Do not add the README's historical download behavior without an explicit request. If network download is reintroduced, validate the URL, status, size, and content separately from drive copying.
- Preserve the Windows-only guard; platform-specific drive discovery should remain isolated and mockable.
- Do not add real personal URLs, credentials, or user paths to the repository.

## Validation

Run syntax checks with `python -m py_compile bean-windows.py`. Because `win32api` is imported before the platform guard, behavioral tests require Windows or a mocked module. Mock drive enumeration and `shutil.copyfile`; cover non-Windows exit, empty drive strings, invalid drives, missing bundled image, permission errors, generic `OSError`, and an existing destination. Do not run copy tests against real drive roots. The project is marked unmaintained, so avoid dependency churn or expansion beyond a requested maintenance fix.
