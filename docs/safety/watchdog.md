# Independent watchdog і crash dump (незалежний сторожовий таймер і дамп збою)

> Оригінал: [Independent Watchdog and Crash Dump](https://ardupilot.org/copter/docs/common-watchdog.html)

ArduPilot вмикає внутрішній незалежний сторожовий таймер (independent watchdog) процесора autopilot (автопілот), який скидає і перезапускає процесор, якщо периферія чи якийсь фрагмент коду виконується надто довго або «вішає» процесор. Це може врятувати апарат у польоті чи русі, а може й ні.

Хоча це не рекомендовано, цю функцію можна вимкнути, встановивши `BRD_OPTIONS` = 0.

У разі «HARD FAULT» (наприклад, недопустима інструкція, доступ до пам'яті за межами тощо) перед скиданням обробник watchdog запише повідомлення «WDG» у бортовий log (журнал польоту), надішле текстове повідомлення «WDG» на GCS (наземна станція керування) і спробує записати файл crash_dump.bin в область flash (флеш-пам'ять) «@SYS». Цей файл crash_dump.bin містить стан процесора і регістри для подальшого аналізу (докладніше — у розділі нижче). «HARD FAULT» — надзвичайно серйозна подія, про яку слід повідомити ArduPilot. Ймовірно, літати на апараті небезпечно, доки причину не усунуто.

У ArduPilot-4.5.1 (і новіших), якщо створено файл crash_dump.bin, перевірка pre-arm (передпольотна перевірка) попередить користувача і не дасть виконати arm (переведення в робочий стан). Файл crash_dump.bin можна стерти, повторно записавши firmware (прошивка) ArduPilot на autopilot, або ігнорувати, встановивши параметр `ARMING_CRSDP_IGN` в 1 (не рекомендовано).

[Відео (YouTube)](https://www.youtube.com/watch?v=ZGuTIPLI_e0)

## Як повідомити про watchdog / crash dump

За допомогою Mission Planner чи іншої GCS завантажте файл crash_dump.bin з області flash «@SYS».

![crash_dump](https://ardupilot.org/copter/_images/crash_dump.png)

Завантажте log dataflash польоту чи роботи, під час якої було створено crash dump. Як завантажувати log-и — див. [тут](https://ardupilot.org/copter/docs/common-downloading-and-analyzing-data-logs-in-mission-planner.html) *(ще не перекладено)*.

Якщо log dataflash не вдається знайти, дізнайтеся git-hash firmware. Він з'являється на вкладці повідомлень GCS невдовзі після запуску.

![git-hash](https://ardupilot.org/copter/_images/git-hash.png)

Відкрийте [форум підтримки ArduPilot](https://discuss.ardupilot.org/), знайдіть категорію для вашого апарата й версії програми (наприклад, [Copter-4.6](https://discuss.ardupilot.org/c/arducopter/copter-46/179), [Plane-4.6](https://discuss.ardupilot.org/c/arduplane/plane-4-6/182), [Rover-4.6](https://discuss.ardupilot.org/c/ardurover/rover-46/180)), створіть «New Topic», додайте в заголовок «watchdog» і прикріпіть файл crash_dump.bin, файл log та/або git-hash, як описано вище. Якщо файли не вдається завантажити напряму, додайте посилання, звідки їх можна завантажити.

## Як визначити, що стався скид watchdog

Один спосіб — переглянути log-и dataflash. Якщо відфільтрувати log, щоб показати лише повідомлення «MSG», видно, що деякі з них містять слово «watchdog». Це явна ознака того, що попередній log чи політ закінчився скиданням через watchdog.

![watchdog](https://ardupilot.org/copter/_images/watchdog.png)

Також має з'явитися повідомлення log WDOG з такими стовпцями, що можуть стати в пригоді розробникам, які досліджують причину спрацювання watchdog:

- Task: номер задачі планувальника АБО

    - -1, якщо головний цикл щойно отримав наступний зразок IMU (інерційний вимірювальний модуль)
    - -2, якщо почався швидкий цикл
    - -3, якщо головний цикл чекав на наступний зразок IMU

- IErr: маска внутрішніх помилок
- IErrCnt: кількість внутрішніх помилок
- MavMsg: ідентифікатор останнього обробленого повідомлення MAVLink
- MavCmd: поле command останнього обробленого повідомлення MAVLink COMMAND_LONG або COMMAND_LONG_INT
- SemLine: номер рядка вихідного коду, якщо програма чекає на семафор, або 0, якщо не чекає
- FL: Fault Line — номер рядка вихідного коду, де стався збій. Зверніть увагу: назву файлу не вказано, але це все одно може бути корисно
- FT: Fault Type — тип збою (див. [FaultType enum в AP_HAL_ChibiOS/system.cpp](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_HAL_ChibiOS/hwdef/common/stm32_util.h#L144-L151))

    - 1 = Reset
    - 2 = Non-Maskable Interrupt (NMI)
    - 3 = Hard Fault (найпоширеніший)
    - 4 = Memory Management Fault
    - 5 = Bus Fault
    - 6 = Usage Fault

- FA: Fault Address — адреса збою (у пам'яті). Наприклад, вона буде 0, якщо була спроба прочитати байт через nullptr
- FP: пріоритет потоку (див. список пріоритетів, що починається з APM_MONITOR_PRIORITY, в [AP_HAL_ChibiOS/Scheduler.h](https://github.com/ardupilot/ardupilot/blob/master/libraries/AP_HAL_ChibiOS/Scheduler.h#L25))
- ICSR: Interrupt Control and State Register (див. «ICSR bit assignments» у документації ST)
