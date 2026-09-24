# Завантаження firmware (прошивки) на плати без сумісного bootloader

> Оригінал: [Loading Firmware to Boards without an ArduPilot Compatible Bootloader](https://ardupilot.org/copter/docs/common-loading-firmware-onto-chibios-only-boards.html)

Тут описано, як завантажити ArduPilot на autopilot (автопілот), на якому ще немає [сумісного з ArduPilot bootloader (завантажувач)](loading-firmware.md#крок-2-перевірте-що-вже-є-на-autopilot), — зазвичай це плата, що постачається з попередньо встановленою Betaflight, INAV чи подібною firmware (прошивка). Bootloader і firmware ArduPilot записуються разом через USB у режимі DFU (режим прошивання через USB) (direct firmware upload).

Це одноразова операція. Після успіху на платі є bootloader ArduPilot, і всі подальші оновлення виконуються звичайним способом через GCS (наземна станція керування), описаним у [Завантаження firmware на плати з сумісним bootloader](firmware-with-bootloader.md).

Якщо на платі вже працює firmware ArduPilot чи PX4, скористайтеся натомість тією сторінкою — DFU вам не потрібен.

Встановлення ArduPilot на такі autopilot включає:

- встановлення потрібного драйвера й програми для запису;
- завантаження відповідного файлу firmware `arduXXX_with_bl.hex`;
- запис його на плату через DFU.

## Завантажте драйвер і програму для запису

[STM32CubeProgrammer](https://www.st.com/en/development-tools/stm32cubeprog.html) встановить потрібні драйвери DFU і вміє записувати firmware на autopilot у режимі DFU. Програма є для Windows, Linux і MacOS. Завантажте і встановіть її. Для встановлення може знадобитися також [JAVA](https://java.com/en/download/).

## Завантажте firmware ArduPilot

Виконайте кроки з [Завантаження файлу firmware](loading-firmware.md#завантаження-файлу-firmware), щоб отримати firmware для вашої плати, вибравши файл `arduXXX_with_bl.hex`. Він містить і bootloader ArduPilot, і firmware — саме це потрібно для запису через DFU; файли `.apj` тут не підходять.

## Запишіть firmware на autopilot

- Затисніть кнопку DFU на платі або тимчасово замкніть її контакти «BOOT» і підключіть USB-кабель (з'єднаний з комп'ютером). Коли плата отримає живлення, відпустіть кнопку або розімкніть контакти.
- Відкрийте диспетчер пристроїв Windows і знайдіть у розділі «Universal Serial Bus devices» пристрій «STM32 BOOTLOADER» — це підтверджує, що плата в режимі DFU.

    <img src="https://ardupilot.org/copter/_images/loading-firmware-device-manager.png" alt="loading-firmware-device-manager" width="450">

- Запустіть STM32CubeProgrammer.

![STM32CubeProgrammer1](https://ardupilot.org/copter/_images/STM32CubeProgrammer1.jpg)

1. Виберіть спосіб підключення: USB.
2. Переконайтеся, що з'явився USB-порт — це означає, що плату виявлено в режимі DFU.
3. Натисніть «Connect».
4. Тут з'являться характеристики процесора плати.
5. Натисніть «Open file» і виберіть завантажений файл «arduXXX_with_bl.hex».
6. Назва файлу з'явиться на вкладці.

![STM32CubeProgrammer2](https://ardupilot.org/copter/_images/STM32CubeProgrammer2.jpg)

7. Натисніть «Download», щоб записати файл на плату.

Тепер можна перезавантажити плату і [переконатися, що firmware працює](loading-firmware.md#крок-4-перевірте-що-все-спрацювало). Подальші оновлення firmware можна робити звичайним способом через GCS, див. [Завантаження firmware на плати з сумісним bootloader](firmware-with-bootloader.md).

## Завантаження firmware на плати із зовнішньою flash

Деякі сучасні плати, насамперед від Seriously Pro Racing (http://www.seriouslypro.com/), використовують мікроконтролери з невеликою внутрішньою flash (флеш-пам'ять), але зі значно більшими зовнішніми мікросхемами flash. Для запису firmware ArduPilot на такі плати потрібні додаткові кроки. Зазвичай на внутрішній flash стоїть якийсь bootloader, а основна firmware зберігається на зовнішній flash.

### Завантаження firmware за допомогою SSBL

Плати серії SPRacing постачаються з пропрієтарним bootloader на внутрішній flash, і для запису іншої firmware їм потрібен bootloader другого рівня (second stage bootloader, SSBL). Є кілька варіантів запису firmware на ці плати, але який би ви не вибрали, спершу ArduPilot треба записати за допомогою SSBL. Виконайте інструкції «INSTALLATION» на https://github.com/spracing/ssbl, щоб записати SSBL на плату. Після цього виконайте інструкції для PX4, щоб записати ArduPilot на плату — https://github.com/spracing/ssbl#px4-installation-to-external-flash, — але замість firmware PX4 використайте образ firmware arducopter.bin. Коротко кроки такі:

- Завантажте https://github.com/spracing/ssbl/releases і встановіть SSBL на зовнішню flash за інструкцією https://github.com/spracing/ssbl#installation-to-external-flash
- Завантажте найновіший бінарний файл ArduPilot для зовнішньої flash, наприклад https://firmware.ardupilot.org/Copter/latest/SPRacingH7/arducopter.bin
- За допомогою dd доповніть бінарний файл до 2 МБ:

```text
dd if=/dev/zero ibs=1k count=2048 of=AP_2MB.bin
dd conv=notrunc if=arducopter.bin of=AP_2MB.bin
```

- Переведіть плату в режим dfu SSBL: вимкніть живлення, затисніть **BIND** (не **BOOT**), увімкніть живлення — світлодіод швидко блимає, відпустіть **BIND** — світлодіод блимає повільно, режим DFU увімкнено.
- Запишіть бінарний файл командою

```text
dfu-util -D AP_2MB.bin -s 0x90100000:0x200000
```

- Перевірте запис. Команда dfu-util нижче копіює вміст flash назад на комп'ютер, а команда diff покаже, чи вміст однаковий. Не намагайтеся літати, якщо diff не повідомив, що файли однакові, — повторіть запис.

```text
dfu-util -U AP_2MB-VERIFY.bin -s 0x90100000:0x200000
diff -sb AP_2MB.bin AP_2MB-VERIFY.bin
```

- Вимкніть живлення, вставте SD-карту (увага: SD-карта *обов'язкова*, без неї firmware не запуститься), увімкніть живлення.
- Налаштуйте плату як зазвичай у Mission Planner.

Тепер на платі має бути робоча firmware. Щоб записати нову firmware, доведеться знову виконати кроки 2–7 (записувати firmware через Mission Planner не можна). Якщо ви впевнені, що ніколи не захочете записати на плату Betaflight, можна встановити bootloader ArduPilot.

### Встановлення bootloader ArduPilot

> **Попередження.** Встановлення bootloader ArduPilot — незворотна операція. Після цього кроку ви не зможете повернути плату до заводської конфігурації чи записати Betaflight — плату довелося б повертати в Seriously Pro для запису заводської firmware, якщо це взагалі можливо.

**Якщо ви впевнені, що хочете використовувати на платі лише ArduPilot**, запис bootloader ArduPilot значно спрощує подальші оновлення.

- Спершу на платі має бути робоча версія ArduPilot — виконайте кроки вище.
- Тепер треба зняти захист від копіювання внутрішньої flash. Це руйнівна операція, що потребує повного стирання flash. ArduPilot дозволяє зробити це легко. Встановіть `BRD_OPTIONS` = 16.
- Вимкніть і увімкніть живлення плати. Здаватиметься, що плата не завантажується, але в цей час стирається сектор flash. Зачекайте кілька секунд і вимкніть живлення.
- Затисніть кнопку **boot** (цього разу **boot**, *а не* **bind**) і увімкніть живлення autopilot. Це переведе плату в режим dfu.
- Завантажте bootloader ArduPilot, наприклад https://github.com/ArduPilot/ardupilot/blob/master/Tools/bootloaders/SPRacingH7_bl.bin
- Встановіть bootloader через dfu:

```text
dfu-util -a 0 --dfuse-address 0x08000000 -D SPRacingH7_bl.bin
```

- Перезавантажте плату.
- Тепер записувати firmware ArduPilot можна вашою улюбленою програмою.
