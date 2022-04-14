from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

from env.dados import LOGIN, PASSWD



class ChromeAuto():

    def __init__(self):
        self.executable_path = './drivers/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        self.chrome = webdriver.Chrome(
            self.executable_path,
            options=self.options
        )

    def access(self, url):
        self.chrome.get(url)
    
    def leave(self):
        self.chrome.quit()
    

class AccessGithub(ChromeAuto):

    def sign_in(self):
        try:
            btn_sign_in = self.chrome.find_element(By.LINK_TEXT, 'Sign in')
            btn_sign_in.click()
        except Exception:
            print('Erro ao clicar em Sign IN')

    def access(self, url="https://github.com/"):
        super().access(url)

    def login(self):
        try:
            input_login = self.chrome.find_element(By.ID, 'login_field')
            input_password = self.chrome.find_element(By.ID, 'password')
            btn_login = self.chrome.find_element(By.CSS_SELECTOR, r'[type="submit"]')
            input_login.send_keys(LOGIN)
            input_password.send_keys(PASSWD)
            sleep(1)
            btn_login.click()
        except Exception:
            print('Erro ao clicar em Login')

    def logout(self):
        try:
            menu_avatar = self.chrome.find_element(By.XPATH,'/html/body/div[1]/header/div[7]/details')
            menu_avatar.click()
            sleep(2)
            link_logout = self.chrome.find_element(By.CSS_SELECTOR, '[class*="dropdown-signout"][type="submit"]')
            link_logout.click()
        except Exception:
            print('Erro ao clicar em Logout')

if __name__ == '__main__':
    browser = AccessGithub()
    browser.access()
    sleep(5)
    browser.sign_in()
    sleep(1)
    browser.login()
    sleep(10)
    browser.logout()
    sleep(30)
    browser.leave()