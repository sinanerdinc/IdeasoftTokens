# IdeasoftTokens
ideasoft altyapılı sitesiniz için api client oluşturup access ve refresh token değerlerini döner.

# Kurulum

python3 üzerinde yazılmıştır. Selenium, time ve json kütüphanesini kullanır.
Python3 paket yöneticisini kurun
```
sudo apt-get install python3-pip
```
ardından selenium kurun
```
sudo pip3 install selenium
```
son olarak ise bilgisayarınızda chrome yüklü olmalı, bu chrome ile selenium kütüphanesinin iletişim kurabilmesi için
https://chromedriver.storage.googleapis.com/index.html?path=2.35/
adresinden chrome driver indirin ve zipten çıkartın.

Artık kodları kullanabilirsiniz.

```
testaa01 = GetTokensFromIdeaApi("https://test.myideasoft.com","/home/sinan/Downloads/selenium/chromedriver")
```
Instance alırken alan adı ve az önce indirdiğiniz chrome driver yolunu verin. Admin paneline girerken kullanıcı adınızı ve şifresiniz login_admin_panel methodu içine girmeyi girmeyi unutmayın.
```
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
```
