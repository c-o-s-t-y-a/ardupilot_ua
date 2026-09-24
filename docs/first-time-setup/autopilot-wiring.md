# Типове підключення autopilot (автопілота)

> Оригінал: [Typical Autopilot Wiring Connections](https://ardupilot.org/copter/docs/common-flight-controller-wiring.html)

<img src="https://ardupilot.org/copter/_images/fc-io.jpg" alt="fc-io" width="450">

Тут описано підключення базової/обов'язкової периферії до autopilot (автопілот). Докладний опис кожного порту/роз'єму autopilot — у [Autopilot I/O](https://ardupilot.org/copter/docs/common-flight-controller-io.html) *(ще не перекладено)*.

## GPS/compass

GPS зазвичай обов'язковий для plane, copter і rover, окрім випадків, коли використовується інший [датчик чи система визначення позиції](https://ardupilot.org/copter/docs/common-non-gps-navigation-landing-page.html) *(ще не перекладено)*. Sub не використовує GPS. Compass (компас) також зазвичай потрібен для Copter, Rover, Sub і QuadPlane (різновид Plane) (альтернативи compass — див. [Compassless](https://ardupilot.org/copter/docs/common-compassless.html) *(ще не перекладено)*), але не для звичайних літаків, хоча й рекомендований.

> **Примітка.** Деякі режими Copter і Rover можуть працювати без GPS і compass (див. документацію апарата щодо його flight mode (польотний режим)).

У системі можна використовувати кілька GPS та/або compass, докладніше — у [GPS Blending](https://ardupilot.org/copter/docs/common-gps-blending.html) *(ще не перекладено)*, [Advanced Compass Setup](https://ardupilot.org/copter/docs/common-compass-setup-advanced.html) *(ще не перекладено)* і [EKF3 Affinity and Lane Switching](https://ardupilot.org/copter/docs/common-ek3-affinity-lane-switching.html) *(ще не перекладено)*.

<img src="https://ardupilot.org/copter/_images/gps-connection.jpg" alt="gps-connection" width="450">

> **Примітка.** TX і RX між autopilot і модулем GPS перехрещуються.

> **Примітка.** За замовчуванням у ArduPilot GPS зазвичай підключено до логічного порту Serial Port 3. Який саме фізичний UART (послідовний порт) призначено на Serial Port 3 на конкретному autopilot, указано в [документації](https://ardupilot.org/copter/docs/common-autopilots.html) *(ще не перекладено)* цього autopilot.

> **Примітка.** Важливо, щоб GPS був підключений до першого порту SERIALx, у якого параметр `SERIALx_PROTOCOL` встановлено в «5» (GPS): якщо на першому порту з протоколом GPS модуль GPS не знайдено, пошук GPS під час запуску припиняється.

Приклад підключення до autopilot Pixhawk, а також додаткову інформацію про налаштування і монтаж наведено на сторінці [Модуль GPS + compass 3DR UBlox](gps-compass-module.md).

## Вхід RC

> **Примітка.** Sub наразі не використовує радіокерування, але це в розробці.

Для керування пілотом зазвичай використовують receiver (приймач) радіокерування. Керувати апаратом виключно з GCS (наземна станція керування) через telemetry (телеметрія) можливо, але не рекомендовано. (Утім, керувати апаратом з GCS можна за допомогою джойстика. Див. [Joysticks](https://ardupilot.org/copter/docs/common-joystick.html) *(ще не перекладено)*.)

<img src="https://ardupilot.org/copter/_images/rx-connection.jpg" alt="rx-connection" width="450">

ArduPilot автоматично розпізнає такі послідовні протоколи receiver:

1. receiver радіокерування (R/C) з PPM
2. receiver SBus
3. receiver FPort (див. [FPort receivers](https://ardupilot.org/copter/docs/common-FPort-receivers.html) *(ще не перекладено)*)
4. receiver Crossfire (CRSF) і ELRS (див. [TBS RC](https://ardupilot.org/copter/docs/common-tbs-rc.html) *(ще не перекладено)*, потрібне повне підключення UART)
5. receiver Spektrum DSM і DSM2
6. сателітні receiver Spektrum DSM-X
7. receiver IBUS
8. receiver MULTIPLEX SRXL версій 1 і 2.

Для традиційних receiver з окремим дротом на кожен канал (PWM (широтно-імпульсна модуляція)) можна використати кодер PPM, що перетворює виходи receiver на PPM.

> **Порада.** Починаючи з firmware (прошивка) ArduPilot 4.0, як вхід для receiver можна використовувати будь-який UART autopilot замість призначеного контакту RCin чи SBUS — для цього встановіть `SERIALx_PROTOCOL` цього порту в 23. Проте деякі послідовні протоколи потребують інверсії (SBUS, FPort), і UART має вміти інвертувати вхід RX параметром `SERIALx_OPTIONS`, інакше знадобиться зовнішній інвертор. Так до autopilot можна також підключити другий receiver для резервування. Якщо перший receiver (перший, визначений як справний після запуску) відмовить, використовуватиметься другий. Зверніть увагу: для другого receiver, коли він стане активним, використовуватимуться ті самі діапазони і trim (підстроювання нейтралі) входів RC, що були відкалібровані. Щоб це працювало правильно, обидва receiver МАЮТЬ бути налаштовані не надсилати імпульсів у режимі failsafe (аварійний захист). Також треба встановити біт 10 у `RC_OPTIONS`.

> **Порада.** Інформацію про сумісні receiver і їх підключення наведено в [Compatible RC Tx/Rx Systems](https://ardupilot.org/copter/docs/common-rc-systems.html) *(ще не перекладено)*. Про використання кількох receiver див. також [Multiple RC receivers](https://ardupilot.org/copter/docs/common-multiple-rx.html) *(ще не перекладено)*.

<img src="https://ardupilot.org/copter/_images/FRSkyTaranis.jpg" alt="FRSky Taranis Transmitter" width="450">

*RC transmitter (пульт радіокерування) FRSky Taranis*

## Підключення моторів/servo

ESC (електронний регулятор обертів) моторів та/або servo (сервопривід) з PWM підключаються до виходів PWM autopilot.

Вони позначені або як виходи MAIN/AUX, або просто як OUTPUT. Ці виходи дають сигнали PWM або Dshot для ESC моторів чи servo рулів. Іноді їх можна використовувати і як GPIO (вивід загального призначення) для керування реле, парашутами, захоплювачами тощо.

Позначки MAIN/AUX на контролерах зазвичай означають, що використовується співпроцесор IOMCU. Він дає виходи, призначені для моторів/servo, і резервний спосіб керування через RC, якщо основний autopilot відмовить. Виходи MAIN ідуть від цього співпроцесора, а виходи з позначкою AUX керуються безпосередньо autopilot. Більшість autopilot у вигляді однієї плати не використовують IOMCU і мають виходи з позначками лише OUTPUTx або Mx.

Ця різниця важлива, бо виходи AUX (і OUTPUT на autopilot без IOMCU) можна використовувати як GPIO, а також для PWM чи Dshot, тоді як виходи MAIN — лише для PWM.

> **Примітка.** Кілька autopilot, що НЕ використовують IOMCU, позначають свої виходи як MAIN, тож насправді їх можна використовувати як GPIO та/або для керування ESC через Dshot. Приклади — CUAV V5 Nano і Holybro Pixhawk 4 Mini.

Часто ці виходи виведено на трирядні колодки контактів, які крім окремих сигналів подають або розводять живлення і землю servo. Це живлення зазвичай подається ззовні, наприклад від ESC чи BEC (стабілізатор живлення), хоча деякі autopilot дають його від внутрішніх стабілізаторів.

Приклад підключення для Rover:

<img src="https://ardupilot.org/copter/_images/servo-motor-connection.jpg" alt="servo-motor-connection" width="450">

Приклад для коптерів, що використовують лише мотори. Тут підключено лише сигнальні лінії ESC.

<img src="https://ardupilot.org/copter/_images/pixhawk_motor_outputs.jpg" alt="pixhawk_motor_outputs" width="450">

Для Copter див. також [Підключення ESC і моторів](connect-escs-and-motors.md).

Коротко: для коптерів підключіть кожен сигнальний дріт від PDB (плата розподілу живлення) до сигнальних контактів (S) основних виходів відповідно до номера мотора:

- Вихід 1 = Мотор 1 — Вихід 5 = Мотор 5
- Вихід 2 = Мотор 2 — Вихід 6 = Мотор 6
- Вихід 3 = Мотор 3 — Вихід 7 = Мотор 7
- Вихід 4 = Мотор 4 — Вихід 8 = Мотор 8

## Підключення зумера і кнопки безпеки

Зумер і кнопка безпеки (safety switch) необов'язкові, але корисні в деяких конфігураціях. Не всі autopilot мають ці роз'єми. BUZZER і SWITCH підключаються до відповідних портів, як показано.

<img src="https://ardupilot.org/copter/_images/safetysw-connection.jpg" alt="safetysw-connection" width="450">

> **Попередження.** Розміщуйте зумер щонайменше за 5 см від flight controller (польотний контролер), інакше шум може заважати роботі accelerometer (акселерометр).

## Підключення іншої периферії

Залежно від вашого обладнання може бути підключено ще будь-яку кількість периферії — датчики, камери, захоплювачі тощо. Вони описані на підсторінках розділу [Додаткове обладнання](https://ardupilot.org/copter/docs/common-optional-hardware.html) *(ще не перекладено)*.

Інформацію про підключення цієї периферії до autopilot наведено на відповідних сторінках.

## Пов'язана інформація

1. [Autopilot I/O](https://ardupilot.org/copter/docs/common-flight-controller-io.html) *(ще не перекладено)*
2. [Приклад підключення на Pixhawk](https://ardupilot.org/copter/docs/common-pixhawk-wiring-and-quick-start.html) *(ще не перекладено)*
3. [Живлення Pixhawk](https://ardupilot.org/copter/docs/common-powering-the-pixhawk.html) *(ще не перекладено)*
4. [Compatible RC Tx/Rx Systems](https://ardupilot.org/copter/docs/common-rc-systems.html) *(ще не перекладено)*
5. [Advanced Pixhawk Quadcopter Wiring Chart](https://ardupilot.org/copter/docs/advanced-pixhawk-quadcopter-wiring-chart.html) *(ще не перекладено)*
