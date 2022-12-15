from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

def main():
    driver = webdriver.Chrome()
    driver.get("https://webreg.burnaby.ca/webreg/Activities/ActivitiesAdvSearch.asp")

    adults_element = driver.find_element(By.XPATH, '//*[@id="browser"]/li[1]/span/a')
    adults_element.click()

    sleep(1)
    sports_element = driver.find_element(By.CSS_SELECTOR, '#browser > li.collapsable > ul > li:nth-child(14) > span > a')
    driver.execute_script("arguments[0].scrollIntoView();", sports_element)
    sports_element.click()

    sleep(1)
    last_page_element = driver.find_element(By.XPATH, '//*[@id="course-tab"]/div[2]/div/div[2]/div[2]/a[4]')
    driver.execute_script("arguments[0].scrollIntoView();", last_page_element)
    last_page_element.click()

    sleep(1)
    volleyball_table_element = driver.find_element(By.XPATH, '//*[@id="activity-1-8634"]/span[1]/a')
    driver.execute_script("arguments[0].scrollIntoView();", volleyball_table_element)
    volleyball_table_element.click()

    sleep(1)
    element = driver.find_element(By.XPATH, '//*[@id="activity-course-row"]/td[9]/table/tbody/tr[1]/td/span/a')
    print(element.id)
    element.click()
    sleep(10)

if __name__ == "__main__":
    main()

# //*[@id="browser"]/li[1]/ul/li[14]/span/a