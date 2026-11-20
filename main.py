"""Round-2 entry for make.fun news-image-20261120.

Copies the bundled front-page image (entry.png, drawn in this session)
to the output directory, then verifies the copy by comparing the
SHA-256 hashes of source and destination, failing loudly on any
mismatch. Standard library only; no network, no randomness,
deterministic: the same bytes every run.
"""

import hashlib
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    if _sha256(src) != _sha256(dst):
        raise SystemExit("copy verification failed: entry.png mismatch")


if __name__ == "__main__":
    main()
