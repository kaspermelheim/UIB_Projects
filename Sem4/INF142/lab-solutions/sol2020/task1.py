
# Hint on making sure that the a message can be split into strings
# Assume a method EAT with argument food with values SALMON and RISE

if __name__ == "__main__":

    # Alternative 1: Use abbreviations and make sure the methods have the same length,
    # for instance 3.

    message = "EATSALMON"
    method = message[:3]
    value = message[3:]

    print(f"Method: {method}\nArgument value: {value}")

    # Alternative 2: Separate methods and argument values by a space and
    # then use split().

    message = "EAT SALMON"
    method, value = message.split()

    print(f"Method: {method}\nArgument value: {value}")

    # Alternative 3: Separate methods and argument values by a <LF>
    # then use splitlines().

    message = "EAT\nRISE"
    method, value = message.splitlines()

    print(f"Method: {method}\nArgument value: {value}")


##################################################
#################### Solution ####################
##################################################

# Methods
# =======
# GETLAN: get the list of available languages
# SETLAN: set the language
# GETNUM: get the numeral of a given number
# Format
# ======
# METHODVAL

resp = {
    "GETLAN": "ESP;NOR;ENG",
    "SETLANESP": "OK",
    "GETNUM5": "cinco"
}
