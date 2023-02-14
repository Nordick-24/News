import time
import pyperclip
from selenium.webdriver.common.by import By


result = [False, False]

def translate(text: str, haveToDelete: bool, translate_input, driver) -> str:
    """  Translate input text  """
    if result[1] is False:
        translate_input.send_keys(text)
        time.sleep(0.7)
        copy_answer = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/div[2]
        /div[3]/c-wiz[2]/div/div[8]/div/div[4]/div[2]/span[2]/button/div[3]
            """)
        copy_answer.click()
        answer = pyperclip.paste()
        haveToDelete = True

        result[0] = answer
        result[1] = True

    else:
        delete_old_translation = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]/
        div[2]/div[3]/c-wiz[1]/div[1]/div/div/span/button/div[3]
        """)
        delete_old_translation.click()
        translate_input.send_keys(text)
        time.sleep(5)
        copy_answer = driver.find_element(By.XPATH, """
        /html/body/c-wiz/div/div[2]/c-wiz/div[2]/c-wiz/div[1]
        /div[2]/div[3]/c-wiz[2]/div/div[8]/div/div[4]/div[2]/
        span[2]/button/div[3]
        """)
        copy_answer.click()
        answer = pyperclip.paste()

        result[0] = answer
        result[1] = True
