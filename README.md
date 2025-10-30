Custom Home Assistant integration for the PHD SOLUTIONS 4K444 HDMI Matrix Switch. ROUTING AND POWER ONLY

Home Assistant integration for the PHD 4K444 HDMI Matrix

🟣 PHD 4K444 HDMI Matrix Integration for Home Assistant
Custom Home Assistant integration by marsh4200 for controlling and monitoring the PHD 4K444 HDMI Matrix Switch.
This integration communicates directly with the matrix over TCP (port 23) to manage power, input routing, and device state — all from Home Assistant.

✨ Features
✅ Power ON / OFF control
✅ Power status sensor (real-time state feedback)
✅ Control HDMI routing (select inputs per output)
✅ Works locally — no internet or cloud required
In Home Assistant, go to HACS → Integrations → ⋮ → Custom repositories 
2. Add this repository URL: https://github.com/marsh4200/phd_4k444

Category: Integration
Click Add, then search for PHD 4K444 Matrix in HACS.
Click Install and restart Home Assistant.
Add the integration in Settings → Devices & Services → Add Integration → PHD 4K444 Matrix.
When adding the integration, enter:  Example Host	IP address of your matrix	192.168.45.11
Port	Control port (default)	23

🎛️ PHD 4K444 Matrix Control Panel

🧠 Entities Created
Entity	Type	Description
switch.phd_4k444_power	Switch	Power toggle for the matrix
sensor.phd_4k444_power_status	Sensor	Shows power state (ON/OFF)

This integration provides 16 routing buttons and 3 power controls for the PHD 4K444 HDMI Matrix.
Each button corresponds to a specific input-to-output route command, allowing fast and direct switching from Input 1–4 to Output 1–4.

🔹 Input-to-Output Routing

Each entity below represents a one-touch command to route an input source to a specific output.

Input → Output	Entity Description
Input 1 → Output 1	PHD 4K444 Matrix
Input 1 → Output 2	PHD 4K444 Matrix
Input 1 → Output 3	PHD 4K444 Matrix
Input 1 → Output 4	PHD 4K444 Matrix
Input 2 → Output 1	PHD 4K444 Matrix
Input 2 → Output 2	PHD 4K444 Matrix
Input 2 → Output 3	PHD 4K444 Matrix
Input 2 → Output 4	PHD 4K444 Matrix
Input 3 → Output 1	PHD 4K444 Matrix
Input 3 → Output 2	PHD 4K444 Matrix
Input 3 → Output 3	PHD 4K444 Matrix
Input 3 → Output 4	PHD 4K444 Matrix
Input 4 → Output 1	PHD 4K444 Matrix
Input 4 → Output 2	PHD 4K444 Matrix
Input 4 → Output 3	PHD 4K444 Matrix
Input 4 → Output 4	PHD 4K444 Matrix
