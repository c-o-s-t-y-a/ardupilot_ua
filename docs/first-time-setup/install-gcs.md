# Installing GCS (встановлення наземної станції керування)

> Оригінал: [Installing Ground Station (GCS) software](https://ardupilot.org/copter/docs/common-install-gcs.html)

ArduPilot працює з [багатьма різними GCS (наземна станція керування)](https://ardupilot.org/copter/docs/common-choosing-a-ground-station.html) *(ще не перекладено)*.

Розробники зазвичай користуються *настільними* GCS: вони дають глибший доступ до параметрів налаштування апарата і розширені засоби налагодження. Якщо ви хочете просто літати, можна обрати GCS для мобільної ОС (iOS, Android).

Посилання для встановлення найпопулярніших GCS:

- [Mission Planner](https://ardupilot.org/planner/) (Windows, Linux, Android): [встановлення Mission Planner](https://ardupilot.org/planner/docs/mission-planner-installation.html). Найсумісніша GCS, яка найшвидше підтримує нові функції та оновлення ArduPilot. Рекомендована і новачкам, і досвідченим користувачам. Найкраще працює у Windows.

- [QGroundControl](http://qgroundcontrol.com/) (Windows, Mac OS X, Linux, Android та iOS). Найпопулярніша GCS для Android і найкраще відображається на малих екранах, як-от смартфони. Має не всі можливості Mission Planner, але для деяких функцій інтерфейс зручніший. Добре працює на всіх платформах.

  - [Завантаження і встановлення](https://docs.qgroundcontrol.com/en/getting_started/download_and_install.html) (stable)
  - [Щоденні збірки](https://docs.qgroundcontrol.com/en/releases/daily_builds.html)

- [APM Planner 2](https://ardupilot.org/planner2/) (Windows, Mac OS X, Linux): [встановлення APM Planner 2](https://ardupilot.org/planner2/docs/installing-apm-planner-2.html). Базова функціональність; наразі погано підтримується й оновлюється.

- [ArduDeck](https://ardudeck.com) (Windows, Mac OS X, Linux): **зараз в альфа-тестуванні — відгуки вітаються!** Безкоштовна GCS з відкритим кодом і сучасним інтерфейсом. Підтримує telemetry (телеметрія) в реальному часі, планування місій з профілями висоти з урахуванням рельєфу, повне керування параметрами, майстри калібрування, запис firmware (прошивка), візуальний редактор Lua-скриптів і підписування MAVLink. Також підтримує Betaflight та iNav через протокол MSP.

  - [Завантаження і встановлення](https://ardudeck.com/docs/Getting-Started)
  - [Вихідний код](https://github.com/rubenCodeforges/ardudeck)
