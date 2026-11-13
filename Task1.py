def calculate_bill(filename):
    total = 0.0
    report = []
    rejected = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Invalid fields")

                    amount = float(parts[2])
                    total += amount
                    report.append(parts[1] + " " + parts[2])

                except ValueError as e:
                    rejected.append((n, line.strip(), str(e)))

        print("Mess Bill Report")
        for item in report:
            print(item)

        print("Total:", total)
        print("Rejected Lines:", rejected)

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("Permission denied")


calculate_bill("mess_oct.txt")
