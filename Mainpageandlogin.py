from playwright.sync_api import sync_playwright, Playwright
from consolelementdebug import setup_console_logging, debug_element_state

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    
    page.goto("https://demo.prestashop.com/#/en/front")
    
    # Debug iframe
    iframe = page.locator("iframe[name=\"framelive\"]")
    frame_content = iframe.content_frame

    sign_in_link = frame_content.locator('//*[@id="_desktop_user_info"]/div/a')
    sign_in_link.click()

    #enter user name and pwd
    email_field = frame_content.locator('//*[@id="field-email"]')
    email_field.wait_for(state="visible")
    email_field.fill("priya.kulk.studies@gmail.com")
    
    password_field = frame_content.locator('//*[@id="field-password"]')
    password_field.wait_for(state="visible")
    password_field.fill("windingtest18")

    sign_in_button = frame_content.locator('//*[@id="submit-login"]')
    sign_in_button.wait_for(state="visible")
    sign_in_button.click()


    input("Press Enter to close...")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)