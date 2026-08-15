import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        
        page.on("console", lambda msg: print(f"Console {msg.type}: {msg.text}"))
        
        print("Navigating...")
        await page.goto("http://localhost:8000/home/main.html?v=123")
        await page.wait_for_timeout(1000)
        
        print("Selecting India...")
        await page.select_option("#fCountry", "india")
        await page.wait_for_timeout(1000)
        
        print("Selecting Andhra Pradesh...")
        await page.select_option("#fState", "andhra-pradesh")
        await page.wait_for_timeout(1000)
        
        print("Selecting Visakhapatnam...")
        # wait, the city value is the html file, e.g. pages/india/andhra-pradesh/visakhapatnam.html
        # let's just select by index or just the first option
        opts = await page.locator('#fCity option').all_inner_texts()
        print("First few cities:", opts[:5])
        
        # let's just click the button with state selected
        print("Clicking Get Pincodes...")
        await page.click("#finderBtn")
        await page.wait_for_timeout(2000)
        
        res = await page.evaluate("document.getElementById('finderResult').innerHTML")
        print("Result HTML snippet:", res[:500])
        
        await browser.close()

asyncio.run(main())
