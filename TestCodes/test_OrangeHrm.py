"""test_OrangeHrm pytest file which includes 5 testcases"""

from TestLocators.OrangeHrm_Locators import Locators
from TestData.OrangeHrm_Data import InputData
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert
import pytest


class Test_OrangeHrmPage:
    # booting function to call starting of every testcase
    @pytest.fixture
    def booting_fun(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument("--incognito")
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=self.chrome_options)
        self.wait = WebDriverWait(self.driver, 10)
        self.alert = Alert(self.driver)
        yield
        self.driver.close()
     # Login testcase
    def test_login(self, booting_fun):
        try:
            self.driver.get(InputData().url)
            username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().login)))
            username.send_keys(InputData().username)
            password.send_keys(InputData().password)
            submit_button.click()
            assert self.driver.title == InputData().home_page
            print("success , Login successfull")

        except NoSuchElementException as e:
            print(e)
    # invalid credentials testcase
    def test_invalid_login(self, booting_fun):
        try:
            self.driver.get(InputData().url)
            username = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().username)))
            password = self.wait.until(EC.presence_of_element_located((By.NAME, Locators().password)))
            submit_button = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators().login)))
            username.send_keys(InputData().username)
            password.send_keys(InputData().invalid_password)
            submit_button.click()
            invalid_credentials = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators().invalid_msg))).text
            assert invalid_credentials == InputData().error_invalid_msg
            print("Success , Invalid Password")
            print()
        except NoSuchElementException as e:
            print(e)
    # add employee testcase
    def test_add_employee(self, booting_fun):
        try:
            self.test_login(booting_fun)
            pim = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().pim)))
            pim.click()
            Add_employee = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().add_employee_icon)))
            Add_employee.click()
            firstname = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().first_name)))
            firstname.send_keys(InputData().first_name)
            lastname = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.last_name)))
            lastname.send_keys(InputData().Last_name)
            employee_id = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators.Employee_id)))
            employee_id.send_keys("10")
            save = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().save_button)))
            save.click()
            success_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().success_msg))).text
            assert success_message == InputData().success_add_msg
            print("sucess , Employee is added")

        except NoSuchElementException as e:
            print(e)
    # edit employee information testcase
    def test_edit_employee(self, booting_fun):
        try:
            self.test_login(booting_fun)
            pim = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().pim)))
            pim.click()
            employee_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().employee_list_icon)))
            employee_list.click()
            edit = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().edit_icon)))
            edit.click()
            fullname = self.wait.until(EC.element_to_be_clickable((By.XPATH, Locators.fullname)))
            fullname.click()
            fullname.clear()
            fullname.send_keys(InputData().full_name)

            save = self.wait.until(EC.presence_of_element_located((By.XPATH, Locators().save_update)))
            save.click()
            update_message = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators().update_msg))).text
            assert update_message == InputData().update_edit_msg
            print("success, employee name is edited")

        except NoSuchElementException as e:
            print(e)
    # delete employee record testcase
    def test_delete_employee(self, booting_fun):
        try:
            self.test_login(booting_fun)
            pim = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.pim)))
            pim.click()
            employee_list = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.employee_list_icon)))
            employee_list.click()
            delete = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators.delete_icon)))
            delete.click()

            del_button = self.wait.until(EC.visibility_of_element_located((By.XPATH, Locators.del_button_icon)))

            del_button.click()

            del_message = self.wait.until(
                EC.visibility_of_element_located((By.XPATH, Locators().del_msg))).text
            assert del_message == InputData().del_employee_msg
            print("success , employee is deleted")
        except NoSuchElementException as e:
            print(e)
