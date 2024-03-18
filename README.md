# Borsabotu2
Fully autonomous stock market bot in development




README
Bu kod, Python programlama dili kullanılarak Selenium ve BeautifulSoup kütüphaneleriyle geliştirilmiştir. Temel amacı, belirli bir finansal veri sitesinden veri çekmek ve kullanıcının belirlediği hisse senedinin kar durumunu hesaplamaktır.

Nasıl Çalışır?
Gerekli Kütüphaneler: Bu kodun çalışması için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

selenium
requests
BeautifulSoup
smtplib
pyautogui (isteğe bağlı)
Web Tarayıcı Ayarları: Kod, Google Chrome tarayıcısını otomatize etmek için Selenium kullanır. Bu nedenle, bilgisayarınızda Google Chrome ve ChromeDriver'ın yüklü olması gerekmektedir.

Kodun Adımları:

İlk olarak, kullanıcıdan ilgilendiği hisse senedini, alış fiyatını, lot sayısını ve Fintables hesabı bilgilerini (kullanıcı adı ve şifre) alır.
Ardından, belirtilen Fintables web sitesine oturum açar ve hisse senedi arama kutusuna girilen değeri yazarak arama yapar.
Son olarak, hisse senedinin anlık fiyatını alır, alış fiyatıyla karşılaştırır ve hesaplanan karı kullanıcıya gösterir.
Kullanım
Kodu çalıştırmak için Python yüklü olmalıdır.
Kodu çalıştırmadan önce, gerekli kütüphanelerin yüklü olduğundan emin olun.
Kod içinde belirtilen adımları izleyerek, gerekli giriş bilgilerini sağlayın ve ilgilendiğiniz hisse senedi için bilgileri girin.
Kodu çalıştırın ve sonucu bekleyin.
Örnek
Aşağıda bir örnek kullanım verilmiştir:

python
Copy code
python main.py
Notlar
Bu kodun düzgün çalışabilmesi için internet bağlantısına ihtiyaç vardır.
Fintables hesabınızın doğru giriş bilgilerini sağladığınızdan emin olun.
Kod, belirli bir web sitesine bağlı olduğu için web sitesinin yapısındaki değişiklikler kodun işleyişini etkileyebilir.
