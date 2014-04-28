# This is a complete workflow test for the program. It is meant to be run locally,
# since it is not meant to test server errors due to conenction. Remember to
# run reset.py before testing.

from selenium import webdriver
from selenium.webdriver.support.ui import Select

import re
import atexit

x = 1
totalTests = 9

def ender():
	if x == 9:
		print "All tests passed!"
	else:
		print "Failed at test {0}".format(x)
	
atexit.register(ender)

driver = webdriver.Chrome();
driver.get("http://localhost:5000/")

# Test 1: login button
driver.find_element_by_css_selector("a[href=\"/user/login\"]").click()
assert driver.title == "parsnip | Login"
x+=1

# Test 2: registration button
driver.find_element_by_css_selector("a[href=\"/user/register\"]").click()
assert driver.title == "parsnip | Register"
x+=1

# Test 3: registration on an existing company
newEmail = "tester@yale.edu"
newPassword = "helloworld"
driver.find_element_by_name("firstname").send_keys("Testy")
driver.find_element_by_name("lastname").send_keys("Tester")
driver.find_element_by_name("email").send_keys(newEmail)
driver.find_element_by_name("password").send_keys(newPassword)
driver.find_element_by_name("password2").send_keys(newPassword)
driver.find_element_by_css_selector("#select2-chosen-1").click()
driver.find_element_by_css_selector("#select2-result-label-2").click()
driver.find_element_by_css_selector(".sign-up-button").click()
x+=1

# Test 4: login of existing account
driver.get("http://localhost:5000/user/login")
driver.find_element_by_name("email").send_keys("pranav.maddi@yale.edu")
driver.find_element_by_name("password").send_keys("goodbyeworld")
driver.find_element_by_css_selector(".sign-up-button").click()
assert driver.title == "parsnip | Dashboard"
x+=1

# Test 5: accepting request to join company
driver.find_element_by_css_selector(".notifications-menu").click()
driver.find_element_by_css_selector(".approve-store").click()
x+=1

# Test 6: logout button
driver.find_element_by_css_selector("#dropdown-for-user-info").click()
driver.find_element_by_css_selector("a[href=\"/user/logout\"]").click()
assert driver.title == "parsnip | Login"
x+=1

# Test 7: new account
driver.find_element_by_name("email").send_keys(newEmail)
driver.find_element_by_name("password").send_keys(newPassword)
driver.find_element_by_css_selector(".sign-up-button").click()
assert driver.title == "parsnip | Dashboard"
x+=1

# Test 8: svg-editor button
driver.find_element_by_css_selector("a[href=\"/floorplan/my-floorplans\"]").click()
assert driver.title == "parsnip | Modify Floorplan"
driver.find_element_by_css_selector("a[href=\"/floorplan/edit-floorplan/1\"]").click()
driver.find_element_by_id("ibeacon").click()
driver.find_element_by_id("svgroot").click()
svgString = driver.execute_script("return svgCanvas.getSvgString();")
assert "beacon=\"yes\"" in svgString
x+=1
	
driver.quit();


