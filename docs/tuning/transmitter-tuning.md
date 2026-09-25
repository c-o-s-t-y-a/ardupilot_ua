# Tuning з RC transmitter

> Оригінал: [Transmitter Based Tuning](https://ardupilot.org/copter/docs/common-transmitter-tuning.html)

Великий обсяг tuning (точне налаштування) параметрів можна виконати в польоті за допомогою RC transmitter (пульт радіокерування). Це призначено для досвідчених користувачів, які не можуть скористатися функціями Autotune або хочуть виконати тонке налаштування з повним ручним керуванням кожним параметром.

## Огляд

Tuning з RC transmitter дає змогу налаштовувати окремий параметр або набір параметрів просто в польоті. Основна ідея — прив'язати значення параметра до ручки-регулятора чи повзунка на RC transmitter і змінювати параметр у польоті, обертаючи ручку.

Спершу встановіть `RCx_OPTION` = 219, де `x` — вільний канал RC, який використовуватиметься для tuning з RC transmitter.

> **Примітка.** До версії 4.6 каналом «tuning» жорстко був канал 6, і встановлювати `RCx_OPTION` = 219 не було потрібно.

> **Примітка.** Можна налаштувати й другий канал tuning через `RCx_OPTION` = 220 і параметри `TUNE2_xx`, щоб за один політ змінювати два набори параметрів tuning.

Параметр `TUNE` визначає, який параметр налаштовується.

Параметр `TUNE_MAX` задає максимальне значення параметра, коли канал у положенні `RCx_MAX`, а параметр `TUNE_MIN` — значення, коли канал tuning у положенні `RCx_MIN`.

## Значення `TUNE`

| Значення | Назва | Параметр |
|---|---|---|
| 0 | **None** | |
| 1 | **Stab Roll/Pitch kP** | `ATC_ANG_RLL_P`, `ATC_ANG_PIT_P` |
| 4 | **Rate Roll/Pitch kP** | `ATC_RAT_RLL_P`, `ATC_RAT_PIT_P` |
| 5 | **Rate Roll/Pitch kI** | `ATC_RAT_RLL_I`, `ATC_RAT_PIT_I` |
| 21 | **Rate Roll/Pitch kD** | `ATC_RAT_RLL_D`, `ATC_RAT_PIT_D` |
| 3 | **Stab Yaw kP** | `ATC_ANG_YAW_P` |
| 6 | **Rate Yaw kP** | `ATC_RAT_YAW_P` |
| 26 | **Rate Yaw kD** | `ATC_RAT_YAW_D` |
| 56 | **Rate Yaw Filter** | `ATC_RAT_YAW_FLTE` |
| 55 | **Motor Yaw Headroom** | `MOT_YAW_HEADROOM` |
| 14 | **Vertical Position kP** | `PSC_D_POS_P` |
| 7 | **Throttle Rate kP** | `PSC_D_VEL_P` |
| 34 | **Throttle Accel kP** | `PSC_D_ACC_P` |
| 35 | **Throttle Accel kI** | `PSC_D_ACC_I` |
| 36 | **Throttle Accel kD** | `PSC_D_ACC_D` |
| 12 | **Horizontal Position kP** | `PSC_NE_POS_P` |
| 22 | **Horizontal Velocity kP** | `PSC_NE_VEL_P` |
| 28 | **Horizontal Velocity kI** | `PSC_NE_VEL_I` |
| 10 | **WP Speed** | `WP_SPD` |
| 25 | **Acro RollPitch kP** | `ACRO_RP_RATE` |
| 40 | **Acro Yaw kP** | `ACRO_Y_RATE` |
| 45 | **RC Feel** | `ATC_INPUT_TC` |
| 13 | **Heli Ext Gyro** | `H_GYR_GAIN` |
| 38 | **Declination** | `COMPASS_DEC` |
| 39 | **Circle Rate** | `CIRCLE_RATE` |
| 46 | **Rate Pitch kP** | `ATC_RAT_PIT_P` |
| 47 | **Rate Pitch kI** | `ATC_RAT_PIT_I` |
| 48 | **Rate Pitch kD** | `ATC_RAT_PIT_D` |
| 49 | **Rate Roll kP** | `ATC_RAT_RLL_P` |
| 50 | **Rate Roll kI** | `ATC_RAT_RLL_I` |
| 51 | **Rate Roll kD** | `ATC_RAT_RLL_D` |
| 52 | **Rate Pitch FF** | `ATC_RAT_PIT_FF` ** |
| 53 | **Rate Roll FF** | `ATC_RAT_RLL_FF` ** |
| 54 | **Rate Yaw FF** | `ATC_RAT_YAW_FF` ** |
| 57 | **Winch** | `WINCH_RATE_MAX` |
| 58 | **SysID Magnitude** | `SID_MAGNITUDE` |
| 59 | **Position Control Max Lean Angle** | `PSC_ANGLE_MAX` |
| 60 | **Loiter Max X/Y Speed** | [Loiter](https://ardupilot.org/copter/docs/loiter-mode.html) *(ще не перекладено)* |

** Лише для традиційних гелікоптерів.

Ці значення можна задати вручну або через Mission Planner.

## Налаштування через Mission Planner

У прикладі процедури нижче використано **Rate Roll P** і **Rate Pitch P**.

![RollPitchTuning](https://ardupilot.org/copter/_images/RollPitchTuning.png)

1. Підключіть autopilot (автопілот) до Mission Planner.
2. У списку параметрів призначте канал `x` для tuning з RC transmitter: `RCx_OPTION` = 219.
3. У Mission Planner виберіть **CONFIG>>Extended Tuning**.
4. У випадному списку **TUNE** виберіть **Rate Roll/Pitch kP**.
5. Задайте **Min** 0,08, **Max** 0,20 (ідеальний коефіцієнт більшості коптерів лежить у цьому діапазоні, хоча для невеликої кількості коптерів **Max** може сягати 0,25).
6. Натисніть кнопку **Write Params**.
7. Поверніть ручку tuning CHx на RC transmitter у мінімальне положення, натисніть кнопку **Refresh Params** і переконайтеся, що значення **Rate Roll P** і **Rate Pitch P** стали 0,08 (або дуже близькими).
8. Поверніть ручку CHx у максимальне положення, натисніть **Refresh Params** і переконайтеся, що **Rate Roll P** змінився на 0,20.
9. Поверніть ручку CHx у середнє положення.
10. Виконайте arm (переведення в робочий стан) і літайте коптером у режимі Stabilize, обертаючи ручку CHx, доки коптер не стане чутливим, але не хитким.
11. Після польоту від'єднайте батарею LiPo і знову підключіть autopilot до Mission Planner.
12. Залишивши ручку CHx у положенні, що дало найкращий результат, поверніться на екран **Copter Pids** і натисніть кнопку **Refresh Params**.
13. У полях **Rate Roll P** і **Rate Pitch P** повторно введіть видиме значення, але трохи змінене, щоб Mission Planner розпізнав зміну і повторно надіслав його на autopilot (примітка: якщо ввести точно те саме число, що відображається в **Rate Roll P**, воно не оновиться). Наприклад, якщо **Rate Roll P** показує «0.1213», введіть «0.1200».
14. Поверніть **CHx Opt** у **None** і натисніть **Write Params**.
15. Натисніть кнопку **Disconnect** угорі праворуч, а потім **Connect**.
16. Переконайтеся, що значення **Rate Roll P** дорівнює введеному на кроці 13.

> **Примітка.** Поки ви обертаєте ручку tuning, значення оновлюються 3 рази на секунду. Натискати кнопку **Refresh** у Mission Planner на кроках 7 і 8 потрібно лише тому, що Copter не надсилає оновлення в Mission Planner у реальному часі.
