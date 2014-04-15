from selenium import webdriver
import re

driver = webdriver.Chrome();
driver.get("http://www.yale.edu/ymso/dummy/svg-edit-2.6/svg-editor.html?extensions=ext-beacon.js");
driver.find_element_by_id("ibeacon").click();
driver.find_element_by_id("svgroot").click();
test1 = driver.execute_script("return svgCanvas.getSvgString();");
print(test1);
if "svg_1" in test1:
	print("yay!");
else:
	print("aww!");
driver.quit()

