# Brute Force Log Analyzer

A Python-based security log analysis tool that detects potential brute-force login attempts by identifying suspicious IP addresses based on failed authentication events.

## Overview

The analyzer reads a CSV file, identifies failed login events (Windows Event ID `4625`), and groups them by source IP address. An IP is flagged as suspicious if it generates **6 or more failed login attempts within 60 seconds**.

## Features

- Reads authentication logs from a CSV file.
- Filters failed login events.
- Groups attempts by source IP address.
- Uses a sliding time window to detect suspicious activity.
- Displays suspicious IP addresses and their attempt counts.

## Technologies Used

- Python 3
- CSV
- datetime
- collections (`defaultdict`)

## Project Structure

```text
Brute-Force-Log-Analyzer/
│
├── analyzer.py
├── security_logs.csv
└── README.md
```

## Detection Settings

| Parameter | Value |
|---|---|
| Event ID | `4625` |
| Failed login threshold | 6 attempts |
| Time window | 60 seconds |

## Dataset

The project uses a CSV dataset containing **3,921 authentication records** with the following fields:

| Field | Description |
|---|---|
| `timestamp` | Date and time of the event |
| `source_ip` | Source IP address |
| `username` | Username used |
| `event_id` | Windows authentication event ID |
| `status` | Authentication result (Failed or Success) |
