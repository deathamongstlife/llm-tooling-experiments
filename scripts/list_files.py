#!/usr/bin/env python3
from pathlib import Path
base = Path(__file__).resolve().parent.parent
for p in sorted(base.rglob("*")):
    if p.is_file():
        print(p.relative_to(base))
