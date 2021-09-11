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

    input_ = request.split()
    method = input_[0]
    value = input_[1] if len(input_) > 1 else None

    if method == "getnumber":
        return numerals.get(language)[int(value)]
    elif method == "getlanguage":
        return ";".join(numerals)
    elif method == "setlanguage":
        if value in numerals:
            language = value
            return "OK"
        else:
            return "OOOOOOF"
    else:
        return "unknown command"


if __name__ == "__main__":

    # Testing
    for key in resp:
        assert resp[key] == response(key)
