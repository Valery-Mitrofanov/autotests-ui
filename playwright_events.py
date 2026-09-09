from playwright.sync_api import sync_playwright, expect

def log_request(request: Request):
    prin


def log_response(response: Response):



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    page.on('request')
    page.on('response')