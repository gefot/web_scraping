from selenium import webdriver
from time import sleep


class Insta_App:

    def __init__(self, username, password, path):
        self.username = username
        self.password = password
        self.path = path
        self.driver = webdriver.Chrome('D:\_gfot\chromedriver')
        self.main_url = 'https://www.instagram.com'
        # self.main_url = 'https://www.instagram.com/accounts/login/?source=auth_switcher'
        self.driver.get(self.main_url)

    def login(self):
        # Show login screen
        login_button = self.driver.find_element_by_link_text('Log in')
        # login_button = self.driver.find_element_by_xpath("//div[@class='gr27e']/p[@class='izU2O']/a")
        login_button.click()
        sleep(2)

        # Login to instagram account
        username_textbox = self.driver.find_element_by_xpath("//div[@class='f0n8F ']/input[@name='username']")
        username_textbox.send_keys(self.username)
        password_textbox = self.driver.find_element_by_xpath("//div[@class='f0n8F ']/input[@name='password']")
        password_textbox.send_keys(self.password)
        password_textbox.submit()
        sleep(3)

        # Select 'Not Now' for notification popup (if there)
        try:
            self.driver.find_element_by_xpath("//button[text()='Not Now']").click()
        except:
            pass


    def select_target_profile(self, target_username):
        target_url = self.main_url + '/' + target_username
        self.driver.get(target_url)

# driver = webdriver.Chrome('D:\_gfot\chromedriver')
# driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
# soup = BeautifulSoup(driver.page_source,'lxml')
# # print(soup.prettify())
#
# signup_button = driver.find_element_by_xpath("//span[@id='react-root']//p[@class='izU2O']/a")
# signup_button.click()


if __name__ == '__main__':
    insta_app = Insta_App('fotgio@hotmail.com', 'xxxxx', 'D:\_gfot\PyCharmProjects\web_scraping\insta_data')
    insta_app.login()
    insta_app.select_target_profile('_gfot')

    input('Press any key to continue')
    insta_app.driver.close()



