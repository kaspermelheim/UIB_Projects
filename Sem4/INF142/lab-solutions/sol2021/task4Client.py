from socket import socket


def request_to_server(sock: socket, message: str) -> str:
    sock.sendall(message.encode())
    resp = sock.recv(1024)
    return resp.decode()


def numeral(sock):
    while (digit := input("numeral> ")).isdigit():
        if len(digit) > 1:
            print("Only digits are supported")
        else:
            print(request_to_server(sock, f"getnumber {digit}"))


def language(sock):
    languages = request_to_server(sock, f"getlanguage").split(";")
    print("Available languages:")
    for l in languages:
        print(l)
    while (l := input("language> ").upper()) not in languages:
        print(f"Language {l} is not available")
    request_to_server(sock, f"setlanguage {l}")


if __name__ == "__main__":

    sock = socket()
    sock_address = ("localhost", 12000)
    sock.connect(sock_address)

    print("Available commands are:\n language\n numeral")
    print("Press Enter to exit")
    while (command := input("command> ").lower()):
        if command == "numeral":
            numeral(sock)
        elif command == "language":
            language(sock)
        else:
            print("Invalid command")
