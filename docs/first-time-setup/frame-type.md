# Клас і тип рами

> Оригінал: [Frame Class and Type Configuration](https://ardupilot.org/copter/docs/frame-type-configuration.html)

## Мультикоптери

Параметри `FRAME_CLASS` і `FRAME_TYPE` мають відповідати фізичній рамі. Список підтримуваних рам — на сторінці [Підключення ESC і моторів](https://ardupilot.org/copter/docs/connect-escs-and-motors.html).

У Mission Planner: **Initial Setup → Mandatory Hardware → Frame Type**. В іншій наземній станції `FRAME_CLASS` і `FRAME_TYPE` можна задати напряму через екран параметрів.

![Вибір типу рами в Mission Planner](https://ardupilot.org/copter/_images/MissionPlanner_Select_Frame-Type.jpg)

> **Примітка.** Для традиційних гелікоптерів уже має бути вибрано «Heli» — не змінюйте. Для [Single Copter і Coax Copter](https://ardupilot.org/copter/docs/singlecopter-and-coaxcopter.html) `FRAME_CLASS` задавайте напряму через Full Parameter List, доки не виправлено [цю проблему](https://github.com/ArduPilot/MissionPlanner/issues/1552).

Далі оберіть **Type** рами. За замовчуванням — **X**.

Для трикоптерів, Y6, традиційних гелікоптерів, бікоптерів, SingleCopter і CoaxCopter тип рами ігнорується.

### Схеми порядку моторів

Див. [Підключення ESC і моторів](https://ardupilot.org/copter/docs/connect-escs-and-motors.html).

## Традиційні гелікоптери

Традиційні гелікоптери використовують окрему прошивку. Налаштування і тюнінг — у розділі [Traditional Helicopters](https://ardupilot.org/copter/docs/traditional-helicopters.html).

HeliQuad — гібридна рама на прошивці традиційного гелікоптера, але з чотирма моторами: [HeliQuads](https://ardupilot.org/copter/docs/heliquads.html).

## Інші конфігурації

- [Tricopter](https://ardupilot.org/copter/docs/tricopter.html)
- [SingleCopter і CoaxCopter](https://ardupilot.org/copter/docs/singlecopter-and-coaxcopter.html)
