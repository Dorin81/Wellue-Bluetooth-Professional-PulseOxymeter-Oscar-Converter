# Wellue-Bluetooth-Professional-PulseOxymeter-Oscar-Converter

This project is a Python script that converts the CSV export from the Wellue Bluetooth Professional Pulse Oxymeter into a binary format accepted by the open-source software Oscar, which is used for CPAP devices. The script allows users to overlay pulse and blood oxygen data with the Resmed Airsense 10 data, providing a comprehensive view of the blood oxygen and pulse during CPAP therapy.

### Main Function Points
- Converts the CSV export from the Wellue Bluetooth Professional Pulse Oxymeter into a binary format accepted by Oscar
- Allows users to overlay pulse and blood oxygen data with the Resmed Airsense 10 data

### Procedure to convert and import data into OSCAR
Export SPO session data as .csv from ViHealth on mobile
Convert with this script
In Oscar, select Data -> Import (F7) -> import from a file -> select the .dat file output of this script

### Technology Stack
- Python

### License
GPL-3.0 license

