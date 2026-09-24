# TBS Crossfire telemetry (телеметрія)

> Оригінал: [TBS Crossfire Telemetry](https://ardupilot.org/copter/docs/common-crsf-telemetry.html)

> **Примітка.** Системи радіокерування ELRS (ExpressLRS) використовують протокол CRSF і підключаються так само. Receiver (приймач) ELRS можна також використовувати в режимі Mavlink — тоді одна пара TX-RX дає і двонаправлену telemetry (телеметрія) Mavlink, і радіокерування. Докладніше — [тут](https://www.expresslrs.org/software/mavlink/).

Receiver TBS Crossfire передають ArduPilot telemetry разом з інформацією радіокерування. ArduPilot підтримує власну telemetry CRSF і розширення до неї, що дають змогу використовувати [Yaapu Telemetry Script](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*. Підключення і налаштування — див. [Crossfire і ELRS](crossfire-elrs.md).

OpenTx виявить власні датчики telemetry CRSF (але обмежену кількість — для більшої кількості відображуваної інформації використайте описаний нижче варіант passthru зі скриптом Yaapu Telemetry). Їх можна відображати на екранах telemetry [OpenTX](https://www.open-tx.org/) або ретранслювати через WIFI модуля CRSF TX на GCS (наземна станція керування) з MAVLink:

![crossfire-telemetry-meaning](https://ardupilot.org/copter/_images/crossfire-telemetry-meaning.jpg)

Ці значення можна відображати на RC transmitter (пульт радіокерування) з OpenTX кількома способами:

- на вбудованих екранах telemetry:

![x9d-telem-screen](https://ardupilot.org/copter/_images/x9d-telem-screen.jpg)

Крім того, якщо встановити біт 8 `RC_OPTIONS`, передаються додаткові елементи telemetry ArduPilot, що дає змогу використовувати [Yaapu Telemetry Script](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)* на RC transmitter з OpenTX. Обмеження і додаткова інформація — [тут](https://discuss.ardupilot.org/t/passthrough-telemetry-over-crsf-crossfire).

![x10-horus](https://ardupilot.org/copter/_images/x10-horus.png)

> **Попередження.** Використовуючи біт 8 `RC_OPTIONS` для passthru, переконайтеся, що жоден порт SERIAL не налаштовано на `SERIALx_PROTOCOL` = 10 (Passthrough), щоб уникнути конфлікту і ненадійної роботи.

Зазвичай для налаштування параметрів системи CRSF TX і RX є кілька скриптів OpenTX. Вони відкриваються довгим натисканням кнопки SYS.

## Редактор параметрів ArduPilot

Крім того, реалізація CRSF в ArduPilot дає змогу змінювати параметри ArduPilot — функціонально подібно до функції ArduPilot [Parameter OSD (накладення даних на відео)](https://ardupilot.org/copter/docs/common-paramosd.html) *(ще не перекладено)*.

Якщо на autopilot (автопілот) є активний OSD (`OSD_TYPE` не дорівнює «0»), ця функція вмикається автоматично. Якщо ні, її ввімкне вибір `OSD_TYPE` = 4 (TX only).

Якщо вибрати на RC transmitter LUA-скрипт Crossfire Configuration, з'явиться:

![crsf-config-screen](https://ardupilot.org/copter/_images/crsf-config-screen.png)

А якщо вибрати в цьому списку апарат ArduPilot, відкриється [Parameter OSD](https://ardupilot.org/copter/docs/common-paramosd.html) *(ще не перекладено)* зі списком усіх параметрів, налаштованих для обох екранів OSD.

![crsf-param-editor](https://ardupilot.org/copter/_images/crsf-param-editor.png)

> **Примітка.** Деякі autopilot, щоб заощадити flash (флеш-пам'ять), показують значення параметрів з текстовими назвами не текстом, а числом. Які autopilot не мають можливості CRSF TEXT — див. [Обмеження firmware (прошивка)](../first-time-setup/limited-firmware.md).

## Меню CRSF на скриптах

ArduPilot підтримує власні меню CRSF, створені Lua-скриптами. Ці меню з'являються поруч із вбудованим редактором параметрів ArduPilot на екрані Crossfire Configuration RC transmitter і можуть давати інтерфейси налаштування під конкретні задачі.

Модуль [crsf_helper.lua](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/crsf-menu.lua) надає високорівневий API, який можна використовувати в LUA-скриптах для створення меню CRSF. Кілька незалежних скриптів меню можуть працювати одночасно — наприклад, меню tuning (точне налаштування) PID і меню налаштування OSD можуть співіснувати без конфліктів.

**Підтримка кількох меню (4.7 і новіші):**

В ArduPilot 4.7 Lua API меню CRSF покращено, щоб надійно підтримувати кілька одночасних меню:

- Новий метод `crsf:peek_menu_event()` дає скриптам змогу переглядати події в черзі, не забираючи їх, тож кожен скрипт може перевірити, чи належить подія до його меню, перш ніж її обробляти.
- Новий метод `crsf:pop_menu_event()` явно забирає подію після того, як скрипт визначив, що вона його.
- Новий метод `crsf:send_response()` — для надсилання загальних відповідей параметрів CRSF.
- Потокобезпечний доступ до черг подій меню завдяки внутрішньому захисту семафором.

Скрипти, що використовують `crsf_helper.lua`, автоматично отримують ці покращення. Скрипти, що напряму використовують низькорівневий API CRSF, слід оновити на схему peek/pop замість старішого `crsf:get_menu_event()`, щоб не забирати події, призначені іншим скриптам.
