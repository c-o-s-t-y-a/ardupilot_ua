# Модуль UBlox GPS + compass (компас)

> Оригінал: [UBlox GPS + Compass Module](https://ardupilot.org/copter/docs/common-installing-3dr-ublox-gps-compass-module.html)

Модуль UBlox GPS + compass (компас) — найпоширеніший GPS для сумісних з ArduPilot autopilot (автопілот). Таких модулів випускає багато виробників; рекомендовані моделі — [тут](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) *(ще не перекладено)*.

ArduPilot автоматично налаштовує GPS невдовзі після запуску, тож калібрувати GPS не потрібно. Проте [compass калібрувати треба](compass-calibration.md).

![GPS_TopAndSide](https://ardupilot.org/copter/_images/GPS_TopAndSide.jpg)

## Підключення до autopilot

![gps-connection](https://ardupilot.org/copter/_images/gps-connection.jpg)

### Приклад: підключення до Pixhawk

Підключіть 6-контактний роз'єм DF13 GPS до порту «GPS» Pixhawk, а 4-контактний роз'єм compass — до порту I2C. Якщо до I2C треба підключити й інші пристрої, compass можна спершу підключити через розгалужувач I2C (`I2C splitter`).

![pixhawk_with_dual_gps](https://ardupilot.org/copter/_images/pixhawk_with_dual_gps.jpg)

Як налаштувати й використовувати другий GPS — на сторінці [GPS Blending](https://ardupilot.org/copter/docs/common-gps-blending.html) *(ще не перекладено)*.

> **Примітка.** Швидкість порту задає драйвер UBlox (параметр `SERIAL4_BAUD = 38` ігнорується).

> **Примітка.** ArduPilot підтримує багато підключених compass, але під час роботи можна використовувати лише до 3. Див. [Advanced Compass Setup](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html) *(ще не перекладено)*.

## Монтаж модуля GPS

Цей модуль дає змогу встановити GPS окремо від flight controller (польотний контролер), щоб GPS мав якнайкращий огляд неба, а compass був віддалений від магнітних полів, що заважають.

> **Порада.** Рекомендована орієнтація — стрілкою модуля вперед апарата, в тому ж напрямку, що й стрілка на autopilot.

Під час монтажу модуля GPS+compass:

- Розмістіть модуль зовні апарата (за потреби — на підвищенні) з вільним оглядом неба, якомога далі від моторів і ESC (електронний регулятор обертів), стрілкою вперед.
- Віддаліть модуль від силових дротів постійного струму і батарей щонайменше на 10 см. Щогла для GPS наполегливо рекомендується.

![gps-mast](https://ardupilot.org/copter/_images/gps-mast.jpg)

- Розмістіть модуль подалі від металевих предметів, що містять залізо, поблизу. (Для кріплення модуля використовуйте нейлонові чи немагнітні кріплення з нержавіючої сталі та нейлонові чи алюмінієві стійки.)
- За можливості скручуйте дроти живлення і землі.

![GPS_sampleMoutning](https://ardupilot.org/copter/_images/GPS_sampleMoutning.jpg)

## Налаштування в Mission Planner

[Калібрування compass у Mission Planner](compass-calibration.md) пояснює найпростіший спосіб відкалібрувати compass, встановлений у рекомендованій орієнтації (стрілки autopilot і compass дивляться вперед апарата).

[Advanced Compass Setup](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html) *(ще не перекладено)* містить докладніші інструкції з калібрування compass, якщо його, наприклад, встановлено в іншій орієнтації.

## Світлодіодні індикатори

Модуль 3DR GPS+compass має два світлодіоди: живлення (світиться червоним) і GPS lock (фіксація позиції GPS) (блимає синім). Більшість GPS мають світлодіод, що показує отримання 3D GPS lock.

| **Світлодіод:** | **Поведінка:** |
|---|---|
| Power | Світиться **червоним**, коли є живлення |
| GPS lock | Блимає **синім**, коли отримано 3D GPS lock |

## Розширене налаштування

Розширене налаштування внутрішніх параметрів GPS UBlox описано в [UBlox GPS Configuration](https://ardupilot.org/copter/docs/common-ublox-gps.html) *(ще не перекладено)*. Але звичайному користувачу це ніколи не потрібно: ArduPilot автоматично налаштовує GPS під час ініціалізації.
