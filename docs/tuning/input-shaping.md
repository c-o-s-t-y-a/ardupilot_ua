# Налаштування параметрів input shaping

> Оригінал: [Setting the input shaping parameters](https://ardupilot.org/copter/docs/input-shaping.html)

Copter має набір параметрів, які визначають, як апарат відчувається в польоті. Це дає змогу налаштувати апарат із дуже агресивним tuning (точне налаштування), але так, щоб у керуванні він лишався дуже слухняним і дружнім.

Найважливіші з цих параметрів:

- `PILOT_Y_RATE`: бажана максимальна швидкість yaw (рискання) у град/с
- `ATC_ACC_P_MAX`: кутове прискорення по pitch (тангаж)
- `ATC_ACC_R_MAX`: кутове прискорення по roll (крен)
- `ATC_ACC_Y_MAX`: кутове прискорення по yaw
- `ATC_ANGLE_MAX`: максимальний кут нахилу

- `ATC_ANG_LIM_TC`: час згладжування апарата
- `ATC_INPUT_TC`: час досягнення 63% усталеного положення по pitch і roll. Помножте на 3, щоб визначити час досягнення усталеного положення.
- `PILOT_Y_RATE_TC`: час досягнення 63% усталеної швидкості yaw. Помножте на 3, щоб визначити час досягнення усталеної швидкості.

Autotune встановлює `ATC_ACC_P_MAX`, `ATC_ACC_R_MAX` і `ATC_ACC_Y_MAX` у максимальні значення на основі вимірювань під час тестів Autotune. Не збільшуйте ці значення понад те, що пропонує Autotune, без ретельного тестування. У більшості випадків пілоти захочуть суттєво їх зменшити.

Для апаратів, призначених для перенесення великих жорстко закріплених корисних навантажень, максимальні значення `ATC_ACC_P_MAX`, `ATC_ACC_R_MAX` і `ATC_ACC_Y_MAX` слід зменшити з урахуванням мінімальної і максимальної злітної маси (TOW):

- `ATC_ACC_P_MAX` × (min_TOW / max_TOW)
- `ATC_ACC_R_MAX` × (min_TOW / max_TOW)
- `ATC_ACC_Y_MAX` × (min_TOW / max_TOW)

`PILOT_Y_RATE` слід задати приблизно 0,5 × `ATC_ACC_Y_MAX`, щоб апарат міг досягти повної швидкості yaw приблизно за пів секунди.

`ATC_ANG_LIM_TC` можна збільшити, щоб отримати дуже плавне відчуття на stick (ручка керування) ціною повільнішої реакції.

Акробатичним апаратам слід залишити значення `ATC_ACC_P_MAX`, `ATC_ACC_R_MAX` і `ATC_ACC_Y_MAX`, отримані від autotune, і зменшити `ATC_ANG_LIM_TC`, щоб отримати бажане пілотом відчуття stick. Пілоти, які хочуть літати в ACRO, можуть налаштувати його відчуття такими параметрами input shaping:

- `ACRO_BAL_PITCH`
- `ACRO_BAL_ROLL`
- `ACRO_RP_EXPO`
- `ACRO_RP_RATE`
- `ACRO_RP_RATE_TC`
- `ACRO_THR_MID`
- `ACRO_TRAINER`
- `ACRO_Y_EXPO`
- `ACRO_Y_RATE`
- `ACRO_Y_RATE_TC`

Повний перелік параметрів input shaping:

- `ACRO_BAL_PITCH`
- `ACRO_BAL_ROLL`
- `ACRO_RP_EXPO`
- `ACRO_RP_RATE`
- `ACRO_RP_RATE_TC`
- `ACRO_THR_MID`
- `ACRO_TRAINER`
- `ACRO_Y_EXPO`
- `ACRO_Y_RATE`
- `ACRO_Y_RATE_TC`
- `ATC_ACC_P_MAX`
- `ATC_ACC_R_MAX`
- `ATC_ACC_Y_MAX`
- `ATC_ANGLE_MAX`
- `ATC_INPUT_TC`
- `ATC_ANG_LIM_TC`
- `ATC_RATE_P_MAX`
- `ATC_RATE_R_MAX`
- `ATC_RATE_Y_MAX`
- `ATC_RATE_WPY_MAX`
- `PILOT_ACC_Z`
- `PILOT_SPD_DN`
- `PILOT_SPD_UP`
- `PILOT_THR_BHV`
- `PILOT_THR_FILT`
- `PILOT_TKO_ALT_M`
- `PILOT_Y_RATE`
- `PILOT_Y_RATE_TC`
- `LOIT_ACC_MAX_M`
- `LOIT_ANG_MAX`
- `LOIT_BRK_ACC_M`
- `LOIT_BRK_DELAY`
- `LOIT_BRK_JRK_M`
- `LOIT_SPEED_MS`
