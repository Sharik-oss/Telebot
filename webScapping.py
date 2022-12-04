from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = 'chromedriver'
driver = webdriver.Chrome(PATH)

driver.get("https://ss.ge/ka/udzravi-qoneba/l/bina?MunicipalityId=96&CityIdList=96&PrcSource=1")

driver.implicitly_wait(5)


def searching(text):
    search = driver.find_element(By.ID, "query")
    search.send_keys(text)
    search.send_keys(Keys.RETURN)
    print("searching...")
    all_info = []
    try:
        article = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.ID, 'latest_articles'))
        )
        time.sleep(5)
        elements = article.find_elements(By.CLASS_NAME, 'latest_article_each')
        print(type(elements), len(elements))
        for element in elements:
            title = element.find_element(By.CLASS_NAME, 'TiTleSpanList')
            price = element.find_element(By.CLASS_NAME, 'latest_price')

            if price.text == '':
                continue
            else:
                info = str(title.text) + ' ' + str(price.text)
                all_info.append(info)
        print(all_info)
        search.clear()
        return all_info

    except ConnectionError:
        driver.quit()