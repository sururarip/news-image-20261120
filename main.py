"""Round-2 entry for make.fun news-image-20261120.

Copies the bundled front-page image (entry.png, drawn in this session)
to the output directory. Standard library only; no network, no
randomness, deterministic: the same bytes every run.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    shutil.copyfile(
        os.path.join(HERE, "entry.png"),
        os.path.join(out_dir, "entry.png"),
    )


if __name__ == "__main__":
    main()
