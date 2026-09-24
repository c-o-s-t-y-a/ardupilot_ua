# Receiver FPort

> Оригінал: [FPort Receivers](https://ardupilot.org/copter/docs/common-FPort-receivers.html)

ArduPilot підтримує FPort/FPort2.

Протокол FPort поєднує передачу на autopilot (автопілот) інформації радіокерування SBus із двонаправленою передачею telemetry (телеметрія) до/від autopilot по одному дроту на високошвидкісній шині.

Багато receiver (приймач) FRSky серій X і R мають цю можливість — від початку або після оновлення firmware (прошивка).

Підключення до autopilot і налаштування залежать від autopilot, бо можливості їхніх UART (послідовний порт) різні. Більшість autopilot на процесорі F4 не мають керованих інверторів перед TX і RX UART і потребують або зовнішнього двонаправленого інвертора (як і підключення SPort), або використання «неінвертованого контакту FPort», який мають деякі receiver, бо протокол FPort має протилежні рівні сигналу порівняно зі звичайною роботою UART. Більшість autopilot на F7 і H7, навпаки, мають внутрішні інвертори, і FPort receiver можна напряму підключити до лінії TX їхніх UART.

> **Примітка.** ArduPilot підтримує 16- і 24-канальний FPort2, але telemetry працює лише в 16-канальному режимі.

## Протокол telemetry

ArduPilot надсилає дані telemetry на receiver через Fport за протоколом [Passthrough telemetry](https://ardupilot.org/copter/docs/common-frsky-passthrough.html) *(ще не перекладено)*. Щоб датчики з'явилися в OpenTX, треба встановити і ввімкнути скрипт, що вміє відображати Passthrough telemetry, як-от [Yaapu FrSky Telemetry Script for OpenTX](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*. Інакше буде виявлено лише датчик GPS.

## Схеми підключення

Схеми підключення — див. [Connecting SPort/FPort](https://ardupilot.org/copter/docs/common-connecting-sport-fport.html) *(ще не перекладено)*.

## Налаштування ArduPilot

Налаштування залежить від autopilot і способу підключення.

> **Примітка.** Будь-яка зміна налаштувань UART набуває чинності після перезавантаження. Нагадування: номери UART не обов'язково відповідають номерам SERIALx. Перевірте [опис плати](https://ardupilot.org/copter/docs/common-autopilots.html) *(ще не перекладено)*.

Загалом autopilot на F4 із зовнішнім двонаправленим інвертором можуть використовувати будь-який UART з таким налаштуванням:

- `SERIALx_PROTOCOL` = 23
- `SERIALx_OPTIONS` = 160 (вмикає підтягувальні резистори на контактах TX і RX для тих схем зовнішніх інверторів, яким це потрібно; на ті, яким не потрібно, не впливає)
- `RSSI_TYPE` = 3

Autopilot на F4 з виходом «неінвертованого FPort» від receiver можуть підключати його до контакту TX будь-якого UART з налаштуванням:

- `SERIALx_PROTOCOL` = 23
- `SERIALx_OPTIONS` = 4 (Half Duplex) або = 132 (Half Duplex, TX Pull-up), якщо receiver не має достатнього навантажувального струму на «неінвертованому» виході
- `RSSI_TYPE` = 3

> **Примітка.** Autopilot на F4 не можуть використовувати контакт RX з виходом «неінвертованого FPort», бо можливість SWAP є лише на autopilot на F7/H7, а Half Duplex потребує підключення до контакту TX UART.

Autopilot на F7/H7 можна напряму підключити до контакту TX будь-якого UART з таким налаштуванням:

- `SERIALx_PROTOCOL` = 23
- `SERIALx_OPTIONS` = 7 (інверсія TX/RX, Half Duplex); якщо використовується «неінвертований» сигнал FPort — то = 4, бо інверсія не потрібна
- `RSSI_TYPE` = 3

    АБО до контакту RX:

- `SERIALx_PROTOCOL` = 23
- `SERIALx_OPTIONS` = 15 (інверсія TX/RX, Half Duplex, обмін контактів TX/RX — SWAP)
- `RSSI_TYPE` = 3

> **Примітка.** Деякі autopilot на F7/H7 мають на UART перетворювачі рівнів, що вносять затримку в режимі Half Duplex, як-от CubeOrange. Якщо наведене вище налаштування не працює, спробуйте встановити `RC_OPTIONS` = 8 — це додасть у протокол вирівнювання для компенсації. Проте використання цієї опції, коли вона не потрібна, зламає роботу.

## Розширені конфігурації

Багато autopilot мають UART, прив'язаний до звичайного контакту входу RC, який частково чи повністю вимкнено, щоб цей контакт можна було використовувати як GPIO (вивід загального призначення) для декодування протоколів RC, зокрема на основі PWM (широтно-імпульсна модуляція). Тому кілька плат тепер мають альтернативне призначення контактів, яке можна вибрати параметром `BRD_ALT_CONFIG`. Це дає змогу використовувати раніше вимкнені UART для FPort, не займаючи додатковий UART.

> **Примітка.** Кілька autopilot (наприклад, Pixhawkx, Cube тощо) зі співпроцесором IOMCU не мають альтернативних конфігурацій для використання контакту RCIN. Доведеться використати UART, як описано вище.

> **Примітка.** CUAVv5Nano може використовувати для FPort свій звичайний вхід RC. Налаштуйте SERIAL5 як для звичайного autopilot на F7/H7, як описано вище.

Такі autopilot мають цю можливість з `BRD_ALT_CONFIG` = 1:

### MatekF405

UART2 RX/TX тепер можна підключити до FPort receiver через зовнішній двонаправлений інвертор SPort/FPort.

- Налаштуйте SERIAL5, як описано вище для autopilot на F4.

### MatekF405-Wing

UART2 RX/TX тепер можна підключити до FPort receiver через зовнішній двонаправлений інвертор SPort/FPort.

- Налаштуйте SERIAL7, як описано вище для autopilot на F4.

### MatekF765-Wing

UART6 RX тепер можна підключити до FPort receiver. Ця плата потребує особливого налаштування:

- `BRD_ALT_CONFIG` = 1
- `SERIAL7_PROTOCOL` = 23
- `SERIAL7_OPTIONS` = 15
- `RC_OPTIONS` = 8 (залежно від receiver і версії його firmware це може бути непотрібним)
- `RSSI_TYPE` = 3

### KakuteF7 і KakuteF7Mini

Звичайний вхід RC, UART6 RX, тепер можна використовувати для FPort з таким налаштуванням:

- `BRD_ALT_CONFIG` = 1
- `SERIAL6_PROTOCOL` = 23
- `SERIAL6_OPTIONS` = 15
- `RSSI_TYPE` = 3
