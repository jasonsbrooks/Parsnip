from selenium import webdriver
import re
passed = 0;
failed = 0;

driver = webdriver.Chrome();
driver.get("http://localhost:5000/");

# Test login button
driver.find_element_by_css_selector("a[href=\"/user/login\"]").click();
assert driver.title == "parsnip | Login"

# Test login using Pranav's account
driver.find_element_by_name("email").send_keys("pranav.maddi@yale.edu")
driver.find_element_by_name("password").send_keys("goodbyeworld")
driver.find_element_by_css_selector(".sign-up-button").click();
assert driver.title == "parsnip | Dashboard"

# Test logout button
driver.find_element_by_class_name("glyphicon glyphicon-user").click();
driver.find_element_by_css_selector("a[href=\"/user/logout\"]").click();
assert driver.title == "parsnip | Login"

# Test registration button
driver.find_element_by_css_selector("a[href=\"/user/register\"]").click();
assert driver.title == "parsnip | Register"

# Test registration
email = "tester@yale.edu"
password = "helloworld"
driver.find_element_by_name("firstname").send_keys("Testy")
driver.find_element_by_name("lastname").send_keys("Tester")
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys("helloworld")
driver.find_element_by_name("password2").send_keys("helloworld")
driver.find_element_by_css_selector(".sign-up-button").click();
assert driver.title == "parsnip | Login"
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
driver.find_element_by_css_selector(".sign-up-button").click();
assert driver.title == "parsnip | Dashboard"

# Test floormap button
driver.find_element_by_css_selector("a[href=\"/floorplan/my-floorplans\"]").click();
assert driver.title == "parsnip | "

driver.find_element_by_id("ibeacon").click();
driver.find_element_by_id("svgroot").click();
svgString = driver.execute_script("return svgCanvas.getSvgString();");
print("Test 1, verify iBeacon button works in svg-edit.");
self.assertIn("svg_1", svgString)
	

print "Summary:"
print "{0} tests passed".format(x)
print "{0} tests failed".format(y)
driver.quit();

