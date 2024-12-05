from selenium import webdriver

class WebsiteDriver:
    def __init__(self, home:str, driver:webdriver):
        self.driver = driver
        self.home = home
        self.articles = []

    def get_home(self) -> None:
        self.driver.get(self.home)

    def validate_cookies(self) -> None:
        raise NotImplementedError

    def get_all_articles_titles(self) -> None:
        raise NotImplementedError

    def clear_titles(self) -> None:
        raise NotImplementedError

    def record_articles(self) -> None:
        raise NotImplementedError