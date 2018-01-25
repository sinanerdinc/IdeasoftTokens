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
testaa01 = GetTokensFromIdeaApi(site,"/home/sinan/Downloads/selenium/chromedriver")
```
Instance alırken az önce indirdiğiniz chrome driver yolunu verin.

# Çalıştır

```
python3 ideashop_tokens.py --site=https://testa.myideasoft.com --u=yonetici --p=sifre123
```
şeklinde kullanabilirsiniz.
