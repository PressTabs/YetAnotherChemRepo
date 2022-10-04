from formulator import formulator
from periodic_table import periodic_table
from units.unit import Unit


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

    if recursive:

        pass
        work = work[3:]

    if not recursive:

        work = work[:len(chemical) + 1] + work[len(chemical) + 3:] + f" = {molar_mass}"

    return molar_mass, work


def basic_conversion(amount: float, substance: str, from_unit: Unit, to_unit: Unit) -> tuple[float, str]:

    if not ((from_unit is Unit.GRAM or Unit.ATOM or Unit.MOLECULE or Unit.PARTICLE or Unit.MOLE) and (to_unit is Unit.GRAM or Unit.ATOM or Unit.MOLECULE or Unit.PARTICLE or Unit.MOLE)):

        raise Exception("Unit Not Excepted " + str(from_unit) + " " + str(to_unit))

    work: str = ""

    if from_unit is to_unit:

        return amount, work

    to_amount: float = amount

    work += f"({amount} {from_unit.name} {substance})"

    if from_unit is not Unit.MOLE:

        if from_unit is Unit.ATOM or Unit.MOLECULE or Unit.PARTICLE:

            work += f"(1 mole {substance} / 6.022 * 10 ^ 23 {from_unit.name} {substance})"

            to_amount *= 1 / (6.022 * (10 ** 23))

        else:

            molar_mass: tuple[float, str] = get_molar_mass(substance)

            work += f"(1 mole {substance} / {molar_mass[0]} {from_unit.name} {substance})"

            to_amount *= 1 / molar_mass[0]

    if to_unit is not Unit.MOLE:

        if to_unit is Unit.ATOM or Unit.MOLECULE or Unit.PARTICLE:

            work += f"(6.022 * 10 ^ 23 {to_unit.name} {substance} / 1 mole {substance})"

            to_amount *= 6.022 * (10 ** 23)

        else:

            molar_mass: tuple[float, str] = get_molar_mass(substance)

            work += f"({molar_mass[0]} {to_unit.name} {substance} / 1 mole {substance}"

            to_amount *= molar_mass[0]

    return amount, work




