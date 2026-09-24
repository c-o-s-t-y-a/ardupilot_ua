# Підключення Mission Planner до autopilot (автопілота)

> Оригінал: [Connect Mission Planner to AutoPilot](https://ardupilot.org/copter/docs/common-connect-mission-planner-autopilot.html)

Тут пояснено, як підключити *Mission Planner* до autopilot (автопілот), щоб отримувати telemetry (телеметрія) і керувати апаратом.

> **Примітка.** Підключення для [завантаження firmware (прошивка)](loading-firmware.md) описано окремо.

## Налаштування підключення

Щоб встановити з'єднання, спершу оберіть спосіб/канал зв'язку, а потім підготуйте фізичне обладнання і драйвери пристроїв Windows. Комп'ютер і autopilot можна з'єднати USB-кабелем, [радіомодемами telemetry](https://ardupilot.org/copter/docs/common-telemetry-landingpage.html) *(ще не перекладено)*, [Bluetooth](https://ardupilot.org/copter/docs/common-mission-planner-bluetooth-connectivity.html#connecting-with-mission-planner) *(ще не перекладено)*, через IP-мережу тощо.

> **Примітка.** Драйвер вашого обладнання зв'язку має бути встановлений у Windows — саме він робить COM-порт підключення і його стандартну швидкість передачі доступними для *Mission Planner*.

![Pixhawk USB Connection](https://ardupilot.org/copter/_images/pixhawk_usb_connection.jpg)

![Connection using SiK Radio](https://ardupilot.org/copter/_images/new-radio-laptop.jpg)

У *Mission Planner* порт і швидкість передачі задаються у випадних списках у верхньому правому куті екрана.

![MisionPlanner_ConnectButton](https://ardupilot.org/copter/_images/MisionPlanner_ConnectButton.png)

Щойно ви під'єднаєте USB або радіомодем telemetry, Windows автоматично призначить autopilot номер COM-порту, і він з'явиться у випадному списку (сам номер значення не має). Також встановлюється відповідна швидкість передачі (зазвичай 115200 для USB і 57600 для радіомодема).

Виберіть потрібний порт і швидкість, потім натисніть **CONNECT**, щоб підключитися до autopilot. Після підключення **Mission Planner** завантажить параметри з autopilot, а кнопка зміниться на **DISCONNECT**:

![MisionPlanner_DisconnectButton](https://ardupilot.org/copter/_images/MisionPlanner_DisconnectButton.png)

> **Порада.** У списку вибору порту є також варіанти TCP і UDP, через які можна підключитися до autopilot по мережі.

Посилання «Stats...» під списком портів відкриває інформацію про з'єднання: чи активне [підписування MAVLink (Signing)](https://ardupilot.org/copter/docs/common-MAVLink2-signing.html) *(ще не перекладено)*, статистику каналу тощо. Іноді це вікно відкривається під поточним екраном, і його треба вивести на передній план.

![MP-stats](https://ardupilot.org/copter/_images/MP-stats.png)

### Підключення кількох апаратів

Додаткові підключення можна створити, клацнувши правою кнопкою на **CONNECT** і вибравши **Connection Options** у випадному меню.

![MP-connect-rightclick-menu](https://ardupilot.org/copter/_images/MP-connect-rightclick-menu.png)

Файл із заздалегідь підготовленим списком підключень можна завантажити через пункт **Connection List**. Приклад формату файлу:

```
tcp://127.0.0.1:5670
udp://127.0.0.1:14550
udpcl://192.168.1.255:14550
serial:com4:115200
```

## Усунення несправностей

Якщо Mission Planner не вдається підключитися:

- Перевірте, що для вибраного способу використовується правильна швидкість передачі (115200 для USB або 57600 для радіомодема/telemetry).
- Якщо підключаєтеся через USB, зачекайте кілька секунд після ввімкнення живлення. Якщо спробувати підключитися під час ініціалізації bootloader (завантажувач), Windows може отримати неправильну інформацію про USB-пристрій. Тоді для наступних спроб може знадобитися від'єднати і знову під'єднати USB, зачекати, поки bootloader перейде до основного коду (кілька секунд), і лише потім підключатися. Зрідка, якщо спроба підключення припала на ініціалізацію bootloader, доводиться перезапускати MP.
- Якщо у Windows використовується COM-порт, перевірте, що COM-порт підключення є в переліку COM-портів (Ports) у Device Manager Windows.
- Якщо autopilot має процесор F7 або H7 і порти CAN, див. розділ нижче — [Проблеми з композитними підключеннями](#проблеми-з-композитними-підключеннями).
- Якщо використовується USB-порт, спробуйте інший фізичний USB-порт.
- Якщо використовується з'єднання UDP або TCP, перевірте, що firewall не блокує IP-трафік.

Також переконайтеся, що на платі autopilot встановлено відповідну firmware ArduPilot і вона коректно завантажилась (на Pixhawk про стан autopilot підкажуть [світлодіоди](https://ardupilot.org/copter/docs/common-leds-pixhawk.html) *(ще не перекладено)* і [звуки](https://ardupilot.org/copter/docs/common-sounds-pixhawkpx4.html) *(ще не перекладено)*).

Якщо ви використовуєте віддалений канал (не USB) і Mission Planner підключається, але не завантажує параметри або не виконує команди (наприклад, зміну режиму), то, ймовірно, на autopilot увімкнено Signing. Див. [MAVLink2 Signing](https://ardupilot.org/copter/docs/common-MAVLink2-signing.html) *(ще не перекладено)*.

## Проблеми з композитними підключеннями

Autopilot з процесорами F7 або H7 та інтерфейсами CAN використовують firmware, яка представляє два USB-інтерфейси: один для звичайного підключення MAVLink, другий — для послідовного з'єднання SLCAN з інтерфейсом CAN (для налаштування і оновлення firmware). Такий пристрій називають композитним USB-пристроєм.

За замовчуванням USB-інтерфейс MAVLink — це SERIAL0, а USB-інтерфейс SLCAN — найвищий порт SERIALx, який має плата. Драйвер Windows, що зараз встановлюється разом із Mission Planner, може обрати будь-який з них; оскільки у firmware ArduPilot обидва за замовчуванням налаштовані на протокол MAVLINK, усе працюватиме незалежно від того, який з них стане COM-портом.

Однак буває ситуація, коли підключитися до очевидного COM-порту зі списку Mission Planner не вдається. Це стається, коли користувач випадково змінює протокол того порту SERIALx, який драйвер Windows використовує як COM-порт MAVLink, на щось інше, ніж MAVLink. Таке легко трапляється, якщо взяти наявний файл параметрів з конфігурації апарата, що використовувався з іншим autopilot, де протокол було змінено. Наприклад, у користувача є літак з autopilot без CAN на F7/H7, він замінює його на autopilot з CAN і під час налаштування літака з новим autopilot завантажує свій старий файл параметрів. Щойно файл параметрів завантажено і autopilot перезапущено, зв'язок зникає і не відновлюється.

Причина в тому, що змінився протокол порту SERIALx, який використовувала Windows. Майже завжди це порт SERIALx з найвищим номером, бо на autopilot без CAN його зазвичай встановлено в -1, а драйвер COM-порту Windows вибрав як COM-порт саме цей інтерфейс замість SERIAL0.

Відновлення виконується так:

- Відкрийте Device Manager Windows і знайдіть у розділі Ports COM-порт, який використовує autopilot. У нього буде той номер COM-порту, через який ви спочатку підключалися до Mission Planner. Клацніть правою кнопкою — серед варіантів буде «Update driver software». Клацніть його.

    ![devicemanager](https://ardupilot.org/copter/_images/devicemanager.png)

- Клацніть «Browse my computer......», потім «Choose from a list...» — з'явиться такий екран:

    ![composite-driver](https://ardupilot.org/copter/_images/composite-driver.png)

- Прокрутіть верхній список до пункту «Composite USB» і клацніть його.

- Тепер знову підключіть autopilot до комп'ютера — з'являться два COM-порти. До одного з них (того, де лишився протокол MAVLink) підключення вдасться, до іншого — ні. Якщо не вдалося до одного, спробуйте інший. Але НЕ від'єднуйте autopilot від комп'ютера, інакше композитний драйвер вивантажиться і доведеться починати спочатку.

- Підключившись до Mission Planner, поверніть протокол цього порту SERIALx на 2 (MAVLink2). Тепер можна від'єднати й знову під'єднати autopilot — він показуватиме лише один COM-порт, і підключення надалі має працювати. Не змінюйте цей протокол, якщо не збираєтеся використовувати інтерфейс SLCAN. Незвично може бути те, що Mission Planner тепер використовує не звичайний SERIAL0, а найвищий порт, але на конфігурацію і роботу autopilot це ніяк не впливає.

## Пов'язані теми

[Підключення Mission Planner через Bluetooth](https://ardupilot.org/copter/docs/common-mission-planner-bluetooth-connectivity.html#connecting-with-mission-planner) *(ще не перекладено)*
