#!/usr/bin/env python3
"""Minimal Cloudflare R2 helper. Reads CF_API_TOKEN + CF_ACCOUNT_ID from ~/.claude/.env
(no shell sourcing). Subcommands:
  list                      -> list bucket names
  pub <bucket>              -> show managed (r2.dev) public domain + enabled state
"""
import json, sys, urllib.request, urllib.error
from pathlib import Path


def env(*names):
    keys = {}
    for line in (Path.home() / ".claude" / ".env").read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, _, v = line.partition("=")
        keys[k.strip()] = v.strip().strip('"').strip("'")
    return [keys.get(n) for n in names]


TOKEN, ACCT = env("CF_API_TOKEN", "CF_ACCOUNT_ID")


def api(path):
    req = urllib.request.Request(
        f"https://api.cloudflare.com/client/v4{path}",
        headers={"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"},
    )
    try:
        return json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as e:
        return {"_http_error": e.code, "_body": e.read().decode()[:300]}


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if not TOKEN or not ACCT:
        print("missing CF_API_TOKEN/CF_ACCOUNT_ID in ~/.claude/.env"); sys.exit(1)
    if cmd == "list":
        r = api(f"/accounts/{ACCT}/r2/buckets")
        if r.get("_http_error"):
            print("HTTP", r["_http_error"], r["_body"]); sys.exit(1)
        for b in r.get("result", {}).get("buckets", []):
            print(b.get("name"), "|", b.get("creation_date", ""))
    elif cmd == "pub":
        bucket = sys.argv[2]
        r = api(f"/accounts/{ACCT}/r2/buckets/{bucket}/domains/managed")
        print(json.dumps(r.get("result", r), indent=2))
    else:
        print("usage: r2.py [list|pub <bucket>]")


if __name__ == "__main__":
    main()
