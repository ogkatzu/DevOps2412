from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
dr = webdriver.Firefox()

try:
    dr.get(r'C:\Users\skatz\PycharmProjects\DevOps2412\tip_calc\index.html')
    billamt = dr.find_element(by="id", value="billamt")
    billamt.send_keys("100")
    dr.find_element(by="xpath", value=r'/html/body/div/div[1]/form/p[4]/select/option[3]').click()
    dr.find_element(by="id", value='peopleamt').send_keys("5")
    dr.find_element(by="id", value="musicQual").send_keys("Excellent")
    dr.find_element(by="id", value="calculate").click()
    actual = dr.find_element(by="id", value="tip").text
    expected = "9"
    assert expected == actual
    # if actual == expected:
    #     print("good")
    # else:
    #     print("not good")
    sleep(10)
finally:
     # Ensure WebDriver instance is closed even if there's an exception
     dr.quit()
