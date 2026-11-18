
import csv
from datetime import datetime
from collections import defaultdict

log_file = "data/security_logs.csv"
failed_logins = defaultdict(list)

with open(log_file, "r", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["event_id"] == "4625":
            ip = row["source_ip"]
            time = datetime.strptime(
                row["timestamp"], "%Y-%m-%d %H:%M:%S"
            )
            failed_logins[ip].append(time)

print("SUSPICIOUS IP ADDRESSES")
print("=" * 45)

for ip, times in failed_logins.items():
    times.sort()
    max_attempts = 0

    for i in range(len(times)):
        attempts = 0

        for j in range(i, len(times)):
            if (times[j] - times[i]).total_seconds() <= 60:
                attempts += 1
            else:
                break

        max_attempts = max(max_attempts, attempts)

    if max_attempts >= 6:
        print(f"Suspicious IP: {ip}")
        print(f"Attempts in 60s: {max_attempts}")
        print("-" * 35)
