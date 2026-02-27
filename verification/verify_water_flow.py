from playwright.sync_api import sync_playwright
import os
import time

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Get absolute path to index.html
        cwd = os.getcwd()
        file_path = f"file://{cwd}/index.html"

        print(f"Opening {file_path}")
        page.goto(file_path)

        # 1. Initial State
        print("Taking initial screenshot...")
        page.screenshot(path="verification/1_initial.png")

        # 2. Start Animation
        print("Starting animation...")
        page.click("#startBtn")

        # Wait for some simulation time (e.g., 2 seconds real time = 6 minutes sim time)
        time.sleep(2)

        print("Taking running screenshot...")
        page.screenshot(path="verification/2_running.png")

        # 3. Pause
        print("Pausing...")
        page.click("#pauseBtn")
        page.screenshot(path="verification/3_paused.png")

        # 4. Reset
        print("Resetting...")
        page.click("#resetBtn")
        page.screenshot(path="verification/4_reset.png")

        browser.close()

if __name__ == "__main__":
    run()
