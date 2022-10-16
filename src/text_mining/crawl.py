# %%
import requests
import os
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class linkedin_crwaler():
    def into_browser(self):
        self.url = "https://www.linkedin.com/jobs/search?keywords=Data%20Analysis&location=Taipei%20City%2C%20Taiwan&locationId=&geoId=111879105&f_TPR=&f_E=1&position=1&pageNum=0"
        self.driver_path = "./chromedriver"
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.url)

        self.element = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(("css selector", "h1 > span"))
        )
        self.no_of_jobs = int(self.element.get_attribute("innerText"))

        ## 以下操作是用於將網頁捲動到最下方，以便抓取所有的職缺資訊
        import tqdm
        i = 2
        for j in tqdm.tqdm(range(100)):
            while i <= int(self.no_of_jobs/25)+1:
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                i += 1
                try:
                    self.driver.find_element(By.XPATH, "/html/body/main/div/section/button").click()
                except:
                    pass
                    time.sleep(5)


    def count_jobs(self):
        self.joblists = self.driver.find_element(By.CLASS_NAME, "jobs-search__results-list")
        self.jobs = self.joblists.find_elements(By.TAG_NAME, "li")

        print(len(self.jobs))


    def get_job_info(self):
        self.job_id_list = []
        self.job_title_list = []
        self.company_name_list = []
        self.job_link_list = []

        for self.job in self.jobs:
            self.job_id = self.job.get_attribute('data-id')
            self.job_id_list.append(self.job_id)

            self.job_title = self.job.find_element(By.CSS_SELECTOR, "h3").get_attribute('innerText')
            self.job_title_list.append(self.job_title)

            self.company_name = self.job.find_element(By.CSS_SELECTOR, "h4").get_attribute('innerText')
            self.company_name_list.append(self.company_name)

            ##self.job_link = self.job.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
            ##self.job_link_list.append(self.job_link)


        self.job_descript = []

        for i in range(len(self.jobs)):
            self.job_click_path = f'/html/body/div[1]/div/main/section[2]/ul/li[{i+1}]/div/div[1]/img'
            self.job_click = self.driver.find_element(By.XPATH, self.job_click_path)
            self.driver.execute_script("arguments[0].click();", self.job_click)
            time.sleep(3)

            self.job_descript_path = '/html/body/div[1]/div/section/div[2]/div/section[1]/div/div'
            self.job_descript_list = self.job.find_element(By.XPATH, self.job_descript_path).get_attribute('innerText')
            self.job_descript.append(self.job_descript_list)



    def to_df(self):
        self.job_data = pd.DataFrame({"company name": self.company_name_list, "title": self.job_title_list, "description": self.job_descript})
        self.job_data["description"] = self.job_data["description"].str.replace('\n', '') ## 將換行字元以空格取代
        self.job_data.to_excel("/Users/abnerteng/GitHub/self-interest-in-text-mining-and-data-analysis/datas/job_data.xlsx", index = False)


if __name__ == '__main__':
    crawler = linkedin_crwaler()
    crawler.into_browser()
    crawler.count_jobs()
    crawler.get_job_info()
    crawler.to_df()
