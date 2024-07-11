from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def get_ai_response(question):
    options = webdriver.EdgeOptions()
    options.headless = True
    driver = webdriver.ChromiumEdge(options = options)
    driver.get("https://iask.ai/?mode=question&options[detail_level]=concise&q={}".format(question))

    try:
        target_data = driver.find_element(By.XPATH, "/html/body/div[1]/main/div[2]/div/div[1]/section/div[1]/div[2]")
        return target_data.text
    except Exception as e:
        print(e)
    finally:
        driver.close()






