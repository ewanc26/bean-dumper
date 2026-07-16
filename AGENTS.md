# AGENTS.md

Guidance for agents working on Bean Dumper, an intentionally small, unmaintained Windows Python learning project.

## Scope

The implementation is the single `bean-windows.py` script. It downloads a configured file, discovers Windows drives, and copies to drives that already contain `beans.jpg`. `beans.jpg` is a sample asset.

## Safety rules

- Treat every filesystem write and overwrite as potentially destructive. Keep the existing opt-in filename check and make destination behavior obvious to the user.
- Never broaden the script into removable-drive propagation, background persistence, autorun behavior, or silent execution.
- Validate URLs, HTTP status, content length, destination paths, and free space. Use timeouts and close resources.
- Preserve the Windows-only guard; platform-specific drive discovery should remain isolated and mockable.
- Do not add real personal URLs, credentials, or user paths to the repository.

## Validation

Run syntax checks with `python -m py_compile bean-windows.py`. Test download and copy logic with mocks or disposable temporary directories/drives, including offline, partial-download, permission-denied, missing marker file, and existing destination cases. Do not run destructive copy tests against real removable media. The project is marked unmaintained, so avoid dependency churn or expansion beyond a requested maintenance fix.
