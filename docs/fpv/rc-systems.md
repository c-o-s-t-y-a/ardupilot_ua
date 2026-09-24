# Системи радіокерування

> Оригінал: [Radio Control Systems](https://ardupilot.org/copter/docs/common-rc-systems.html)

![rc_systems](https://ardupilot.org/copter/_images/rc_systems.png)

Тут наведено огляд систем RC transmitter (пульт радіокерування) і receiver (приймач), які можна використовувати з autopilot (автопілот) ArduPilot.

## Сумісні протоколи RC

Autopilot ArduPilot сумісні з такими протоколами виходу receiver:

1. receiver PPM-Sum
2. receiver SBus
3. Fast SBus (з відео/RC-систем DJI HDL)
4. receiver i-BUS
5. [FPort receiver](fport.md)
6. [receiver-сателіти Spektrum SRXL2, DSM, DSM2 і DSM-X](https://ardupilot.org/copter/docs/common-spektrum-rc.html) *(ще не перекладено)*
7. [receiver Multiplex SRXL версій 1 і 2](https://ardupilot.org/copter/docs/common-srxl-receivers.html) *(ще не перекладено)*
8. [receiver CRSF](crossfire-elrs.md) (зокрема системи ExpressLRS)
9. [mLRS (з telemetry (телеметрія))](https://ardupilot.org/copter/docs/common-mlrs-rc.html) *(ще не перекладено)* (MAVLink)
10. [Graupner SUM-D](https://ardupilot.org/copter/docs/common-graupner-rc.html) *(ще не перекладено)*
11. [IRC Ghost](https://www.immersionrc.com/fpv-products/ghost/)
12. периферія DroneCAN може декодувати ці протоколи RC на периферійному пристрої і передавати на autopilot
13. RC, підключене через MAVLink (не плутати з MAVLink RC Overrides, що використовуються для керування функціями RC джойстиком з GCS (наземна станція керування))
14. паралельні виходи PWM (широтно-імпульсна модуляція), закодовані в PPM-Sum зовнішнім кодером (див. нижче; на багатьох сучасних autopilot не підтримується)

## Підключення receiver

Для всіх наведених вище протоколів ArduPilot автоматично визначає протокол системи receiver. Проте залежно від протоколу і типу autopilot фізичне підключення до autopilot може відрізнятися.

Деякі протоколи, насамперед SRXL2, CRSF і ELRS, потребують повного підключення UART (послідовний порт).

Крім того, інші протоколи, що теж передають telemetry, як-от FPort, зазвичай потребують двонаправленого напівдуплексного підключення, щоб отримувати telemetry. Для цих протоколів вихід TX UART слід підключати до послідовного входу receiver. На платах F7 і H7 можна також підключитися до входу RX UART з деяким додатковим налаштуванням.

### PPM-Sum/SBus/i-BUS

Такі receiver зазвичай підключаються до контакту входу RCin чи SBUS на autopilot.

Щоб підключити receiver PPM-Sum чи SBus, наприклад, до Pixhawk, під'єднайте дроти землі (чорний), живлення (червоний) і сигналу (зазвичай білий — на схемі нижче помаранчевий) до контактів RC на Pixhawk.

![RCIN_connection](https://ardupilot.org/copter/_images/RCIN_connection.jpg)

> **Порада.** Параметр, що вмикає вихід SBus на autopilot типу PixHawk, — `BRD_SBUS_OUT`. Він лише передає SBus назовні іншим пристроям, як-от servo (сервопривід). Він не для підключення receiver до RCin чи SBus In.

### DSM/DSM2/DSM-X/SRXL/SUM-D

На autopilot без окремого входу `DSM` їх можна підключати, як описано вище. Проте на autopilot з IOMCU (сімейство Pixhawk/Cube) з міркувань продуктивності наполегливо рекомендовано використовувати вхід `DSM` autopilot.

![pixhawk_spektrum_connection](https://ardupilot.org/copter/_images/pixhawk_spektrum_connection.jpg)

### FPort/FPort2

FPort — двонаправлений протокол: в один бік іде RC за SBus, в інший — послідовна telemetry. Якщо підключити його до autopilot як SBus, частину RC буде декодовано, але вбудовану telemetry буде втрачено. Як підключати до одного з UART autopilot — див. [документацію з налаштування FPort](fport.md).

### mLRS

[mLRS](https://ardupilot.org/copter/docs/common-mlrs-rc.html) *(ще не перекладено)* може давати і радіокерування, і telemetry MAVLink. Receiver mLRS мають вихідний контакт RC, який можна налаштувати на протокол SBUS або CRSF (CRSF — лише дані RC). Для SBUS його можна підключити до контакту RCin autopilot. Для CRSF чи SBUS його можна підключити до контакту RX будь-якого UART autopilot і налаштувати цей порт на протокол RC. Протокол CRSF дає змогу передавати на autopilot інформацію RSSI/LQ.

Для необов'язкової telemetry на receiver є окремий порт TX/RX, який підключається до UART telemetry MAVLink autopilot. Якщо ви не використовуєте RC overrides з GCS (наприклад, джойстик), однопровідне підключення RC можна не робити, а налаштувати receiver mLRS видавати канали RC через MAVLink.

### SRXL2/CRSF/ELRS

Ці двонаправлені протоколи потребують UART. Налаштування і підключення — див. посилання нижче.

### IRC Ghost

Потребує підключення до повного UART через його контакт TX. Порт слід налаштувати на напівдуплексний вхід RC, наприклад для SERIAL2:

- `SERIAL2_PROTOCOL` = 23 (RCinput)
- `SERIAL2_OPTIONS` = 4 (Half-Duplex)
- `RSSI_TYPE` = 3

### Вхід RC на UART

> **Примітка.** Будь-який вхід RX UART автоматично визначає всі протоколи (крім PPM і SRXL2/CRSF/ELRS, які потребують ще й підключення контакту TX UART), якщо протокол порту SERIAL встановлено в 23 (наприклад, зазвичай `SERIAL2_PROTOCOL` для UART TELEM2, якщо використовується). Виняток — SBUS, підключений до UART на autopilot на F4. Він потребує зовнішнього інвертора, бо SBUS інвертований, а autopilot на F4 не мають вибору інверсії на контактах UART.

> **Примітка.** Швидкість UART автоматично встановлюється і контролюється firmware (прошивка), щойно виявлено будь-який послідовний протокол RC.

## Вибір радіосистеми

Вибір залежить від багатьох чинників: дальності, вимог до telemetry, ціни, сумісності з наявним обладнанням тощо. Більшість виробників пропонують багато моделей з різними можливостями. Багато систем інші виробники розібрали й «клонували», пропонуючи дешевші версії RC transmitter і receiver. Багато RC transmitter підтримують кілька протоколів і працюють на firmware [OpenTX](https://www.open-tx.org/), дуже гнучкій, що також дає змогу використовувати LUA-скрипти для відображення даних telemetry на РК-екрані.

### Дальність

Дальність радіокерування дуже залежить від системи, встановлення, антен, рельєфу і навіть погоди. Але загалом, для цілей цього огляду, системи RC можна поділити на короткого радіуса (до 2 км), середнього (2–10 км) і далекого (>10 км). Крім того, вони можуть мати однонаправлену (з апарата на RC transmitter) або двонаправлену (між апаратом і RC transmitter) telemetry.

### Telemetry

RC transmitter FrSky Horus зі скриптом Yaapu LUA

![x10-horus](https://ardupilot.org/copter/_images/x10-horus.png)

Одні системи мають прозорі радіомодеми, що передають telemetry від autopilot, інші — пропрієтарні протоколи. Системи з пропрієтарними протоколами часто мають засоби відображення даних telemetry на екрані самого RC transmitter, як-от FRSky чи RC transmitter на [OpenTX](https://www.open-tx.org/).

Швидкість telemetry — від 56K до 1–2K бод залежно від протоколу, а іноді й відстані. Часто дальність telemetry менша за дальність радіокерування.

[Consult]

### Кількість каналів

Для більшості апаратів ArduPilot потрібно щонайменше 5 каналів, проте в більшості систем зазвичай доступно 8–16 каналів, що дуже зручно для керування іншими функціями апарата, як-от камерами чи опціями польоту. Багатьом апаратам, як-от багатьом QuadPlane, лише для базової роботи потрібно 8 каналів.

Нижче — таблиця з кількома поширеними системами з цими характеристиками. Зверніть увагу: не всі версії RC transmitter та/або receiver певного виробника можуть мати ці характеристики. Також існує багато «клонів» чи «сумісних» версій цих систем; наведено лише оригінальні системи.

| Оригінальний виробник | Дальність | Telemetry | Швидкість telem | Дисплей TX | Протокол RC | Примітки |
|---|---|---|---|---|---|---|
| Flysky | Коротка | Так | - | так | i-BUS/SBUS | 7 |
| FrSky X series | Коротка | Двонапр. | Середня | так | PPM-SUM/SBUS/FPort | 2 |
| Futaba | Коротка | Ні | - | - | SBus | |
| Graupner | Коротка | Так | Середня | так | SUM-D | |
| Multiplex | Коротка | Ні | - | - | SRXL | |
| Spektrum | Коротка | Власна виробника | - | так | DSM/DSM2/DSM-X/SRXL | |
| FrSky R9 series | Середня | Двонапр. | Середня | так | PPM-SUM/SBUS/FPort | 2 |
| IRC Ghost | Середня | Власна виробника | | так | IRC Ghost | |
| CRSF | Далека | Двонапр. | Змінна | так | SBUS/CRSF | 3 |
| DragonLink | Далека | Двонапр. | 56K | через MTP/LUA | PPM_SUM/SBUS | 1 |
| ELRS | Далека | Двонапр. | Змінна | необов'язково | SBUS/CRSF/Mavlink | 4 |
| HereLink | Далека | Двонапр. | 56K | вбудований | SBUS | 8 |
| mLRS | Далека | Двонапр. | 12K - 91K | через LUA | SBUS/CRSF | 5 |
| SIYI | Далека | Двонапр. | 56K | вбудований | SBUS | 8 |

Примітка 1: DragonLink дає прозорий канал 56 кбод для telemetry, що дає змогу передавати повну telemetry MAVLink з апарата на передавальний модуль і назад. Dragonlink — додатковий модуль до RC transmitter, як-от FRSky Taranis чи RadioMaster T16. Див. [DragonLink](https://ardupilot.org/copter/docs/common-dragonlink-rc.html) *(ще не перекладено)*. Є [конвертери MTP (Mavlink to Passthru)](https://www.rcgroups.com/forums/showthread.php?3089648-Mavlink-To-FrSky-Passthrough-Converter), що дають змогу напряму відображати дані telemetry MAVLink на RC transmitter з OpenTX за допомогою [Yaapu Telemetry LUA Script](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*.

Примітка 2: Див. [Yaapu Telemetry Script](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*. Крім відображення даних telemetry, з RC transmitter, сумісного з Open TX, можна змінювати параметри через telemetry FRSky. Більшість RC transmitter, сумісних з FRSky, працюють на [OpenTX](https://www.open-tx.org/). Зверніть увагу: системи R9 не зовсім далекого радіуса, але мають значно більшу дальність, ніж звичайні системи FRSky, які самі на верхній межі категорії короткого радіуса — 1.6–2 км.

Примітка 3: ArduPilot дає змогу надсилати свої дані telemetry через CRSF так, щоб їх можна було відображати на RC transmitter з [OpenTX](https://www.open-tx.org/) за допомогою [Yaapu Telemetry LUA Script](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*. Крім відображення даних telemetry, з RC transmitter, сумісного з Open TX, можна також змінювати параметри через telemetry CRSF. Див. [TBS Crossfire Telemetry](crsf-telemetry.md).

Примітка 4: ELRS (ExpressLRS) — гнучка система з відкритим кодом, що може видавати протоколи CRSF, SBUS чи MAVLink (із вбудованим RC). Telemetry потребує CRSF чи Mavlink, а receiver має бути підключений до повного UART. Докладніше — див. [сайт ExpressLRS](https://www.expresslrs.org/) і [TBS CRSF/ ELRS](crossfire-elrs.md).

Примітка 5: Проєкт mLRS — firmware, створена спеціально для передачі і RC, і MAVLink. Доступна швидкість telemetry залежить від вибраного режиму і регулюється контролем потоку RADIO_STATUS. Вона використовує протокол RC CRSF (TBS Crossfire) і на receiver, і на передавальному модулі. Також вона має повну telemetry MAVLink через послідовні підключення на передавальному модулі й receiver.

Примітка 6: «Власна виробника» (Vendor Specific) telemetry означає, що вони підтримують додаткові датчики на апараті і можуть відображати інформацію на певних RC transmitter свого виробника, але не надсилають telemetry ArduPilot з апарата на сумісні з ArduPilot GCS чи скрипти відображення OpenTX.

Примітка 7: Receiver має підтримувати telemetry i-BUS (шукайте порт SENS на receiver або дивіться характеристики виробу).

Примітка 8: Ці системи, крім радіокерування і telemetry апарата, мають вбудовану передачу HD-відео з камер з Ethernet чи HDMI.

## Посилання на системи радіокерування

Без вбудованої telemetry:

1. [Flysky (без порту SENS)](https://ardupilot.org/copter/docs/common-flysky-rc.html) *(ще не перекладено)*
2. [Futaba](https://ardupilot.org/copter/docs/common-futaba-rc.html) *(ще не перекладено)*
3. [Spektrum](https://ardupilot.org/copter/docs/common-spektrum-rc.html) *(ще не перекладено)*

З вбудованою telemetry:

1. [DragonLink](https://ardupilot.org/copter/docs/common-dragonlink-rc.html) *(ще не перекладено)*
2. [Flysky (з портом SENS)](https://ardupilot.org/copter/docs/common-flysky-rc.html) *(ще не перекладено)*
3. [FRSky](https://ardupilot.org/copter/docs/common-frsky-rc.html) *(ще не перекладено)*
4. [Graupner (HOTT)](https://ardupilot.org/copter/docs/common-graupner-rc.html) *(ще не перекладено)*
5. [Herelink — система RC/telemetry/HD-відео](https://ardupilot.org/copter/docs/common-herelink.html) *(ще не перекладено)*
6. [mLRS](https://ardupilot.org/copter/docs/common-mlrs-rc.html) *(ще не перекладено)*
7. [Multiplex (підтримки telemetry M-Link в ArduPilot поки немає)](https://ardupilot.org/copter/docs/common-multiplex-rc.html) *(ще не перекладено)*
8. [SIYI](https://ardupilot.org/copter/docs/common-siyi-rc.html) *(ще не перекладено)*
9. [Spektrum SRXL2](https://ardupilot.org/copter/docs/common-spektrum-rc.html) *(ще не перекладено)*
10. [TBS CRSF/ ELRS](crossfire-elrs.md)

Багатопротокольні:

1. [RC transmitter Jumper T16 Pro/ RadioMaster T16](https://ardupilot.org/copter/docs/common-jumperT16pro.html) *(ще не перекладено)*

### Рекомендації

Давати рекомендації складно, бо спектр можливостей, функцій і цін дуже широкий.

У Європі Multiplex і Graupner — усталені системи, що відповідають рекомендаціям ЄС щодо випромінювання (як і багато інших марок як опція).

Flysky випускає дуже дешеві системи початкового рівня.

FRSky і Spektrum мають найбільшу базу користувачів, причому Spektrum домінує серед систем RC для паркових і початкових моделей. FRSky має можливості telemetry і використовує [OpenTX](https://www.open-tx.org/), дуже гнучку firmware, в яку постійно додаються нові функції.

Jumper T16 і RadioMaster T16 — клони RC transmitter на OpenTX, схожі на FRSky Horus, з кількома вбудованими протоколами RC.

## Кодери PPM

[Кодер PPM](https://www.amazon.com/s?k=ppm+encoder) дає змогу використовувати будь-який старіший receiver, що має лише виходи PWM на кожен канал замість виходу SBUS чи PPM. Докладніше — див. [PPM Encoders](https://ardupilot.org/copter/docs/common-ppm-encoders-new.html) *(ще не перекладено)*. На багатьох нових autopilot цей протокол уже не підтримується, і він поступово застаріває.
