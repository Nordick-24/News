import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import translate

import time
import pyperclip


haveToDelete = False
driver = webdriver.Firefox()
driver.get('https://translate.google.com/')

close_cookie_message = driver.find_element(By.XPATH, """
/html/body/c-wiz/div/div/div/div[2]/div[1]/div[3]/div[1]/div[1]/form[2]/div/div/button
""")
time.sleep(4)  # If browser don't load all needest, he died

close_cookie_message.click()

translate_input = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]/div[3]/c-wiz[1]/span/span/div/textarea
        """)
select_language_input = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[1]/c-wiz/div[5]/button/div[3]
        """)
select_language_input.click()

find_language = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[2]/input
        """)
find_language.send_keys('Russian')
select_russian = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[1]/c-wiz/div[2]/c-wiz/div[2]/div/div[4]/div/div[1]
        """)
select_russian.click()

del close_cookie_message, select_language_input, find_language, select_russian



def parseHackerNews() -> None:
    try:
        pageNumber = 1
        while True:
            print(f"{pageNumber}- page number")
            link = f"https://news.ycombinator.com/?p={pageNumber}"
            responce = requests.get(link).text
            soup = BeautifulSoup(responce, "lxml")

            blockAnythings = soup.find_all("tr", class_="athing")

            for title in blockAnythings:
                title = title.find_all("td", class_="title")

                for titleline in title:
                    titleline = titleline.find_all("span", class_="titleline")

                    for name in titleline:
                        name = name.find("a")

                    for link in titleline:
                        link = link.find("a").get("href")

                        if "https://github.com" not in link:
                            continue

                        for resultName in name:
                            translate.translate(resultName, haveToDelete, translate_input, driver)
                            print(pyperclip.paste())
                            print(link)
                            print("-----")

            pageNumber += 1
    except KeyboardInterrupt:
        pass

parseHackerNews()

