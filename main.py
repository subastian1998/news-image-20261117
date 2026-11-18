#!/usr/bin/env python3
"""news-image-20261117 entry (Python 3.13, standard library only).

The image is the entry.png beside this file: a newspaper front page summing
up the world news of Tuesday 17 November 2026. The program copies it to
/output/entry.png. No network, no timestamps, no randomness, so both runs
write the same bytes.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil

# Source and destination are fixed paths; shutil.copyfile copies bytes only,
# so the output is identical on every run by construction.
HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
