#!/usr/bin/env python3
"""SnackTrack Pro — the worst app idea ever pitched.

Writes a single-sentence pitch (<= 240 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Stdlib only, deterministic, no trailing newline, mode 0644.
"""

import os
import tempfile

PITCH = (
    "SnackTrack Pro uses AI to tell you the exact second your leftovers "
    "become leftovers, so busy professionals never again wonder whether "
    "the sandwich they just made is technically a leftover yet."
)

# Gate: /output/entry.txt must be UTF-8 text of 1 to 240 characters.
assert 1 <= len(PITCH) <= 240, f"pitch is {len(PITCH)} characters"
assert PITCH == PITCH.strip(), "pitch must not start or end with whitespace"
assert "\n" not in PITCH, "pitch must be a single line"


def main() -> None:
    pitch = PITCH
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="") as f:
            f.write(pitch)
        os.chmod(tmp, 0o644)
        os.replace(tmp, target)
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise


if __name__ == "__main__":
    main()
