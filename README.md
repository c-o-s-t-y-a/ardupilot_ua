# ArduPilot Copter — українською

Неофіційний український переклад ключових розділів документації [ArduPilot Copter](https://ardupilot.org/copter/).

- Оригінал: https://ardupilot.org/copter/ (джерела — [ArduPilot/ardupilot_wiki](https://github.com/ArduPilot/ardupilot_wiki))
- Ліцензія оригіналу і перекладу: [CC BY-SA 3.0](https://creativecommons.org/licenses/by-sa/3.0/)
- Переклад не пов'язаний з командою ArduPilot і може відставати від оригіналу. У разі розбіжностей правильним є оригінал.
- Стан перекладу і версії джерел: [translation-status.md](translation-status.md)
- **Читати як сайт:** https://c-o-s-t-y-a.github.io/ardupilot_ua/ (пошук, підказки до термінів, темна тема)

## Принципи перекладу

- Технічні терміни — **англійською**, як у Mission Planner і на форумах. При першій появі на сторінці — переклад у дужках: «failsafe (аварійний захист)». Усі терміни з поясненнями — на сторінці [Терміни](docs/glossary.md).
- Назви параметрів, flight mode-ів, кнопок і меню Mission Planner — англійською без перекладу (`FRAME_CLASS`, **Calibrate Accel**, Loiter).
- Перекладаємо лише з RST-джерел; технічний зміст не скорочуємо.
- Кожна сторінка має посилання на оригінал.

## Зміст

- [Перше налаштування](docs/first-time-setup/index.md)
  1. [Встановлення GCS](docs/first-time-setup/install-gcs.md)
     - [Вибір GCS](docs/first-time-setup/choosing-gcs.md)
  2. [Збирання системи autopilot](docs/first-time-setup/autopilot-assembly.md)
     - [Монтаж autopilot](docs/first-time-setup/mounting-autopilot.md)
     - [Підключення autopilot](docs/first-time-setup/autopilot-wiring.md)
     - [Підключення ESC і моторів](docs/first-time-setup/connect-escs-and-motors.md)
     - [Модуль GPS + compass](docs/first-time-setup/gps-compass-module.md)
     - [Гасіння вібрацій](docs/first-time-setup/vibration-damping.md)
     - [Магнітні завади](docs/first-time-setup/magnetic-interference.md)
  3. [Завантаження firmware](docs/first-time-setup/loading-firmware.md)
     - [На плати з bootloader](docs/first-time-setup/firmware-with-bootloader.md)
     - [На плати без bootloader (DFU)](docs/first-time-setup/firmware-dfu.md)
     - [З SD-карти](docs/first-time-setup/firmware-sd-card.md)
     - [Custom Firmware Builder](docs/first-time-setup/custom-firmware.md)
     - [Оновлення bootloader](docs/first-time-setup/bootloader-update.md)
     - [Обмеження firmware](docs/first-time-setup/limited-firmware.md)
  4. [Підключення Mission Planner до autopilot](docs/first-time-setup/connect-mission-planner.md)
     - [Telemetry](docs/first-time-setup/telemetry.md)
     - [Bluetooth](docs/first-time-setup/bluetooth.md)
     - [MAVLink2 Signing](docs/first-time-setup/mavlink-signing.md)
     - [Значення світлодіодів](docs/first-time-setup/leds-pixhawk.md)
     - [Звуки (Pixhawk)](docs/first-time-setup/sounds-pixhawk.md)
  5. [Обов'язкова конфігурація обладнання](docs/first-time-setup/mandatory-hardware.md)
     - [Огляд системи](docs/first-time-setup/basic-operation.md)
     - [Тип frame](docs/first-time-setup/frame-type.md)
     - [Підключення ESC і моторів](docs/first-time-setup/connect-escs-and-motors.md)
     - [Калібрування радіокерування](docs/first-time-setup/radio-calibration.md)
     - [Калібрування accelerometer](docs/first-time-setup/accelerometer-calibration.md)
     - [Калібрування compass](docs/first-time-setup/compass-calibration.md)
     - [Flight mode на RC transmitter](docs/first-time-setup/flight-mode-switch.md)
     - [Калібрування ESC](docs/first-time-setup/esc-calibration.md)
     - [Діапазон моторів](docs/first-time-setup/set-motor-range.md)
- [Терміни](docs/glossary.md)

## Для перекладачів

```bash
scripts/fetch-upstream.sh                     # sparse-клон ardupilot_wiki у .upstream/
scripts/check-terms.py docs/**/*.md           # терміни, транслітерації, залишки RST
scripts/check-params.py <page.md> <src.rst>   # усі параметри з джерела є в перекладі
scripts/update-status.py <page.md> <src.rst>  # записати сторінку в translation-status.md
scripts/check-stale.sh                        # які сторінки застаріли відносно upstream

pip install -r requirements.txt && mkdocs serve   # сайт локально: http://127.0.0.1:8000
```

Нова сторінка: додайте її в `nav` у `mkdocs.yml`, у зміст тут і в `docs/index.md`.
