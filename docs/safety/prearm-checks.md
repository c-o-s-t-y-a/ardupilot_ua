# Pre-arm safety checks (передпольотні перевірки безпеки)

> Оригінал: [Pre-Arm Safety Checks](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html)

ArduPilot має набір передпольотних перевірок безпеки pre-arm (передпольотна перевірка), які не дають виконати arm (переведення в робочий стан) рушійної системи апарата, якщо до початку руху виявлено будь-яку з досить великої кількості проблем — пропущене калібрування, помилку конфігурації чи погані дані датчиків. Ці перевірки допомагають запобігти аваріям і відльотам, але деякі з них за потреби можна вимкнути.

[Відео (YouTube)](https://www.youtube.com/watch?v=gZ3H2eLmStI)

> **Попередження.** Ніколи не вимикайте перевірки arm (тобто `ARMING_SKIPCHK` не дорівнює «0»), крім випадків стендового тестування. Завжди усувайте всі помилки pre-arm чи arm ПЕРЕД спробою польоту. Інакше можна втратити апарат.

## Як дізнатися через GCS, яка перевірка pre-arm не пройдена

Пілот помітить, що перевірку pre-arm не пройдено, бо не зможе виконати arm, а світлодіод сповіщень, якщо він є, блиматиме жовтим. Щоб визначити, яка саме перевірка не пройдена:

1. Підключіть autopilot (автопілот) до GCS (наземна станція керування) USB-кабелем або через [telemetry (телеметрія)](../first-time-setup/telemetry.md).
2. Переконайтеся, що GCS підключена до апарата (наприклад, у Mission Planner натисніть кнопку «Connect» угорі праворуч).
3. Увімкніть RC transmitter (пульт радіокерування) і спробуйте виконати arm (звичайним способом — throttle (газ) вниз, yaw (рискання) праворуч, — або перемикачем RCx_OPTION).
4. Перша причина невдалої перевірки pre-arm з'явиться червоним у вікні HUD.

Поки апарат disarmed (не в робочому стані), повідомлення про невдалі перевірки pre-arm також надсилаються на GCS приблизно кожні 30 секунд. Якщо ви хочете вимкнути це і отримувати їх лише після невдалої спроби arm, встановіть біт 1 (значення 1) у `ARMING_OPTIONS`.

Нижче перелічено повідомлення в тому вигляді, як їх показує GCS (зазвичай з префіксом «PreArm:»).

### Повідомлення про помилки pre-arm (усі типи апаратів)

| Повідомлення | Причина | Рішення |
|---|---|---|
| `3D Accel calibration needed` | Калібрування accelerometer (акселерометр) не виконано | Виконайте [калібрування accelerometer](../first-time-setup/accelerometer-calibration.md) |
| `Accels calibrated requires reboot` | Після калібрування accelerometer autopilot треба перезавантажити | Перезавантажте autopilot |
| `Accels inconsistent` | Два accelerometer розходяться на 0.75 м/с² | Повторіть [калібрування accelerometer](../first-time-setup/accelerometer-calibration.md). Дайте autopilot прогрітися і перезавантажте. Якщо помилка не зникає, замініть autopilot. Якщо двигун внутрішнього згоряння працює до arm, як можливе рішення див. біт 2 `ARMING_OPTIONS`. |
| `ADSB out of memory` | Autopilot вичерпав пам'ять | Вимкніть частину функцій або замініть на потужніший autopilot |
| `Accels not healthy` | Щонайменше один accelerometer не надає даних | Перезавантажте autopilot. Якщо помилка не зникає, замініть autopilot |
| `AHRS: not using configured AHRS type` | EKF3 ще не готовий, апарат використовує DCM | Якщо ви в приміщенні, вийдіть надвір. Забезпечте надійний GPS lock (фіксація позиції GPS). Перевірте, чи правильно налаштовано EKF (розширений фільтр Калмана) — див. `AHRS_EKF_TYPE` |
| `AHRS: waiting for home` | GPS ще не отримав фіксацію | Якщо ви в приміщенні, вийдіть надвір. Переконайтеся, що калібрування compass (компас) і accelerometer виконано. Усуньте джерела радіозавад, що можуть заважати GPS |
| `Airspeed: 1 not healthy` | Autopilot не може отримати дані від датчика | Перевірте фізичне підключення і [налаштування](https://ardupilot.org/copter/docs/common-airspeed-sensor.html) *(ще не перекладено)* |
| `AP_Relay not available` | Парашут налаштовано неправильно | Парашут керується через реле, але функції реле немає у firmware (прошивка). Ймовірно, використовувався [Custom build server](https://custom.ardupilot.org/) — зберіть firmware з увімкненим реле |
| `Auxiliary authorisation refused` | Зовнішня система відмовила в авторизації | Перевірте зовнішню систему авторизації |
| `Baro: not healthy` | Barometer (барометр) не надає даних | Перезавантажте autopilot. Якщо помилка не зникає, замініть autopilot |
| `Batch sampling requires reboot` | Функція пакетного запису потребує перезавантаження autopilot | Перезавантажте autopilot або перевірте налаштування [пакетного запису](https://ardupilot.org/copter/docs/common-imu-batchsampling.html) *(ще не перекладено)* |
| `Battery below minimum arming capacity` | Ємність батареї нижча за BATT_ARM_MAH | Замініть батарею або змініть `BATT_ARM_MAH` |
| `Battery below minimum arming voltage` | Напруга батареї нижча за BATT_ARM_VOLT | Замініть батарею або змініть `BATT_ARM_VOLT` |
| `Battery capacity failsafe critical >= low` | Неправильне налаштування failsafe (аварійний захист) батареї | Перевірте, що `BATT_LOW_MAH` більший за `BATT_CRT_MAH` |
| `Battery critical capacity failsafe` | Ємність батареї нижча за BATT_CRT_MAH | Замініть батарею або змініть `BATT_CRT_MAH` |
| `Battery critical voltage failsafe` | Напруга батареї нижча за BATT_CRT_VOLT | Замініть батарею або змініть `BATT_CRT_VOLT` |
| `Battery low capacity failsafe` | Ємність батареї нижча за BATT_LOW_MAH | Замініть батарею або змініть `BATT_LOW_MAH` |
| `Battery low voltage failsafe` | Напруга батареї нижча за BATT_LOW_VOLT | Замініть батарею або змініть `BATT_LOW_VOLT` |
| `Battery unhealthy` | Батарея не надає даних | Перевірте фізичне підключення монітора батареї і [налаштування](https://ardupilot.org/copter/docs/common-powermodule-landingpage.html) *(ще не перекладено)* |
| `Battery voltage failsafe critical >= low` | Неправильне налаштування failsafe батареї | Перевірте, що `BATT_LOW_VOLT` більша за `BATT_CRT_VOLT` |
| `BendyRuler OA requires reboot` | Зміна налаштувань обходу перешкод потребує перезавантаження | Перезавантажте autopilot. Див. [налаштування обходу перешкод](https://ardupilot.org/copter/docs/common-object-avoidance-landing-page.html) *(ще не перекладено)* |
| `Board (Xv) out of range 4.3-5.8v` | Напруга плати нижча за BRD_VBUS_MIN або занадто висока | Перевірте живлення. Якщо живлення від USB, підключіть батарею або замініть USB-кабель |
| `BTN_PINx=y invalid` | Кнопку налаштовано неправильно | BTNx_PIN має недопустиме значення. Перевірте [інструкцію з налаштування кнопок](https://ardupilot.org/copter/docs/common-buttons.html) *(ще не перекладено)* |
| `BTN_PINx=y, set SERVOz_FUNCTION=-1` | Кнопку налаштовано неправильно | Встановіть SERVOz_FUNCTION у -1 |
| `Can't check rally without position` | EKF ще не має оцінки позиції | Зачекайте або перейдіть туди, де кращий прийом GPS |
| `Check EK3_SRCx_POSXY/VELXY/POSZ/VELZ/YAW` | Параметр джерела EKF3 має непідтримуване значення | Перевірте вказаний [набір параметрів EK3_SRC](https://ardupilot.org/copter/docs/common-ekf-sources.html) *(ще не перекладено)* і виберіть підтримуване джерело |
| `Check fence` | Не вдалося ініціалізувати функцію огорожі (fence) | Перезавантажте autopilot |
| `Check mag field (xy diff:x>875)` | Горизонтальна напруженість поля compass занадто велика або мала | Перенесіть апарат подалі від металу навколо. Віддаліть compass від металу на frame (рама). Повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. |
| `Check mag field (z diff:x>875)` | Вертикальна напруженість поля compass занадто велика або мала | Перенесіть апарат подалі від металу навколо. Віддаліть compass від металу на frame. Повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. |
| `Check mag field: x, max y, min z` | Напруженість поля compass занадто велика або мала | Перенесіть апарат подалі від металу навколо. Віддаліть compass від металу на frame. Повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. |
| `Chute has no channel` | Парашут налаштовано неправильно | Парашут керується через PWM (широтно-імпульсна модуляція), але функцію виходу servo (сервопривід) не налаштовано (напр. потрібно SERVOx_FUNCTION = 27). Див. [інструкцію з налаштування парашута](parachute.md) |
| `Chute has no relay` | Парашут налаштовано неправильно | Парашут керується через реле, але вихід реле не налаштовано. Див. [інструкцію з налаштування парашута](parachute.md) |
| `Chute is released` | Парашут уже розкрито | Перезавантажте autopilot |
| `Compass calibrated requires reboot` | Після калібрування compass autopilot треба перезавантажити | Перезавантажте autopilot |
| `Compass calibration running` | Триває калібрування compass | Завершіть або скасуйте [калібрування compass](../first-time-setup/compass-calibration.md) |
| `Compass not calibrated` | Зміщення compass нульові або змінилася кількість датчиків | Виконайте [калібрування compass](../first-time-setup/compass-calibration.md) |
| `Compass X not healthy` | Compass X не надає даних | Перевірте з'єднання між compass X і autopilot та [налаштування](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) *(ще не перекладено)* |
| `Compass offsets too high` | Параметри зміщень compass занадто великі | Віддаліть compass від металу на frame і повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. Збільште `COMPASS_OFFS_MAX`. |
| `Compasses inconsistent` | Кути або напруженість поля двох compass не збігаються | Перевірте орієнтацію compass (напр. `COMPASS_ORIENT`). Віддаліть compass від металу на frame. Повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. |
| `CrashDump data detected` | Записано дані Crash Dump | Стався збій процесора, дані записано. Plane, ймовірно, небезпечно використовувати в польоті! Див. [crash_dump](watchdog.md#crash-dump) |
| `Dijkstra OA requires reboot` | Зміна налаштувань обходу перешкод потребує перезавантаження | Перезавантажте autopilot. Див. [налаштування обходу перешкод](https://ardupilot.org/copter/docs/common-object-avoidance-landing-page.html) *(ще не перекладено)* |
| `Disarm Switch on` | Допоміжний перемикач **Disarm** у верхньому положенні | Переведіть перемикач **Disarm** у нижнє положення або перевірте налаштування [допоміжних функцій](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* |
| `Downloading logs` | Arm неможливий, поки завантажуються log-и (журнал польоту) | Дочекайтеся, поки log-и завантажаться, скасуйте завантаження або перезавантажте autopilot |
| `DroneCAN: Duplicate Node x../y!` | DroneCAN бачить однакові ідентифікатори вузлів у двох пристроїв | Очистіть DNS-сервер DroneCAN, встановивши `CAN_D1_UC_OPTION` = 1, і перезавантажте |
| `DroneCAN: Failed to access storage!` | Можлива апаратна проблема | Перезавантажте autopilot |
| `DroneCAN: Failed to add Node x!` | DroneCAN не зміг встановити з'єднання з пристроєм | Перевірте фізичне підключення датчика і живлення |
| `DroneCAN: Node x unhealthy!` | Пристрій DroneCAN не надає даних | Перевірте фізичне підключення датчика і живлення |
| `Duplicate Aux Switch Options` | Два перемикачі допоміжних функцій для однієї функції | Перевірте налаштування [допоміжних функцій](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)*. Перевірте, чи немає параметрів `RCx_OPTION` з однаковими значеннями |
| `EK3 sources require x` | Вибране джерело EKF3 недоступне | Підключіть або налаштуйте названий датчик або змініть відповідний [набір параметрів EK3_SRC](https://ardupilot.org/copter/docs/common-ekf-sources.html) *(ще не перекладено)*, щоб використовувати доступне джерело |
| `EKF3 Roll/Pitch inconsistent by x degs` | Оцінки кута нахилу по roll (крен) або pitch (тангаж) не збігаються | Зазвичай через те, що EKF3 не отримує достатньої точності GPS, але можливі й помилки інших датчиків. Вийдіть надвір, зачекайте або перезавантажте autopilot. |
| `EKF3x vel error y` | EKF3 має інновацію швидкості «y» | EKF3 отримує великі інновації позиції/швидкості. Перевірте GPS, зачекайте або перезавантажте. |
| `EKF3 waiting for GPS config data` | Автоматичне налаштування GPS не завершено | Перевірте підключення і налаштування GPS, особливо якщо це GPS на DroneCAN |
| `EKF3 Yaw inconsistent by x degs` | Оцінки кута yaw не збігаються | Зачекайте або перезавантажте autopilot |
| `Failed to open mission.stg` | Не вдалося завантажити місію з SD-карти | Перевірте SD-карту. Спробуйте повторно зберегти місію на SD-карту |
| `Failed to create log directory /APM/LOGS : ENOMEM` | Не вдалося створити на SD-карті каталог для log | Зменште `LOG_FILE_BUFSIZE` або вимкніть інші функції, щоб зменшити використання пам'яті |
| `Fence requires position` | Якщо огорожі (fence) увімкнено, потрібна оцінка позиції | Зачекайте або перенесіть апарат туди, де відкрите небо. Зменште кількість джерел радіозавад |
| `FENCE_ALT_MAX < FENCE_ALT_MIN` | FENCE_ALT_MAX має бути більшим за FENCE_ALT_MIN | Збільште `FENCE_ALT_MAX` або зменште `FENCE_ALT_MIN` |
| `FENCE_MARGIN is less than FENCE_RADIUS` | FENCE_MARGIN має бути більшим за FENCE_RADIUS | Збільште `FENCE_RADIUS` або зменште `FENCE_MARGIN` |
| `FENCE_MARGIN too big` | FENCE_ALT_MAX - FENCE_ALT_MIN < 2x FENCE_MARGIN | Зменште `FENCE_MARGIN` або збільште різницю між `FENCE_ALT_MAX` і `FENCE_ALT_MIN` |
| `Fences enabled, but none selected` | Огорожі увімкнено, але жодної не задано | Вимкніть частину чи всі огорожі через `FENCE_ENABLE` або `FENCE_TYPE` або задайте відсутні огорожі |
| `Fences invalid` | Багатокутна огорожа недійсна | Перевірте, що лінії багатокутної огорожі не перетинаються |
| `FETtec: Invalid motor mask` | Неправильне налаштування FETtec | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FETtec: Invalid pole count x` | Неправильне налаштування FETtec | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FETtec: No uart` | Неправильне налаштування FETtec | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FETtec: Not initialised` | ESC (електронний регулятор обертів) FETtec не обмінюються даними з autopilot | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FETtec: x of y ESCs are not running` | ESC FETtec не обертають мотори | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FETtec: x of y ESCs are not sending telem` | ESC FETtec не обмінюються даними з autopilot | Див. [налаштування FETtec](https://ardupilot.org/copter/docs/common-fettec-onewire.html) *(ще не перекладено)* |
| `FFT calibrating noise` | Аналіз FFT Harmonic Notch не завершено | Дочекайтеся завершення [аналізу FFT у польоті](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `FFT config MAXHZ xHz > yHz` | Неправильне налаштування FFT Harmonic Notch | Див. [налаштування In-Flight FFT Harmonic Notch](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `FFT self-test failed, max error Hz` | Збій FFT Harmonic Notch | Див. [налаштування In-Flight FFT Harmonic Notch](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `FFT still analyzing` | Аналіз FFT Harmonic Notch не завершено | Дочекайтеся завершення [аналізу FFT у польоті](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `FFT: calibrated xHz/xHz/xHz` | Проблема FFT Harmonic Notch | Див. [налаштування In-Flight FFT Harmonic Notch](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `FFT: resolution is xHz, increase length` | Неправильне налаштування FFT Harmonic Notch | Див. [налаштування In-Flight FFT Harmonic Notch](https://ardupilot.org/copter/docs/common-imu-fft.html) *(ще не перекладено)* |
| `Generator: Not healthy` | Генератор не обмінюється даними з autopilot | Перевірте [налаштування генератора](https://ardupilot.org/copter/docs/common-generators.html) *(ще не перекладено)* |
| `Generator: No backend driver` | Firmware не містить вибраного генератора | Зберіть версію firmware з потрібним генератором на custom.ardupilot.org |
| `GPS alt error xm (see BARO_ALTERR_MAX)` | Висоти за GPS і BARO сильно розходяться | Прочитайте опис параметра `BARO_ALTERR_MAX` |
| `GPS and AHRS differ by Xm` | Позиції за GPS і EKF розходяться щонайменше на 10 м | Дочекайтеся покращення якості GPS. Перенесіть апарат туди, де відкрите небо. Зменште кількість джерел радіозавад |
| `GPS blending unhealthy` | Щонайменше один GPS не надає якісних даних | Перенесіть апарат туди, де відкрите небо. Зменште кількість джерел радіозавад. Перевірте [налаштування GPS blending](https://ardupilot.org/copter/docs/common-gps-blending.html) *(ще не перекладено)* |
| `GPS Node x not set as instance y` | Помилка налаштування GPS на DroneCan | Перевірте `GPS1_CAN_NODEID` і `GPS2_CAN_NODEID` |
| `GPS positions differ by Xm` | Позиції двох GPS розходяться на 50 м або більше | Дочекайтеся покращення якості GPS. Перенесіть апарат туди, де відкрите небо. Зменште кількість джерел радіозавад |
| `GPS x still configuring this GPS` | Автоматичне налаштування GPS не завершено | Дочекайтеся завершення налаштування. Перевірте підключення і налаштування GPS, особливо якщо це GPS на DroneCAN |
| `GPS x: Bad fix` | GPS не має надійного lock | Перенесіть апарат туди, де відкрите небо. Зменште кількість джерел радіозавад |
| `GPS x: not healthy` | GPS не надає даних | Перевірте фізичне підключення GPS до autopilot і [налаштування](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) *(ще не перекладено)* |
| `GPS x: primary but TYPE 0` | Основний GPS не налаштовано | Перевірте `GPS_PRIMARY` і переконайтеся, що відповідний `GPS1_TYPE` чи `GPS2_TYPE` збігається з типом використаного GPS |
| `GPS x: was not found` | GPS від'єднано або налаштовано неправильно | Перевірте фізичне підключення GPS до autopilot і [налаштування](https://ardupilot.org/copter/docs/common-positioning-landing-page.html) *(ще не перекладено)* |
| `GPSx yaw not available` | GPS-for-yaw налаштовано, але він не працює | Перейдіть туди, де кращий прийом GPS. Перевірте налаштування [GPS-for-yaw](https://ardupilot.org/copter/docs/common-gps-for-yaw.html) *(ще не перекладено)* |
| `Gyro x rate yHz < loop rate z Hz` | Частота циклу вища за частоту даних gyro (гіроскоп) | Зменште `SCHED_LOOP_RATE` |
| `Gyros inconsistent` | Два gyro розходяться щонайменше на 5 °/с | Перезавантажте autopilot і тримайте апарат нерухомо, доки не завершиться калібрування gyro. Дайте autopilot прогрітися і перезавантажте. Якщо помилка не зникає, замініть autopilot. Якщо двигун внутрішнього згоряння працює до arm, як можливе рішення див. біт 2 `ARMING_OPTIONS`. |
| `Gyros not calibrated` | Калібрування gyro, яке зазвичай виконується під час запуску, не вдалося | Перезавантажте autopilot і тримайте апарат нерухомо, доки не завершиться калібрування gyro |
| `Gyros not healthy` | Щонайменше один gyro не надає даних | Перезавантажте autopilot. Якщо помилка не зникає, замініть autopilot |
| `Hardware safety switch` | Апаратну кнопку безпеки не натиснуто | Натисніть кнопку безпеки (зазвичай зверху на GPS) або вимкніть її, встановивши `BRD_SAFETY_DEFLT` у нуль, і перезавантажте autopilot |
| `heater temp low (x < 45)` | Температура нагрівача плати нижча за BRD_HEAT_TARG | Дочекайтеся, поки плата прогріється. Цільову температуру можна змінити параметром `BRD_HEAT_TARG` |
| `In OSD menu` | Триває налаштування OSD | Завершіть налаштування OSD. Перевірте [налаштування OSD](https://ardupilot.org/copter/docs/common-osd-overview.html) *(ще не перекладено)* |
| `Internal errors 0x%x l:%u %s` | Сталася внутрішня помилка | Перезавантажте autopilot. Повідомте про помилку команді розробників |
| `Invalid FENCE_ALT_MAX value` | FENCE_ALT_MAX має бути додатним | Збільште `FENCE_ALT_MAX` |
| `Invalid FENCE_ALT_MIN value` | FENCE_ALT_MIN має бути більшим за -100 | Збільште `FENCE_ALT_MIN` |
| `Invalid FENCE_MARGIN value` | FENCE_MARGIN має бути додатним | Збільште `FENCE_MARGIN` |
| `Invalid FENCE_RADIUS value` | FENCE_RADIUS має бути додатним | Збільште `FENCE_RADIUS` |
| `Logging failed` | Не вдалося записати log-и. Можливо, апаратна несправність | Перезавантажте autopilot. Замініть autopilot |
| `Logging not started` | Не вдалося записати log-и. Можливо, апаратна несправність | Перезавантажте autopilot. Замініть autopilot |
| `Main loop slow (xHz < 400Hz)` | Процесор autopilot перевантажено | Зачекайте, щоб побачити, чи помилка тимчасова. Вимкніть частину функцій або замініть на потужніший autopilot. Зменште `SCHED_LOOP_RATE` |
| `Margin is less than inclusion circle radius` | Радіус круглої огорожі менший за FENCE_MARGIN | Збільште розмір відповідної круглої огорожі або зменште `FENCE_MARGIN` |
| `memory low for auxiliary authorisation` | Autopilot вичерпав пам'ять | Вимкніть частину функцій або замініть на потужніший autopilot |
| `Missing mission item: do land start` | Місії Auto потрібна команда DO_LAND_START | Додайте в місію команду DO_LAND_START або змініть параметр `ARMING_MIS_ITEMS` |
| `Missing mission item: land` | Місії Auto потрібна команда LAND | Додайте в місію команду LAND або змініть параметр `ARMING_MIS_ITEMS` |
| `Missing mission item: RTL` | Місії Auto потрібна команда RTL | Додайте в місію команду RTL або змініть параметр `ARMING_MIS_ITEMS` |
| `Missing mission item: takeoff` | Місії Auto потрібна команда TAKEOFF | Додайте в місію команду TAKEOFF або змініть параметр `ARMING_MIS_ITEMS` |
| `Missing mission item: vtol land` | Місії Auto потрібна команда VTOL_LAND | Додайте в місію команду VTOL_LAND або змініть параметр `ARMING_MIS_ITEMS` |
| `Missing mission item: vtol takeoff` | Місії Auto потрібна команда VTOL_TAKEOFF | Додайте в місію команду VTOL_TAKEOFF або змініть параметр `ARMING_MIS_ITEMS` |
| `Mode channel and RCx_OPTION conflict` | Перемикач flight mode (польотний режим) на RC також використовується для допоміжної функції | Змініть FLTMODE_CH (або MODE_CH для Rover) чи RCx_OPTION, щоб усунути конфлікт |
| `Mode requires mission` | Спроба arm у режимі Auto без місії | Виконайте arm в іншому режимі або створіть і завантажте місію Auto |
| `Motors Emergency Stopped` | Мотори зупинено аварійною зупинкою | Зніміть аварійну зупинку. Див. [допоміжні функції](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* |
| `Mount: check TYPE` | Неправильне налаштування кріплення (підвісу камери) | Перевірте, чи правильне значення `MNT1_TYPE`. Перевірте [налаштування підвісу](https://ardupilot.org/copter/docs/common-cameras-and-gimbals.html) *(ще не перекладено)* |
| `Mount: not healthy` | Підвіс не обмінюється даними з autopilot | Перевірте фізичне з'єднання між autopilot і підвісом та [налаштування підвісу](https://ardupilot.org/copter/docs/common-cameras-and-gimbals.html) *(ще не перекладено)* |
| `Multiple SERIAL ports configured for RC input` | Неправильне налаштування RC | Див. [Кілька receiver (приймач) радіокерування](https://ardupilot.org/copter/docs/common-multiple-rx.html) *(ще не перекладено)* |
| `No mission library present` | Функцію місій Auto вимкнено | Ймовірно, firmware зібрано на [Custom build server](https://custom.ardupilot.org/) без місій Auto. Зберіть firmware з увімкненими місіями Auto |
| `No rally library present` | Функцію точок rally вимкнено | Ймовірно, firmware зібрано на [Custom build server](https://custom.ardupilot.org/) без точок rally. Зберіть firmware з точками rally |
| `No SD card` | SD-карта пошкоджена або відсутня | Відформатуйте або замініть SD-карту |
| `No sufficiently close rally point located` | Точки rally далі за RALLY_LIMIT_KM | Перенесіть [точки rally](https://ardupilot.org/copter/docs/common-rally-points.html) *(ще не перекладено)* ближче до поточного розташування апарата або збільште `RALLY_LIMIT_KM` |
| `OA requires reboot` | Зміна налаштувань обходу перешкод потребує перезавантаження | Перезавантажте autopilot. Див. [налаштування обходу перешкод](https://ardupilot.org/copter/docs/common-object-avoidance-landing-page.html) *(ще не перекладено)* |
| `OpenDroneID: ARM_STATUS not available` | Неправильне налаштування OpenDroneID | Див. [налаштування Remote ID](https://ardupilot.org/copter/docs/common-remoteid.html) *(ще не перекладено)* |
| `OpenDroneID: operator location must be set` | Розташування оператора недоступне | Див. [налаштування Remote ID](https://ardupilot.org/copter/docs/common-remoteid.html) *(ще не перекладено)* |
| `OpenDroneID: SYSTEM not available` | Неправильне налаштування OpenDroneID | Див. [налаштування Remote ID](https://ardupilot.org/copter/docs/common-remoteid.html) *(ще не перекладено)* |
| `OpenDroneID: UA_TYPE required in BasicID` | Неправильне налаштування OpenDroneID | Див. [налаштування Remote ID](https://ardupilot.org/copter/docs/common-remoteid.html) *(ще не перекладено)* |
| `OSD_TYPE2 not compatible with first OSD` | Налаштування OSD1 і OSD2 несумісні | Вимкніть другий OSD (встановіть `OSD_TYPE2` у нуль) або перевірте [налаштування OSD](https://ardupilot.org/copter/docs/common-osd-overview.html) *(ще не перекладено)* |
| `Param storage failed` | Апаратна несправність Eeprom | Перевірте живлення або замініть autopilot |
| `parameter storage full` | Сховище Eeprom заповнене | Збережіть параметри. Скиньте до стандартних. Завантажте збережені параметри. |
| `PiccoloCAN: Servo x not detected` | Неправильне налаштування PiccoloCAN або проблема з servo | Перевірте [інструкцію з налаштування Currawong Velocity ESC](https://ardupilot.org/copter/docs/common-velocity-can-escs.html) *(ще не перекладено)* |
| `Pin x disabled (ISR flood)` | Датчик на контакті GPIO (вивід загального призначення) швидко змінює стан | Перевірте датчик, підключений до вказаного контакту |
| `Pitch (RCx) is not neutral` | Stick (ручка керування) pitch на RC transmitter не в центрі | Поставте stick pitch у центр або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `Pitch radio max too low` | Максимум каналу pitch RC нижчий за 1700 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або збільште `RC2_MAX` вище 1700 |
| `Pitch radio min too high` | Мінімум каналу pitch RC вищий за 1300 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або зменште `RC2_MIN` нижче 1300 |
| `PRXx: No Data` | Датчик наближення не надає даних | Перевірте фізичне підключення датчика наближення і [налаштування](https://ardupilot.org/copter/docs/common-proximity-landingpage.html) *(ще не перекладено)* |
| `PRXx: Not Connected` | Датчик наближення не надає даних | Перевірте фізичне підключення датчика наближення і [налаштування](https://ardupilot.org/copter/docs/common-proximity-landingpage.html) *(ще не перекладено)* |
| `Radio failsafe on` | Спрацював failsafe RC | Увімкніть RC transmitter або перевірте налаштування failsafe RC |
| `Rangefinder x: Not Connected` | Далекомір не надає даних | Перевірте фізичне підключення далекоміра до autopilot і [налаштування](https://ardupilot.org/copter/docs/common-rangefinder-landingpage.html) *(ще не перекладено)*. Також перевірте, чи далекомір взагалі є у firmware: багатьох немає, і їх треба додати через [custom firmware server](https://custom.ardupilot.org) |
| `RC calibrating` | Триває калібрування RC | Завершіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `RC not calibrated` | Калібрування RC не виконано | Виконайте [калібрування радіокерування](../first-time-setup/radio-calibration.md). `RC3_MIN` і `RC3_MAX` мають бути змінені зі стандартних значень (1100 і 1900), а для каналів 1–4 значення MIN має бути 1300 або менше, а MAX — 1700 або більше. |
| `RC not found` | Failsafe RC увімкнено, але сигналу RC немає | Увімкніть RC transmitter або перевірте підключення receiver до autopilot. Якщо ви працюєте лише з GCS, див. [common-gcs-only-operation](https://ardupilot.org/copter/docs/common-gcs-only-operation.html) *(ще не перекладено)* |
| `RCx_MAX is less than RCx_TRIM` | Неправильне налаштування RC | Змініть RCx_TRIM так, щоб він був меншим за RCx_MAX, або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `RCx_MIN is greater than RCx_TRIM` | Неправильне налаштування RC | Змініть RCx_TRIM так, щоб він був більшим за RCx_MIN, або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `RELAYx_PIN=y invalid` | Реле налаштовано неправильно | RELAYx_PIN має недопустиме значення. Перевірте [інструкцію з налаштування реле](https://ardupilot.org/copter/docs/common-relay.html) *(ще не перекладено)* |
| `RELAYx_PIN=y, set SERVx_FUNCTION=-1` | Реле налаштовано неправильно | Встановіть SERVOx_FUNCTION у -1 |
| `RNGFNDx_PIN not set` | Далекомір налаштовано неправильно | Встановіть RNGFNDx_PIN у ненульове значення. Див. [налаштування далекоміра](https://ardupilot.org/copter/docs/common-rangefinder-landingpage.html) *(ще не перекладено)* |
| `RNGFNDx_PIN=y invalid` | Далекомір налаштовано неправильно | RNGFNDx_PIN має недопустиме значення. Перевірте [налаштування далекоміра](https://ardupilot.org/copter/docs/common-rangefinder-landingpage.html) *(ще не перекладено)* |
| `RNGFNDx_PIN=y, set SERVOx_FUNCTION=-1` | Далекомір налаштовано неправильно | Встановіть SERVOx_FUNCTION у -1 |
| `Roll (RCx) is not neutral` | Stick roll на RC transmitter не в центрі | Поставте stick roll у центр або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `Roll radio max too low` | Максимум каналу roll RC нижчий за 1700 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або збільште `RC1_MAX` вище 1700 |
| `Roll radio min too high` | Мінімум каналу roll RC вищий за 1300 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або зменште `RC1_MIN` нижче 1300 |
| `RPMx_PIN not set` | Датчик обертів (RPM) налаштовано неправильно | Перевірте значення RPMx_PIN. Перевірте [інструкцію з налаштування RPM](https://ardupilot.org/copter/docs/common-rpm.html) *(ще не перекладено)* |
| `RPMx_PIN=y invalid` | Датчик обертів (RPM) налаштовано неправильно | RPMx_PIN має недопустиме значення. Перевірте [інструкцію з налаштування RPM](https://ardupilot.org/copter/docs/common-rpm.html) *(ще не перекладено)* |
| `RPMx_PIN=y, set SERVOx_FUNCTION=-1` | Датчик обертів (RPM) налаштовано неправильно | Встановіть SERVOz_FUNCTION у -1 |
| `Same Node Id x set for multiple GPS` | Помилка налаштування GPS на DroneCan | Перевірте, що `GPS1_CAN_NODEID` і `GPS2_CAN_NODEID` різні. Встановіть один із них у нуль і перезавантажте autopilot |
| `Same rfnd on different CAN ports` | Два далекоміри на різних портах CAN | Перевірте інструкції з налаштування USD1, TOFSensP, NanoRadar чи Benewake |
| `Scripting: loaded CRC incorrect want: x` | Скрипт має неправильну CRC | Замініть Lua-скрипт на очікувану версію |
| `Scripting: running CRC incorrect want: x` | Скрипт має неправильну CRC | Замініть Lua-скрипт на очікувану версію |
| `Scripting: xxx failed to start` | Lua-скрипт не вдалося запустити | Autopilot вичерпав пам'ять або Lua-скрипт налаштовано неправильно. Див. [Lua-скрипти](https://ardupilot.org/copter/docs/common-lua-scripts.html) *(ще не перекладено)* |
| `Scripting: xxx out of memory` | Lua-скрипту не вистачило пам'яті | Збільште `SCR_HEAP_SIZE` або перевірте [налаштування Lua-скриптів](https://ardupilot.org/copter/docs/common-lua-scripts.html) *(ще не перекладено)* |
| `Servo voltage to low (Xv < 4.3v)` | Напруга шини servo нижча за 4.3 В | Перевірте живлення задньої шини servo |
| `SERVOx_FUNCTION=y on disabled channel` | Вихід PWM налаштовано неправильно | SERVOx_FUNCTION задано для виходу servo, який вимкнено. Див. [налаштування BLHeli](https://ardupilot.org/copter/docs/common-blheli32-passthru.html) *(ще не перекладено)* |
| `SERVOx_MAX is less than SERVOx_TRIM` | Вихід PWM налаштовано неправильно | Встановіть SERVOx_TRIM меншим за SERVOx_MAX |
| `SERVOx_MIN is greater than SERVOx_TRIM` | Вихід PWM налаштовано неправильно | Встановіть SERVOx_TRIM більшим за SERVOx_MIN |
| `System not Initialized` | Система ще завантажується | Зачекайте; якщо найближчим часом не мине, можлива проблема з датчиком, яку не виявила інша діагностика |
| `temperature cal running` | Триває температурне калібрування | Дочекайтеся завершення [температурного калібрування](../first-time-setup/imu-temperature-calibration.md) або перезавантажте autopilot |
| `terrain data expired, possible errors` | Застарілі дані рельєфу, що можуть містити помилки | Оновіть дані рельєфу на SD-карті |
| `terrain disabled` | Місія Auto використовує рельєф, але рельєф вимкнено | Увімкніть базу даних рельєфу (встановіть `TERRAIN_ENABLE` = 1) або видаліть з місії Auto пункти, що використовують висоти над рельєфом. Для коптерів також перевірте RTL_ALT_TYPE. |
| `Terrain out of memory` | Autopilot вичерпав пам'ять | Вимкніть частину функцій або замініть на потужніший autopilot |
| `terrain required but disabled` | Місія Auto використовує рельєф, але його немає у firmware | Скористайтеся custom build server і додайте базу даних рельєфу або видаліть з місії Auto пункти, що використовують висоти над рельєфом. Для коптерів також перевірте RTL_ALT_TYPE. |
| `Throttle (RCx) is not neutral` | Stick throttle на RC transmitter занадто високо | Опустіть stick throttle або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `Throttle radio max too low` | Максимум каналу throttle RC нижчий за 1700 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або збільште `RC2_MAX` вище 1700 |
| `Throttle radio min too high` | Мінімум каналу throttle RC вищий за 1300 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або зменште `RC1_MIN` нижче 1300 |
| `Too many auxiliary authorisers` | Понад 3 зовнішні системи керують arm | Перевірте зовнішню систему авторизації |
| `vehicle outside fence` | Апарат поза огорожею | Перенесіть апарат усередину огорожі |
| `VisOdom: not healthy` | Датчик візуальної одометрії не надає даних | Перевірте фізичне підключення візуальної одометрії і [налаштування](https://ardupilot.org/copter/docs/common-non-gps-navigation-landing-page.html) *(ще не перекладено)* |
| `VisOdom: out of memory` | Autopilot вичерпав пам'ять | Вимкніть частину функцій або замініть на потужніший autopilot |
| `VTOL Fwd Throttle iz not zero` | Stick VTOL Fwd throttle на RC transmitter високо | Опустіть stick VTOL Fwd throttle або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `waiting for terrain data` | Очікування потрібних даних рельєфу від GCS | Зачекайте або перейдіть туди, де кращий прийом GPS; перевірте, чи правильно встановлено `TERRAIN_OPTIONS`. |
| `Yaw (RCx) is not neutral` | Stick yaw на RC transmitter не в центрі | Поставте stick yaw у центр або повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) |
| `Yaw radio max too low` | Максимум каналу yaw RC нижчий за 1700 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або збільште `RC2_MAX` вище 1700 |
| `Yaw radio min too high` | Мінімум каналу yaw RC вищий за 1300 | Повторіть [калібрування радіокерування](../first-time-setup/radio-calibration.md) або зменште `RC1_MIN` нижче 1300 |

### Повідомлення про помилки pre-arm (лише Copter/Heli)

| Повідомлення | Причина | Рішення |
|---|---|---|
| `ADSB threat detected` | Failsafe ADSB. Поруч пілотовані повітряні судна | Див. [налаштування ADSB](https://ardupilot.org/copter/docs/common-ads-b-receiver.html) *(ще не перекладено)* |
| `AHRS not healthy` | AHRS/EKF ще не готовий | Зачекайте. Перезавантажте autopilot |
| `Altitude disparity` | Висоти barometer і EKF розходяться щонайменше на 1 м | Дочекайтеся стабілізації висоти EKF. Перезавантажте autopilot |
| `Auto mode not armable` | Arm у режимі Auto неможливий | Перемкніться в інший режим (наприклад, Loiter) або встановіть `RTL_OPTIONS` = 3. Див. [режим Auto](https://ardupilot.org/copter/docs/auto-mode.html) *(ще не перекладено)* |
| `Bad parameter: ATC_ANG_PIT_P must be > 0` | Неправильне налаштування регулятора положення (attitude controller) | Збільште вказаний параметр до значення, більшого за нуль. Див. [інструкції з tuning (точне налаштування)](https://ardupilot.org/copter/docs/tuning-process-instructions.html) *(ще не перекладено)* |
| `Bad parameter: PSC_POSXY_P must be > 0` | Неправильне налаштування регулятора позиції (position controller) | Збільште вказаний параметр до значення, більшого за нуль. Див. [інструкції з tuning](https://ardupilot.org/copter/docs/tuning-process-instructions.html) *(ще не перекладено)* |
| `Battery failsafe` | Спрацював failsafe батареї | Підключіть батарею і перевірте її напругу та ємність. Див. [налаштування failsafe батареї](battery-failsafe.md) |
| `Check ACRO_BAL_ROLL/PITCH` | ACRO_BAL_ROLL, ACRO_BAL_PITCH від'ємні або занадто великі | Змініть `ACRO_BAL_ROLL` на значення від 0 до `ATC_ANG_RLL_P` та/або `ACRO_BAL_PITCH` — від 0 до `ATC_ANG_PIT_P`. Див. [режим Acro](https://ardupilot.org/copter/docs/acro-mode.html) *(ще не перекладено)* |
| `Check ANGLE_MAX` | ANGLE_MAX занадто великий | Зменште `ATC_ANGLE_MAX` до 80 (напр. 80 градусів) або менше |
| `Check FS_THR_VALUE` | Неправильне налаштування failsafe RC | Встановіть `FS_THR_VALUE` між 910 і мінімумом throttle RC (напр. `RC3_MIN`. Див. [налаштування failsafe батареї](battery-failsafe.md) |
| `Check PILOT_SPEED_UP` | PILOT_SPEED_UP занадто малий | Збільште `PILOT_SPD_UP` до додатного значення (напр. 1 = 1 м/с). Див. [режим AltHold](https://ardupilot.org/copter/docs/altholdmode.html) *(ще не перекладено)* |
| `Collective below failsafe (TradHeli only)` | Вхід collective з RC нижчий за FS_THR_VALUE | Увімкніть RC transmitter або перевірте `FS_THR_VALUE`. Перевірте [налаштування failsafe RC](radio-failsafe.md) |
| `EKF attitude is bad` | EKF не має доброї оцінки положення | Дочекайтеся стабілізації положення за EKF. Перезавантажте autopilot. Замініть autopilot |
| `EKF compass variance` | Напрямок compass виглядає неправильним | Перенесіть апарат подалі від металу навколо. Віддаліть compass від металу на frame. Повторіть [калібрування compass](../first-time-setup/compass-calibration.md). Вимкніть вбудований compass. |
| `EKF height variance` | Показання barometer нестабільні або високі вібрації | Зачекайте. [Виміряйте вібрації](https://ardupilot.org/copter/docs/common-measuring-vibration.html) *(ще не перекладено)* і додайте [віброізоляцію](../first-time-setup/vibration-damping.md) |
| `EKF position variance` | Позиція GPS нестабільна | Зачекайте. Якщо ви в приміщенні, вийдіть надвір. Усуньте джерела радіозавад, що можуть заважати GPS |
| `EKF velocity variance` | Швидкості за GPS або optical flow нестабільні | Зачекайте. Якщо ви в приміщенні, вийдіть надвір. Усуньте джерела радіозавад, що можуть заважати GPS. Перевірте [калібрування optical flow](https://ardupilot.org/copter/docs/common-optical-flow-sensor-setup.html) *(ще не перекладено)* |
| `Fence enabled, need position estimate` | Огорожу ввімкнено, тож потрібна оцінка позиції | Зачекайте. Якщо ви в приміщенні, вийдіть надвір. Переконайтеся, що калібрування compass і accelerometer виконано. Усуньте джерела радіозавад, що можуть заважати GPS. Див. [налаштування огорожі](https://ardupilot.org/copter/docs/common-geofencing-landing-page.html) *(ще не перекладено)* |
| `FS_GCS_ENABLE=2 removed, see FS_OPTIONS` | Неправильне налаштування failsafe GCS | Встановіть `FS_GCS_ENABLE` = 1 і перевірте параметр `FS_OPTIONS`. Див. [налаштування GCS Failsafe](gcs-failsafe.md) |
| `GCS failsafe on` | Спрацював failsafe GCS | Перевірте з'єднання telemetry. Див. [налаштування GCS Failsafe](gcs-failsafe.md) |
| `GPS glitching` | Позиція GPS нестабільна | Зачекайте. Якщо ви в приміщенні, вийдіть надвір. Усуньте джерела радіозавад, що можуть заважати GPS |
| `High GPS HDOP` | Горизонтальна точність GPS занадто низька | Зачекайте або перейдіть туди, де кращий прийом GPS. Можна підняти `GPS_HDOP_GOOD`, але це рідко добра ідея |
| `Home too far from EKF origin` | Home більш ніж за 50 км від початку координат EKF | Перезавантажте autopilot, щоб скинути початок координат EKF на поточне розташування |
| `Interlock/E-Stop Conflict (TradHeli only)` | Налаштовано несумісний перемикач допоміжної функції | Приберіть Interlock, E-Stop чи Emergency Stop з налаштувань [допоміжних функцій](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* |
| `Invalid MultiCopter FRAME_CLASS` | Параметр FRAME_CLASS налаштовано неправильно | Завантажено firmware мультикоптера, але `FRAME_CLASS` вказує гелікоптер. Запишіть firmware гелікоптера або змініть `FRAME_CLASS` |
| `Inverted flight option not supported` | Допоміжна функція перевернутого польоту не підтримується | Приберіть перемикач [допоміжної функції](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* перевернутого польоту |
| `Leaning` | Нахил апарата більший за ANGLE_MAX | Вирівняйте апарат |
| `Motor Interlock Enabled` | Motor Interlock у середньому або верхньому положенні | Переведіть перемикач [допоміжної функції](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* motor interlock у нижнє положення |
| `Motor Interlock not configured` | Гелікоптерам потрібен налаштований motor interlock | Увімкніть перемикач [допоміжної функції](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* motor interlock |
| `Motors: Check frame class and type` | Невідомий або неправильно налаштований клас чи тип frame | Введіть правильний клас та/або тип frame |
| `Motors: Check MOT_PWM_MIN and MOT_PWM_MAX` | MOT_PWM_MIN або MOT_PWM_MAX налаштовано неправильно | Встановіть `MOT_PWM_MIN` = 1000 і `MOT_PWM_MAX` = 2000 і повторіть [калібрування ESC](../first-time-setup/esc-calibration.md) |
| `Motors: MOT_SPIN_ARM > MOT_SPIN_MIN` | MOT_SPIN_ARM занадто великий або MOT_SPIN_MIN занадто малий | Зменште `MOT_SPIN_ARM` нижче `MOT_SPIN_MIN`. Див. [Діапазон моторів](../first-time-setup/set-motor-range.md) |
| `Motors: MOT_SPIN_MIN too high x > 0.3` | Значення параметра MOT_SPIN_MIN занадто велике | Зменште `MOT_SPIN_MIN` нижче 0.3. Див. [Діапазон моторів](../first-time-setup/set-motor-range.md) |
| `Motors: no SERVOx_FUNCTION set to MotorX` | Щонайменше один вихід мотора не налаштовано | Перевірте значення SERVOx_FUNCTION на «Motor1», «Motor2» тощо. Перевірте [налаштування ESC і моторів](../first-time-setup/connect-escs-and-motors.md) |
| `Need Alt Estimate` | EKF ще не обчислив висоту | Зачекайте. Дайте autopilot прогрітися. Переконайтеся, що [калібрування accelerometer](../first-time-setup/accelerometer-calibration.md) виконано. |
| `Need Position Estimate` | EKF не має оцінки позиції | Зачекайте. Якщо ви в приміщенні, вийдіть надвір. Переконайтеся, що калібрування compass і accelerometer виконано. Усуньте джерела радіозавад, що можуть заважати GPS |
| `Proximity x deg, ym (want > Zm)` | Перешкоди занадто близько до апарата | Віддаліть перешкоди від апарата або перевірте датчик. Див. [налаштування датчиків наближення](https://ardupilot.org/copter/docs/common-proximity-landingpage.html) *(ще не перекладено)* |
| `RTL mode not armable` | Arm у режимі RTL неможливий | Перемкніться в інший flight mode |
| `RTL_ALT_TYPE is above-terrain but no rangefinder` | RTL використовує далекомір, але далекомір недоступний | Перевірте [налаштування далекоміра](https://ardupilot.org/copter/docs/common-rangefinder-landingpage.html) *(ще не перекладено)*, зокрема RNGFNDx_ORIENT=251 |
| `RTL_ALT_TYPE is above-terrain but no terrain data` | RTL використовує рельєф, але база даних рельєфу недоступна | Встановіть `TERRAIN_ENABLE` = 1. Див. [Terrain Following](terrain-following.md) |
| `RTL_ALT_TYPE is above-terrain but RTL_ALT>RNGFND_MAX` | Висота повернення RTL вища за дальність далекоміра | Зменште `RTL_ALT_M` нижче RNGFNDx_MAX. Див. [Terrain Following](terrain-following.md) |
| `Safety Switch` | Апаратну кнопку безпеки не натиснуто | Натисніть кнопку безпеки (зазвичай зверху на GPS) або вимкніть її, встановивши `BRD_SAFETY_DEFLT` у нуль, і перезавантажте autopilot |
| `Throttle below failsafe` | Вхід throttle RC нижчий за FS_THR_VALUE | Увімкніть RC transmitter або перевірте `FS_THR_VALUE`. Перевірте [налаштування failsafe RC](radio-failsafe.md) |
| `Vehicle too far from EKF origin` | Апарат більш ніж за 50 км від початку координат EKF | Перезавантажте autopilot, щоб скинути початок координат EKF на поточне розташування |
| `winch unhealthy` | Лебідка не обмінюється даними з autopilot | Перевірте фізичне підключення лебідки і [налаштування](https://ardupilot.org/copter/docs/common-daiwa-winch.html) *(ще не перекладено)* |

## Вимкнення перевірок pre-arm

> **Попередження.** Вимикати перевірки pre-arm не рекомендовано. Якщо це взагалі можливо, причину невдалої перевірки pre-arm слід усунути до експлуатації апарата. Якщо ви впевнені, що невдала перевірка pre-arm — не справжня проблема, цю перевірку можна пропустити.

Окремі перевірки arm можна пропустити, встановивши параметр `ARMING_SKIPCHK` у значення, відмінне від 0. Наприклад, значення 4 пропускає перевірки того, що GPS має lock. За вкрай незвичайних обставин можна встановити параметр у -1, щоб пропустити всі поточні й майбутні перевірки pre-arm (хоча обов'язкові перевірки все одно лишаються).
