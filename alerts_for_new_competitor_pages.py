# How To Build a Slack Bot That Alerts You When Your Competitor Launches a New Page

import os
import serpapi
import requests
import json
import schedule
import time
from dotenv import load_dotenv
load_dotenv()

SERPAPI_KEY = os.environ["SERPAPI_API_KEY"]
DOMAIN = "serpapi.com"
DB_FILE = "known_urls.json"
SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK_URL"]

def get_all_pages():
   urls = set()
   client = serpapi.Client(api_key=SERPAPI_KEY)
   for start in range(0, 100, 10):
       results = client.search({
           'engine': 'google',
           'google_domain': 'google.com',
           'q': f"site:{DOMAIN} -site:forum.{DOMAIN} -site:{DOMAIN}/blog -site:{DOMAIN}/careers -site:{DOMAIN}/release-notes",
           'start': start,
       })
       if "organic_results" not in results:
           break
       for result in results["organic_results"]:
           urls.add(result["link"])
   return urls

def load_urls():
    try:
        with open(DB_FILE) as f:
            return set(json.load(f))
    except:
        return set()

def save_urls(urls):
     with open(DB_FILE, "w") as f:
          json.dump(list(urls), f)
          
def send_slack_alert(urls):
   if urls:
       message = {
           "text": f"🚨 New competitor pages detected:\n{'\n'.join(urls)}"
       }
   else:
       message = {
           "text": "✅ No new competitor pages detected."
       }
   requests.post(SLACK_WEBHOOK, json=message)

def check_new_pages():
    print("Checking for new pages...")
    known_urls = load_urls()
    current_urls = get_all_pages()
    new_pages = current_urls - known_urls
    send_slack_alert(new_pages)
    new_seen_set = known_urls.union(current_urls)
    save_urls(new_seen_set)

# Schedule the bot to run every day at 9 AM
schedule.every().day.at("09:00").do(check_new_pages)
print("Competitor monitoring bot running...")

while True:
    schedule.run_pending()
    time.sleep(60)