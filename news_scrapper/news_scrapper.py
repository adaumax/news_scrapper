from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException


class LeMonde:
    def __init__(self, driver=webdriver.Chrome()):
        self.driver = driver
        self.home = "https://www.lemonde.fr/"
        self.articles = []

    def get_home(self):
        self.driver.get(self.home)

    def validate_cookies(self):
        button_xpath = "//button[@class='gdpr-lmd-button gdpr-lmd-button--big gdpr-lmd-button--slate-darker']"
        try :
            validate_button = self.driver.find_element(By.XPATH, button_xpath)
            validate_button.click()
        except ElementNotInteractableException:
            pass


    def get_articles_titles(self):
        articles_xpath = "//*[@class='article__title']"
        for article in self.driver.find_elements(By.XPATH, articles_xpath):
            if article.text and not "LIVE" in article.text:
                self.articles.append(article)



if __name__ == "__main__":
    le_monde = LeMonde()
    le_monde.get_home()
    le_monde.validate_cookies()
    le_monde.get_articles_titles()
    for i in le_monde.articles:
        print(i.text)
    # print(le_monde.articles)
