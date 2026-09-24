# Failsafe (аварійний захист)

> Оригінал: [Failsafe](https://ardupilot.org/copter/docs/failsafe-landing-page.html)

Copter має низку механізмів failsafe (аварійний захист), що полегшують повернення апарата і не дають йому блукати, якщо керування втрачено. Основні теми failsafe перелічено нижче.

> **Примітка.** Якщо спрацював failsafe радіокерування, батареї, GCS (наземна станція керування) чи втрати даних рельєфу і його дія змінює режим апарата, апарат лишається в цьому режимі, доки пілот сам не змінить режим.

1. [Radio Failsafe](radio-failsafe.md) — втрата сигналу радіокерування
2. [Battery Failsafe](battery-failsafe.md) — низький заряд батареї
3. [GCS Failsafe](gcs-failsafe.md) — втрата зв'язку з GCS
4. [Failsafe EKF (розширений фільтр Калмана)](ekf-failsafe.md) — збій оцінки позиції
5. [Dead Reckoning Failsafe](dead-reckoning-failsafe.md) — політ за розрахунком після втрати GPS
6. [Vibration Failsafe](vibration-failsafe.md) — надмірні вібрації
7. [Terrain Data Loss Failsafe](terrain-following.md) — втрата даних рельєфу (див. розділ про RTL через втрату даних рельєфу)
8. [Crash Check](crash-check.md) — виявлення аварії
9. [Парашут](parachute.md)
10. [Independent Watchdog](watchdog.md) — незалежний сторожовий таймер

Див. також: [Arming the motors](arming.md) і [перевірки pre-arm (передпольотна перевірка)](prearm-checks.md).
