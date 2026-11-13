def save_returns(books):
    with open("returns.log", "a", encoding="utf-8") as log:
        for book in books:
            log.write(book.strip() + "\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as f:
            books = f.readlines()

        save_returns(books)

    except FileNotFoundError:
        with open("error.log", "a") as error:
            error.write("Missing file: " + day_file + "\n")

    except PermissionError:
        with open("error.log", "a") as error:
            error.write("Permission denied: " + day_file + "\n")


process("day1.txt")
process("day2.txt")
process("day3.txt")

with open("returns.log", "r") as f:
    print(f.read())
