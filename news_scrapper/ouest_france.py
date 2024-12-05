from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException

from news_scrapper.website_driver import WebsiteDriver

class OuestFrance(WebsiteDriver):
    def __init__(self, home: str="https://www.ouest-france.fr/", driver:webdriver = webdriver.Chrome() ):
        super().__init__(home=home, driver=driver)

    def validate_cookies(self):
        try:
            button_xpath = "//*[@id='didomi-notice-agree-button']"
            self.driver.find_element(By.XPATH, button_xpath).click()
        except (ElementNotInteractableException, NoSuchElementException):
            pass

    def _get_main_page_articles(self) -> None:
        news_path = self.home + "actualite-en-continu/"
        free_articles_xpath = "//*[@class='su-title titre  ']"
        reserved_article_xpath = "//*[@class='su-title titre  monet ']"

        self.driver.get(news_path)
        for xpath in [free_articles_xpath, reserved_article_xpath]:
            for article in self.driver.find_elements(By.XPATH, xpath):
                self.articles.append(article.text)

    def _get_archives_articles(self) -> None:
        archives_path = self.home + "actualite-en-continu/archives/"
        all_articles_xpath = "//*[@class='su-title titre  ']"

        self.driver.get(archives_path)
        for articles in self.driver.find_elements(By.XPATH, all_articles_xpath):
            self.articles.append(articles.text)

    def _clear_rubric_in_article_title(self) -> None:
        # Todo : change implementation to regexp
        prefixes_to_clean = ["ENTRETIEN. ", "SONDAGE. ", "  DIRECT. ", "REPORTAGE. ", "POINT DE VUE. ", "VIDÉO. ", "COMMENTAIRE. ", "INFOGRAPHIES. ", "INFOGRAPHIES. "]
        for prefix in prefixes_to_clean:
            for index, article in enumerate(self.articles):
                if article.startswith(prefix):
                    self.articles[index] = article.replace(prefix, "")

    def _clear_newline_in_article_title(self) -> None:
        # Todo : change implementation to regexp, using newline as a selector
        prefixes_new_line_to_clean = ["REPORTAGE", "DÉCRYPTAGE", "ACTU", "RENCONTRE"]
        for prefix in prefixes_new_line_to_clean:
            for index, article in enumerate(self.articles):
                if article.startswith(prefix):
                    article = article.split(" ")
                    self.articles[index] = " ".join(article[1:])

    def get_all_articles_titles(self) -> None:
        self._get_main_page_articles()
        self._get_archives_articles()

    def clear_titles(self) -> None:
        self._clear_rubric_in_article_title()
        self._clear_newline_in_article_title()


if __name__ == "__main__":
    ouest_france = OuestFrance()
    ouest_france.get_home()
    ouest_france.validate_cookies()
    ouest_france.get_all_articles_titles()
    ouest_france.clear_titles()
    for i in ouest_france.articles:
        print(f"article = '{i}'")
