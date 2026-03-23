import urllib.request
import urllib.parse
import json
import csv
import time
import os

KEYWORDS_GROUPS = [
    ["UX", "UI", "usability", "user experience"],
    ["smell", "layout", "design", "interface"]
]
REPO = "eclipse-platform/eclipse.platform.ui"

def fetch_issues():
    all_items = []
    seen_ids = set()
    for group in KEYWORDS_GROUPS:
        query = f"repo:{REPO} " + " OR ".join([f'"{k}"' for k in group])
        encoded_query = urllib.parse.quote_plus(query)
        
        api_url = f"https://api.github.com/search/issues?q={encoded_query}&per_page=100"
        print(f"Fetching from: {api_url}")
        req = urllib.request.Request(api_url, headers={"Accept": "application/vnd.github.v3+json", "User-Agent": "UX-Smell-Extractor"})
        
        try:
            with urllib.request.urlopen(req) as response:
                data = json.loads(response.read().decode())
                for item in data.get("items", []):
                    if item["id"] not in seen_ids:
                        seen_ids.add(item["id"])
                        all_items.append(item)
                print(f"Total results found in this group: {data.get('total_count', 0)}")
        except urllib.error.HTTPError as e:
            print(f"HTTP Error: {e.code} - {e.reason}")
            try:
                print(e.read().decode())
            except Exception:
                pass
            if e.code == 403:
                print("Rate limit exceeded. Please provide a GitHub Token.")
        time.sleep(2)
    
    return all_items

def save_to_csv(issues, filename="eclipse_ux_issues.csv"):
    if not issues:
        print("No issues found to save.")
        return
    
    filepath = os.path.join(os.path.dirname(__file__), filename)
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Title", "State", "URL", "Labels", "Created At"])
        for issue in issues:
            labels = ", ".join([l["name"] for l in issue.get("labels", []) if isinstance(l, dict)])
            writer.writerow([
                issue["number"], 
                issue["title"], 
                issue["state"], 
                issue["html_url"], 
                labels, 
                issue["created_at"]
            ])
    print(f"Saved {len(issues)} issues to {filepath}")

if __name__ == "__main__":
    print("Fetching UX issues from Eclipse Platform UI...")
    issues = fetch_issues()
    if issues:
        save_to_csv(issues)
