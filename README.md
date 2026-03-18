# Build a Slack Bot That Alerts You When Your Competitor Launches a New Page

In this tutorial, we’ll build a simple system that uses SerpApi's Google Search API to detect when a new competitor domain URL appears in search results and then sends an alert to a Slack channel.

Code examples for blog post: serpapi.com/blog/build-a-slack-bot-that-alerts-you-when-your-competitor-launches-a-new-page

## Getting Started

To start, you’ll need a SerpApi account, a Slack workspace (and a Slack Incoming Webhook URL), and Python installed.

### Create a Slack Webhook
1. Go to Slack → Apps
2. Search for Incoming Webhooks
3. Create a webhook for your channel

You will get a Webhook URL like: https://hooks.slack.com/services/XXXX/XXXX/XXXX

Save this, as we'll need it later.

### Code Related Setup Steps

1. Install `serpapi` (SerpApi's new Python library), the python-dotenv library, and the schedule library in your environment:

```
pip install serpapi python-dotenv schedule
```

2. To begin scraping data, create a free account on serpapi.com. You'll receive 250 free search credits each month to explore the API. Get your SerpApi API Key from this page.

3. [Optional but Recommended] Set your API key in an environment variable, instead of directly pasting it in the code. Refer here to understand more about using environment variables. For this tutorial, I have saved the API key in an environment variable named "SERPAPI_API_KEY" in my .env file.

4. [Optional but Recommended] Set up your Slack Webhook URL as an an environment variable as well. In your .env file, this will look like this:

```
SERPAPI_API_KEY=<YOUR PRIVATE API KEY>
SLACK_WEBHOOK_URL=<YOUR PRIVATE WEBHOOK URL>
```
5. Set constants as needed in the code file `alerts_for_new_competitor_pages.py`:
```
SERPAPI_KEY = os.environ["SERPAPI_API_KEY"] -> Set the environment variable OR replace with your API key if you're not using environment variables
DOMAIN = "" -> Add your domain
DB_FILE = "known_urls.json"
SLACK_WEBHOOK = os.environ["SLACK_WEBHOOK_URL"] -> Set the environment variable OR replace with your API key if you're not using environment variables
```

## Run The Code

Head to the project folder and run the code file using `python alerts_for_new_competitor_pages.py`

This will start the scheduler. To keep the tasks running even after you close your terminal or IDE, you can choose to run the script as a persistent background process. For linux/macOS, use `disown` to detach the script from the terminal, e.g., `python3 script.py & disown`.

If you want to just test your implementation, comment the scheduler related lines and just add a line to call the `check_new_pages()` function. 

---

## Sample Output

Once this is set up, your Slack channel will receive alerts like this once a day:

> 🚨 New competitor pages detected:
> 
> https://competitor.com/products/ai-assistant
> 
> https://competitor.com/features/fast-mode

I ran the code twice for the domain serpapi.com. The first time, I got some new pages and the next time, since all the webpages were already seen, I got a message letting me know that no new pages were detected. These were the alerts I received: 

<img width="1526" height="389" alt="image" src="https://github.com/user-attachments/assets/5e5f587e-3a34-4087-9531-e2b225d2231c" />

This lets you instantly spot new product launches, new feature releases, and new landing pages which are showing up in search results for any company.

---
