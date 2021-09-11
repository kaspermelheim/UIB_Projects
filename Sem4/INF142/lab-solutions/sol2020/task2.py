from task1 import resp


numerals = {
    "ESP": ["cero", "uno", "dos", "tres", "cuatro", "cinco",
            "seis", "siete", "ocho", "nueve"],
    "NOR": ["nul", "en", "to", "tre", "fire", "fem",
            "seks", "sju", "åtte", "ni"],
    "ENG": ["zero", "one", "two", "three", "four", "five",
            "six", "seven", "eight", "nine"]
}
language = "ENG"


def response(request: str) -> str:
    global language
    method = request[:6]
    if method == "GETLAN":
        return ";".join(numerals)
    elif method == "SETLAN":
        language = request[6:]
        return "OK"
    elif method == "GETNUM":
        return numerals[language][int(request[6:])]
    else:
        return "BAD REQUEST"


if __name__ == "__main__":

    # Testing
    for key in resp:
        assert resp[key] == response(key)
