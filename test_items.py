import time
def test_basket_button_is_exist(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    browser.implicitly_wait(15)
    time.sleep(30)
    button = len(browser.find_element_by_css_selector(".btn-add-to-basket").text)
    assert button > 0