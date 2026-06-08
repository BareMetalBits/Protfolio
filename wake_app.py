"""
Visits the Streamlit app with a real headless browser.
- If the app is sleeping  → clicks "Yes, get this app back up!"
- If the app is awake     → holds the connection for 8 s so the Streamlit
                            WebSocket session fully registers, then closes.

The browser does NOT stay open between GitHub Actions runs.
Each 10-minute ping resets Streamlit's 12-hour inactivity timer, which is
all that is needed to keep the app from ever going to sleep.
"""
import sys
from playwright.sync_api import sync_playwright, TimeoutError as PWTimeout

APP_URL    = "https://dhairya-panchal.streamlit.app/"
SLEEP_TEXT = "Yes, get this app back up!"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(
        user_agent=(
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    )

    print(f"Visiting {APP_URL} ...")
    try:
        page.goto(APP_URL, timeout=60_000, wait_until="domcontentloaded")
    except PWTimeout:
        print("⚠️  Page load timed out — Streamlit may still be booting.")
        browser.close()
        sys.exit(0)

    try:
        # ── Case 1: App is sleeping ────────────────────────────────────────
        wake_btn = page.get_by_text(SLEEP_TEXT)
        wake_btn.wait_for(timeout=6_000)

        print("💤  App is sleeping — clicking wake button...")
        wake_btn.click()

        # Wait for sleep screen to disappear (up to 30 s)
        page.wait_for_function(
            f"!document.body.innerText.includes('{SLEEP_TEXT}')",
            timeout=30_000,
        )
        print("✅  App woke up. Holding connection for 10 s to let it fully boot...")
        page.wait_for_timeout(10_000)
        print("    Done.")

    except PWTimeout:
        # ── Case 2: App is already awake ───────────────────────────────────
        # Hold the connection briefly so the Streamlit WebSocket session
        # fully registers as active before we close the browser.
        print("✅  App is already awake — holding connection for 8 s...")
        page.wait_for_timeout(8_000)
        print("    Session registered. Done.")

    except Exception as e:
        print(f"⚠️  Unexpected error: {e}")

    finally:
        browser.close()
