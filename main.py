import time
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver = r"<chromedriver.exe directory>"
LINKED_IN = "https://www.linkedin.com/jobs/search/?currentJobId=3272620708&f_AL=true&keywords=python%20developer&refresh=true"

email_id = 'email'
password = 'password'

driver = webdriver.Chrome(service= Service(chrome_driver))

driver.get(LINKED_IN)
login = driver.find_element(By.XPATH, '/html/body/div[1]/header/nav/div/a[2]')
login.click()
email_entry = driver.find_element(By.NAME, 'session_key')
email_entry.send_keys(email_id)
password_entry = driver.find_element(By.NAME, 'session_password')
password_entry.send_keys(password)

#Saving only one Job
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.click()
that_job_save = driver.find_element(By.XPATH, '//*[@id="main"]/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
that_job_save.click()
thats_it = driver.find_element(By.XPATH, '//*[@id="ember96"]')
thats_it.click()
time.sleep(3)
click = None
while(click == None):
    click = WebDriverWait(driver, 3).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="ember324"]/div[2]/div[1]/div[3]/div[1]/div[1]/button/span'))
    )
click.click()