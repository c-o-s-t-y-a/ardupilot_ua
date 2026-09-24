# Завантаження firmware (прошивки) на плати з сумісним bootloader

> Оригінал: [Loading Firmware to Boards with an ArduPilot Compatible Bootloader](https://ardupilot.org/copter/docs/common-loading-firmware-onto-pixhawk.html)

Тут показано, як за допомогою GCS (наземна станція керування) Mission Planner записати firmware (прошивка) на autopilot (автопілот), на якому вже встановлено [сумісний з ArduPilot bootloader (завантажувач)](loading-firmware.md#крок-2-перевірте-що-вже-є-на-autopilot). Це звичайний спосіб для кожного оновлення firmware після того, як ArduPilot встановлено.

Якщо на autopilot ніколи не працювала firmware ArduPilot чи PX4, дивіться натомість [Завантаження firmware на плати без сумісного bootloader](firmware-dfu.md).

> **Примітка.** На деяких autopilot firmware можна оновити також [записом з SD-карти](firmware-sd-card.md).

## Виберіть COM-порт

Коли autopilot [підключено до комп'ютера через USB](loading-firmware.md), а як GCS використовується *Mission Planner*, відкрийте випадний список COM-портів у верхньому правому куті вікна поруч із кнопкою **Connect**. Виберіть **AUTO** або конкретний порт вашої плати. Встановіть швидкість (Baud rate) **115200**, як показано. Поки що **не** натискайте **Connect**.

![Pixhawk_ConnectWithMP](https://ardupilot.org/copter/_images/Pixhawk_ConnectWithMP.png)

## Встановлення firmware

На екрані **SETUP → Install Firmware** у Mission Planner виберіть іконку, що відповідає вашому типу апарата чи frame (рама) (наприклад, Quad, Hexa). На запитання «Are you sure?» відповідайте **Yes**.

![Mission Planner: Install Firmware Screen](https://ardupilot.org/copter/_images/Pixhawk_InstallFirmware.jpg)

> **Примітка.** Деякі плати орієнтовані на певний тип апарата, і firmware для інших апаратів для них автоматично не збирається. Проте ArduPilot для таких апаратів усе одно можна зібрати на [Custom Firmware Server](https://custom.ardupilot.org/).

Mission Planner спробує визначити, яку плату ви використовуєте. Він може попросити від'єднати плату, натиснути OK і підключити її знову, щоб визначити тип плати.

![Mission Planner: Install Firmware Prompt](https://ardupilot.org/copter/_images/Pixhawk_InstallFirmware2.png)

Часто з'являється випадний список варіантів firmware для плати, з якого можна вибрати (наприклад, варіанти з двонаправленим DShot, якщо вони є). Для плат, що мають спільний з Pixhawk ідентифікатор, список буде довгим, як показано нижче:

![pixhawk-firmware](https://ardupilot.org/copter/_images/pixhawk-firmware.png)

Виберіть firmware, що підходить вашій платі. Для плат з позначкою «Pixhawk» зазвичай найкращий вибір — firmware Pixhawk1.

> **Попередження.** На деяких платах з маркуванням Pixhawk 2.4.x можуть стояти інші датчики, ніж в оригіналі, через що можливі помилки pre-arm (передпольотна перевірка) або відсутність другого IMU (інерційний вимірювальний модуль). Обхідний шлях для відомої заміни на деяких платах barometer (барометр) MS5611 на MS5607 — див. параметр `BARO_OPTIONS`. IMU теж можуть бути замінені. За можливості купуйте autopilot у партнерів ArduPilot.

Якщо все гаразд, унизу праворуч з'явиться статус зі словами «erase...», «program...», «verify..» і «Upload Done». Firmware успішно записано на плату.

Після запису або ввімкнення живлення bootloader зазвичай кілька секунд завершує роботу і переходить до основного коду. Не натискайте CONNECT, доки це не станеться. Як перевірити результат — див. [Перевірте, що все спрацювало](loading-firmware.md#крок-4-перевірте-що-все-спрацювало).

## Встановлення Beta, розробницької або власної збірки

Іконки firmware вище встановлюють поточний реліз `Stable`. Щоб встановити `Beta`, `latest` або власну збірку, спершу [завантажте файл .apj](loading-firmware.md#завантаження-файлу-firmware) для вашої плати, а потім запишіть його через опцію «Load custom firmware» у Mission Planner:

- підключіть комп'ютер з GCS до autopilot USB-кабелем;
- виберіть COM-порт і швидкість (зазвичай 115200, але можна вищу, якщо ваше обладнання дозволяє) для плати. Вони вибираються вгорі праворуч. **Не** натискайте Connect;
- перейдіть на екран встановлення firmware в MP («Setup >> Install Firmware»);
- натисніть посилання «Load custom firmware» і виберіть завантажений файл .apj (не вибирайте файли .hex — вони призначені лише для способів DFU (режим прошивання через USB)/JTAG/SWD). Якщо посилання «Load custom firmware» не видно, виберіть «Config >> Planner» і встановіть у списку «Layout» значення «Advanced»;
- можливо, перед попереднім кроком доведеться натиснути «Force bootloader» (якщо на плату раніше вже записано bootloader ArduPilot);

    <img src="https://ardupilot.org/copter/_images/mission-planner-load-custom-firmware.png" alt="mission-planner-load-custom-firmware" width="450">

- виконуйте інструкції щодо від'єднання і підключення плати, якщо вони з'являться;
- якщо все гаразд, унизу екрана з'явиться статус, наприклад «erase...», «program...», «verify..» і «Upload Done».

> **Примітка.** На сторінці Install Firmware у Mission Planner є також опція **Beta firmware**, яка не потребує ручного завантаження. Проте пізніший реліз `Stable` може вже бути новішим за запропонований `Beta`, тож спершу перевірте звичайну опцію запису для вашого апарата.
