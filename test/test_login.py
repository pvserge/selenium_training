import pytest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver(request):

    # Chrome browser
    # options = webdriver.ChromeOptions()
    # options.add_argument("start-maximized")
    # wd = webdriver.Chrome(chrome_options=options)

    # Firefox browser (new)
    wd = webdriver.Firefox()
    # wd = webdriver.Firefox(capabilities={"marionette": True})
    # Firefox browser ESR v45 (old)
    # wd = webdriver.Firefox(capabilities={"marionette": False}, firefox_binary="/Applications/Firefox 3.app/Contents/MacOS/firefox-bin")
    # Firefox Nightly v69
    # wd = webdriver.Firefox(capabilities={"marionette": True}, firefox_binary="/Applications/Firefox Nightly.app/Contents/MacOS/firefox-bin")

    # Safari browser
    # wd = webdriver.Safari()

    # PhantomJS browser
    # wd = webdriver.PhantomJS(executable_path="/Users/qa/phantomjs/bin/phantomjs")

    # Cookies
    # driver.add_cookie({'name': 'test', 'test': 'bar'})
    # test_cookie = driver.get_cookie('test')
    # cookies = driver.get_cookies()
    # driver.delete_cookie('test')
    # driver.delete_all_cookies()

    # Print capabilities of current browser
    print("Capabilities are: %s" % wd.capabilities)
    request.addfinalizer(wd.quit)
    return wd


def test_login(driver):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    driver.find_element_by_name("login").click()
    WebDriverWait(driver, 10).until(EC.title_is("My Store"))
