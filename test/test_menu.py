from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_menu(driver, wait):
    driver.get("http://localhost/litecart/admin/login.php")
    driver.find_element_by_name("username").send_keys("admin")
    driver.find_element_by_name("password").send_keys("admin")
    driver.find_element_by_name("login").click()
    wait.until(EC.title_is("My Store"))

    def are_elements_present(driver, *args):
        return len(driver.find_elements(*args)) > 0

    def get_list_of_links(driver, *args):
        return driver.find_elements(*args)

    links_amount = len(get_list_of_links(driver, By.CSS_SELECTOR, "ul#box-apps-menu a"))
    if links_amount > 0:
        for i in range(links_amount):
            links = get_list_of_links(driver, By.CSS_SELECTOR, "ul#box-apps-menu a")
            links[i].click()
            assert are_elements_present(driver, By.CSS_SELECTOR, "h1")
            sublinks_amount = len(get_list_of_links(driver, By.CSS_SELECTOR, "[class = docs] a"))
            if sublinks_amount > 0:
                for n in range(sublinks_amount):
                    links = get_list_of_links(driver, By.CSS_SELECTOR, "[class = docs] a")
                    links[n].click()
                    assert are_elements_present(driver, By.CSS_SELECTOR, "h1")
            driver.get("http://localhost/litecart/admin")
    else:
        print("No links found")
        assert False



