from selenium.webdriver.support import expected_conditions as EC


def test_login(driver, wait):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    # WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, 'btnK')))
    driver.find_element_by_name("login").click()
    wait.until(EC.title_is("My Store"))
