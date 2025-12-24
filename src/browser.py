from playwright.sync_api import BrowserType


def launch_browser(playwright):
    return playwright.chromium.launch(headless=True)
