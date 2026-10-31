"""Optional external link audit; never part of offline course tests."""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import re
from urllib.request import Request, urlopen
from urllib.error import HTTPError

ROOT = Path(__file__).resolve().parents[1]


def check(url):
    try:
        with urlopen(Request(url, headers={"User-Agent": "Academy-Link-Audit/1.0"}), timeout=12) as response:
            return url, str(response.status), response.url
    except HTTPError as error:
        return url, str(error.code), str(error.url)
    except Exception as error:
        return url, "unverified", type(error).__name__


if __name__ == "__main__":
    urls = sorted({url for lesson in (ROOT / "lessons").glob("*/LESSON.md")
                   for url in re.findall(r"https://[^\s)]+", lesson.read_text())})
    print("# External lesson link audit\n\nChecked 2026-10-31 using HTTP GET. 200 means reachable, not a verified content/paywall review. Redirect targets are recorded. 403/429/transport errors are inconclusive; 404 is a broken URL. No student progress is affected.\n")
    print("| URL | HTTP/status | Final URL or error |\n| --- | --- | --- |")
    with ThreadPoolExecutor(max_workers=8) as pool:
        for url, status, final in pool.map(check, urls):
            print(f"| {url} | {status} | {final} |")
