# QuikTune

> Оригінал: [QuikTune](https://ardupilot.org/copter/docs/quiktune.html)

- [Відео на YouTube](https://www.youtube.com/watch?v=K_T9ikEQmlc)

Lua-скрипт [VTOL QuikTune](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/applets/VTOL-quicktune.md) спрощує пошук доброго tuning (точне налаштування) параметрів керування положенням мультикоптера.

Скрипт повільно збільшує відповідні коефіцієнти, доки не виявить коливання. Тоді він зменшує коефіцієнти на 60% і переходить до наступного коефіцієнта.
Коли всі коефіцієнти налаштовано, tuning завершується, і користувач може зберегти нові коефіцієнти або відкинути їх.

> **Примітка.** Переконайтеся, що ви підготували апарат до tuning, задавши параметри, описані тут: [Підготовка апарата до tuning](setup.md). Також для найкращого tuning налаштуйте notch (режекторний фільтр) проти шуму, див. [Налаштування notch-фільтрів](notch-filtering.md). QuikTune можна запустити й без цього кроку, щоб отримати початковий tuning; якщо апарат не може стабільно виконати перше висіння, див. [Ручний tuning roll (крен) і pitch (тангаж)](manual-roll-pitch.md). Потім налаштуйте фільтри і повторіть tuning для найкращого результату.

Скрипт намагається налаштувати всі ці параметри (у наведеному порядку):

- `ATC_RAT_RLL_D`
- `ATC_RAT_RLL_P` і `ATC_RAT_RLL_I`
- `ATC_RAT_PIT_D`
- `ATC_RAT_PIT_P` і `ATC_RAT_PIT_I`
- `ATC_RAT_YAW_D`
- `ATC_RAT_YAW_P` і `ATC_RAT_YAW_I`

Перевага над [AutoTune](autotune.md): QuikTune безпечніший, бо апарату не потрібно рухатися чи смикатися.
Недолік: QuikTune не може визначити максимальні кутові прискорення апарата (наприклад, `ATC_ACC_R_MAX`, `ATC_ACC_P_MAX`, `ATC_ACC_Y_MAX`).

## Встановлення скрипта

- Встановіть `SCR_ENABLE` = 1, щоб увімкнути скрипти, і перезавантажте autopilot (автопілот).
- Завантажте [VTOL-quicktune.lua](https://raw.githubusercontent.com/ArduPilot/ardupilot/master/libraries/AP_Scripting/applets/VTOL-quicktune.lua) на ПК.
- Скопіюйте скрипт у каталог APM/scripts на SD-карті autopilot. У MP найпростіше скористатися екраном **Config, MAVFtp**.

    ![quiktune-mp-mavftp](https://ardupilot.org/copter/_images/quiktune-mp-mavftp.png){ width="450" }

- Перезавантажте autopilot і встановіть `QUIK_ENABLE` = 1.
- Якщо запускати/зупиняти tuning буде перемикач RC, встановіть `RCx_OPTION` = 300, де «x» — номер вхідного каналу RC. Або ж задайте в одному з рядків вкладки **Aux Function** у Mission Planner значення **Scripting1**.

    ![quiktune-mp-auxfunction](https://ardupilot.org/copter/_images/quiktune-mp-auxfunction.png){ width="450" }

## Запуск QuikTune

- Дочекайтеся безвітряного дня і вирушайте на відкриту місцевість з добрим прийомом GPS.
- Підключіться наземною станцією (наприклад, Mission Planner або QGC) і переконайтеся, що видно вкладку **Messages**. Саме там з'являтимуться повідомлення tuning.
- Переведіть перемикач RC у нижнє положення АБО натисніть кнопку **Low** у **Aux Function** в MP.
- Виконайте arm (переведення в робочий стан), злетіть у режимі Loiter і наберіть висоту близько 3 м.
- Почніть tuning, перевівши перемикач RC у середнє положення АБО натиснувши кнопку **Mid** у **Aux Function** в MP.
- Стежте за перебігом tuning на вкладці **Messages** GCS (наземна станція керування).
- Якщо потрібно, змініть позицію апарата з RC transmitter (пульт радіокерування). Це тимчасово призупинить tuning і відновить початкові коефіцієнти. Tuning продовжиться за кілька секунд після повернення stick (ручка керування) RC у центральне положення.
- Якщо апарат починає сильно коливатися, скасуйте tuning, перевівши перемикач RC у нижнє положення АБО натиснувши кнопку **Low** у **Aux Function** в MP.
- Коли tuning завершиться, прийміть нові коефіцієнти, перевівши допоміжний перемикач RC у верхнє положення АБО натиснувши кнопку **High** у **Aux Function** в MP.
- Сядьте і виконайте disarm (виведення з робочого стану) апарата.

## Розширене налаштування

Повний перелік доступних [налаштувань параметрів — тут](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/applets/VTOL-quicktune.md).
