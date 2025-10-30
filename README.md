# phd_4k444
Custom Home Assistant integration for the PHD 4K444 HDMI Matrix Switch. ROUTING AND POWER ONLY

Home Assistant integration for the PHD 4K444 HDMI Matrix

🟣 PHD 4K444 HDMI Matrix Integration for Home Assistant
Custom Home Assistant integration by marsh4200 for controlling and monitoring the PHD 4K444 HDMI Matrix Switch.
This integration communicates directly with the matrix over TCP (port 23) to manage power, input routing, and device state — all from Home Assistant.

✨ Features
✅ Power ON / OFF control
✅ Power status sensor (real-time state feedback)
✅ Control HDMI routing (select inputs per output)
✅ Works locally — no internet or cloud required
In Home Assistant, go to HACS → Integrations → ⋮ → Custom repositories 2. Add this repository URL: https://github.com/marsh4200/phd_4k444

Category: Integration
Click Add, then search for PHD 4K444 Matrix in HACS.
Click Install and restart Home Assistant.
Add the integration in Settings → Devices & Services → Add Integration → PHD 4K444 Matrix.
When adding the integration, enter:

Setting	Description	Example
Host	IP address of your matrix	192.168.88.110
Port	Control port (default)	23
🧠 Entities Created
Entity	Type	Description
switch.phd_4k444_power	Switch	Power toggle for the matrix
sensor.phd_4k444_power_status	Sensor	Shows power state (ON/OFF)
media_player.phd_matrix_output_1 → media_player.phd_matrix_output_4	Media Players	Route input to output (1–4)
