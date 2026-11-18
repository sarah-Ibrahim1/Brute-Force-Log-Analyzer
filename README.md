# Brute Force Log Analyzer

A Python-based security log analysis tool that detects potential brute-force login attempts by identifying suspicious IP addresses based on failed authentication events.

## Overview

This project analyzes authentication logs stored in a CSV file to identify potential brute-force activity.

The analyzer filters failed login events, groups them by source IP address, and examines timestamps using a sliding time window.

An IP address is flagged as suspicious when it generates **6 or more failed login attempts within 60 seconds**.

## Features

- CSV-based security log analysis.
- Detection of failed login attempts using Windows Event ID `4625`.
- Grouping authentication events by source IP address.
- Timestamp conversion and time-based analysis.
- Sliding 60-second detection window.
- Identification of suspicious IP addresses.
- Clear detection results showing the number of attempts within the detection window.

## Technologies Used

- **Python 3**
- CSV module
- datetime module
- collections module (`defaultdict`)

## Project Structure

```text
Brute-Force-Log-Analyzer/
│
├── analyzer.py
├── security_logs.csv
└── README.md
```

## Detection Logic

The analyzer follows these steps:

1. Reads authentication records from the CSV file.
2. Filters failed login events using Event ID `4625`.
3. Groups failed login timestamps by source IP address.
4. Sorts timestamps chronologically.
5. Checks failed login attempts within consecutive 60-second windows.
6. Flags IP addresses with 6 or more failed attempts within the detection window.

### Detection Threshold

| Parameter | Value |
|---|---|
| Event ID | 4625 |
| Failed login threshold | 6 attempts |
| Time window | 60 seconds |
| Detection output | Suspicious IP address |

## Dataset

The project uses a CSV dataset containing **3,921 authentication log records**.

The dataset includes the following fields:

| Field | Description |
|---|---|
| `timestamp` | Date and time of the authentication event |
| `source_ip` | IP address generating the event |
| `username` | Account associated with the event |
| `event_id` | Windows authentication event ID |
| `status` | Authentication result (Failed or Success) |




