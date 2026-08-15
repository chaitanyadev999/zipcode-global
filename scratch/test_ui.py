import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        # Listen for console events
        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))
        page.on("pageerror", lambda err: print(f"Page Error: {err}"))
        
        print("Navigating...")
        await page.goto("http://localhost:8000/home/main.html")
        await page.wait_for_timeout(1000)
        
        print("Selecting India...")
        await page.select_option("#fCountry", "india") # Wait, is value "india"? No, value is "in"
        await page.select_option("#fCountry", "india")
        
        await page.wait_for_timeout(2000)
        
        # Check if disabled
        disabled = await page.evaluate("document.getElementById('fState').disabled")
        options = await page.evaluate("document.getElementById('fState').innerHTML")
        print(f"State dropdown disabled? {disabled}")
        print(f"State options: {options}")
        
        await browser.close()

asyncio.run(main())
