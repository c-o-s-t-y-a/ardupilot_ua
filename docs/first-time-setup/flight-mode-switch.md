# Налаштування flight mode (польотних режимів) на RC transmitter

> Оригінал: [RC Transmitter Flight Mode Configuration](https://ardupilot.org/copter/docs/common-rc-transmitter-flight-mode-configuration.html)

Тут показано, як налаштувати до 6 flight mode (польотний режим) autopilot (автопілот), які вибиратимуться з RC transmitter (пульт радіокерування) через канал flight mode (`FLTMODE_CH` для plane/copter/sub, `MODE_CH` для rover). Змінювати flight mode можна також каналами RC, налаштованими як [допоміжні функції](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)*.

## Налаштування flight mode

Відповідність між положенням перемикача і flight mode задається на екрані *Mission Planner Flight Mode*.

![Mission Planner: Flight Mode Screen (Copter)](https://ardupilot.org/copter/_images/mp_setup_flight_mode.png)

Щоб налаштувати flight mode, доступні з RC transmitter:

- Увімкніть RC transmitter.
- Підключіть Pixhawk (чи інший autopilot) до *Mission Planner*.
- Перейдіть на екран **Initial Setup → Mandatory Hardware → Flight Modes**.

    > **Примітка.** Коли ви перемикаєте перемикач flight mode на RC transmitter, зелена смуга підсвічування переміщується на інше положення.

- У випадному списку в кожному рядку виберіть flight mode для відповідного положення перемикача.
- (Copter) Переконайтеся, що принаймні одне положення перемикача лишається призначеним на STABILISE.
- (Copter) За бажанням поставте позначку [Simple Mode](https://ardupilot.org/copter/docs/simpleandsuper-simple-modes.html#simpleandsuper-simple-modes-simple-mode) *(ще не перекладено)* для цього положення перемикача. Можна також увімкнути [Super Simple mode](https://ardupilot.org/copter/docs/simpleandsuper-simple-modes.html#simpleandsuper-simple-modes-super-simple-mode) *(ще не перекладено)*. Якщо позначено і Simple mode, і Super Simple mode, використовуватиметься Super Simple.
- Закінчивши, натисніть **Save Modes**.

(Copter) Деякі режими можна також вмикати [допоміжними перемикачами](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* (так звані перемикачі опцій ch7, ch8). Наприклад, можна виділити окремий перемикач під RTL.

## Вибір каналу flight mode

Канал flight mode — це вхідний канал радіокерування, який ArduPilot відстежує для зміни режиму.

У Copter він задається параметром `FLTMODE_CH`. За замовчуванням — канал 5.

## Налаштування RC transmitter

Щоб положенню перемикача можна було призначити режим, RC transmitter має видавати сигнали PWM (широтно-імпульсна модуляція) у правильному діапазоні.

> **Примітка.** Зазвичай діапазон — від 1000 до 2000 мкс (від 1,0 до 2,0 мс; мс — мілісекунда, мкс — мікросекунда). Правильні діапазони PWM для кожного режиму показано поруч із кожним випадним списком вибору режиму на екрані *Mission Planner Flight Mode* (див. [знімок екрана вище](#налаштування-flight-mode)).

Якщо потрібні лише три режими (трипозиційний перемикач), налаштуйте RC transmitter так, щоб для відповідних положень перемикача він видавав імпульси PWM тривалістю 1165, 1425 і 1815 мкс.

Якщо потрібні 6 режимів, RC transmitter має видавати імпульси PWM тривалістю приблизно 1165, 1295, 1425, 1555, 1685 і 1815 мкс. Зазвичай цього досягають, налаштувавши на RC transmitter мікс двопозиційного і трипозиційного перемикачів (разом 6 режимів). Можна зробити це й аналоговою крутилкою, якщо вона є, але надійно виставляти крутилку саме в потрібне положення для шести різних значень важко.

У розділах нижче є посилання на те, як налаштувати RC transmitter різних виробників і як перевірити (у Mission Planner), що кожне положення перемикача видає потрібний сигнал PWM.

### Перевірка положень перемикачів RC transmitter

Перевірити тривалість імпульсів PWM для кожного режиму можна на екрані *Mission Planner Radio Calibration*.

Просто перемикайте режими на RC transmitter і переконайтеся, що PWM на вибраному каналі відповідає потрібним значенням. На знімку екрана нижче канал flight mode — Radio 5.

![mp_radio_calibration_ch5_pwm](https://ardupilot.org/copter/_images/mp_radio_calibration_ch5_pwm.png)

### Інструкції для конкретної апаратури RC

Ось кілька інструкцій від користувачів, як це зробити (або як додати режими на апаратуру RC лише з двопозиційним перемикачем) на різних системах RC:

- **Будь-який RC transmitter на OpenTX:**

    Просто виберіть два перемикачі (один має бути трипозиційним) і додайте такі мікси на канал flight mode, який використовує ваш апарат. У прикладі нижче — літак із каналом 8 для flight mode (за замовчуванням): перемикач SB вибирає три flight mode, коли перемикач SA вгорі, і ще три flight mode, коли SA не вгорі.

    ![OpenTX-flight-mode-setup](https://ardupilot.org/copter/_images/OpenTX-flight-mode-setup.jpg)

- **RC transmitter типу TX16 із шестипозиційним перемикачем**

    Задайте джерелом каналу flight mode шестипозиційний перемикач «6P», але з кривою, яка зсуває кожне положення в центр потрібного ArduPilot діапазону PWM для відповідного режиму, як показано нижче:

    ![mode_curve](https://ardupilot.org/copter/_images/mode_curve.png)

- [JR XG8 DMSS](https://www.diydrones.com/forum/topics/how-to-set-up-6-apm-flight-modes-on-1-channel-of-jr-xg8-rc)
- [JR9303](https://diydrones.com/profiles/blogs/how-to-program-6-flight-modes)
- [JR X2720](https://diydrones.com/forum/topics/six-flight-modes-can-be-done)
- [FlySky FS-I6](https://diydrones.com/profiles/blogs/flysky-fs-i6-flight-modes)
- [Futaba T8FG](https://diydrones.com/profiles/blogs/acmapm-futaba-t8fg-super-mode)
- [Futaba T8J](https://www.diydrones.com/profiles/blogs/pixhawk-futaba-t8j-6-modes-configuration-with-2-switches-c-d)
- [Futaba T7CP](https://diydrones.com/profiles/blogs/configure-6-flight-modes-for)
- [Futaba T6EX](https://diydrones.com/profiles/blogs/four-modes-switch-for-futaba)
- [Futaba 9ZAP/ZHP](https://diydrones.com/profiles/blogs/flight-mode-switching-on-a)
- [Futaba T10CAG](https://diydrones.com/profiles/blogs/getting-six-fly-modes-on-futaba-t10cag-transmitter)
- [Futaba T14](https://diydrones.com/profiles/blogs/futaba-t14-mz-mode-configuration-for-all-6-modes)
- [Futaba T14SG](https://diydrones.com/forum/topics/set-6-point-switch-for-flight-mode-control-in-futaba-t14sg)
- [Futaba 9C Super](https://diydrones.com/profiles/blogs/6-positions-for-futaba-9c-super)
- [Graupner MX-16](https://diydrones.com/profiles/blogs/six-modes-with-graupner-mx-16)
- [Turnigy 9x](https://diydrones.com/profiles/blogs/mode-switch-setup-for-turnigy-1) (або ще простіший спосіб — [тут!](https://diydrones.com/profiles/blogs/another-way-to-set-modes-on-turnigy-9x)) — [Turnigy 9x з firmware (прошивка) ER9x](https://diydrones.com/profiles/blogs/mode-switch-setup-for-turnigy)
- [Turnigy 9XR](https://diydrones.com/profiles/blogs/change-between-6-modes-with-turnigy-9xr-using-mixing)
- [Turnigy TGY-I6](https://diydrones.com/profiles/blogs/flysky-fs-i6-flight-modes)
- [Hitech Aurora 9](https://www.diydrones.com/forum/topics/quad-goes-to-full-throttle?commentId)
- [Spektrum DX8](https://diydrones.com/profiles/blogs/spectrum-dx8-2-switches-1-tx-channel-6-flight-modes?) (альтернативний спосіб — нижче)
- [Spektrum DX7s](https://diydrones.com/profiles/blogs/getting-6-modes-out-of-channel-5-on-a-spektrum-dx7s)
- [Spektrum DX7 Version 6](https://diydrones.com/profiles/blogs/dx7-new-version-6-flight-mode-setup-with-pixhawk)

Або [зберіть власний шестипозиційний перемикач!](https://diydrones.com/profiles/blogs/6-position-mode-switch-for-apm)

### Spektrum DX8 (альтернативний спосіб)

Тут описано альтернативний спосіб налаштувати 6 режимів на Spektrum DX8. Він використовує перемикач Gear і перемикач Flight mode. Усі інші перемикачі можна призначити на власний розсуд. Цей спосіб також дає змогу виставити кожен режим посередині його діапазону тривалості імпульсу, щоб невеликі відхилення не перемикали режим. Під час цих налаштувань стежте за поточним PWM (Current PWM) на екрані налаштування Flight Modes у Mission Planner.

1. Налаштуйте перемикачі (потрібні для 6 режимів).

    - Тримаючи натиснутим коліщатко, увімкніть DX8, прокрутіть до Switch Select, натисніть коліщатко. Налаштуйте перемикачі так:

        - Gear = Gear (канал 5)
        - FMode = Inh — не призначений на канал; використовується в міксі з перемикачем Gear (канал 5) для 6 режимів

    - Інші — як завгодно. Один із варіантів:

        - Knob на aux1 = канал 6 для нахилу камери / tuning (точне налаштування)
        - Mix = aux2 = канал 7 для збереження Way Point чи RTL, auto trim (підстроювання нейтралі) або інших налаштувань у конфігурації APM.
        - Flap на aux3 = канал 8 для інших потреб

    - Натискайте BACK, доки не з'явиться звичайний екран, або вимкніть і знову увімкніть живлення.

2. Налаштуйте servo (сервопривід) для каналу 5 без міксу (канал Gear, керований перемикачем Gear).

    Це значення без міксу — перемикач F Mode у положенні 0; найменша тривалість імпульсу — 1165 мкс (режим 1), найбільша — 1815 мкс (режим 6).

- Натисніть коліщатко, прокрутіть до Servo Setup, виберіть канал Gear, виберіть Sub Trim.
- Встановіть sub trim у 0.
- Виберіть Travel.
- Встановіть travel (ліво, положення 0) для імпульсу 1165 мкс (~90 %).
- Встановіть travel (право, положення 1) для імпульсу 1815 мкс (~74 %).
- Налаштуйте Mix 1, щоб змінювати тривалість імпульсу Gear, коли F Mode у положенні 1:

    - Натисніть коліщатко, прокрутіть до Mixing, натисніть коліщатко, прокрутіть до першого рядка під Mix (там xxx > xxx, AIL > RUD або інший мікс), натисніть коліщатко, виберіть Mix 1, натисніть коліщатко.
    - Встановіть Mix: Gear > Gear. Gear змінює Gear залежно від положення перемикача F Mode.
    - Встановіть Offset = 0, Trim = Inh.
    - Встановіть SW = FM 1.
    - Поставте перемикач F Mode на RC transmitter у положення 1.
    - Поставте перемикач Gear на RC transmitter у положення 0.
    - Встановіть верхній Rate для тривалості імпульсу 1290 мкс для режиму 2 (~-35 %)

        (зміна = 400 мкс \* -90 % \* -35 % = 126 мкс. Результат = 1165 мкс + 126 мкс = 1251 мкс = режим 2)

    - Поставте перемикач Gear на RC transmitter у положення 1.
    - Встановіть нижній Rate для тривалості імпульсу 1685 мкс для режиму 5 (~-45 %)

        (зміна = 400 мкс \* +73 % \* -45 % = -131 мкс. Результат = 1815 мкс - 131 мкс = 1684 мкс = режим 5)

- Налаштуйте mix 2, щоб змінювати тривалість імпульсу Gear, коли F Mode у положенні 2:

    - Mix: Gear > Gear. Gear змінює Gear залежно від положення перемикача F Mode.
    - Встановіть Offset = 0, Trim = Inh.
    - Встановіть SW = FM2.
    - Поставте перемикач F Mode на RC transmitter у положення 2.
    - Поставте перемикач Gear на RC transmitter у положення 0.
    - Встановіть верхній Rate для тривалості імпульсу 1425 мкс для режиму 3 (~-72 %) (зміна = 400 мкс \* -90 % \* -72 % = 259 мкс. Результат = 1165 мкс + 259 мкс = 1424 мкс = режим 3)
    - Поставте перемикач Gear на RC transmitter у положення 1.
    - Встановіть нижній Rate для тривалості імпульсу 1550 мкс для режиму 4 (~-89 %) (зміна = 400 мкс \* +73 % \* -89 % = -262 мкс. Результат = 1815 мкс - 262 мкс = 1553 мкс = режим 4)
