from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

driver.set_page_load_timeout(15)
driver.maximize_window()
driver.get("https://test.crowdstreet.com/")

# wait for webpage to load
driver.implicitly_wait(10)

# click on Create Account button
CreateAccount1_btn = driver.find_element(By.XPATH, '(//a[@href="/invexp/accounts/create-account"])[1]').click()

# Create Account
inputFName_txt = driver.find_element(By.ID, 'firstName').send_keys('Jane')
inputLName_txt = driver.find_element(By.ID, 'lastName').send_keys('Doe')
inputEmail_txt = driver.find_element(By.ID, 'email').send_keys('Testmail1@gmail.com')
inputPwd_txt = driver.find_element(By.ID, 'password').send_keys('Test@1234')
inputConfirmPwd_txt = driver.find_element(By.ID, 'confirmPassword').send_keys('Test@1234')
inputTerms_rad = driver.find_element(By.ID, 'hasAgreedTos').click()
selectInvestor_chk = driver.find_element(By.XPATH, '(//input[@id="accreditedYes"])[1]').click()

# Wait for reCAPTCHA iFrame to load
driver.implicitly_wait(5)

# Find reCAPTCHA iFrame and Switch to it
iFrame = driver.find_element(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
driver.switch_to.frame(iFrame)

# Select I am not robot checkbox from iFrame and click the element
Robot_chk = driver.find_element(By.XPATH, '//*[@id="recaptcha-anchor"]').send_keys(Keys.ENTER)

# switch back to default/parent frame
driver.switch_to.default_content()
# driver.switch_to.parent_frame()

# hover over the Create Account button and click it
element_hover = driver.find_element(By.XPATH, '//*[@id="content-well"]/div[2]/div/div[2]/form/button/span')
ActionChains(driver).move_to_element(element_hover).perform()
CreateAccount2_btn = element_hover.click()

# verify if account was created and navigate to My Account page
AccountName = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app-header"]/div[2]/div[1]/div[2]/div[3]/div/div/div[1]/div/abbr'))).text
print("Account created: " + AccountName)

MyAccount = driver.find_element(By.XPATH, '(//a[@class="submenu-link"])[9]')
ActionChains(driver).move_to_element(MyAccount).perform()
MyAccount.click()

# exit the webpage
driver.close()

