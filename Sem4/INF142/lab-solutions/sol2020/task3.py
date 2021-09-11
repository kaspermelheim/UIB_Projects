from task2 import response


def numeral():
    while (digit := input("numeral> ")).isdigit():
        if len(digit) > 1:
            print("Only digits are supported")
        else:
            print(response(f"GETNUM{digit}"))


def language():
    languages = response("GETLAN").split(";")
    print("Available languages:")
    for l in languages:
        print(l)
    while (l := input("language> ").upper()) not in languages:
        print(f"Language {l} is not available")
    response(f"SETLAN{l}")


if __name__ == "__main__":

    print("Available commands are:\n language\n numeral")
    print("Press Enter to exit")
    while (command := input("command> ").lower()):
        if command == "numeral":
            numeral()
        elif command == "language":
            language()
        else:
            print("Invalid command")
