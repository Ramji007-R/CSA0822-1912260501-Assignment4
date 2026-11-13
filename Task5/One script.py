def read_file(filename):
    with open(filename, "r") as f:
        return f.readlines()


def percentage(present, total):
    if total == 0:
        return 0
    return (present / total) * 100


def write_report(filename, data):
    with open(filename, "w") as f:
        f.write(data)


def consecutive_absences(records):
    result = []

    for reg, status in records.items():
        for i in range(len(status) - 2):
            if status[i:i+3] == ["A", "A", "A"]:
                result.append(reg)
                break

    return result


if __name__ == "__main__":
    print("Attendance Module")
    print("Percentage:", percentage(20, 25))
