from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    for i in range(0,14):
        page.goto(f'https://www.meesho.com/soft-toys-kids/pl/3l1?page={i}')
        card=page.query_selector_all('//div[@class="sc-ftTHYK dSpUEW NewProductCardstyled__CardStyled-sc-6y2tys-0 ccpfUL NewProductCardstyled__CardStyled-sc-6y2tys-0 ccpfUL"]')
        for items in card:
            image_src=items.query_selector('//div[@class="sc-ftTHYK dSpUEW NewProductCardstyled__CardStyled-sc-6y2tys-0 ccpfUL NewProductCardstyled__CardStyled-sc-6y2tys-0 ccpfUL"]/div[@class="NewProductCardstyled__ProductImage-sc-6y2tys-18 iWWQS"]/img')
            price=items.query_selector('//h5[@class="sc-eDvSVe dwCrSh"]')
            
    # ---------------------
            context.close()
            browser.close()


with sync_playwright() as playwright:
    run(playwright)
