# Значення світлодіодів

> Оригінал: [LEDs Meaning](https://ardupilot.org/copter/docs/common-leds-pixhawk.html)

Тут пояснено, як розуміти кольори й послідовності блимання основного та/або зовнішнього світлодіода (світлодіодів), якщо параметр `NTF_LED_OVERRIDE` має стандартне значення `standard`. Деяким світловим сигналам відповідають звукові, перелічені на сторінці [Звуки (Pixhawk)](sounds-pixhawk.md).

## Плати з 1 або 2 світлодіодами сповіщень

Такі плати мають на борту один (LED A) або два (LED A і LED B) світлодіоди — зазвичай, але не завжди, зелений і синій відповідно.

Після запуску LED A зазвичай показує стан системи, а LED B — стан GPS. Кожна показана нижче послідовність спалахів повторюється щосекунди. Наприклад, коли autopilot (автопілот) у режимі калібрування ESC (електронний регулятор обертів), LED A блимає з частотою 4 Гц і коефіцієнтом заповнення 50 % по черзі з LED B.

Стани й події наведено в порядку пріоритету. Наприклад, у випадку двох світлодіодів LED A показуватиме послідовність failsafe (аварійний захист) батареї, навіть якщо одночасно спрацював і failsafe RC.

| СТАН | LED A | LED B |
|---|---|---|
| Ініціалізація (калібрування gyro (гіроскоп) тощо) \* | <img src="https://ardupilot.org/copter/_images/initializinga.gif" alt="init" width="40"> | |
| **Save Trim** або калібрування ESC | <img src="https://ardupilot.org/copter/_images/savetrima.gif" alt="savetrima" width="40"> | <img src="https://ardupilot.org/copter/_images/savetrimb.gif" alt="savetrimb" width="40"> |
| Калібрування compass (компас) | <img src="https://ardupilot.org/copter/_images/compasscala.gif" alt="compcala" width="40"> | <img src="https://ardupilot.org/copter/_images/compasscalb.gif" alt="compcalb" width="40"> |
| AUTOTUNE:<br>завершено<br>невдало | <br><img src="https://ardupilot.org/copter/_images/autotunecomplete.gif" alt="atc" width="40"><br><img src="https://ardupilot.org/copter/_images/autotunefail.gif" alt="atf" width="40"> | |
| ARMED (у робочому стані):<br>failsafe батареї \*<br>failsafe RC або GCS (наземна станція керування)<br>готовий до польоту (ARMED) \* | <br><img src="https://ardupilot.org/copter/_images/battfs.gif" alt="battfs" width="40"><br><img src="https://ardupilot.org/copter/_images/controlfs.gif" alt="fs" width="40"><br><img src="https://ardupilot.org/copter/_images/armed.gif" alt="armed" width="40"> | |
| DISARMED (не в робочому стані):<br>перевірки pre-arm (передпольотна перевірка) не пройдено \*<br>готовий до arm (переведення в робочий стан) \* | <br><img src="https://ardupilot.org/copter/_images/prearmfail.gif" alt="prearm" width="40"><br><img src="https://ardupilot.org/copter/_images/readytoarm.gif" alt="ready" width="40"> | |
| GPS:<br>немає lock або немає GPS<br>lock (спалахів = кількість супутників / 2) | | <br>не світиться<br><img src="https://ardupilot.org/copter/_images/gps.gif" alt="gps" width="40"> 8 супутників |

\* Якщо світлодіод один, показуються лише ці сигнали. Сигнал failsafe батареї показується також для failsafe GCS і RC.

## RGB-світлодіоди

Стани й події наведено в порядку пріоритету.

| СТАН | LED |
|---|---|
| Ініціалізація (калібрування gyro тощо) | <img src="https://ardupilot.org/copter/_images/rgb-initializing.gif" alt="rgbinit" width="40"> |
| **Save Trim** або калібрування ESC | <img src="https://ardupilot.org/copter/_images/rgb-savetrim.gif" alt="rgbsavetrim" width="40"> |
| Failsafe через протікання<br>Failsafe EKF (розширений фільтр Калмана)<br>Збій GPS<br>Failsafe радіо/GCS/батареї | <img src="https://ardupilot.org/copter/_images/rgb-leakfs.gif" alt="rgbleakfs" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-ekffs.gif" alt="rgbekffs" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-gps-glitch.gif" alt="rgbgpsglitch" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-controlfs.gif" alt="rgbcontrolfs" width="40"> |
| ARMED:<br>3D-фіксація<br>немає дійсної фіксації GPS | <br><img src="https://ardupilot.org/copter/_images/rgb-armed.gif" alt="rgbarmed" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-armed-nogps.gif" alt="rgbarmednogps" width="40"> |
| DISARMED:<br>перевірки pre-arm не пройдено<br>добра фіксація DGPS \*<br>добра фіксація GPS \*<br>погана фіксація GPS | <br><img src="https://ardupilot.org/copter/_images/rgb-prearmfail.gif" alt="rgbprearm" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-good-dgps.gif" alt="rgbready1" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-good-gps.gif" alt="rgbready2" width="40"><br><img src="https://ardupilot.org/copter/_images/rgb-bad-gps.gif" alt="rgbbadgps" width="40"> |

\* GPS lock (фіксація позиції GPS) показується лише тоді, коли позиція стала дійсною, а для цього потрібно більше, ніж просто GPS lock.

## Відеоогляд

[Відео (YouTube)](https://www.youtube.com/watch?v=j-CMLrAwlco)

## Значення світлодіодів і зумера

**Блимає червоним і синім**: ініціалізація gyro. Тримайте апарат нерухомо й рівно, поки він ініціалізує датчики.

**Блимає синім**: disarmed, GPS lock не знайдено. Для режимів autopilot, loiter і return-to-launch потрібен GPS lock.

**Світиться синім**: armed без GPS lock.

**Блимає зеленим**: disarmed (готовий до arm), GPS lock отримано. Швидкий подвійний сигнал під час disarm (виведення з робочого стану) зі стану armed.

**Швидко блимає зеленим**: те саме, що вище, але GPS використовує SBAS (тож оцінка позиції має бути кращою).

**Світиться зеленим — з одним довгим сигналом у момент arm:** armed, GPS lock отримано. Готовий до польоту!

**Подвійні спалахи жовтим:** перевірки pre-arm не пройдено (система відмовляється виконувати arm).

**Одинарні спалахи жовтим:** спрацював failsafe радіокерування.

**Блимає жовтим — зі швидким пищанням**: спрацював failsafe батареї.

**Блимає жовтим і синім — з послідовністю тонів високий-високий-високий-низький (та-та-та-там):** збій GPS або спрацював failsafe GPS.

**Блимає червоним і жовтим — з висхідним тоном:** збій EKF або інерціальної навігації.

**Блимає червоним, синім і зеленим**: увімкнено режим калібрування ESC Copter. Див. [Калібрування ESC](esc-calibration.md).

[Послідовність тонів SOS](https://download.ardupilot.org/downloads/wiki/pixhawk_sound_files/NoSDCard_short.wav): немає SD-карти (або інша помилка SD, наприклад неправильне форматування тощо).
