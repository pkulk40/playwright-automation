from playwright.sync_api import sync_playwright, Playwright, expect
import pytest

def get_title(page) -> str:
    return page.title()

def test_page_title():
    """Test that the page title is correct"""
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()
        page.goto("https://www.automationexercise.com/")
        
        # Test the title
        expect(page).to_have_title("Automation Exercise")
        
        browser.close()
if __name__ == "__main__":
    # Run the test with HTML report
    pytest.main([__file__, "--html=report.html", "--self-contained-html"])