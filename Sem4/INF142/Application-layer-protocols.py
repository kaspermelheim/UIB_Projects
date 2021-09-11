"""
Protocol
=======

Order
----
Request message followed by a response

Format
----
String

Request:

Command[3] | Number | 
---------------------
Payload             |
---------------------

Response:

Code                | 
---------------------
Payload             |
---------------------

"""

import os

def get(file_number: int) -> str:
    with open(f"file{file_number}.txt", "r") as file:
        return file.read()

def put(file_number: int, text: str) -> None:
    with open(f"file{file_number}.txt", "w") as file:
        file.write(text)

def delete(file_number: int) -> None:
    os.remove(f"file{file_number}.txt")

command_to_method = {
    "GET" : get,
    "PUT" : put,
    "DEL" : delete
}

def on_receipt_reply(request: str) -> str:
    try:
        command = request[:3]
        index = request.index("\n")
        body = request[index+1:]
        number = int(request[3:index])
        method = command_to_method[command]
    except:
        return "400\nBad request"

    args = (number, body) if body else (number,)

    try:
        response = method(*args)
    except OSError as error:
        return "404\n" + error.strerror
        
    return "200\n" + (response if response else "")

if __name__ == "__main__":
    while text := input("> "):
        text += "\n"+input("> ")
        print("--- Response "+"-"*12)
        print(on_receipt_reply(text))
        print("-"*25)

