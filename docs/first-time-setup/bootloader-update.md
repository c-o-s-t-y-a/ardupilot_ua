# Bootloader update (оновлення завантажувача)

> Оригінал: [Updating the Bootloader](https://ardupilot.org/copter/docs/common-bootloader-update.html)

Bootloader (завантажувач) — невелика програма, що працює (зазвичай лише кілька секунд) під час увімкнення autopilot (автопілот). Одне з головних завдань bootloader — давати змогу легко оновлювати основну firmware (прошивка), тобто ArduPilot.

Майже всі autopilot постачаються з попередньо встановленим bootloader, і більшості користувачів ніколи не доведеться його оновлювати, але оновлення до найновішого bootloader ArduPilot має переваги:

- Виправлення помилок, як-от проблеми «Parameter Reset», виправленої в Copter-4.0.4, Plane-4.0.6.
- Назва COM-порту може бути зрозумілішою. Наприклад, вона може містити «ArduPilot».

> **Попередження.** Оновлення bootloader потенційно може перетворити плату на «цеглину» (тобто вона перестане відповідати і приймати нову firmware). Не вимикайте живлення autopilot під час оновлення.

## Де завантажити найновіший bootloader?

Bootloader ArduPilot входить до складу firmware ArduPilot, але за замовчуванням не використовується. Щоб встановити новий bootloader, основній firmware ArduPilot треба надіслати спеціальну команду.

<img src="https://ardupilot.org/copter/_images/bootloader-file-description.png" alt="bootloader-file-description" width="450">

> **Примітка.** Деякі autopilot з 1 MB flash (флеш-пам'ять) НЕ містять bootloader у firmware, щоб заощадити flash, і описані нижче спроби оновлення з firmware завершаться повідомленням про помилку в Mission Planner чи MAVProxy. У таких випадках потрібно записати firmware `xxxx_bl.hex` для autopilot через DFU (режим прошивання через USB), як описано в [Завантаження firmware на плати без сумісного bootloader](firmware-dfu.md), так, ніби на ньому ще немає firmware ArduPilot.

## Оновлення через Mission Planner

- Встановіть на autopilot свіжу версію ArduPilot (див. [Завантаження firmware](loading-firmware.md)).
- Підключіться і переконайтеся, що в autopilot є щонайменше 20k вільної пам'яті. Відкрийте вкладку Quick на екрані Data, двічі клацніть будь-який запис і виберіть «freemem».

    <img src="https://ardupilot.org/copter/_images/bootloader-update-MP-memory-check.png" alt="bootloader-update-MP-memory-check" width="450">

- Відкрийте сторінку Setup >> Install Firmware і натисніть кнопку «Bootloader Update».

    <img src="https://ardupilot.org/copter/_images/bootloader-update-MP.png" alt="bootloader-update-MP" width="450">

- Перезавантажте autopilot.

## Оновлення через QGC

Процес схожий на Mission Planner (див. вище), тільки кнопка «Flash ChibiOS Bootloader» розташована на сторінці Firmware у розділі Configuration (іконка шестерні).

<img src="https://ardupilot.org/copter/_images/bootloader-update-QGC.png" alt="bootloader-update-QGC" width="450">

## Оновлення через MAVProxy

- У терміналі MAVProxy введіть «flashbootloader».

## Додаткова інформація

- Інформація про bootloader для розробників — [тут](https://ardupilot.org/dev/docs/bootloader.html).
- Вихідний код bootloader — у [Tools/AP_Bootloader](https://github.com/ArduPilot/ardupilot/tree/master/Tools/AP_Bootloader).
- Скомпільовані бінарні файли — на [firmware.ardupilot.org/Tools/Bootloaders](https://firmware.ardupilot.org/Tools/Bootloaders/).

[Відео (YouTube)](https://www.youtube.com/watch?v=oxThS6CGd6I)
