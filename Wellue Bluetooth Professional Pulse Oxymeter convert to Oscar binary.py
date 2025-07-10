#!/usr/bin/env python3
# script for WellueFS20F-2021 Wellue Bluetooth Professional Pulse Oxymeter
# Export SPO session data as .csv from ViHealth on mobile
# Convert with this script
# In Oscar, select Data -> Import (F7) -> import from a file -> select the .dat file output of this script

import csv
from datetime import datetime, timedelta
import sys

# Time format from CSV
TIME_FORMAT = "%H:%M:%S %b %d %Y"

def convert_to_oscar_dat(csv_filename, output_filename=None):
    with open(csv_filename, newline='') as f:
        reader = csv.DictReader(f)
        records = []

        for row in reader:
            try:
                time = datetime.strptime(row['Time'], TIME_FORMAT)
                spo2 = int(row['Oxygen Level'])
                pulse = int(row['Pulse Rate'])
                records.append((time, spo2, pulse))
            except Exception as e:
                print(f"Skipping invalid row: {row} — {e}")

    if not records:
        print("No valid data found.")
        return

    # Sort records just in case
    records.sort(key=lambda r: r[0])

    start_time = records[0][0]
    duration_seconds = len(records)

    # Set output filename if not provided
    if not output_filename:
        output_filename = f"oscar_oxy_{start_time.strftime('%Y%m%d_%H%M%S')}.dat"

    print(f"Writing to: {output_filename} ({duration_seconds} seconds)")

    with open(output_filename, "wb") as out:
        # Header
        out.write(b'\x00')  # ID
        out.write(duration_seconds.to_bytes(2, byteorder='little', signed=False))

        # Each second's data
        for time, spo2, pulse in records:
            out.write(b'\x00\x00\x00')  # Unknown ID fields

            out.write((time.year - 2000).to_bytes(1, 'little'))
            out.write(time.month.to_bytes(1, 'little'))
            out.write(time.day.to_bytes(1, 'little'))
            out.write(time.hour.to_bytes(1, 'little'))
            out.write(time.minute.to_bytes(1, 'little'))
            out.write(time.second.to_bytes(1, 'little'))

            out.write(spo2.to_bytes(1, 'little'))
            out.write(pulse.to_bytes(1, 'little'))

    print("Conversion complete.")

# ----------- MAIN -----------

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python csv_to_oscar_dat.py <input.csv> [output.dat]")
        sys.exit(1)

    input_csv = sys.argv[1]
    output_dat = sys.argv[2] if len(sys.argv) > 2 else None

    # input_csv = "FS20F_20250701204630.csv"
    # output_dat = "Wellue Bluetooth Professional.dat"

    convert_to_oscar_dat(input_csv, output_dat)
