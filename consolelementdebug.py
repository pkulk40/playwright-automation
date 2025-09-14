import time
import logging
from playwright.sync_api import Page, Locator

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_console_logging(page: Page):
    """Setup console and error logging for the page"""
    def handle_console(msg):
        print(f"Console {msg.type}: {msg.text}")
        logger.info(f"Browser console {msg.type}: {msg.text}")
    
    def handle_page_error(error):
        print(f"Page error: {error}")
        logger.error(f"Page JavaScript error: {error}")
    
    page.on("console", handle_console)
    page.on("pageerror", handle_page_error)

def debug_element_state(locator: Locator, name: str = "element"):
    """Debug element state with timing"""
    print(f"\n--- Debugging {name} ---")
    
    start_time = time.time()
    count = locator.count()
    count_time = time.time() - start_time
    print(f"Count: {count} (took {count_time:.3f}s)")
    
    if count > 0:
        start_time = time.time()
        visible = locator.is_visible()
        visible_time = time.time() - start_time
        print(f"Visible: {visible} (took {visible_time:.3f}s)")
        
        start_time = time.time()
        enabled = locator.is_enabled()
        enabled_time = time.time() - start_time
        print(f"Enabled: {enabled} (took {enabled_time:.3f}s)")
        
        start_time = time.time()
        text = locator.first.text_content()
        text_time = time.time() - start_time
        print(f"Text: '{text}' (took {text_time:.3f}s)")
    else:
        print("Element not found - skipping state checks")