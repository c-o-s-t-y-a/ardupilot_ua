# Підключення ESC і моторів

> Оригінал: [Connect ESCs and Motors](https://ardupilot.org/copter/docs/connect-escs-and-motors.html)

Тут пояснено, як підключити ESC (електронний регулятор обертів), мотори і пропелери до autopilot (автопілот). Як приклад використано Pixhawk, але інші autopilot підключаються схоже.

Підключіть дроти живлення (+), землі (-) і сигналу (s) кожного ESC до основних вихідних контактів autopilot відповідно до номера мотора. Порядок моторів для вашого типу frame (рама) — нижче.

![Pixhawk output pins (numbered). First 4 pins are colour-coded for connecting a Quadframe](https://ardupilot.org/copter/_images/Pixhwak_outputs.jpg)

*Вихідні контакти Pixhawk (пронумеровані). Перші 4 контакти позначені кольором для підключення квадрокоптера.*

## Схеми порядку моторів

Схеми нижче показують порядок моторів для кожного типу frame. Напрямок обертання пропелера позначено зеленим (за годинниковою стрілкою, CW) або синім (проти годинникової стрілки, CCW). Червоні літери показують, який мотор має обертатися під час функції **Motor Test** у Mission Planner (вкладка SETUP → Optional Hardware).

![Legend for motor-order diagrams](https://ardupilot.org/copter/_images/MOTORS_CW_CCWLegend.jpg)

*Легенда до схем порядку моторів.*

### Квадрокоптери (QUAD)

<img src="https://ardupilot.org/copter/_images/m_01_00_quad_plus.svg" alt="QUAD PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_01_quad_x.svg" alt="QUAD X" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_02_quad_v.svg" alt="QUAD V" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_03_quad_h.svg" alt="QUAD H" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_04_quad_v_tail.svg" alt="QUAD V TAIL" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_05_quad_a_tail.svg" alt="QUAD A TAIL" width="260">

> **Примітка.** Frame Quad A Tail і V Tail не використовують передні мотори для керування yaw (рискання) (NYT). Напрямок обертання моторів не критичний для базової роботи, але якщо передні мотори не обертаються в протилежні боки, команди roll (крен) і pitch (тангаж) спричинятимуть небажаний yaw, що зменшує запас керування yaw.

<img src="https://ardupilot.org/copter/_images/m_01_06_quad_plus_rev.svg" alt="QUAD PLUS (REVERSED)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_12_quad_x_bf.svg" alt="QUAD X (BETAFLIGHT)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_13_quad_x_dji.svg" alt="QUAD X (DJI)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_14_quad_x_cw.svg" alt="QUAD X (CLOCKWISE)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_16_quad_plus_nyt.svg" alt="QUAD PLUS (NO YAW TORQUE)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_17_quad_x_nyt.svg" alt="QUAD X (NO YAW TORQUE)" width="260">

> **Примітка.** Frame Quad «No Yaw Torque» (NYT) призначені насамперед для конфігурацій [VTOL Tailsitter](https://ardupilot.org/plane/docs/guide-tailsitter.html) *(ще не перекладено)* з великими аеродинамічними рулями. Напрямок обертання цих моторів не важливий, але якщо напрямки обертання не налаштовано як на якійсь звичайній frame QUAD, команди roll і pitch спричинятимуть небажаний yaw, що зменшує запас керування yaw рулями літака.

<img src="https://ardupilot.org/copter/_images/m_01_18_quad_x_bf_rev.svg" alt="QUAD X (BF REVERSED)" width="260">
<img src="https://ardupilot.org/copter/_images/m_01_19_quad_y4a.svg" alt="QUAD Y4A" width="260">

### Гексакоптери (HEXA)

<img src="https://ardupilot.org/copter/_images/m_02_00_hexa_plus.svg" alt="HEXA PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_02_01_hexa_x.svg" alt="HEXA X" width="260">
<img src="https://ardupilot.org/copter/_images/m_02_03_hexa_h.svg" alt="HEXA H" width="260">
<img src="https://ardupilot.org/copter/_images/m_02_13_hexa_x_dji.svg" alt="HEXA X (DJI)" width="260">
<img src="https://ardupilot.org/copter/_images/m_02_14_hexa_x_cw.svg" alt="HEXA X (CLOCKWISE)" width="260">

### Октокоптери (OCTO)

<img src="https://ardupilot.org/copter/_images/m_03_00_octo_plus.svg" alt="OCTO PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_01_octo_x.svg" alt="OCTO X" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_02_octo_v.svg" alt="OCTO V" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_03_octo_h.svg" alt="OCTO H" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_13_octo_x_dji.svg" alt="OCTO X (DJI)" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_14_octo_x_cw.svg" alt="OCTO X (CLOCKWISE)" width="260">
<img src="https://ardupilot.org/copter/_images/m_03_15_octo_i.svg" alt="OCTO I" width="260">

### Октоквадри (OCTO QUAD)

<img src="https://ardupilot.org/copter/_images/m_04_00_octo_quad_plus.svg" alt="OCTO QUAD PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_01_octo_quad_x.svg" alt="OCTO QUAD X" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_02_octo_quad_v.svg" alt="OCTO QUAD V" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_03_octo_quad_h.svg" alt="OCTO QUAD H" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_12_octo_quad_x_bf.svg" alt="OCTO QUAD X (BETAFLIGHT)" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_14_octo_quad_x_cw.svg" alt="OCTO QUAD X (CLOCKWISE)" width="260">
<img src="https://ardupilot.org/copter/_images/m_04_18_octo_quad_x_bf_rev.svg" alt="OCTO QUAD X (BF REVERSED)" width="260">
<img src="https://ardupilot.org/copter/_images/m_17_01_corotating_x.svg" alt="COROTATING X" width="260">
<img src="https://ardupilot.org/copter/_images/m_17_14_corotating_x_cw.svg" alt="COROTATING X (CW)" width="260">

> **Примітка.** Frame Corotating X і X (CW) треба налаштовувати з `FRAME_CLASS` 17, і на autopilot має працювати [скрипт X8-corotating.lua](https://github.com/ArduPilot/ardupilot/libraries/AP_Scripting/examples/X8-corotating.lua).

### Y6

<img src="https://ardupilot.org/copter/_images/m_05_00_y6_a.svg" alt="Y6 A" width="260">
<img src="https://ardupilot.org/copter/_images/m_05_10_y6_b.svg" alt="Y6 B" width="260">
<img src="https://ardupilot.org/copter/_images/m_05_11_y6_f.svg" alt="Y6 F" width="260">

### Трикоптери (TRICOPTER)

<img src="https://ardupilot.org/copter/_images/m_07_00_tricopter.svg" alt="TRICOPTER" width="260">
<img src="https://ardupilot.org/copter/_images/m_07_06_tricopter_pitch_rev.svg" alt="TRICOPTER PITCH REVERSED" width="260">

> **Примітка.** Оскільки для керування yaw використовується хвостовий (або носовий) servo (сервопривід), напрямок обертання моторів трикоптера не критичний для базової роботи, але якщо передні мотори не обертаються в протилежні боки, команди roll і pitch спричинятимуть небажаний yaw, що зменшує запас керування yaw. Якщо хвостовий (або носовий) servo відхиляється у відповідь на yaw не в той бік, встановіть з 0 на 1 або параметр напрямку входу RC `RCn_REVERSE`, або параметр `SERVOn_REVERSE` поворотного servo. Докладніше — на [сторінці налаштування Tricopter](https://ardupilot.org/copter/docs/tricopter.html) *(ще не перекладено)*.

### Бікоптери (BICOPTER)

<img src="https://ardupilot.org/copter/_images/m_10_00_bicopter.svg" alt="BICOPTER" width="260">

> **Примітка.** За бажанням мотори бікоптера можуть обертатися в напрямках, протилежних показаним (наприклад, CW ліворуч, CCW праворуч).

### Додекагекса (DODECAHEXA)

<img src="https://ardupilot.org/copter/_images/m_12_00_dodecahexa_plus.svg" alt="DODECAHEXA PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_12_01_dodecahexa_x.svg" alt="DODECAHEXA X" width="260">

### Декакоптери (DECA)

<img src="https://ardupilot.org/copter/_images/m_14_00_deca_plus.svg" alt="DECA PLUS" width="260">
<img src="https://ardupilot.org/copter/_images/m_14_01_deca_x_and_cw_x.svg" alt="DECA X (and CW X)" width="260">

### Власні frame

За допомогою [Lua-скриптів](https://ardupilot.org/copter/docs/common-lua-scripts.html) *(ще не перекладено)* можна налаштувати власні типи frame з кількістю моторів до 12. Коефіцієнти roll, pitch і yaw для кожного мотора треба розрахувати й завантажити зі скрипта. Це вмикається встановленням `FRAME_CLASS` у 15 — Scripting Matrix. Див. [приклад для quad plus](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/MotorMatrix_setup.lua) і [приклад відмовостійкого hex](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/examples/MotorMatrix_fault_tolerant_hex.lua).

> **Примітка.** Не всі autopilot підтримують скрипти, див. [обмеження firmware (прошивка)](limited-firmware.md).

### Як розрізнити пропелери за і проти годинникової стрілки

На схемах вище показано два типи пропелерів: за годинниковою стрілкою (їх називають pusher) і проти годинникової стрілки (puller). Найнадійніше розпізнати тип пропелера за формою, як показано нижче. Товща кромка — передня, вона рухається в напрямку обертання. Задня кромка має виразніший вигин і зазвичай тонша.

<img src="https://ardupilot.org/copter/_images/prop-direction.png" alt="prop_direction" width="450">

## Перевірка напрямку обертання моторів

Якщо ви виконали [калібрування радіокерування](radio-calibration.md) і [калібрування ESC](esc-calibration.md), можна перевірити, що мотори обертаються в правильному напрямку:

1. Переконайтеся, що на коптері немає пропелерів!
2. Увімкніть RC transmitter (пульт радіокерування) і переконайтеся, що перемикач flight mode (польотний режим) стоїть у Stabilize.
3. Підключіть батарею.
4. Виконайте arm (переведення в робочий стан) коптера: тримайте throttle (газ) внизу і руль напрямку (rudder) праворуч п'ять секунд.
5. Якщо з throttle внизу і вправо arm не вдається і мотори не обертаються, найімовірніше, не пройдено pre-arm (передпольотна перевірка).

    - Про невдалу перевірку pre-arm також сигналізує червоний світлодіод arm, що блимає двічі й повторює це.
    - Якщо перевірка pre-arm не пройдена, перейдіть на [сторінку перевірок Pre-Arm](https://ardupilot.org/copter/docs/common-prearm-safety-checks.html) *(ще не перекладено)* і виправте проблему або вимкніть перевірку, перш ніж продовжити.

6. Коли arm вдається, дайте трохи throttle і подивіться, в який бік обертається кожен мотор. Напрямки мають відповідати показаним на схемах вище для вибраної frame.
7. Змініть напрямок кожного мотора, що обертається не в той бік.

    > **Порада.** Напрямок мотора змінюється просто: поміняйте місцями два з трьох силових дротів між ESC і мотором.

## Перевірка нумерації моторів через Motor Test у Mission Planner

Інший спосіб перевірити, що мотори підключено правильно, — тест «Motors» у меню Initial Setup Mission Planner.

![Mission Planner: Motor Test](https://ardupilot.org/copter/_images/MissionPlanner_MotorTest.png)

Коли Mission Planner підключено до апарата через MAVLink, можна натискати зелені кнопки, показані вище, — відповідний мотор обертатиметься п'ять секунд. Літери відповідають номерам моторів, як у прикладі нижче.

- Спершу зніміть пропелери!
- Якщо жоден мотор не обертається, підніміть «Throttle %» до 10 % і спробуйте знову. Якщо не допоможе — спробуйте 15 %.

Першим обертатиметься мотор, розташований прямо спереду, для конфігурації +, або перший мотор праворуч від напрямку вперед — для конфігурації X. Далі тест моторів іде за годинниковою стрілкою.

![APM_2_5_MOTORS_QUAD_enc](https://ardupilot.org/copter/_images/APM_2_5_MOTORS_QUAD_enc.jpg)

Для X8 спершу обертатиметься верхній передній правий мотор, потім нижній передній правий, і далі за тією самою схемою по колу.

OctoV спершу обертатиме передній правий мотор, а далі — теж за годинниковою стрілкою до переднього лівого мотора.

## Використання PDB

![3dr_power_distribution_board](https://ardupilot.org/copter/_images/3dr_power_distribution_board.jpg)

Є два способи підключення виходів на мотори: або підключити ESC безпосередньо до autopilot, АБО використати PDB (плата розподілу живлення).

Якщо використовуєте PDB, підключіть дроти живлення (+), землі (-) і сигналу (s) кожного ESC до PDB відповідно до номера мотора. Порядок моторів для вашого типу frame — вище. Потім підключіть сигнальні дроти з PDB до основних вихідних сигнальних контактів autopilot (переконавшись, що номери моторів збігаються з номерами основних виходів контролера). Якщо ви використовуєте power module (модуль живлення), підключати дроти живлення і землі від PDB до плати autopilot необов'язково. Якщо ви хочете використати ці дроти на додачу до power module, замість нього або як спільну точку для малопотужних servo, підключіть дріт землі (-) до контакту землі (-) основного виходу, а дріт живлення (+) — до контакту живлення (+) основного виходу.

## ESC з оптичною розв'язкою KDE (та інших виробників)

Серії KDEXF-UAS і KDEF-UASHV мають оптичну розв'язку і не видають живлення BEC (стабілізатор живлення) для периферійного обладнання. Їм потрібно +5 В для живлення оптрона, а Pixhawk хоч і може живитися від шини servo, сам +5 В на шину servo не подає. ESC треба живити від BEC або перемичкою з вільного роз'єму на платі. Наполегливо рекомендуємо живити шину від BEC, а не перемичкою.

![Pixhawk-Correction-to-KDE-ESC2](https://ardupilot.org/copter/_images/Pixhawk-Correction-to-KDE-ESC2.png)

ESC KDE мають фіксовані діапазони PWM (широтно-імпульсна модуляція), тож діапазон кожного вихідного сигналу PWM треба задати вручну так, щоб RCx_MIN дорівнював 1100, а RCx_MAX — 1900 мкс, на сторінці Advanced Parameter або Full Parameter у Mission Planner.

## Проблеми ESC з Pixhawk

Є повідомлення, що деякі ESC не працюють з Pixhawk.

Pixhawk має працювати з будь-яким ESC, який працює зі звичайним receiver (приймач) радіокерування (бо надсилає такий самий тип сигналу), але є [один відомий виняток — ESC EMAX](https://github.com/ArduPilot/ardupilot/issues/2094).

Здебільшого проблеми спричинені неправильним підключенням. Завжди підключайте сигнал і землю. Як підключати лінію +5 В, вирішуйте залежно від типу вашого ESC. Для Pixhawk потрібно підключити і сигнал, і сигнальну землю, щоб ESC запрацював.

Докладніше — у [цьому відео](https://youtu.be/6C1YG1e2aTo).
