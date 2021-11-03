from formulator import formulator
from periodic_table import periodic_table


def has_multiple_upper(string: str) -> bool:
    """Assumes string starts with an upper"""

    if len(string) <= 1:

        return False

    for char in string[1:]:

        if char.isupper():

            return True

    return False


def get_molar_mass(chemical: str, recursive: bool = False) -> tuple[float, str]:

    molar_mass: float = 0

    work: str = ""

    if not recursive:

        work += chemical + ":"

    composition: tuple[list[str], list[int], int] = formulator(chemical)

    elements: list[str] = composition[0]

    subscripts: list[int] = composition[1]

    for counter in range(len(elements)):

        element: str = elements[counter]

        subscript: int = subscripts[counter]

        if has_multiple_upper(element):

            constituent: tuple[float, str] = get_molar_mass(element, recursive=True)

            molar_mass += constituent[0] * subscript

            work += f" + ({constituent[1]}) * {subscript}"

            continue

        element_mass: float = periodic_table.get_atomic_mass(element)

        molar_mass += element_mass * subscript

        work += f" + {element_mass} * {subscript}"

    work = work[:len(chemical) + 1] + work[len(chemical) + 3:]

    if recursive:

        work = work[2:]

    return molar_mass, work
