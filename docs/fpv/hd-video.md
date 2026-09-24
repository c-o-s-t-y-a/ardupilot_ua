# Системи HD-відео для FPV

> Оригінал: [High Definition Live Video FPV Systems](https://ardupilot.org/copter/docs/common-video-landingpage.html)

У цьому розділі описано системи живого відео, що передають відео FPV (вигляд від першої особи) високої чіткості (HD) з апарата на наземну станцію або в FPV-окуляри. Про інші системи FPV стандартної чіткості (SD) див. розділ [FPV](index.md).

## Система передачі HD-відео Herelink

![herelink](https://ardupilot.org/copter/_images/herelink.jpg)

### Огляд

Herelink — інтегрована система, що поєднує пульт, наземну станцію і бездротову цифрову передачу; розроблена для використання з Cube та іншими autopilot (автопілот) на firmware (прошивка) ArduPilot або PX4.

Більше про Herelink — на [сторінці Herelink](https://ardupilot.org/copter/docs/common-herelink.html) *(ще не перекладено)*.

---

## Система передачі HD-відео і радіокерування CUAV серії H16

![h16](https://ardupilot.org/copter/_images/cuav-video/h16.jpg)

### Огляд

Розумний пульт H16 — канал зв'язку для БПЛА, що поєднує радіокерування, передачу даних і передачу HD-відео. Він працює на операційній системі Android і підтримує поширені наземні станції, як-от QGC; як і на Android-телефон, на нього можна встановлювати інші Android-застосунки на свій розсуд.

### Можливості

- Працює на ОС Android.
- Кольоровий РК-екран 7 дюймів.
- Вбудована цифрова система передачі, яка одночасно передає HD-відео, дані дрона й сигнали радіокерування.
- Може запускати наземну станцію QGC (QGroundControl), причому можна встановити будь-яку версію QGC, не чекаючи випуску спеціально адаптованої наземної станції.
- Чотири трипозиційні перемикачі й дві ручки-регулятори краще відповідають потребам промислового застосування: можна легко керувати допоміжним обладнанням на БПЛА.
- HD-відео 1080P.
- Дисплей високої чіткості з яскравістю 2000 ніт, тож дані добре видно на сонці.
- Передача telemetry (телеметрія) і відео на інші пристрої через WIFI.
- Подібний до смартфона: можна встановити велику кількість Android-застосунків.
- Можна одночасно під'єднати камеру MIPI і камеру HDMI.
- Надвелика дальність передачі — 30 км.

Докладніше — за посиланнями нижче:

- [Документація CUAV](https://doc.cuav.com) *(в оригіналі посилання без https://)*
- [Магазин CUAV](https://store.cuav.net/index.php?id_product=125&rewrite=cuav-h16-pro-hd-video-transmission-system&controller=product)

---

## Цифрова FPV-система DJI

![DJI_FPV](https://ardupilot.org/copter/_images/DJI_FPV.jpg)

Інструкції з налаштування OSD (накладення даних на відео) в окулярах DJI див. на сторінці [MSP OSD](msp-osd.md).

### Огляд

<!-- terms-ignore: FPV -->
Цифрову систему DJI Digital FPV System створено для дрон-рейсингу. Вона складається з повітряного модуля DJI FPV Air Unit Module, камери DJI FPV Camera, окулярів DJI FPV Goggles і пульта DJI FPV Remote Controller.

### Можливості

- Вхід MSP telemetry
- 5 ГГц, 8 каналів
- Режим низької затримки 720p/120 кадр/с: <28 мс
- Режим високої якості 720p/60 кадр/с: <40 мс
- Максимальна дальність передачі: до 4 км

Більше — на сайті [DJI](https://www.dji.com) *(в оригіналі посилання без https://)*.

---

## Повітряна система DJI OcuSync

![DJI_Ocustnc](https://ardupilot.org/copter/_images/DJI_Ocustnc.jpg)

DJI OcuSync Air System — інтегроване рішення для передачі відео високої роздільності, що складається з камери, повітряного модуля Air Unit, трьох антен та інших з'єднувачів. Разом з окулярами DJI Goggles RE система OcuSync Air System підтримує бездротову передачу відео, зображень і даних autopilot.

Повітряний модуль Air Unit можна встановити на гоночні дрони, моделі літаків, RC-машинки або безпілотні апарати для рятувальних операцій та інспекцій; з firmware V01.05.00 і новішої він підтримує вхід telemetry як MSP, так і MAVLink.

### Можливості

- Вхід telemetry MAVLink і MSP
- Двочастотна передача 2,4 ГГц / 5,8 ГГц
- FHSS і до 19 фіксованих каналів
- Передача відео високої роздільності до 1280×960 при 50 кадр/с
- Мінімальна затримка: від 50 мс (при 480p і 50 кадр/с)
- Максимальна дальність передачі: до 7 км (2,4 ГГц, за нормами FCC, без перешкод)

Більше — на сайті [DJI](https://www.dji.com) *(в оригіналі посилання без https://)*.

---

## Sky-Drones Smartlink

![Sky_Link](https://ardupilot.org/copter/_images/Sky_Link.png)

Smartlink — широкосмуговий цифровий канал передачі даних із вбудованим бортовим комп'ютером, що підтримує до двох каналів HD-відео, telemetry MAVLink і керування з наднизькою затримкою та дальністю до 20 км.

### Можливості

- Сумісний з MAVLink
- 2,4 ГГц / до 1000 мВт, налаштовується
- 2 HDMI, Full HD до 1080p / 60 кадр/с
- Дальність передачі: 20 км FCC / 10 км
- LTE-зв'язок як опція
- Супутниковий зв'язок як опція

Більше — на [сайті](https://sky-drones.com/smartlink) Sky-Drones.

Відео з розпакуванням — [тут](https://www.youtube.com/watch?v=2qtE4nuTXKU).

Купити — [онлайн](https://sky-drones.com/telemetry/smartlink-set.html).

---

## SIYI AK28

![SIYI_AK28](https://ardupilot.org/copter/_images/SIYI_AK28.png)

Система HD-відео/радіокерування/telemetry на 2,4 ГГц на основі ОС Android, на яку, крім звичайних програм наземних станцій, як-от QGC, можна встановлювати й використовувати багато інших Android-застосунків.

Окрім звичайного радіокерування, система може керувати додатковим обладнанням на апараті через допоміжні канали керування.

Докладніше, зокрема посібники, — на [сайті SIYI](http://en.siyi.biz/en/ak28/overview).

### Де купити

- [RC Hobby Japan](https://www.rchobby-jp.com/index.php?main_page=product_info&cPath=67&products_id=4455)
- [Holybro](http://www.holybro.com/product/siyi-ak28-android-smart-remote-controller/)

### Відео з розпакуванням

- [Відео на YouTube](https://www.youtube.com/watch?v=DPHKe86SiqI)

---

## XBLink Plus

[![XBLink Plus](https://cdn-images.xbstation.com/only_xblink_plus.png)](https://xbstation.com/store/xblink-plus)

### Огляд

XBLink 4G Plus — апаратне рішення «підключи й працюй» для польотів БПЛА поза прямою видимістю (BVLOS), що забезпечує безперебійне керування, захищену передачу даних і якісне потокове відео. Сумісне з багатьма платформами й корисними навантаженнями, розроблене для розширення можливостей систем БПЛА у професійному застосуванні, добре поєднується з CubePilot.

### Можливості

- Керування БПЛА через Mission Planner і QGroundControl
- Підтримувані платформи: MacOS, Windows, Android
- Сумісне з MAVLink
- Потокове HD-відео
- Сумісне з Herelink, Siyi та іншими системами пультів
- Керування другим пілотом
- RTK NTRIP через 4G
- Підтримка різних корисних навантажень для систем БПЛА, зокрема USB-камер, IP-камер, RTK GPS тощо
- Керування камерами Sony
- Керування підвісами Gremsy

Більше про XBLink — на [XBStation](https://xbstation.com/store/xblink-plus).

## Інші системи

- [SkyViper video](https://discuss.arduPilot.org/t/using-the-skyviper-sonix-board-with-any-pixhawk/23932)
- [Wifi Broadcast](https://github.com/bortek/EZ-WifiBroadcast/wiki)
- [SkyDriod T12](https://www.heliengadin.com/products/skydroid-t12-remote-controller-with-digital-video)
