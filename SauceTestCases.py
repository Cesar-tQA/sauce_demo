#This file only have the all of test cases of this automation practice
import Data
from Methods import SauceDemoPage
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestSauceDemoAutomation_practice:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.get(Data.test_page_url)

    def test_sauce_demo(self):
        self.driver.get(Data.test_page_url)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located(
            SauceDemoPage.page_name))
        assert self.driver.current_url == Data.test_page_url, f"Error: 'page' no abre la pagina de SauceDemo"

    def test_set_user(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.set_user()
        user_field = self.driver.find_element(*SauceDemoPage.page_name)
        assert user_field.get_attribute('value') == Data.user_name, (f"Error 'from' El nombre de usuario no se ingreso "
                                                                     f"correctamente")

    def test_set_password(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.set_password()
        user_field = self.driver.find_element(*SauceDemoPage.page_password)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.page_password))
        assert user_field.get_attribute('value') == Data.password, (f"Error 'set' La contraseña que se ingreso no es"
                                                                    f" la correcta")

    def test_login_button(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_login_button()
        login_field = self.driver.find_element(*SauceDemoPage.login_button)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.login_button))
        assert login_field.is_displayed(), f"Error 'Click' No se realiza loggin adecuadamente"
        assert self.driver.current_url.endswith("inventory.html"), "Error: No se redirigió a la pagina de inventario"

    def test_click_sauce_labs_back(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_sauce_labs_backpack()
        lab_backpack = self.driver.find_element(*SauceDemoPage.sauce_labs_backpack)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.sauce_labs_bike_light))
        assert lab_backpack.is_displayed(), f"Error 'Click' No se detecto labs backpack"

    def test_click_sauce_labs_bike_light(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_sauce_labs_bike_light()
        labs_bike_light = self.driver.find_element(*SauceDemoPage.sauce_labs_bike_light)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.sauce_labs_onesie))
        assert labs_bike_light.is_displayed(), f"Error 'Click' No se detecto labs bike ligth"

    def test_click_sauce_labs_onesie(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_sauce_labs_onesie()
        labs_onesie = self.driver.find_element(*SauceDemoPage.sauce_labs_onesie)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.sauce_labs_bolt_tshirt))
        assert labs_onesie.is_displayed(), f"Error 'Click' No se detecto labs onesie"

    def test_labs_bolt_tshirt(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_sauce_labs_bolt_tshirt()
        labs_bolt_tshirt = self.driver.find_element(*SauceDemoPage.sauce_labs_bolt_tshirt)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.sauce_labs_fleece_jacket))
        assert labs_bolt_tshirt.is_displayed(), f"Error 'Click' No se detecto bolt tshirt"

    def test_click_labs_fleece_jacket(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_sauce_labs_fleece_jacket()
        labs_fleece_jacket = self.driver.find_element(*SauceDemoPage.sauce_labs_fleece_jacket)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(SauceDemoPage.pay_car))
        assert labs_fleece_jacket.is_displayed(), f"Error 'Click' No se detecto fleece jacket"

    def test_pay_cart(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_pay_car()
        pay_cart = self.driver.find_element(*SauceDemoPage.pay_car)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.element_to_be_clickable(
            SauceDemoPage.total_pay))
        assert pay_cart.is_displayed(), f"Error 'Click' No se detecto Pay Car"
        assert pay_cart == "5", (f"Error 'Contador' No se seleccionaron todos los elementos en el carrito,"
                                 f" pero se encontraron {pay_cart}")

    def test_total_pay_cart(self):
        sauce_demo = SauceDemoPage(self.driver)
        sauce_demo.click_to_total_pay()
        total_pay_cart = self.driver.find_element(*SauceDemoPage.total_pay)
        WebDriverWait(self.driver, timeout=10).until(expected_conditions.presence_of_element_located(
            SauceDemoPage.total_pay))
        total_text = total_pay_cart.text
        total_value = float(total_text.replace("$", "").strip())
        assert total_pay_cart.is_displayed(), f"Error 'Click' No se detecto el Checkout"
        assert total_value >= 5, f"Error 'Total' La compra es menor a 5, total encontrado {total_value}"

    @classmethod
    def teardown_class(cls):
        if cls.driver:
            cls.driver.quit()

