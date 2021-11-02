import json

#   I did not create the PeriodicTableJSON.json file nor the periodic-table-lookup.json file.
#   Credit for those files is attributed to Bowserinator at
#   https://github.com/Bowserinator/Periodic-Table-JSON

#   Advanced type checking lol :>
#   p_table: dict[str, list[dict[str, str or int or float]]] = {}

with open("periodic-table-lookup.json", encoding="UTF-8") as file:

    p_lookup_table: dict[str, list[str] or dict[str, str or int or float]] = json.load(file)

abbr_lookup_table: dict[str, dict[str, str or int or float]] = {info["symbol"]: info for info in
                                                                list(p_lookup_table.values())[1:]}


def return_element_data(element: str) -> dict[str, str or int or float]:

    non_abbr_data: dict[str, str or int or float] or None = p_lookup_table.get(element)

    if non_abbr_data is not None:

        return non_abbr_data

    abbr_data: dict[str, str or int or float] = abbr_lookup_table.get(element)

    if abbr_data is not None:

        return abbr_data

    raise Exception("Invalid Element Inputted: " + element)


"""
def get_VALUE(element: str) -> TYPE:

    element_data: dict[str, str or int or float] = return_element_data(element)

    return element_data["VALUE"]
"""


def get_atomic_mass(element: str) -> float:

    element_data: dict[str, str or int or float] = return_element_data(element)

    return float(element_data["atomic_mass"])


def is_abbreviation(element: str) -> bool:

    if p_lookup_table.get(element) is not None:

        return False

    if abbr_lookup_table.get(element) is not None:

        return True

    raise Exception("Invalid Element Inputted: " + element)


def get_group(element: str) -> str:

    element_data: dict[str, str or int or float] = return_element_data(element)

    return element_data["category"]


def get_atomic_number(element: str) -> int:

    element_data: dict[str, str or int or float] = return_element_data(element)

    return element_data["number"]


def get_electron_config(element: str) -> tuple[str, str]:

    element_data: dict[str, str or int or float] = return_element_data(element)

    return element_data["electron_configuration"], element_data["electron_configuration_semantic"]
