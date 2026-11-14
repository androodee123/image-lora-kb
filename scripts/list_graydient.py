#!/usr/bin/env python3
"""List EVERY Hugging Face repo under the account (models + datasets) and their files.
civit, civit2 and private are the Graydient source of truth; all other repos are flagged
"in HF repo <name>, not on Graydient".

Metadata only (paths, sizes, LFS sha256). NEVER downloads weights.
Uses huggingface_hub's default credential store silently; never prints or stores a token.
Writes data/raw/hf/{civit,civit2,private}.jsonl
"""
from __future__ import annotations
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "data" / "raw" / "hf"
GRAYDIENT_REPOS = ["Octavian123/civit", "Octavian123/civit2", "Octavian123/private"]
ACCOUNT = "Octavian123"


def main() -> int:
    from huggingface_hub import HfApi
    api = HfApi()
    OUT.mkdir(parents=True, exist_ok=True)
    repos = [(r.id, "model") for r in api.list_models(author=ACCOUNT)]
    repos += [(r.id, "dataset") for r in api.list_datasets(author=ACCOUNT)]
    for repo, rtype in repos:
        rows = []
        for i in api.list_repo_tree(repo, repo_type=rtype, recursive=True):
            if not hasattr(i, "size"):
                continue
            lfs = getattr(i, "lfs", None)
            sha = getattr(lfs, "sha256", None) if lfs else None
            rows.append({"repo": repo, "repo_type": rtype, "on_graydient": repo in GRAYDIENT_REPOS, "path": i.path, "size": i.size, "sha256": sha})
        (OUT / f"{repo.split('/')[1]}.jsonl").write_text("\n".join(json.dumps(r) for r in rows) + "\n")
        print(f"{repo}: {len(rows)} paths", file=sys.stderr)
    return 0

if __name__ == "__main__":
    sys.exit(main())
