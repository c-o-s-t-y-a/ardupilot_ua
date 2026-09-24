# HeliQuads (мультикоптери зі змінним кроком гвинтів)

> Оригінал: [HeliQuads (Variable Pitch Multicopters)](https://ardupilot.org/copter/docs/heliquads.html)

[Відео (YouTube)](https://www.youtube.com/watch?v=J6WJSXm7zWQ)

<!-- terms-ignore: pitch -->
ArduPilot підтримує HeliQuad, які також називають квадрокоптерами із загальним кроком гвинтів (Collective Pitch Quadcopters) або мультикоптерами зі змінним кроком (Variable Pitch Multicopters).

![heliquad](https://ardupilot.org/copter/_images/heliquad.png)

> **Примітка.** Для HeliQuad базовою потрібна firmware (прошивка) [традиційного гелікоптера](traditional-helicopters.md). Її можна завантажити з [сервера firmware](https://firmware.ardupilot.org/). Під час компіляції Copter тепер створюються обидві firmware — для традиційного гелікоптера і для мультиротора.

<!-- terms-ignore: pitch -->
Ці апарати мають незалежне керування загальним кроком (collective pitch) кожного з 4 гвинтів, а один електромотор обертає всі 4 гвинти з однаковою швидкістю через паси і вал. Апарат дуже акробатичний, здатний до перевернутого польоту, але може страждати від [високого рівня вібрацій](https://ardupilot.org/copter/docs/common-measuring-vibration.html) *(ще не перекладено)*.

## Де купити

- WLtoys Assassin V383 продається, зокрема, на [WLtoys.eu](https://wltoys.eu/wltoys-v383)

## Підключення й налаштування

<img src="https://ardupilot.org/copter/_images/heliquad-pixhawk.png" alt="heliquad-pixhawk" width="500">

- кожен servo (сервопривід) підключається до тих самих виходів, що використовувалися б для моторів на звичайному мультикоптері ([див. порядок тут](connect-escs-and-motors.md));
- ESC (електронний регулятор обертів) мотора підключається до виходу 8 autopilot (автопілот);
- на апарат треба записати [firmware традиційного гелікоптера](traditional-helicopters.md).

Для WLToys Assassin V383 [є файл параметрів](https://github.com/ArduPilot/ardupilot/blob/master/Tools/Frame_params/WLToys_V383_HeliQuad.param), яким можна одразу задати всі параметри. Для інших збірок треба встановити такі стандартні параметри:

- `FRAME_CLASS` у 13 (HeliQuad)
- `FRAME_TYPE` у 1 («X», якщо передній правий мотор обертається проти годинникової стрілки) або 3 («H», якщо передній правий мотор обертається за годинниковою стрілкою)

Як і на [традиційному гелікоптері](traditional-helicopters.md), [допоміжний перемикач](https://ardupilot.org/copter/docs/common-auxiliary-functions.html) *(ще не перекладено)* слід налаштувати на «Motor Interlock», щоб вмикати й вимикати мотор. Зазвичай це канал 8, тож можна встановити `RC8_OPTION` у 32.

## Відео

Тест перевернутого польоту: [відео (YouTube)](https://www.youtube.com/watch?v=1yEWhOULeGM)

Фото апарата CanberraUAV:

![heliquad-canberrauav](https://ardupilot.org/copter/_images/heliquad-canberrauav.jpg)
