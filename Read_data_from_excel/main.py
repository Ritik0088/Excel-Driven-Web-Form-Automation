import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time




def run_app():
    excel_data = pd.read_excel("data1.xlsx")


    #setup selenium
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(r"file:///D:/All_work/Automation_engineer/Read_data_from_excel/index.html")
    time.sleep(1)

    #Loop through the rows
    for index, row in excel_data.iterrows():
        name=row["Name"]
        email=row["Email"]
        phone=row["Phone"]
        service=row["Service"]
        details=row["Details"]

        driver.find_element(By.ID, "full-name").send_keys(name)
        driver.find_element(By.ID, "email").send_keys(email)
        driver.find_element(By.ID, "phone").send_keys(phone)
        service_elem = driver.find_element(By.ID,"service")
        service_select= Select(service_elem)
        service_select.select_by_visible_text(service)
        driver.find_element(By.ID, "details").send_keys(details)
        time.sleep(1)
        driver.find_element(By.ID,"submit").click()
        time.sleep(1)   
    driver.quit()

if __name__ == '__main__':
    run_app()