#!/usr/bin/env python3
"""Join Layer 1 and a finished Layer 2 into one ready-to-paste tutor file.

Usage:
    python assemble_tutor.py --layer2 layer2.md --out my-tutor.md

Layer 1 is read from ../references/layer-1.md (next to this script's folder), so it is
always copied word for word instead of being retyped.
"""
import argparse
import sys
from pathlib import Path

LAYER1 = Path(__file__).resolve().parent.parent / "references" / "layer-1.md"


def strip_wrapping_fence(text: str) -> str:
    """Drop a ``` fence wrapped around the whole document, if present."""
    lines = text.strip().splitlines()
    if len(lines) >= 2 and lines[0].startswith("```") and lines[-1].strip() == "```":
        return "\n".join(lines[1:-1]).strip()
    return text.strip()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--layer2", required=True, help="Path to the finished Layer 2 markdown file")
    parser.add_argument("--out", required=True, help="Where to write the combined tutor file")
    args = parser.parse_args()

    if not LAYER1.exists():
        print(f"Layer 1 not found at {LAYER1}", file=sys.stderr)
        return 1

    layer2_path = Path(args.layer2)
    if not layer2_path.exists():
        print(f"Layer 2 file not found: {layer2_path}", file=sys.stderr)
        return 1

    layer1 = LAYER1.read_text(encoding="utf-8").strip()
    layer2 = strip_wrapping_fence(layer2_path.read_text(encoding="utf-8"))

    if not layer2.startswith("# LAYER TWO"):
        print("Warning: Layer 2 does not start with '# LAYER TWO: ...'. Check the template.", file=sys.stderr)

    combined = f"{layer1}\n\n---\n\n{layer2}\n"
    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(combined, encoding="utf-8")
    print(f"Wrote {out_path} ({len(combined):,} characters)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
