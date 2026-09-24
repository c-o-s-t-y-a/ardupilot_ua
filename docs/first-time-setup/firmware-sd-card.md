# Завантаження firmware (прошивки) з SD-карти

> Оригінал: [Loading Firmware via SD Card](https://ardupilot.org/copter/docs/common-install-sdcard.html)

На деяких autopilot (автопілот) firmware (прошивка) ArduPilot можна оновити, поклавши файл зі спеціальною назвою на SD-карту і запустивши bootloader (завантажувач) autopilot (наприклад, перезапустивши живлення плати).

> **Примітка.** Наразі це вміють лише небагато autopilot. Як визначити, чи є ця можливість у вашого autopilot, — див. нижче. Це можуть лише autopilot на H7 з SD-картою, підключеною через MMC, і поки що не на всіх із них цю функцію додано.

## Навіщо це потрібно?

Цей спосіб корисний з кількох причин:

- Немає зручного, надійного доступу до USB-порту апарата.
- Потрібно оновити firmware апарата через радіомодем telemetry (телеметрія).
- Апарат далеко, і місцевим операторам може бути складно оновлювати firmware звичайними засобами. Так виробники (OEM) можуть віддалено покласти оновлений файл на SD-карту користувачів, і він запишеться під час наступного запуску апарата.

## Чи вміє це мій autopilot?

Для цього потрібно кілька складників:

- autopilot має підтримувати SD-карту;
- SD-карта має бути ввімкнена в його bootloader;
- код bootloader і запис firmware мають бути ввімкнені у файлах опису апаратної частини autopilot (hwdefs).

Щоб перевірити, чи є ця можливість у конкретного autopilot, подивіться в каталозі його firmware на [сервері збірок firmware](https://firmware.ardupilot.org), чи є там файл `xxxxxx.abin`.

## Bootloader

Потрібен bootloader, який уміє записувати firmware з SD-карти (і, звісно, autopilot має підтримувати SD-карту). Новіші autopilot з SD-картою можуть мати або не мати цієї можливості та відповідного bootloader в описі апаратної частини (якщо не мають — див. [Самостійна збірка firmware](#самостійна-збірка-firmware)).

Якщо поточна firmware autopilot підтримує цю можливість, для запису з SD-карти може знадобитися оновити поточний bootloader. Зверніть увагу: оновлення bootloader autopilot — операція, яка може зробити плату непрацездатною, і відновити її буде складно. Особливо це стосується плат, що не мають виведеного контакту «boot0», як-от CubeOrange. Пам'ятайте про цей ризик і будьте готові витратити чимало часу на відновлення плати, якщо під час оновлення bootloader щось піде не так.

Щоб оновити bootloader, скористайтеся [інструкцією з оновлення bootloader](bootloader-update.md); зверніть увагу, що для отримання придатного bootloader потрібна свіжа firmware (4.5 або новіша).

## Файл firmware

На SD-карту кладеться спеціальний файл «xxxxx.abin», створений саме для цього. Це бінарний файл з невеликим текстовим блоком з інформацією про бінарний файл — насамперед із контрольною сумою, яку bootloader перевіряє перед записом на плату.

Для плат, що підтримують запис з SD-карти, на [сервері збірок firmware](https://firmware.ardupilot.org) також є файли `.abin`.

## Назва файлу firmware

Назва файлу, яку отримує firmware під час збірки, — ***не*** та, що потрібна на SD-карті. Згенеровані файли `.abin` містять назву апарата, наприклад «arduplane.abin».

Для запису з SD-карти правильна лише одна назва файлу — `ardupilot.abin`. Кладучи файл на SD-карту, обов'язково перейменуйте його на `ardupilot.abin`.

## Копіювання файлу на SD-карту

Це можна зробити засобами операційної системи, як ви зазвичай працюєте з SD-картою (наприклад, у файловому менеджері).

Можна також передати файл у кореневий каталог SD-карти через `MAVFTP` за допомогою Mission Planner чи подібної GCS (наземна станція керування).

![MP-install-firmware-sdcard](https://ardupilot.org/copter/_images/MP-install-firmware-sdcard.png)

Перш ніж продовжити, переконайтеся, що розмір файлу правильний.

Після завершення передачі перелік файлів у каталозі має виглядати приблизно так:

```text
RTL> ftp put /home/pbarker/arducopter.abin ardupilot.abin
RTL> Putting /home/pbarker/arducopter.abin as ardupilot.abin
Sent file of length  1847687
RTL> ftp list
RTL> Listing /
 D APM
   ardupilot.abin   1847687
Total size 1804.38 kByte
```

## Запуск запису

Перезапустіть живлення плати, щоб увійти в bootloader: він автоматично перевірить наявність файлу оновлення firmware і почне запис. Щоб обійтися без перезапуску живлення, autopilot можна також перезавантажити командою [PREFLIGHT_REBOOT_SHUTDOWN](https://mavlink.io/en/messages/common.html#MAV_CMD_PREFLIGHT_REBOOT_SHUTDOWN) з полем «Param1», встановленим у 3 (тобто «Reboot autopilot and keep it in the bootloader until upgraded»).

Перевірка firmware і запис у внутрішню flash (флеш-пам'ять) апарата мають зайняти приблизно 1 хвилину.

Якщо процес завершиться успішно, файл буде перейменовано на `ardupilot-flashed.abin`. Після завершення запису апарат має запустити firmware.

## Усунення несправностей

Під час запису firmware може статися кілька проблем, але є засоби діагностики, що допоможуть з'ясувати, в чому річ.

- На кожному етапі запису файл `ardupilot.abin` перейменовується відповідно до етапу.
- Якщо файл називається `ardupilot-verify.abin`, процес зупинився під час перевірки контрольної суми файлу або плату було перервано в цей момент.
- Якщо файл називається `ardupilot-verify-failed.abin`, контрольна сума, обчислена bootloader, не збіглася з [the bootloader] у метаданих `.abin`.
- Якщо файл називається `ardupilot-flash.abin`, процес зупинився під час запису firmware або плату було перервано в цей момент. Найімовірніше, у такому разі плата не запуститься з firmware ArduPilot, і знадобиться повторний запис.
- Якщо файл називається `ardupilot-flashed.abin`, цей розділ вам не потрібен — запис пройшов успішно!

## Самостійна збірка firmware

Якщо autopilot підтримує SD-карту, але на [сервері збірок firmware](https://firmware.ardupilot.org) немає firmware, придатної для запису з SD-карти, firmware можна зібрати самостійно. Для цього треба налаштувати середовище збірки, а потім змінити hwdefs autopilot, щоб зібрати придатний bootloader і firmware `xxxx.abin`, див. [Building the code](https://ardupilot.org/dev/docs/building-the-code.html) *(ще не перекладено)*.

У файл `hwdef-bl.dat` треба додати:

```text
define AP_BOOTLOADER_FLASH_FROM_SD_ENABLED 1
define FATFS_HAL_DEVICE SDCD1
define HAL_OS_FATFS_IO 1
# FATFS support:
define CH_CFG_USE_MEMCORE 1
define CH_CFG_USE_HEAP 1
define CH_CFG_USE_SEMAPHORES 0
define CH_CFG_USE_MUTEXES 1
define CH_CFG_USE_DYNAMIC 1
define CH_CFG_USE_WAITEXIT 1
define CH_CFG_USE_REGISTRY 1
```

- Також треба додати налаштування SD-карти. Приклад — [опис autopilot MatekH743](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_HAL_ChibiOS/hwdef/MatekH743/hwdef-bl.dat).

У файл `hwdef.dat` треба додати:

```text
env BUILD_ABIN True
```

Під час збірки firmware ви побачите таке — зверніть увагу, що створено файл .abin:

```text
     BUILD SUMMARY
Build directory: /home/pbarker/rc/ardupilot/build/CubeOrange
Target         Text (B)  Data (B)  BSS (B)  Total Flash Used (B)  Free Flash (B)  External Flash Used (B)
---------------------------------------------------------------------------------------------------------
bin/arduplane   1868612      3536   258740               1872148           93928  Not Applicable

Build commands will be stored in build/CubeOrange/compile_commands.json
'plane' finished successfully (24.283s)
pbarker@fx:~/rc/ardupilot(master)$ ls -l build/CubeOrange/bin
total 18792
-rwxrwxr-x 1 pbarker pbarker 3135448 Sep 29 19:15 arduplane
-rw-rw-r-- 1 pbarker pbarker 1872247 Sep 29 19:15 arduplane.abin
-rw-rw-r-- 1 pbarker pbarker 1684192 Sep 29 19:15 arduplane.apj
-rwxrwxr-x 1 pbarker pbarker 1872152 Sep 29 19:15 arduplane.bin
-rw-rw-r-- 1 pbarker pbarker 5148900 Sep 29 19:15 arduplane.hex
-rw-rw-r-- 1 pbarker pbarker 5509380 Sep 29 19:15 arduplane_with_bl.hex
```

## Відео

[Демонстрація (YouTube)](https://www.youtube.com/watch?v=hCdXe1UTjK4)
