import requests

vuln_paths = [
    "/.git/config", "/admin", "/phpinfo.php", "/server-status",
    "?id=1' OR '1'='1", "?q=<script>alert(1)</script>"
]

headers = {
    "User-Agent": "BugBountyScanner/1.0"
}

def scan_target(target):
    print(f"🔍 Scanning: {target}")
    for path in vuln_paths:
        url = target + path
        try:
            r = requests.get(url, headers=headers, timeout=5)
            if r.status_code == 200:
                print(f"[+] Possible Issue Found at: {url}")
        except requests.RequestException:
            continue

if __name__ == "__main__":
    target_url = input("Enter target URL (e.g., https://example.com): ").strip().rstrip('/')
    scan_target(target_url)
