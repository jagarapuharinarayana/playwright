import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect

async def run(playwright: Playwright) -> None:
    browser = await playwright.firefox.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://www.guvi.com/")

    # Your login and navigation steps...
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
    await page.get_by_role("link", name="play JavaScript Zero to Hero in Telugu JavaScript Zero to Hero in Telugu Language: Telugu 0% Completed").click()
    await page.locator("button").filter(has_text=re.compile(r"^Play$")).click()     

    # Get the video URL from the source attribute
    video_url = await page.evaluate('() => document.querySelector(".embed-responsive-item").src')

    # Fetch the video content using the fetch API within the browser context
    video_content = await page.evaluate(f'''
        async function fetchVideoContent(url) {{
            const response = await fetch(url);
            const blob = await response.blob();
            return blob;
        }}
        return fetchVideoContent("{video_url}");
    ''')

    # Save the video content to a file
    with open('video.mp4', 'wb') as f:
        f.write(video_content)

    print("Video downloaded successfully.")

    await browser.close()

async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
