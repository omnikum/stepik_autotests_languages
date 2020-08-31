def test_basket_button(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(5)
    button = len(browser.find_element_by_css_selector(".btn-add-to-basket").text)
    assert button > 0