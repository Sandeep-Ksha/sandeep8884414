import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time


# Setting up the webdriver
driver = webdriver.Chrome()

# Navigating to the login page of the website
driver.get("https://www.facebook.com/login")
time.sleep(3)

# Reading usernames and passwords from a CSV file
with open("credentials.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  

    for row in reader:
        username = row[0]
        password = row[1]

        # Finding the username and password input fields
        username_field = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[1]/input")
        password_field = driver.find_element(By.XPATH,"/html/body/div[1]/div[1]/div[1]/div/div[2]/div[2]/form/div/div[2]/div/div/input")

        # Clearing any existing values in the input fields
        username_field.clear()
        password_field.clear()

        # Entering the username and password
        username_field.send_keys(username)
        password_field.send_keys(password)

        # Submitting the login form
        password_field.send_keys(Keys.RETURN)
        time.sleep(5)


driver.close()
