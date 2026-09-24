# Dead reckoning failsafe (політ за розрахунком після втрати позиції)

> Оригінал: [Dead Reckoning Failsafe](https://ardupilot.org/copter/docs/deadreckoning-failsafe.html)

Copter має Dead Reckoning Failsafe (аварійний захист), який дає змогу апарату повернутися додому (або частково повернутися), якщо він втратив GPS (точніше — якщо він втратив оцінку позиції, яка може базуватися на GPS, OpticalFlow тощо).

> **Примітка.** Цей failsafe доступний у Copter-4.3 (і новіших).

> **Примітка.** Схожу функціональність дає скрипт [copter-deadreckon-home.lua](https://github.com/ArduPilot/ardupilot/tree/master/libraries/AP_Scripting/applets/copter-deadreckon-home.lua) ([відео1](https://www.youtube.com/watch?v=KKShYheW4J0), [відео2](https://www.youtube.com/watch?v=esM0EqMH_BE)).

## Налаштування

- Налаштуйте [оцінку швидкості вітру](https://ardupilot.org/copter/docs/airspeed-estimation.html) *(ще не перекладено)*, зокрема параметри `EK3_DRAG_BCOEF_X`, `EK3_DRAG_BCOEF_Y` і `EK3_DRAG_MCOEF`.
- Встановіть `FS_DR_ENABLE` у «2» (RTL) або в один з інших доступних варіантів.
- Встановіть `FS_DR_TIMEOUT` — скільки секунд апарат може зберігати керованість після втрати GPS. Для більшості апаратів це лише 10–30 секунд.

## Коли він спрацьовує?

Failsafe dead reckoning спрацьовує за тих самих умов, що й [failsafe EKF (розширений фільтр Калмана)](ekf-failsafe.md): коли будь-які дві з «дисперсій» EKF — для compass (компас), позиції чи швидкості — довше 1 секунди перевищують параметр `FS_EKF_THRESH`. На практиці очікується, що зазвичай failsafe спрацьовуватиме через втрату GPS.

## Що станеться, коли спрацює failsafe?

- Після втрати GPS апарат ще 7–10 секунд летітиме як звичайно.
- На GCS (наземна станція керування) з'явиться «Dead Reckoning started», а апарат перейде в режим [RTL](https://ardupilot.org/copter/docs/rtl-mode.html) *(ще не перекладено)* і полетить додому.
- Якщо апарат не долетить додому за `FS_DR_TIMEOUT` секунд, спрацює [failsafe EKF](ekf-failsafe.md), і апарат перейде в режим [Land](https://ardupilot.org/copter/docs/land-mode.html) *(ще не перекладено)*.
- Навіть якщо GPS відновиться, поки апарат повертається додому, апарат лишиться в RTL.

## Перевірка

Щоб перевірити в симуляторі чи на реальному апараті, виконайте інструкції нижче. Перевіряючи на реальному апараті, будьте готові знову взяти керування в ручному режимі (наприклад, [Stabilize](https://ardupilot.org/copter/docs/stabilize-mode.html) *(ще не перекладено)* чи [AltHold](https://ardupilot.org/copter/docs/altholdmode.html) *(ще не перекладено)*).

- Встановіть `RC9_OPTION` у 65, щоб можна було вимикати GPS [допоміжним перемикачем](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* (можна використати будь-який вхідний канал RC).
- Виконайте arm (переведення в робочий стан) і летіть у будь-якому режимі, що потребує GPS (наприклад, [Loiter](https://ardupilot.org/copter/docs/loiter-mode.html) *(ще не перекладено)*, [Guided](https://ardupilot.org/copter/docs/ac2_guidedmode.html) *(ще не перекладено)*, [Auto](https://ardupilot.org/copter/docs/auto-mode.html) *(ще не перекладено)* тощо).
- Переконайтеся, що EKF обчислив оцінку швидкості вітру: перевірте «wind_dir» та/або «wind_vel» на GCS (див. «Viewing Windspeed and Direction in Real-Time» на [цій сторінці](https://ardupilot.org/copter/docs/airspeed-estimation.html) *(ще не перекладено)*).
- Підніміть допоміжний перемикач, щоб вимкнути GPS.
- Протягом 7–10 секунд на GCS має з'явитися «Dead Reckoning started», а апарат має перейти в режим RTL і полетіти додому.
- Через `FS_DR_TIMEOUT` секунд спрацює failsafe EKF, і апарат перейде в режим Land.
- Якщо позиція апарата надто дрейфує, перемкніться в режим AltHold, щоб повернути керування апаратом.
- Опустіть допоміжний перемикач будь-коли, щоб знову ввімкнути GPS.
- Після тестування зменште або збільште параметр `FS_DR_TIMEOUT`, щоб він відповідав максимальній кількості секунд, протягом яких апарат зберігає керованість без GPS.

## Відео

- [Відео 1 (YouTube)](https://www.youtube.com/watch?v=G-vYP_IQZeM)
- [Відео 2 (YouTube)](https://www.youtube.com/watch?v=Xq-ecwgFKzA)
