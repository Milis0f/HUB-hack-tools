#!/usr/bin/python3
"""Simple website analyzer."""

import re
import sys
from typing import Optional

import requests


def fetch(url: str) -> Optional[requests.Response]:
    try:
        response = requests.get(url, timeout=10)
        return response
    except requests.RequestException as exc:  # pragma: no cover - network errors
        print(f"Error fetching {url}: {exc}")
        return None


def extract_title(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return "No title found"


def analyze(url: str) -> None:
    response = fetch(url)
    if not response:
        return
    print(f"URL: {response.url}")
    print(f"Status code: {response.status_code}")
    print(f"Server: {response.headers.get('Server', 'Unknown')}")
    print(f"Title: {extract_title(response.text)}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python weban.py <url>")
        sys.exit(1)
    analyze(sys.argv[1])
