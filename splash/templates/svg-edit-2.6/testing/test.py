from selenium import webdriver
import re
x = 0;
y = 0;

driver = webdriver.Chrome();
driver.get("http://www.yale.edu/ymso/dummy/svg-edit-2.6/svg-editor.html?extensions=ext-beacon.js");


# Test 1
driver.find_element_by_id("ibeacon").click();
driver.find_element_by_id("svgroot").click();
test1 = driver.execute_script("return svgCanvas.getSvgString();");
print("Test 1, verify iBeacon button works in svg-edit.");
if "svg_1" in test1:
	print("Test 1 passed.");
	x = x + 1;
else:
	print("Test 1 failed.");
	y = y + 1;

print "Summary:"
print "{0} tests passed".format(x)
print "{0} tests failed".format(y)
driver.quit();

