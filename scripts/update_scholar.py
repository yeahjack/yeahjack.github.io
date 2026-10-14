#!/usr/bin/env python3
"""Refresh the public Scholar snapshot; never replace missing data with zero.

One public profile request, no publication crawling, proxies or CAPTCHA bypass.
The standard library is sufficient for Scholar's small server-rendered table.
"""

import argparse
from datetime import datetime, timezone
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import tempfile
from urllib.request import Request, urlopen


SCHOLAR_ID = "hBZs76kAAAAJ"
AUTHOR_NAME = "Yijie Xu"
PROFILE_URL = f"https://scholar.google.com/citations?user={SCHOLAR_ID}&hl=en"


class ProfileParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.table_depth = 0
        self.cell = None
        self.row = []
        self.rows = []
        self.name_depth = 0
        self.name_parts = []

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if attrs.get("id") == "gsc_prf_in":
            self.name_depth = 1
        elif self.name_depth:
            self.name_depth += 1
        if tag == "table" and (self.table_depth or attrs.get("id") == "gsc_rsb_st"):
            self.table_depth += 1
        if self.table_depth:
            if tag == "tr":
                self.row = []
            elif tag in ("td", "th"):
                self.cell = []

    def handle_data(self, data):
        if self.name_depth:
            self.name_parts.append(data)
        if self.cell is not None:
            self.cell.append(data)

    def handle_endtag(self, tag):
        if self.name_depth:
            self.name_depth -= 1
        if self.table_depth:
            if tag in ("td", "th") and self.cell is not None:
                self.row.append("".join(self.cell).strip())
                self.cell = None
            elif tag == "tr":
                self.rows.append(self.row)
            elif tag == "table":
                self.table_depth -= 1


def parse_citations(html):
    if re.search(r"recaptcha|g-recaptcha|unusual traffic", html, re.IGNORECASE):
        raise ValueError("Scholar returned a verification page, not citation data")
    parser = ProfileParser()
    parser.feed(html)
    name = " ".join("".join(parser.name_parts).split())
    if name != AUTHOR_NAME:
        raise ValueError("Scholar profile identity is missing or unexpected")
    if not any(len(row) >= 3 and row[1] == "All" for row in parser.rows):
        raise ValueError("Scholar's all-time metric column is missing")
    matches = [row for row in parser.rows if len(row) >= 3 and row[0] == "Citations"]
    if len(matches) != 1 or not re.fullmatch(r"\d{1,3}(?:,\d{3})*|\d+", matches[0][1]):
        raise ValueError("Scholar's total citation count is missing or malformed")
    return int(matches[0][1].replace(",", ""))


def fetch_citations():
    request = Request(PROFILE_URL, headers={
        "User-Agent": "YijieXu-academic-site/1.0 (+https://yjx.me/)",
        "Accept-Language": "en-US,en;q=0.9",
    })
    with urlopen(request, timeout=20) as response:
        if response.status != 200 or response.headers.get_content_type() != "text/html":
            raise ValueError("Scholar did not return a successful HTML response")
        body = response.read(2_000_001)
        if len(body) > 2_000_000:
            raise ValueError("Unexpectedly large Scholar response")
        html = body.decode(response.headers.get_content_charset() or "utf-8")
    return parse_citations(html)


def write_snapshot(root, count, checked_on):
    badge_path = root / "gs_data.json"
    metadata_path = root / "_data" / "scholar.yml"
    if isinstance(count, bool) or not isinstance(count, int) or count < 0:
        raise ValueError("Citation count must be a nonnegative integer")
    if badge_path.exists():
        previous = json.loads(badge_path.read_text(encoding="utf-8"))
        previous_count = int(previous["message"].split()[0])
        if count == 0 and previous_count > 0:
            raise ValueError("Refusing an unexpected reset to zero; keeping the last snapshot")
    badge = {
        "schemaVersion": 1,
        "label": "Google Scholar",
        "message": f"{count} citations",
        "color": "245f7a",
        "labelColor": "626b70",
        "namedLogo": "googlescholar",
        "logoColor": "white",
        "style": "flat-square",
    }
    metadata = (
        "# Automatically refreshed by scripts/update_scholar.py.\n"
        f"total_citations: {count}\n"
        f"checked_on: {json.dumps(checked_on)}\n"
        f"source_url: {json.dumps(PROFILE_URL)}\n"
    )
    outputs = [(badge_path, json.dumps(badge, indent=2) + "\n"), (metadata_path, metadata)]
    # Prepare both outputs before replacing either. Failed fetches never reach this point.
    prepared = []
    try:
        for target, content in outputs:
            with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=target.parent,
                                             prefix=".scholar-", delete=False) as temp:
                temp.write(content)
                prepared.append((Path(temp.name), target))
        for temp, target in prepared:
            temp.replace(target)
    finally:
        for temp, _ in prepared:
            temp.unlink(missing_ok=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    try:
        count = fetch_citations()
        checked_on = datetime.now(timezone.utc).date().isoformat()
        write_snapshot(args.root, count, checked_on)
    except Exception as error:
        print(f"Scholar update failed; last successful snapshot retained: {error}", file=sys.stderr)
        return 1
    print(f"Verified {AUTHOR_NAME}: {count} total citations (checked {checked_on})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
