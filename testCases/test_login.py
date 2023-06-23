from pageObjects.LoginPage import LoginPage
import pytest
from selenium import webdriver


class Test_001_Login:
    baseURL = "https://admin-demo.nopcommerce.com/"
    username = "dmin@yourstore.com"
    password = "admin"

    def test_homePageTitle(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        actual_title = self.driver.title
        self.driver.close()
        if actual_title == "Your store. Login":
            assert True
        else:
            assert False

    def test_loginPage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.lp.clickLogout()
