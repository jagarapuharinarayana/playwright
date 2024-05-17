from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    for i in range(1,15):
        page.goto(f"https://www.flipkart.com/search?q=ssd&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page={i}")
        # # images=page.eval_on_selector_all('//img[@class="DByuf4"]', 'elements => elements.map(e => e.getAttribute("src"))')
        # names=page.eval_on_selector_all('//a[@class="wjcEIp"]','elements=>elements.map(e=>e.textContent)')
        # # ratings=page.eval_on_selector_all('//div[@class="XQDdHH"]','elements=>elements.map(e=>e.textContent)')
        # prices=page.eval_on_selector_all('//div[@class="Nx9bqj"]','elements=>elements.map(e=>e.textContent)')
        # print(f"Page {i}:")
   
        # for id,(names,prices) in enumerate(zip(names,prices),start=1):
        #  print(f"{id}.{names}:    {prices}")
        cards = page.query_selector_all('//div[@class="slAVV4"]')
        # cards=page.eval_on_selector_all('//div[@class="slAVV4"]')
        print(f"Page {i}:")
        for idx, card in enumerate(cards, start=1):
            names=page.query_selector('//a[@class="wjcEIp"]').text_content().strip() if card.query_selector('//a[@class="wjcEIp"]')else 'N/A'
            images=page.query_selector('//img[@class="DByuf4"]').get_attribute('src') if card.query_selector('//img[@class="DByuf4"]') else 'No Image'
            ratings=page.query_selector('//div[@class="XQDdHH"]').text_content().strip() if card.query_selector('//div[@class="XQDdHH"]')else 'No Rating'
            prices=page.query_selector('//div[@class="Nx9bqj"]').text_content().strip() if card.query_selector('//div[@class="Nx9bqj"]')else 'N/A'
            print(f"{idx}. Name: {names}\n   Price: {prices}\n   Rating: {ratings}\n   Image: {images}")
            
    


      
   
    
    context.close()
    browser.close()



with sync_playwright() as playwright:
    run(playwright)
