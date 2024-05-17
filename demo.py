import asyncio
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    
    await page.goto("https://www.guvi.com/")
   
    await page.get_by_role("link", name="Login").click()
    await page.get_by_label("Email Address").click()
    await page.get_by_label("Email Address").fill("hariallrounder@gmail.com")
    await page.get_by_label("Password").click()
    await page.get_by_label("Password").fill("hari9676669141")
    await page.locator("#login-btn").click()
    async with page.expect_popup() as page1_info:
        await page.get_by_role("link", name="Subscribe Now").click()
    page1 = await page1_info.value
    await page1.close()

    # Evaluate XPath expression to query titles
    titles = await page.eval_on_selector_all(
        '//*[@class="font-weight-bold mb-1 text-black"]',
        'elements => elements.map(e => e.textContent)' 
        
    )
    
    
    # Loop through titles and print them
    for title in titles:
        print(title.strip())
    for i,j in enumerate(titles):
        print(f"{i + 1}: {j}")
        
    video_url = await page.eval_on_selector('video', 'e => e.src')

    # Download the video using requests or any other library
    if video_url:
        import requests
        video_response = requests.get(video_url)
        with open('video.mp4', 'wb') as f:
            f.write(video_response.content)
        print("Video downloaded successfully.")
    else:
        print("No video found on the page.")


    await context.close()
    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
