# TestWorkspace
For my test project to write the automation test case for creating an account in the test.crowdstreet.com website, I am using Selenium WebDriver’s Python bindings with Google Chrome and ChromeDriver.
I am using Selenium which is an open-source, web-based automation tool. I chose Python because it’s a very easy language to use and Python APIs make it easy to connect with a browser through Selenium Web driver. Selenium can send the standard Python commands to different browsers such as Chrome, Firefox, IE on different operating systems to perform different tasks on the browser.
This test workspace contains files to demonstrate step-by-step process to write the automation test the python PyCharm IDE. 

## Selenium project using PyCharm IDE:

## [Pre-Requisites](###Pre-Requisites)
 #### Required Items
*	Python on Windows.
*	PyCharm IDE.
*	Selenium Webdriver Packages
*	Chrome Driver

## [Installations](###Installations)
* #### Python download link - https://www.python.org/downloads/
 
* #### PyCharm IDE download link: https://www.jetbrains.com/pycharm/download/#section=windows
  Install the PyCharm community edition.
  
*  #### Chrome driver installation link: https://sites.google.com/a/chromium.org/chromedriver/downloads
   Check the version of Chrome installed on your machine and download the web-driver zip file from the below link suitable to the version of the browser. Chrome driver will be installed in the form an executable for windows. Extract the zip file to desired location. Right click on executable of web-driver and copy the path. Add the chrome driver to your system path. 
	 
 *  #### Selenium Installation in Python:
    Open a Terminal/cmd and write the below command to install selenium libraries in python.
    
    *pip install -U selenium*
 
## Functional Test Quick Start
1. Clone Create_Account.py locally
2. Run the functional test
   * Open the test file 'Create_Account.Py' file in PyCharm.
   * When the test is open, right click and choose to run the file in the test runner.
   * Execute test from Terminal: Click on View -> Tool Windows -> Terminal -> Navigate to the folder where 'Create_Account.py' is located and type the command 
     *python create_account.py*
   
#### ADDITIONAL INFO: 
 *	Create-Account API Testing document uploaded.
 *	Readme document with screen shots for installation.

### Use case to CREATE AN ACCOUNT:
	* From Selenium Import webdriver and other libraries.
	* Initialize the chrome driver.
	* Maximize the window using maximize_window() function.
	* Use get() function and pass URL as the parameter.
	* Use find_element_by_id(), find_element_by_xpath(), find_element_by_css_selectors() to find elements on the webpage.
	* Use ActionChains to hover over elements, click() function to click on buttons, send_keys() function to enter text in text boxes and quit() function to close the browser.
	* Use switch_to.frame(iFrame) and driver.switch_to.default_content() when working with the reCAPTCHA frame.




