from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.apollopharmacy.in/")
    cards=page.query_selector_all('//div[@class="Grid_Item__KaQ4v"]')
    
    for card in cards:
        name_element=card.query_selector('//a[@class="cardAnchorStyle Yz "]//h2') 
        image_element=card.query_selector('//div[@class="Zz"]/img')
        if name_element and image_element:
        # Extracting text content of name element and image source attribute
            names = name_element.inner_text()
            images_src = image_element.get_attribute('src')
            
            print(f"Name: {names}, Image: {images_src}")
    else:
        print("Name or image element not found for a card.")
    
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
