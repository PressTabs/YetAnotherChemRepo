def formulator(formula: str) -> tuple[list[str], list[int], int]:
    """Takes a chemical formula and turns it in a better notation for computer processing"""
    element_list: list[str] = []
    subscript_list: list[int] = []
    charge: int = 0

    polyatomic_started: bool = False
    element_started: bool = False

    element: str = ""

    #   Storing subscript as an string so it can easily be concatenated unlike an int

    subscript: str = ""

    #   Going for a pure interpreter style so won't use .split() to obtain the charge, using if check instead
    for char in formula:

        if polyatomic_started:

            if char == ")":

                polyatomic_started = False
                continue

            element += char

        elif char.isalpha():

            if char.isupper() and element != "":

                #   Same code 1, recode with function
                element_list.append(element)
                element = ""

                if subscript == "":
                    subscript_list.append(1)

                else:

                    subscript_list.append(int(subscript))
                    subscript = ""

            element += char

        elif char.isdigit():

            subscript += char

        elif char == "(":

            polyatomic_started = True

            if element != "":

                # Same code 1, recode with function
                element_list.append(element)
                element = ""

                if subscript == "":
                    subscript_list.append(1)

                else:

                    subscript_list.append(int(subscript))
                    subscript = ""

    if element != "":

        element_list.append(element)

    if subscript == "":

        subscript_list.append(1)

    else:

        subscript_list.append(int(subscript))

        #   Implement charge here

    return element_list, subscript_list, charge
