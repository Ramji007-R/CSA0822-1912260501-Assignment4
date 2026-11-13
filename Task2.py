from pathlib import Path

attendance = {}
errors = []

files = list(Path(".").glob("attendance_*.txt"))

for file in files:
    try:
        with open(file, "r", encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid fields")

                    reg, date, status = parts

                    if status not in ("P", "A"):
                        raise ValueError("Invalid status")

                    if reg not in attendance:
                        attendance[reg] = [0, 0]

                    if status == "P":
                        attendance[reg][0] += 1
                    else:
                        attendance[reg][1] += 1

                except ValueError as e:
                    errors.append(f"{file}, Line {n}: {e}")

    except (FileNotFoundError, PermissionError) as e:
        errors.append(f"{file}: {e}")

with open("attendance_report.txt", "w") as f:
    for reg, counts in attendance.items():
        total = sum(counts)
        percentage = counts[0] / total * 100
        f.write(f"{reg}: {percentage:.2f}%\n")

with open("low_attendance.txt", "w") as f:
    for reg, counts in attendance.items():
        total = sum(counts)
        percentage = counts[0] / total * 100

        if percentage < 75:
            f.write(f"{reg}: {percentage:.2f}%\n")

with open("error_log.txt", "w") as f:
    for error in errors:
        f.write(error + "\n")

print("Attendance processing completed.")
