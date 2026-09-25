# Налаштування throttle висіння

> Оригінал: [Setting Hover Throttle](https://ardupilot.org/copter/docs/ac_throttlemid.html)

Copter автоматично навчається throttle (газ) висіння (раніше це називали «mid throttle»).
Значення `MOT_THST_HOVER` поступово наближається до середнього виходу моторів щоразу, коли апарат стабільно висить у неручних flight mode (польотний режим) (тобто в усіх режимах, крім Stabilize і Acro).

Якщо ви хочете задати `MOT_THST_HOVER` вручну, найкраще завантажити log (журнал польоту) dataflash і задати значення, яке видно в полі CTUN.ThO. Зазвичай воно між 0,2 і 0,6, але може бути нижчим, якщо коптер має дуже високе відношення потужності до ваги.

Якщо з якоїсь причини ви хочете вимкнути навчання, задайте параметр `MOT_HOVER_LEARN` 0.

![throttle_mid_learning](https://ardupilot.org/copter/_images/throttle_mid_learning.png)
