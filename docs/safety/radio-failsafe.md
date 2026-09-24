# Radio failsafe (аварійний захист при втраті радіокерування)

> Оригінал: [Radio Failsafe](https://ardupilot.org/copter/docs/radio-failsafe.html)

Copter підтримує кілька налаштовуваних варіантів failsafe (аварійний захист) на випадок, коли зв'язок між RC transmitter (пульт радіокерування) пілота і receiver (приймач) autopilot (автопілот) втрачено. Ця сторінка пояснює, як налаштувати і перевірити цей failsafe. Зверніть увагу: раніше «**Radio failsafe**» називався «**Throttle failsafe**» — через те, як деякі receiver використовують канал throttle (газ), щоб сигналізувати про втрату зв'язку.

> **Попередження.** Для frame (рама) Single Helicopter, Dual Helicopter і Quad Helicopter у Copter 3.6 і раніше в будь-якому режимі `H_RSC_MODE` (H_RSC Mode) або в Copter 4.0 у режимі RC Passthrough `H_RSC_Mode` receiver має утримувати останнє значення каналу 8, коли сигнал RC transmitter втрачено. Якщо receiver не надсилає сигнал або не утримує значення каналу 8, мотор буде зупинено, і гелікоптер розіб'ється.

![RadioFailsafe_Intro](https://ardupilot.org/copter/_images/RadioFailsafe_Intro.jpg)

> **Примітка.** Copter також підтримує інші види failsafe, зокрема [батареї](battery-failsafe.md), [GCS (наземна станція керування)](gcs-failsafe.md) і [EKF (розширений фільтр Калмана)/DCM](ekf-failsafe.md). Докладніше — на сторінці [Failsafe](index.md).

## Коли спрацьовує failsafe

Якщо його ввімкнено і правильно налаштовано, radio failsafe спрацює, якщо будь-яка з цих умов триває довше за `RC_FS_TIMEOUT` секунд (за замовчуванням 1 с):

- Пілот вимикає RC transmitter.
- Апарат виходить за межі дальності RC, і сигнал втрачається.
- Втрачаються RC_OVERRIDES, якщо використовується [керування лише з GCS](https://ardupilot.org/copter/docs/common-gcs-only-operation.html) *(ще не перекладено)*.
- Receiver втрачає живлення (малоймовірно).
- Обриваються дроти між receiver і autopilot (малоймовірно).

Radio failsafe також спрацює, якщо пілот з RC transmitter опустить канал throttle нижче `FS_THR_VALUE`.

## Що станеться

Коли спрацьовує radio failsafe, коптер можна параметрами налаштувати нічого не робити, негайно сідати, виконати RTL або SmartRTL. Також можна налаштувати ігнорування failsafe під час місії в режимі Auto або продовження посадки, якщо апарат уже на етапі посадки.

- Якщо коптер disarmed (не в робочому стані), failsafe не спрацює.
- Якщо коптер armed (у робочому стані), але вже приземлився, він одразу виконає disarm (виведення з робочого стану).
- Якщо коптер armed у режимі Stabilize чи Acro, throttle на мінімумі, а апарат не в [AirMode](../fpv/airmode.md), коптер одразу виконає disarm.
- Інакше коптер виконає дії, налаштовані параметрами, описаними нижче.

Якщо failsafe знімається (тобто RC transmitter і receiver знову мають зв'язок), коптер лишається в режимі failsafe. Він **не** повертається автоматично до flight mode (польотний режим), що був активний до спрацювання failsafe. Тобто якщо, наприклад, апарат був у Loiter, коли спрацював failsafe, і режим автоматично змінився на RTL, то навіть після відновлення зв'язку між RC transmitter і receiver апарат лишиться в RTL. Щоб знову взяти керування в Loiter, пілоту треба перевести перемикач flight mode в інше положення, а потім назад у Loiter.

## Налаштування receiver

За замовчуванням більшість нових receiver просто перестають видавати імпульси, якщо зв'язок з RC transmitter втрачено. Проте деякі дешеві receiver налаштовані просто утримувати всі канали в останньому відомому положенні. Це погано, бо autopilot ніяк не може дізнатися, що пілот втратив керування апаратом. Натомість receiver треба налаштувати так, щоб він сигналізував autopilot про втрату зв'язку; для цього є два способи (залежно від receiver). Усі марки RC transmitter/receiver трохи відрізняються, тож дізнайтеся з інструкції до вашого RC transmitter, який спосіб доступний і як його налаштувати.

### Налаштування receiver для способу «низький throttle»

**Спосіб «Low-Throttle»** опускає канал throttle (зазвичай канал 3) нижче нижньої межі його звичайного діапазону (зазвичай нижче 1000 мкс). Цей спосіб використовують системи Futaba і багато старіших систем. Нижче — як налаштувати RC transmitter Futaba T7C з receiver R617FS чи TFR4-B, що використовують спосіб «low throttle».

[Відео (YouTube)](https://www.youtube.com/watch?v=qf8YinLKQww)

Багато receiver дозволяють задати положення для failsafe або просто натисканням кнопки на receiver, або безпосередньо з RC transmitter. У цьому разі RC transmitter тимчасово налаштовують видавати сигнал throttle нижче звичайного нижнього холостого положення (якщо нижнє холосте — 1000 мкс, то надсилатиметься 990 мкс), задають це як значення failsafe для receiver, а потім повертають нижнє положення stick (ручка керування) до звичайного холостого. Це значення, нижче холостого throttle, потім задають у `FS_THR_VALUE`, як описано нижче.

### Налаштування receiver для способу «немає сигналу»

**Спосіб «No Signal»** — receiver перестає надсилати сигнали autopilot. Це бажаний спосіб, і так працює більшість сучасних receiver FrSky. Нижче — як налаштувати 9-канальний RC transmitter FlySky з receiver FrSky D4R-II, що використовує спосіб «No Signal».

[Відео (YouTube)](https://www.youtube.com/watch?v=FhKREgqjCpM)

## Налаштування параметрів

Параметр `FS_THR_ENABLE` можна задати в повному списку чи дереві параметрів Mission Planner або через випадний список *failsafe options* у меню Initial Setup >> Mandatory Hardware >> Failsafe у Mission Planner.

- **Disabled** (значення 0) повністю вимикає radio failsafe.
- **Enabled Always RTL** (значення 1) перемикає коптер у режим RTL. Якщо позиція GPS непридатна, коптер натомість перейде в режим Land.
- **Enabled Continue with Mission in Auto Mode** (у версіях 4.0 і новіших це значення не діє — його функцію замінив параметр `FS_OPTIONS`, див. нижче) (значення 2) ігнорує failsafe під час місії в режимі Auto. В інших випадках поводиться так само, як *Enabled Always RTL*. У ArduCopter 4.0 цієї опції вже немає. Натомість для цієї функції див. параметр `FS_OPTIONS`. Якщо задати це значення в Copter 4.0 і новіших, воно автоматично конвертується в (значення 1), а до бітової маски `FS_OPTIONS` додається біт (0) «Continue if in auto mode on Radio Failsafe».
- **Enabled Always Land** (значення 3) перемикає коптер у режим Land.
- **Enabled SmartRTL or RTL** (значення 4) перемикає коптер у режим SmartRTL. Якщо SmartRTL недоступний, коптер натомість перейде в режим RTL. Якщо позиція GPS непридатна, коптер натомість перейде в режим Land.
- **Enabled SmartRTL or Land** (значення 5) перемикає коптер у режим SmartRTL. Якщо SmartRTL недоступний, коптер натомість перейде в режим Land.
- **Enabled Auto DO_LAND_START or RTL** (значення 6) переходить до найближчого пункту місії «DO_LAND_START» або виконує RTL, якщо пункт «DO_LAND_START» у місії не запрограмовано (див. [DO_LAND_START](https://ardupilot.org/copter/docs/common-do-land-start.html) *(ще не перекладено)*).
- **Enabled always Brake or Land** виконує BRAKE або LAND, якщо позиція GPS недоступна.
- Будь-яке недопустиме значення (наприклад, випадково введене 99) поводиться так само, як **Enabled Always LAND**.

Параметр `FS_THR_VALUE` можна задати в повному списку чи дереві параметрів Mission Planner або значенням **FS PWM** у меню Initial Setup >> Mandatory Hardware >> Failsafe у Mission Planner. Він має бути:

- щонайменше на 10 PWM (широтно-імпульсна модуляція) більшим за значення PWM каналу 3, коли stick throttle повністю внизу, а RC transmitter **вимкнено**;
- щонайменше на 10 PWM меншим за значення PWM каналу 3, коли stick throttle повністю внизу, а RC transmitter **увімкнено**;
- вищим за 910 PWM.

Параметр `FS_OPTIONS` (Copter 4.0 і новіші) — бітова маска для вибору однієї чи кількох опцій, що змінюють стандартні дії failsafe радіокерування, GCS і батареї. У повному списку чи дереві параметрів Mission Planner найпростіше задати цей (як і будь-який інший бітовий) параметр у зручному спливному вікні з позначками. Спершу, маючи підключення до інтернету, обов'язково виконайте Help > Check Beta Updates, щоб отримати найсвіжіші описи параметрів. Біти `FS_OPTIONS` такі:

- біт 0: продовжувати в режимі auto при [Radio Failsafe](radio-failsafe.md)
- біт 1: продовжувати в режимі auto при [Ground Control Station Failsafe](gcs-failsafe.md)
- біт 2: продовжувати в режимі guided при [Radio Failsafe](radio-failsafe.md)
- біт 3: продовжувати посадку при будь-якому failsafe
- біт 4: продовжувати під керуванням пілота при [Ground Control Station Failsafe](gcs-failsafe.md)
- біт 5: відпускати захоплювач під час обробки failsafe
- якщо жоден з бітів вище не встановлено, виконується дія `FS_THR_ENABLE`, як налаштовано.

> **Примітка.** На дії під час radio failsafe впливають лише біти 0, 2, 3 і 5. Цей параметр також працює разом із failsafe батареї та GCS, тож задаючи його, враховуйте всі опції.

Нижче — знімок екрана меню Initial Setup >> Mandatory Hardware >> Failsafe у Mission Planner.

![RadioFailsafe_MPSetup](https://ardupilot.org/copter/_images/RadioFailsafe_MPSetup.png)

## Перевірка

Перевірити failsafe можна такими тестами, підключивши autopilot до Mission Planner USB-кабелем або через telemetry (телеметрія). Ці тести можна виконати без LiPo-батареї, але якщо ви підключаєте батарею, спершу зніміть пропелери.

**Тест №1: якщо використовується спосіб «Low-Throttle», переконайтеся, що канал throttle падає при втраті радіозв'язку**

1. Переконайтеся, що RC transmitter увімкнено і підключено, throttle повністю внизу, а flight mode — Stabilize.
2. Значення PWM throttle (канал 3) має бути приблизно таким, як на першій ілюстрації нижче. Воно може бути більшим чи меншим, але однозначно має бути щонайменше на 10 більшим за значення в полі FS PWM.
3. Вимкніть RC transmitter — значення PWM throttle має впасти щонайменше на 10 нижче значення в полі FS PWM (як на другій ілюстрації нижче).

![MPFailsafeSetup1](https://ardupilot.org/copter/_images/MPFailsafeSetup1.jpg)

**Тест №2: мотори виконують disarm у STABILIZE чи ACRO з нульовим throttle**

- Перемкніться в режим stabilize, виконайте arm (переведення в робочий стан) моторів, але тримайте throttle на нулі. Вимкніть RC transmitter. Мотори мають одразу виконати disarm (червоний світлодіод почне блимати, а на екрані Flight Data у Mission Planner з'явиться DISARMED).

**Тест №3: flight mode змінюється на RTL чи LAND, коли throttle вище нуля**

- Перемкніться в режим stabilize, виконайте arm моторів і підніміть throttle до середини. Вимкніть RC transmitter. Flight mode має змінитися на RTL, якщо є GPS lock (фіксація позиції GPS), або на LAND, якщо GPS lock немає (flight mode і стан GPS lock видно на екрані flight data в Mission Planner).

**Тест №4: повернення керування після зняття failsafe**

- продовжуючи тест №3, знову увімкніть RC transmitter;
- поки flight mode досі RTL чи LAND і апарат armed, переведіть перемикач flight mode в інше положення, а потім назад у stabilize. Переконайтеся, що flight mode на сторінці Failsafe оновлюється відповідно.

**Тест №5 (необов'язковий): зняття живлення з receiver**

- Перемкніться в режим stabilize, виконайте arm моторів і тримайте throttle вище нуля.
- Обережно від'єднайте дроти живлення між receiver і autopilot.
- Flight mode має змінитися на RTL чи LAND, як описано в тесті №3.

> **Попередження.** Перш ніж знову підключити живлення receiver, від'єднайте autopilot, щоб знеструмити його.

## Вибір flight mode через receiver (**НЕ ВИКОРИСТОВУЙТЕ!**)

Замість того щоб налаштовувати receiver і autopilot, як описано вище (способи «Low-Throttle» і «No Signal»), receiver можна налаштувати так, щоб він виставляв канал 5 (канал flight mode) у [слот flight mode](https://ardupilot.org/copter/docs/flight-modes.html) *(ще не перекладено)*, для якого задано RTL. Наприклад, receiver можна налаштувати змінювати значення PWM каналу 5 на 1700 мкс, що відповідає «Flight Mode 5», якому потім на екрані Initial Setup >> Mandatory Hardware >> Flight Modes у Mission Planner можна призначити RTL.

Хоча це нібито працює, це категорично не рекомендовано, бо може призвести до ситуацій, що закінчуються аварією. Оскільки autopilot ніяк не може знати, що стався failsafe RC, можлива небажана поведінка, наприклад заміна інших failsafe (низького заряду батареї чи GCS) змінами режиму.
