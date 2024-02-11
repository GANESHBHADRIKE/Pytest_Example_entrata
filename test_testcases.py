import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# below line indicate that i have use the fixture which is created in the conftest.py file 

@pytest.mark.usefixtures("setup_module")
class Test_Website():

    def test_HomePage(self):            

        # Test Case to maximize and get the current url of the Site                    

    
        self.driver.maximize_window()
        # launching the application 
        print(self.driver.title)
        print(self.driver.current_url)


        # It will handle the cookies popup appeare on the website will launching the website
        try:
            popup = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//button[@id='rcc-confirm-button']"))
            
        )
            popup.click()
        except:
            print("no cookies popup appeare") 

        
        assert "Entrata" in self.driver.title

    def test_resources_button(self):

        # Testcase 2 
        # it will check the visiblity of the element and perform mouse hover action and clcik on the resources tab
        element_to_hover_over = self.driver.find_element(By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]")

        # Perform mouseover action using ActionChains
        action = ActionChains(self.driver)
        action.move_to_element(element_to_hover_over).perform()

        

        Resources = self.driver.find_element(By.XPATH,"//div[@class='header-nav-item']//a[@class='main-nav-link'][normalize-space()='Resources']")        
        Resources.click()


    def test_watch_demo(self):

        # this test case will just click on the watchdemo button
        watchdemo = self.driver.find_element(By.XPATH,"//a[@class='button-default solid-dark-button'][normalize-space()='Watch Demo']")        
        watchdemo.click()
    

    def test_form_fill(self):

        # this test case will fill all the fiin elds required to the test cases
        self.driver.implicitly_wait(10)
        print(self.driver.current_url)
        self.driver.find_element(By.XPATH,"//input[@id='FirstName']").send_keys("Ganesh")
        self.driver.find_element(By.NAME,"LastName").send_keys("Bhadrike")
        self.driver.find_element(By.XPATH,"//input[@id='Email']").send_keys("bhadrikeganesh3@gmail.com")
        self.driver.find_element(By.NAME,"Company").send_keys("ACC Highland South Parking Garage")
        self.driver.find_element(By.XPATH,"//input[@id='Phone']").send_keys("9769348082")

        # select from the dropdown 

        dropdown_element = self.driver.find_element(By.ID,"Unit_Count__c")
        dropdown = Select(dropdown_element)

        # Select option by visible text
        dropdown.select_by_value("11 - 100")
        assert dropdown.first_selected_option.text == "11 - 100"

        self.driver.find_element(By.XPATH,"//input[@id='Title']").send_keys("Automation Engineer")

        self.driver.execute_script("window.scrollBy(0,500)","")

        Submit = self.driver.find_element(By.XPATH,"//button[@type='submit']")

        # will check the submit button is visible or not

        assert Submit.is_displayed()
        self.driver.back()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR,".button-default.outline-dark-button").click()

        

    def test_sigin(self):

        #this test case will perfom the sign in task and check the elements present on the next page

        manager_login = self.driver.find_element(By.XPATH,"//a[@title='Client Login Button']").text
        resident_login = self.driver.find_element(By.CSS_SELECTOR,"a[title='Resident Portal Login Button']")

        assert manager_login == "Property Manager Login"
        assert resident_login.get_attribute("title") == "Resident Portal Login Button"