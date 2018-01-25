from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import json

class GetTokensFromIdeaApi():
    """access_token ve refresh_token değerlerini hızlıca oluşturup geri döner."""

    appName= ""
    appRedirectUrl= ""
    appClientId=""
    appClientSecret=""
    appCode=""

    def __init__(self, base_url,driver_path):
        self.base_url = base_url
        self.driver_path = driver_path
        self.browser = webdriver.Chrome(executable_path=self.driver_path)

    def open_url(self,url):
        self.url = url
        self.browser.get(self.base_url+self.url)
        time.sleep(1)

    def login_admin_panel(self,username,password):
        (self.browser.find_element_by_id("username")).send_keys(username)
        (self.browser.find_element_by_id("pass")).send_keys(password)
        (self.browser.find_element_by_name("Submit")).click()

    def add_new_client(self):
        self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_GridData"]/div[1]/div[1]/div[3]/a').click();
        time.sleep(1)
        self.browser.find_element_by_id("name").send_keys("Test")
        self.browser.find_element_by_id("redirect_uri").send_keys(self.base_url+"/info.html")
        self.browser.find_element_by_id("buton1").click()
        time.sleep(1)


    def add_permission(self):
        # izin sayfasına git
        self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_Row0-Column5"]/a').click()
        time.sleep(1)
            #İzin ekle
        self.browser.find_element_by_xpath('//*[@id="Grid_client_permission_grid_GridData"]/div[3]/div[1]/div[3]/a').click();
        time.sleep(1)
            # Kullanıcı adı seç
        selectUser = Select(self.browser.find_element_by_id('userId'))
        selectUser.select_by_visible_text('yonetici')
            # Katalog izni
        selectCatalog = Select(self.browser.find_element_by_id('catalog'))
        selectCatalog.select_by_visible_text('Okuma/Yazma')
            # Order izni
        selectOrder = Select(self.browser.find_element_by_id('order'))
        selectOrder.select_by_visible_text('Okuma/Yazma')
            # Diğer İzinler
        selectOthers = Select(self.browser.find_element_by_id('others'))
        selectOthers.select_by_visible_text('Okuma/Yazma')
            # Kaydet butonuna bas
        self.browser.find_element_by_xpath('//*[@id="buton1"]').click()

    def get_app_info(self):
        self.appName = self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_Row0-Column1"]').text
        self.appRedirectUrl = self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_Row0-Column2"]').text
        self.appClientId = self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_Row0-Column3"]').text
        self.appClientSecret = self.browser.find_element_by_xpath('//*[@id="Grid_client_grid_Row0-Column4"]').text

    def get_code(self):
        # Code almak için istek atıyoruz.
        self.browser.get(self.base_url+"/admin/user/auth?client_id="+self.appClientId+"&state=deneme&redirect_uri="+self.appRedirectUrl+"&response_type=code")
        time.sleep(1)
        # Uygulamaya İzin veriyoruz.
        self.browser.find_element_by_xpath('//*[@id="content"]/div/form/input[7]').click()
        time.sleep(1)
        # Gelen code değerini alıyoruz.
        self.appCode = (self.browser.current_url).split("code=")[1]

    def get_tokens(self):
        # Token Alıyoruz.
        self.browser.get(self.base_url+"/oauth/v2/token?client_id="+self.appClientId+"&client_secret="+self.appClientSecret+"&grant_type=authorization_code&code="+self.appCode+"&redirect_uri="+self.appRedirectUrl)
        # Token json geldiği için ayıklıyoruz.
        jsonVar = json.loads(self.browser.find_element_by_tag_name('body').text)
        for k, v in jsonVar.items():
            if k == "refresh_token":
                print(k," : ",v)
            if k == "access_token":
                print(k," : ",v)

    def close_connection(self):
        self.browser.close()

## Başlıyoruz.
testaa01 = GetTokensFromIdeaApi("https://test.myideasoft.com","/home/sinan/Downloads/selenium/chromedriver")
testaa01.open_url("/admin")
testaa01.login_admin_panel("yonetici","1234567")
testaa01.open_url("/admin/client/list")
testaa01.add_new_client()
testaa01.add_permission()
testaa01.open_url("/admin/client/list")
testaa01.get_app_info()
testaa01.get_code()
testaa01.get_tokens()
testaa01.close_connection()
