import pandas as pd
import time
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC


def scrape_b3_data(output_file='data.parquet'):
    options = Options()
    options.add_argument('--headless')

    driver = webdriver.Chrome(options=options)
    driver.get('https://sistemaswebb3-listados.b3.com.br/indexPage/day/IBOV?language=pt-br')

    Select(driver.find_element(By.ID, 'segment')).select_by_value('2')

    wait = WebDriverWait(driver, 10)
    data_table = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))

    data = []

    while True:
        rows = data_table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')

            row_data = {
                'sector': cells[0].text,
                'code': cells[1].text,
                'action': cells[2].text,
                'action_type': cells[3].text,
                'theoretical_quantity': cells[4].text,
                'sector_percentage': cells[5].text,
                'accumulated_percentage': cells[6].text
            }

            data.append(row_data)

        try:
            driver.find_element(By.CLASS_NAME, 'pagination-next').find_element(By.TAG_NAME, 'a').click()
            time.sleep(2)
            data_table = wait.until(EC.presence_of_element_located((By.TAG_NAME, 'table')))
        except NoSuchElementException:
            # If the "next" button is not found, we're on the last page and can break the loop
            break

    driver.quit()

    data_frame = pd.DataFrame(data)
    data_frame.to_parquet(output_file)

    return output_file


if __name__ == "__main__":
    scrape_b3_data()
