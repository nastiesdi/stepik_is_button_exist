
import time


link ='http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/'


class TestLogin(object):
    def test_is_button_exist(self, browser):
        browser.get(link)
        # browser.find_element_by_css_selector("#login_link")
        # browser.get(link)
        time.sleep(10)
        button = browser.find_element_by_class_name("btn-add-to-basket")
        assert button


