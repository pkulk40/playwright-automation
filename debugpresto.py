"""
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
    email_field = frame_content.locator('input#field-email')

    #field-email
    email_field.wait_for(state="visible")
    email_field.fill("priya.kulk.studies@gmail.com")
    page.pause()
    password_field = frame_content.locator('input#field-password')
    password_field.wait_for(state="visible")
    #password_field.fill("windingtest18")
    password_field.click()  # Focus the field first
    #password_field.press_sequentially("windingtest18")
    
    #frame_content.locator("#field-password").evaluate("element => element.click()")
    password_field.press_sequentially("windingtest18")

    #password_field.fill("windingtest18")
    
    
    #sign_in_button.wait_for(state="visible")
    #sign_in_button.click()
    #sign_in_button.dispatch_event("click")
   
    #frame_content.locator("form#login-form").evaluate("form => form.submit()")
    password_field.wait_for(state="attached")
    page.wait_for_timeout(500)  # Simple delay instead
    sign_in_button = frame_content.locator('button[type="submit"]:has-text("Sign in")')
    sign_in_button.click()
   

    print(f"Submit button clicked: {sign_in_button.is_enabled()}")
    page.wait_for_timeout(1000)
    print(f"Email value: {email_field.input_value()}")
    print(f"Password value: {password_field.input_value()}")
    input("Press Enter to close...")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)


    """

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

    # Enter email
    email_field = frame_content.locator('input#field-email')
    email_field.wait_for(state="visible")
    email_field.fill("priya.kulk.studies@gmail.com")
    
    # Enter password (working approach)
    password_field = frame_content.locator('input#field-password')
    password_field.wait_for(state="visible")
    password_field.press_sequentially("windingtest18")
    
    
    # Wait before submitting
    page.wait_for_timeout(500)
    
    # Click submit button
    #unvisible_button = page.locator(unvisible_button_path)
    #unvisible_button.evaluate("node => node.click()")
    sign_in_button = frame_content.locator('button[type="submit"]:has-text("Sign in")')
    sign_in_button.evaluate("node => node.click()")

    # Debug output
    print(f"Submit button clicked: {sign_in_button.is_enabled()}")
    page.wait_for_timeout(1000)
    print(f"Email value: {email_field.input_value()}")
    print(f"Password value: {password_field.input_value()}")
    
    input("Press Enter to close...")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)