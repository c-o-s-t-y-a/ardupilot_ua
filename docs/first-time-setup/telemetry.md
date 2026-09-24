# Telemetry (телеметрія)

> Оригінал: [Telemetry (landing page)](https://ardupilot.org/copter/docs/common-telemetry-landingpage.html)

Copter/Plane/Rover/Blimp можуть обмінюватися інформацією з GCS (наземна станція керування) (або з RC transmitter (пульт радіокерування)) через telemetry (телеметрія). Інформацію з налаштування для вашої конфігурації — див. за посиланнями нижче.

> **Примітка.** Деякі системи радіокерування мають telemetry на додачу до керування.

> **Примітка.** Більшість «чистих» радіомодемів telemetry підключаються до autopilot (автопілот) через послідовний UART (послідовний порт) за протоколом MAVLink 1 або 2. Див. [Telemetry Port Setup](https://ardupilot.org/copter/docs/common-telemetry-port-setup.html) *(ще не перекладено)*.

![Telemetry_LandingImage](https://ardupilot.org/copter/_images/Telemetry_LandingImage.jpg)

> **Примітка.** Для дорогих систем, що використовують радіокерування через канал telemetry, варто розглянути [резервування telemetry](https://ardupilot.org/copter/docs/common-redundant-telemetry.html) *(ще не перекладено)*.

## Короткий радіус (<10 км)
1. [Bluetooth](bluetooth.md)
2. [CUAV PW-Link](https://ardupilot.org/copter/docs/common-cuav-pwlink.html) *(ще не перекладено)*
3. [DroneBridge for ESP32](https://ardupilot.org/copter/docs/common-esp32-telemetry.html) *(ще не перекладено)*
4. [ESP8266 wifi telemetry](https://ardupilot.org/copter/docs/common-esp8266-telemetry.html) *(ще не перекладено)*
5. [FrSky telemetry](https://ardupilot.org/copter/docs/common-frsky-telemetry.html) *(ще не перекладено)*
6. [i-BUS telemetry](https://ardupilot.org/copter/docs/common-ibus-telemetry.html) *(ще не перекладено)*
7. [Yaapu Bi-Directional Telemetry GCS](https://ardupilot.org/copter/docs/common-yaapu-gcs.html) *(ще не перекладено)*
8. [HOTT telemetry](https://ardupilot.org/copter/docs/common-hott-telemetry.html) *(ще не перекладено)*
9. [MSP (version 4.2)](https://ardupilot.org/copter/docs/common-msp-overview-4.2.html) *(ще не перекладено)*
10. [SiK Radio v1](https://ardupilot.org/copter/docs/common-3dr-radio-v1.html) *(ще не перекладено)*
11. [SiK Radio v2](https://ardupilot.org/copter/docs/common-sik-telemetry-radio.html) *(ще не перекладено)*
12. [SiK Radio configuration](https://ardupilot.org/copter/docs/common-configuring-a-telemetry-radio-using-mission-planner.html) *(ще не перекладено)*
13. [SiK Radio advanced configuration](https://ardupilot.org/copter/docs/common-3dr-radio-advanced-configuration-and-technical-information.html) *(ще не перекладено)*
14. [Teravolt AeroTel-24](https://ardupilot.org/copter/docs/common-AeroTel-24.html) *(ще не перекладено)*
15. [XBee](https://ardupilot.org/copter/docs/common-telemetry-xbee.html) *(ще не перекладено)*

## Великий радіус
1. [Andruav Android Cellular](https://cloud.ardupilot.org/andruav-index.html)
2. [Blicube RLINK P900](https://ardupilot.org/copter/docs/common-blicube-rlink.html) *(ще не перекладено)*
3. [ClearSky Airlink 4G LTE Telemetry](https://ardupilot.org/copter/docs/common-airlink-telemetry.html) *(ще не перекладено)*
4. [CRSF/ELRS Telemetry](https://ardupilot.org/copter/docs/common-crsf-telemetry.html) *(ще не перекладено)*
5. [CUAV P8 Radio](https://ardupilot.org/copter/docs/common-cuav-p8.html) *(ще не перекладено)*
6. [CUAV P9 Radio](https://ardupilot.org/copter/docs/common-cuav-p9.html) *(ще не перекладено)*
7. [DragonLink](https://ardupilot.org/copter/docs/common-dragonlink-rc.html) *(ще не перекладено)*
8. [Herelink](https://ardupilot.org/copter/docs/common-herelink.html) *(ще не перекладено)*
9. [Holybro SiK Telemetry Radio - Long Range](https://holybro.com/collections/telemetry-radios/products/sik-telemetry-radio-1w)
10. [Holybro 900Mhz XBP9X Telemetry Radio](https://shop.holybro.com/xbp9x-radio_p1268.html)
11. [Holybro Microhard Radio Telemetry Radio (P900/P840/P400-C1S)](https://holybro.com/products/microhard-radio)
12. [Holybro Microhard Radio Telemetry Radio V2 (P400/P900)](https://holybro.com/collections/telemetry-radios/products/microhard-telemetry-radio-v2)
13. [LTE Modems using Lua driver](https://github.com/ArduPilot/ardupilot/blob/master/libraries/AP_Scripting/drivers/LTE_modem.md)
14. [LTM telemetry](https://ardupilot.org/copter/docs/common-ltm-telemetry.html) *(ще не перекладено)*
15. [mLRS](https://ardupilot.org/copter/docs/common-mlrs-rc.html) *(ще не перекладено)*
16. [RFD900](https://ardupilot.org/copter/docs/common-rfd900.html) *(ще не перекладено)*
17. [Rockblock Satellite Modem](https://ardupilot.org/copter/docs/common-telemetry-rockblock.html) *(ще не перекладено)*
18. [SKYRELAY Conduit](https://ardupilot.org/copter/docs/common-skyrelay-conduit.html) *(ще не перекладено)*
19. [SPL Satellite Telemetry](https://discuss.ardupilot.org/t/stretching-comm-links-from-indoors-to-the-globe/45896)
20. [UAVCast 3G/4G Cellular](https://ardupilot.org/copter/docs/common-uavcast-telemetry.html) *(ще не перекладено)*
21. [XBStation 4G LTE Link](https://ardupilot.org/copter/docs/common-xbstation-telemetry.html) *(ще не перекладено)*

## Застосунки та інформація
1. [FlightDeck FrSky Transmitter App](https://ardupilot.org/copter/docs/common-frsky-flightdeck.html) *(ще не перекладено)*
2. [MAVLink2 Packet Signing (Security)](mavlink-signing.md)
3. [MAVLink High Latency Protocol](https://ardupilot.org/copter/docs/common-MAVLink-high-latency.html) *(ще не перекладено)*
4. [Repeater for Wireless Ground Station Connections](https://ardupilot.org/copter/docs/common-wireless-gcs-repeater.html) *(ще не перекладено)*
5. [Telemetry Radio Regional Regulations](https://ardupilot.org/copter/docs/common-telemetry-radio-regional-regulations.html) *(ще не перекладено)*

- [Yaapu Telemetry Scripts for OpenTX](https://ardupilot.org/copter/docs/common-frsky-yaapu.html) *(ще не перекладено)*
