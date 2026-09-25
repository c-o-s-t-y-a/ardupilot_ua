# AutoTrim

> Оригінал: [AutoTrim](https://ardupilot.org/copter/docs/autotrim.html)

Вітер, звісно, сильно впливає на коптер і зносить його. Проте ви можете помітити, що, літаючи в режимі Stabilize навіть за безвітряної погоди, коптер постійно зміщується в той самий бік. Здебільшого це можна виправити функціями **Save Trim** або **Automatic Trim**.

> **Примітка.** Більшості користувачів ця процедура не потрібна, бо [калібрування accelerometer (акселерометр)](../first-time-setup/accelerometer-calibration.md) добре задає значення trim (підстроювання нейтралі).

### AHRS AutoTrim

У режимі AHRS AutoTrim поправки по roll (крен) і pitch (тангаж) фіксуються, поки ви літаєте в стабільному висінні. Налаштуйте перемикач [Auxiliary Functions](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* на «In Flight AHRS trim adjust» («182»). Далі використано CH7:

1. Переконайтеся, що перемикач CH7 дає понад 1800 на екрані Mission Planner **Setup > Mandatory Hardware > Radio Calibration**.

    ![MP_SaveTrim_Ch7PWMCheck](https://ardupilot.org/copter/_images/MP_SaveTrim_Ch7PWMCheck.png)

2. Задайте `RCx_OPTION` вибраного каналу значенням «AHRS AutoTrim» (182) на екрані **Aux Function** у Mission Planner і натисніть кнопку **Write Params**. Як призначати опції будь-якому каналу RC, див. [Auxiliary Functions](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)*.

3. Знайдіть безвітряне місце з достатнім простором, щоб літати, ні в що не врізавшись.

4. Переведіть апарат у ручний режим Stabilize/AltHold або в режим утримання позиції Loiter/PosHold (рекомендовано).

5. Виконайте arm (переведення в робочий стан) апарата і підніміть його у висіння. Щоб увімкнути autotrim, апарат має бути в польоті. Переведіть налаштований перемикач (CH7) у верхнє положення (>1800 мкс). На GCS (наземна станція керування) надійде повідомлення «Autotrim running».

6. У ручному режимі літайте коптером близько 25 секунд у стабільному висінні на місці, не даючи йому зміщуватися, за допомогою stick (ручка керування) pitch і roll. У міру підстроювання trim потрібно дедалі менше поправок stick. У режимі утримання позиції злетіть і дайте коптеру висіти на місці, не торкаючись stick.

7. Коли результат влаштовує, переведіть перемикач у нижнє положення — trim збережеться — і сідайте. На GCS надійде повідомлення «Trim save».

8. Злетіть у режимі AltHold і перевірте, чи коптер тепер летить рівно. Якщо ні, повторіть кроки 4–7.

> **Примітка.** Trim можна задати вручну, змінивши `AHRS_TRIM_X` і `AHRS_TRIM_Y`. Trim по roll — `AHRS_TRIM_X`, trim по pitch — `AHRS_TRIM_Y`. Обидва значення в радіанах; roll ліворуч і pitch носом уперед — від'ємні числа.

> **Примітка.** Майже неможливо позбутися зміщення повністю, щоб коптер лишався цілком нерухомим без жодних команд. Може бути краще повертати коптер по yaw (рискання) на 90 градусів і щоразу утримувати цю орієнтацію близько 6–7 секунд, щоб зовнішні збурення взаємно компенсувалися — так trim вийде кращим.

### Save Trim

> **Примітка.** Описаний вище метод AHRS AutoTrim кращий, бо не потребує зміни trim на RC transmitter (пульт радіокерування) після калібрування радіокерування.

**Save Trim** по суті переносить trim з RC transmitter у trim AHRS autopilot (автопілот) (параметри `AHRS_TRIM_X` і `AHRS_TRIM_Y`) — ті самі значення, які підстроює описаний вище метод AHRS AutoTrim. Зазвичай після [калібрування accelerometer](../first-time-setup/accelerometer-calibration.md) trim на RC transmitter ніколи не змінюють, але в цьому випадку це робиться **тимчасово**. Функцію **Save Trim** («5») призначають будь-якому вільному каналу RC, зазвичай на перемикачі, через [Auxiliary Functions](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)*. У прикладі нижче використано канал 7.

1. Переконайтеся, що перемикач CH7 дає понад 1800 на екрані Mission Planner **Setup > Mandatory Hardware > Radio Calibration**.

    ![MP_SaveTrim_Ch7PWMCheck](https://ardupilot.org/copter/_images/MP_SaveTrim_Ch7PWMCheck.png)

2. Задайте `RCx_OPTION` вибраного каналу значенням **Save Trim** (5) на екрані **Aux Function** у Mission Planner і натисніть кнопку **Write Params**. Як призначати опції будь-якому каналу RC, див. [Auxiliary Functions](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)*.

    ![MP_SaveTrim_Ch7](https://ardupilot.org/copter/_images/MP_SaveTrim_Ch7.png)

3. Із перемикачем CH7 у вимкненому (нижньому) положенні літайте коптером у режимі Stabilize чи AltHold і за допомогою trim roll і pitch на RC transmitter досягніть рівного польоту.

4. Сядьте і приберіть throttle (газ) у нуль.

5. Відпустіть stick roll і pitch і переведіть перемикач CH7 у верхнє положення щонайменше на 1 секунду. На вкладці **Messages** екрана **Flight Data** у MP має з'явитися «Trim saved».

6. Поверніть trim roll і pitch на RC transmitter у центр і злетіть знову — тепер коптер має летіти рівно. Якщо ні, повторіть кроки 3, 4 і 5.

> **Примітка.** **Save Trim** працює й тоді, коли ввімкнено [режим Simple чи Super Simple](https://ardupilot.org/copter/docs/simpleandsuper-simple-modes.html) *(ще не перекладено)*, але стежте, щоб не змінювати курс апарата між посадкою і перемиканням CH7 у верхнє положення, бо trim збережеться відносно курсу апарата в цей момент.

### Метод на столі

Trim також можна оновити, встановивши апарат рівно, підключившись до Mission Planner (чи, можливо, інших наземних станцій), вибравши **Initial Setup, Mandatory Hardware, Accel Calibration** і натиснувши нижню кнопку **Calibrate Level**.

![AccelCalibration_MP](https://ardupilot.org/copter/_images/AccelCalibration_MP.png)

Утім, зверніть увагу: те, що HUD показує level (рівне положення), поки апарат на землі, не обов'язково означає, що він не зміщуватиметься горизонтально в польоті, — через інші дрібні проблеми конструкції, зокрема неідеально рівне встановлення flight controller (польотний контролер) на frame (рама), розташування центру ваги і/або трохи нахилені мотори.
