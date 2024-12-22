import requests
import logging
import html2text
from utils.load_env import SCRAPE_FISH_API_KEY, JINA_URI, SCRAPE_FISH_URI
import json


def scrape_website(website_url):
    try:
        jina_url = f"{JINA_URI}{website_url}"

        headers = {
            'Accept': 'application/json',
            'X-Return-Format': 'text'
        }
        response = requests.get(jina_url, headers=headers)
        response_json = response.json()

        # Extract text content
        raw_text = response_json["data"]["text"]
        return raw_text
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        raise


def scrapefish_website(website_url, rules):
    try:
        payload = {
            "api_key": SCRAPE_FISH_API_KEY,
            "url": website_url,
            "render_js": "true",
            "js_scenario": json.dumps(rules)
        }

        response = requests.get(SCRAPE_FISH_URI, params=payload)
        raw_text = html2text.html2text(response.content.decode('utf-8'))
        
        return raw_text
    except Exception as e:
        logging.error(f"Scraping failed: {e}")
        raise


def build_js_scenario(
    pagination_type="None",
    num_scrolls=1,
    scroll_pixels=1400,
    num_button_clicks=1,
    button_selector="#load-more"
):
    """
    Builds the js_scenario dictionary for Scraping Fish based on user-selected pagination rules.

    Args:
        pagination_type (str): "None", "Scroll", or "Button"
        num_scrolls (int): Times to scroll (if "Scroll")
        scroll_pixels (int): Pixels per scroll (if "Scroll")
        num_button_clicks (int): How many times to click the button (if "Button")
        button_selector (str): CSS selector of the button (if "Button")

    Returns:
        dict: The 'js_scenario' steps for Scraping Fish.
    """
    steps = []

    if pagination_type == "Scroll":
        # Multiple scroll steps
        for _ in range(num_scrolls):
            steps.append({"scroll": scroll_pixels})
            steps.append({"wait": 3000})  # wait 3 seconds after each scroll

    elif pagination_type == "Button":
        # Click a button multiple times
        # Could also do "click_and_wait_for_navigation" if the site triggers a full navigation
        for _ in range(num_button_clicks):
            steps.append({"click": button_selector})
            steps.append({"wait": 3000})  # wait 3 seconds after each click

    else:
        # Default: single scroll with a random wait
        steps = [
            {"scroll": 1200},
            {
                "wait": {
                    "random": {
                        "min_ms": 1000,
                        "max_ms": 3000
                    }
                }
            }
        ]

    return {"steps": steps}

