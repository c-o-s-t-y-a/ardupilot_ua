# ArduPilot Copter українською

Неофіційний український переклад ключових розділів документації [ArduPilot Copter](https://ardupilot.org/copter/).

> **Примітка.** Переклад не пов'язаний з командою ArduPilot і може відставати від оригіналу. У разі розбіжностей правильним є оригінал. Кожна сторінка має посилання на свій оригінал.

## Як читати

Технічні терміни залишено **англійською** — так, як ви побачите їх у Mission Planner, на форумах і в оригінальній документації. При першій появі на сторінці поруч стоїть переклад у дужках: «failsafe (аварійний захист)». Наведіть курсор на термін (або торкніться на телефоні), щоб побачити пояснення. Усі терміни зібрано на сторінці [Терміни](glossary.md).

Назви параметрів (`FRAME_CLASS`), режимів польоту (Loiter, RTL), кнопок і меню Mission Planner (**Calibrate Accel**) не перекладаються.

## Зміст

- [Перше налаштування](first-time-setup/index.md)
    1. [Встановлення GCS](first-time-setup/install-gcs.md)
    2. [Збирання системи autopilot](first-time-setup/autopilot-assembly.md)
        - [Монтаж autopilot](first-time-setup/mounting-autopilot.md)
        - [Підключення autopilot](first-time-setup/autopilot-wiring.md)
        - [Підключення ESC і моторів](first-time-setup/connect-escs-and-motors.md)
        - [Модуль GPS + compass](first-time-setup/gps-compass-module.md)
        - [Гасіння вібрацій](first-time-setup/vibration-damping.md)
        - [Магнітні завади](first-time-setup/magnetic-interference.md)
    3. [Завантаження firmware](first-time-setup/loading-firmware.md)
        - [На плати з bootloader](first-time-setup/firmware-with-bootloader.md)
        - [На плати без bootloader (DFU)](first-time-setup/firmware-dfu.md)
        - [З SD-карти](first-time-setup/firmware-sd-card.md)
        - [Custom Firmware Builder](first-time-setup/custom-firmware.md)
        - [Оновлення bootloader](first-time-setup/bootloader-update.md)
        - [Обмеження firmware](first-time-setup/limited-firmware.md)
    4. [Підключення Mission Planner до autopilot](first-time-setup/connect-mission-planner.md)
    5. [Обов'язкова конфігурація обладнання](first-time-setup/mandatory-hardware.md)
        - [Огляд системи](first-time-setup/basic-operation.md)
        - [Тип frame](first-time-setup/frame-type.md)
        - [Підключення ESC і моторів](first-time-setup/connect-escs-and-motors.md)
        - [Калібрування радіокерування](first-time-setup/radio-calibration.md)
        - [Калібрування accelerometer](first-time-setup/accelerometer-calibration.md)
        - [Калібрування compass](first-time-setup/compass-calibration.md)
        - [Flight mode на RC transmitter](first-time-setup/flight-mode-switch.md)
        - [Калібрування ESC](first-time-setup/esc-calibration.md)
        - [Діапазон моторів](first-time-setup/set-motor-range.md)
- [Терміни](glossary.md)

## Ліцензія

Оригінал і переклад поширюються на умовах [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/). Джерела: [ArduPilot/ardupilot_wiki](https://github.com/ArduPilot/ardupilot_wiki). Вихідні тексти перекладу — [на GitHub](https://github.com/c-o-s-t-y-a/ardupilot_ua).
