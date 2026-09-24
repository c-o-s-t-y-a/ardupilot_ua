# Вибір GCS (наземної станції керування)

> Оригінал: [Choosing a Ground Station](https://ardupilot.org/copter/docs/common-choosing-a-ground-station.html)

Ця сторінка дає загальний огляд доступних GCS (наземна станція керування) і посилання на них, щоб ви могли зробити правильний вибір.

## Огляд

GCS — зазвичай програма, що працює на комп'ютері, телефоні чи RC transmitter (пульт радіокерування) на землі й обмінюється даними з вашим БПЛА через [бездротову telemetry (телеметрія)](telemetry.md) або USB-кабель. Вона показує в реальному часі дані про роботу і позицію БПЛА і може слугувати «віртуальною кабіною» з багатьма тими ж приладами, що були б у вас у справжньому літаку. GCS можна також використовувати для керування БПЛА в польоті, завантаження нових команд місії і встановлення параметрів. Часто її використовують і для перегляду відео з камер БПЛА в реальному часі.

GCS також потрібна, щоб налаштувати конфігурацію autopilot (автопілот) перед використанням і оновлювати firmware (прошивка) autopilot.

Існує щонайменше десять різних GCS. Для настільних комп'ютерів є *Mission Planner*, *APM Planner 2*, *MAVProxy*, *QGroundControl*, *UgCS* і *LOGOS*. Для планшетів/смартфонів — *QGroundControl*, *Tower* (DroidPlanner 3), *MAVPilot*, *AndroPilot* і *SidePilot*, які можна використовувати для зв'язку з ArduPilot.

Вибір конкретної GCS часто залежить від вашого апарата і бажаної обчислювальної платформи:

- Користувачі **готових до польоту** апаратів можуть віддати перевагу портативності й простоті *QGroundControl* чи іншої GCS на планшеті або телефоні.
- Користувачам **самозбірних апаратів/наборів** і розробникам часто потрібні інструменти налаштування й аналізу, тож їм знадобиться (принаймні спочатку) *Mission Planner*, *QGroundControl*, *APM Planner 2* чи інша повнофункціональна GCS.
- **Розробники коду** оцінять деякі можливості *MAVProxy*.

## GCS для настільних комп'ютерів

### Mission Planner

Повнофункціональна і широко вживана GCS.

- **Платформа**: Windows, Mac OS X (через Mono)
- **Ліцензія**: [відкритий код](https://github.com/ArduPilot/MissionPlanner/blob/master/COPYING.txt) (GPLv3)

![MP-FP-Screen](https://ardupilot.org/copter/_images/MP-FP-Screen.jpg)

- [Завантажити](https://firmware.ardupilot.org/Tools/MissionPlanner/MissionPlanner-latest.msi)
- [Вікі](https://ardupilot.org/planner/)
- [Форум підтримки](https://discuss.ardupilot.org/c/ground-control-software/mission-planner)
- [Список проблем](https://github.com/ArduPilot/MissionPlanner/issues)
- [Вихідний код](https://github.com/ArduPilot/MissionPlanner)

### APM Planner 2.0

GCS для macOS, Linux і Windows. Порівняно з іншими має меншу аудиторію і менший набір функцій.

- **Платформа**: Windows, macOS, Linux
- **Ліцензія**: [відкритий код](https://github.com/ArduPilot/apm_planner/blob/master/license.txt) (GPLv3)

    ![planner2_choose_agcs](https://ardupilot.org/copter/_images/planner2_choose_agcs.jpg)

- [Вікі](https://ardupilot.org/planner2/)
- [Форум підтримки](https://discuss.ardupilot.org/c/ground-control-software/apm-planner-2-0)
- [Список проблем](https://github.com/ArduPilot/apm_planner/issues)
- [Вихідний код](https://github.com/ArduPilot/apm_planner)

### MAVProxy

GCS для Linux, яку часто використовують розробники коду. Насамперед інтерфейс командного рядка з графічними модулями для карти й редагування місій. Написана на Python і розширюється модулями Python.

- **Платформа**: Linux
- **Ліцензія**: [відкритий код](https://github.com/tridge/MAVProxy/blob/master/COPYING.txt) (GPLv3)

![mavproxy_linux](https://ardupilot.org/copter/_images/mavproxy_linux.jpg)

- [Вікі](https://ardupilot.org/mavproxy/)
- [Список проблем](https://github.com/ArduPilot/MAVProxy/issues)
- [Вихідний код](https://github.com/ArduPilot/MAVProxy)

### QGroundControl

QGroundControl працює з autopilot, що підтримують MAVLink, зокрема з ArduPilot. Серед GCS вона унікальна тим, що працює на всіх платформах — настільних і мобільних.

- **Платформа**: Windows, Mac OS X, Linux, Android та iOS
- **Ліцензія**: [відкритий код](http://www.qgroundcontrol.org/license) (GPLv3)

![QGroundControlTabletImage](https://ardupilot.org/copter/_images/QGroundControlTabletImage.jpg)

- [Вебсайт](http://qgroundcontrol.com/)
- [Форум підтримки](https://discuss.px4.io/c/qgroundcontrol/15)

### UgCS — Universal Ground Control Station

Універсальна і проста у використанні GCS з 3D-інтерфейсом. Підтримує APM, Pixhawk, а також дрони інших виробників, як-от DJI, Mikrokopter тощо. Призначена як для ентузіастів, так і для професіоналів. Уміє одночасно обмінюватися даними з кількома дронами і керувати ними.

<!-- terms-ignore: receiver -->
UgCS підтримує кілька шарів карти, а також різних постачальників карт. Серед можливостей UgCS — імпорт DEM, підтримка транспондерів і приймачів ADS-B, режим Click & Go, режим джойстика, геотегування зображень і запис відео. UgCS також має програвач telemetry, що дає змогу переглядати всі польоти.

UgCS має вбудовані заборонені для польотів зони навколо всіх великих аеропортів, а також дає змогу створювати власні заборонені зони.

Підтримує встановлення з кількома вузлами, тобто кількох пілотів з ноутбуками UgCS у полі можна підключити до центрального сервера керування.

- **Платформа**: Windows, Mac OS X, Ubuntu
- **Ліцензія**: пропрієтарна, є також безкоштовна ліцензія (UgCS Open)
- [Вебсайт UgCS](http://www.ugcs.com)
- [Група DIY Drones для користувачів UgCS](https://diydrones.com/group/ugcs)
- [Репозиторій UgCS на Github](https://github.com/ugcs)

### LOGOS

<!-- terms-ignore: bind -->
GCS, створена для спрощення планування складних місій, що включають сканування територій, фото- і відеозйомку. Має режим 3D-перегляду, прив'язку до фізичних споруд і вбудований симулятор, що допомагає краще уявити заплановані місії.

- **Платформа**: Windows
- **Ліцензія**: пропрієтарна. Можна користуватися безкоштовно, але розширені функції недоступні без покупки.

![LOGOS_GCS](https://ardupilot.org/copter/_images/LOGOS_GCS.png)

- [Завантажити](https://aerologos.by/download)
- [Вебсайт](https://aerologos.by/)
- [Youtube](https://www.youtube.com/@AerologosBusinessAccount/)

## Мобільні GCS

### QGroundControl

QGroundControl працює з autopilot, що підтримують MAVLink, зокрема з ArduPilot. Серед GCS вона унікальна тим, що працює на всіх платформах — настільних і мобільних.

- **Платформа**: Windows, Mac OS X, Linux, Android та iOS
- **Ліцензія**: [відкритий код](http://www.qgroundcontrol.org/license) (GPLv3)

![QGroundControlTabletImage](https://ardupilot.org/copter/_images/QGroundControlTabletImage.jpg)

- [Вебсайт](http://qgroundcontrol.com/)
- [Форум підтримки](https://discuss.px4.io/c/qgroundcontrol/15)

### Tower

Tower (він же «DroidPlanner 3») — GCS для телефонів і планшетів на Android. Призначена для кінцевих користувачів і ентузіастів, має такі функції, як follow-me, «dronies» (тобто «селфі», але зняті дроном) і спеціальні місії для 3D-картографування.

- **Платформа**: телефони й планшети на Android
- **Ліцензія**: [відкритий код](https://github.com/DroidPlanner/Tower/blob/develop/LICENSE.md) (GPLv3)

![tower_droid_planner3_structure_scan](https://ardupilot.org/copter/_images/tower_droid_planner3_structure_scan.jpg)

- [Завантажити Tower](https://play.google.com/store/apps/details?id=org.droidplanner.android) (і [3DR Services](https://play.google.com/store/apps/details?id=org.droidplanner.services.android)) з Google Play.
- [Список сумісних пристроїв Android](https://github.com/arthurbenemann/droidplanner/wiki/Compatible-Devices)
- [Вікі](https://github.com/DroidPlanner/Tower/wiki)
- [Форум підтримки](https://discuss.ardupilot.org/c/ground-control-software/tower)
- [Список проблем](https://github.com/DroidPlanner/Tower/issues)
- [Вихідний код](https://github.com/DroidPlanner/droidplanner)

> **Примітка.** Старі версії ([DroidPlanner 2](https://play.google.com/store/apps/details?id=org.droidplanner) і [Droid Planner 1](https://play.google.com/store/apps/details?id=com.droidplanner)) також можна завантажити з Google Play.

### MAV Pilot 1.4

GCS у кишені, що підтримує переважно autopilot ArduPilot на iPhone/iPad. Підтримує типи апаратів Plane, Copter і Rover.

Як підключити її до autopilot — див. на вебсайті.

- **Платформа**: iPhone, iPad
- **Ліцензія**: пропрієтарна

![MAVPilot_1.4](https://ardupilot.org/copter/_images/MAVPilot_1.4.png)

- [Анонс релізу, блог і обговорення](https://diydrones.com/profiles/blogs/mav-pilot-1-4-for-iphone-released)
- [Блог підтримки](http://www.communistech.com/support/)
- [Форум підтримки](http://www.communistech.com/forums/)
- [Посилання на iTunes Store](https://itunes.apple.com/ca/developer/communis-tech/id649232032)

### SidePilot

Сумісна з ArduPilot GCS для iPhone/iPad.

Як підключити її до autopilot — див. на вебсайті.

- **Платформа**: iPhone, iPad
- **Ліцензія**: пропрієтарна

![sidepilot](https://ardupilot.org/copter/_images/sidepilot.jpg)

- [Анонс релізу, блог і обговорення](https://diydrones.com/profiles/blogs/sidepilot-app-version-1-1-formerly-imavlink)
- [Вебсайт](http://sidepilot.net)
- [Форум підтримки](http://sidepilot.net/forum)
- [Посилання на iTunes Store](https://itunes.apple.com/us/app/sidepilot/id1138193193?ls=1&mt=8)

### AndroPilot

GCS для Android, призначена для ентузіастів.

> **Примітка.** AndroPilot активно не розробляється. Її придатність для новіших версій firmware потребує перевірки.

- **Платформа**: телефони й планшети на Android
- **Ліцензія**: [відкритий код](https://github.com/geeksville/arduleader/blob/master/LICENSE.md) (GPLv3)

![Andropilot_-_Android_Apps_on_Google_Play](https://ardupilot.org/copter/_images/Andropilot_-_Android_Apps_on_Google_Play.jpg)

- [Завантажити (Google Play)](https://play.google.com/store/apps/details?id=com.geeksville.andropilot)
- [Список сумісних пристроїв Android](https://github.com/geeksville/arduleader/wiki/Android%20Device%20Compatibility%20List)
- [Вікі](https://github.com/geeksville/arduleader/wiki)
- [Форум підтримки](https://discuss.ardupilot.org/c/ground-control-software/other-gcs)
- [Список проблем](https://github.com/geeksville/arduleader/issues)
- [Вихідний код](https://github.com/geeksville/arduleader/tree/master/andropilot)

## Додаткове обладнання для GCS

### Android

Для пристроїв Android знадобиться:

- Планшет чи смартфон на Android. *QGroundControl* може підключатися з телефона до autopilot через Bluetooth, WIFI або USB. Для USB пристрій має вміти працювати як USB-хост (OTG).
- Спосіб зв'язку з autopilot апарата:
    - [SiK Telemetry Radio System](https://ardupilot.org/copter/docs/common-sik-telemetry-radio.html) *(ще не перекладено)* чи інший радіомодем telemetry ([Telemetry](telemetry.md)) з кабелем OTG — для далекого зв'язку в повітрі з відповідним модулем telemetry на апараті.
    - WIFI ([ESP8266 wifi telemetry](https://ardupilot.org/copter/docs/common-esp8266-telemetry.html) *(ще не перекладено)*)
    - Bluetooth ([Bluetooth-модем telemetry](bluetooth.md))
    - для підключення через USB на столі — кабель USB OTG (зазвичай дешевше $2 на [ebay](http://www.ebay.com/sch/i.html?_trksid=m570.l3201&_nkw=usb+otg+cable&_sacat=0) і [Amazon](http://www.amazon.com/T-Flash-Adapter-Samsung-GT-i9100-GT-N7000/dp/B005FUNYSA/ref=sr_1_5?ie=UTF8&qid=1376262351&sr=8-5&keywords=android+otg+cable)).
    - Інший спосіб telemetry ([Telemetry](telemetry.md))

### iOS

Для пристроїв iOS знадобиться:

- Пристрій на iOS, як-от iPad чи iPhone. Для iPad рекомендовано версію з мобільним зв'язком — у ній краща підтримка GPS.
- Канал Wifi або Bluetooth LE до дрона.
- Міст до [SiK Telemetry Radio System](https://ardupilot.org/copter/docs/common-sik-telemetry-radio.html) *(ще не перекладено)* через Wifi або Bluetooth LE.

    Докладніше — у постачальників застосунків для iOS.

### Настільні комп'ютери (Windows/Mac/Linux)

Для настільних комп'ютерів знадобиться:

- USB-кабель, Bluetooth-модуль, WIFI-адаптер чи інший засіб зв'язку з переліку тут: [Telemetry](telemetry.md).

## Підсторінки

1. [ArduCopter MAVLink Messages](https://ardupilot.org/copter/docs/ArduCopter_MAVLink_Messages.html) *(ще не перекладено)*
