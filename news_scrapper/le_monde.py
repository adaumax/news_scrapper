from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException

from news_scrapper.website_driver import WebsiteDriver

class LeMonde(WebsiteDriver):
    def __init__(self, home="https://www.lemonde.fr/", driver=webdriver.Chrome()):
        super().__init__(home=home, driver=driver)

    def validate_cookies(self) -> None:
        button_xpath = "//button[@class='gdpr-lmd-button gdpr-lmd-button--big gdpr-lmd-button--slate-darker']"
        try :
            validate_button = self.driver.find_element(By.XPATH, button_xpath)
            validate_button.click()
        except ElementNotInteractableException:
            pass


    def get_all_articles_titles(self) -> None:
        # TODO excluded_titles = ["APPEL À TÉMOIGNAGES", "LIVE"]
        articles_xpath = "//*[@class='article__title']"

        for article in self.driver.find_elements(By.XPATH, articles_xpath):
            if article.text and not "LIVE" in article.text:
                self.articles.append(article)




if __name__ == "__main__":
    le_monde = LeMonde()
    le_monde.get_home()
    le_monde.validate_cookies()
    le_monde.get_all_articles_titles()
    for i in le_monde.articles:
        print(i.text)
    # print(le_monde.articles)
