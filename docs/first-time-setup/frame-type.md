# Frame class and type (клас і тип рами)

> Оригінал: [Frame Class and Type Configuration](https://ardupilot.org/copter/docs/frame-type-configuration.html)

## Мультикоптери

Параметри `FRAME_CLASS` і `FRAME_TYPE` мають відповідати фізичній frame (рама), яку ви використовуєте. Перелік підтримуваних frame мультикоптерів — на сторінці [Підключення ESC (електронний регулятор обертів) і моторів](connect-escs-and-motors.md).

У Mission Planner виберіть Initial Setup, **Mandatory Hardware → Frame Type**. В іншій GCS (наземна станція керування) параметри `FRAME_CLASS` і `FRAME_TYPE` можна задати напряму на екрані редагування параметрів.

![MissionPlanner_Select_Frame-Type](https://ardupilot.org/copter/_images/MissionPlanner_Select_Frame-Type.jpg)

> **Примітка.** Для традиційних гелікоптерів уже має бути вибрано «Heli» — не змінюйте цього. Для [Single Copter і Coax Copter](https://ardupilot.org/copter/docs/singlecopter-and-coaxcopter.html) *(ще не перекладено)* параметр `FRAME_CLASS` задавайте напряму через Full Parameter List, доки не виправлено [цю проблему](https://github.com/ArduPilot/MissionPlanner/issues/1552).

Далі виберіть «Type» frame для вашого апарата. За замовчуванням — **X**.

Для трикоптерів, Y6, традиційних гелікоптерів, бікоптерів, SingleCopter і CoaxCopter тип frame ігнорується.

### Схеми порядку моторів

Перелік підтримуваних frame мультикоптерів — на сторінці [Підключення ESC і моторів](connect-escs-and-motors.md).

## Традиційні гелікоптери

Традиційні гелікоптери використовують окрему версію firmware (прошивка). Налаштування і tuning (точне налаштування) — у розділі [Traditional Helicopters](https://ardupilot.org/copter/docs/traditional-helicopters.html) *(ще не перекладено)*.

HeliQuad — гібридна frame на firmware традиційного гелікоптера, але з чотирма моторами.

1. [HeliQuads](https://ardupilot.org/copter/docs/heliquads.html) *(ще не перекладено)*

## Інші конфігурації

1. [Tricopter](https://ardupilot.org/copter/docs/tricopter.html) *(ще не перекладено)*
2. [SingleCopter і CoaxCopter](https://ardupilot.org/copter/docs/singlecopter-and-coaxcopter.html) *(ще не перекладено)*
