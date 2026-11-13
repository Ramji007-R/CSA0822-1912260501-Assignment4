def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.readlines()

def valid_email(email):
    if " " in email:
        return False

    if email.count("@") != 1:
        return False

    name, domain = email.split("@")

    if not name or "." not in domain:
        return False

    if domain.startswith(".") or domain.endswith("."):
        return False

    return True


def validate_record(line):
    parts = line.strip().split(",")

    if len(parts) != 5:
        raise ValueError("Damaged record")

    if not valid_email(parts[3]):
        raise ValueError("Invalid email")

    return parts

from .validator import validate_record


def process_files(files):
    seen = set()
    master = []
    events = {}
    errors = []

    for filename in files:
        try:
            with open(filename, "r", encoding="utf-8") as f:

                for n, line in enumerate(f, 1):
                    try:
                        parts = validate_record(line)

                        reg, name, dept, email, event_data = parts

                        if reg in seen:
                            raise ValueError("Duplicate registration")

                        seen.add(reg)
                        master.append(line.strip())

                        for event in event_data.split(";"):
                            event = event.strip()

                            if event:
                                if event not in events:
                                    events[event] = []

                                events[event].append(
                                    reg + "," + name
                                )

                    except ValueError as e:
                        errors.append(
                            f"{filename}, Line {n}: {e}"
                        )

        except (FileNotFoundError, PermissionError) as e:
            errors.append(f"{filename}: {e}")

    return master, events, errors

def write_reports(master, events, errors):

    with open("master_list.txt", "w") as f:
        for record in master:
            f.write(record + "\n")

    for event, students in events.items():

        safe_name = "".join(
            c if c.isalnum() else "_" for c in event
        )

        with open(safe_name + ".txt", "w") as f:
            for student in students:
                f.write(student + "\n")

    with open("summary.txt", "w") as f:
        f.write("Total Registrations: " + str(len(master)) + "\n")
        f.write("Total Events: " + str(len(events)) + "\n")

        for event, students in events.items():
            f.write(event + ": " + str(len(students)) + "\n")

    with open("error_log.txt", "w") as f:
        for error in errors:
            f.write(error + "\n")

from .processor import process_files
from .report import write_reports


def main():

    files = [
        "department1.txt",
        "department2.txt",
        "department3.txt",
        "department4.txt",
        "department5.txt"
    ]

    master, events, errors = process_files(files)

    write_reports(master, events, errors)

    print("Processing completed successfully.")
    print("Total Registrations:", len(master))
    print("Total Errors:", len(errors))


if __name__ == "__main__":
    main()
