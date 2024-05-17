import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.locator("body").click()
    mobile_names={}
    for i in range(0,42):
        await page.goto(f"https://www.flipkart.com/search?q=mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off%2F&page={i}")
        titles=await page.eval_on_selector_all('//div[@class="KzDlHZ"]',
                                        'elements => elements.map(e => e.textContent)')
        prices=await page.eval_on_selector_all('//div[@class="Nx9bqj _4b5DiR"]',
                                        'elements => elements.map(e => e.textContent)')
        
        # for title, price in zip(titles, prices):
        #     mobile_names[title] = price
        
        print(f"Page {i}:")
        # for title, price in mobile_names.items():
        #     print(f"{title}: {price}")
        for idx, (title, price) in enumerate(zip(titles, prices), start=1):
            print(f"{idx}. {title}: {price}")
    # images=await page.eval_on_selector_all( '//img[@class="DByuf4"]',
    # 'elements => elements.map(e => e.getAttribute("src"))')
    # for j in images:
    #     print(j)
        
    

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
