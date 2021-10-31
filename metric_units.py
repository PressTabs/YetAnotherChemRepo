from unit import Unit

#   Won't support abbreviations for now cus I'm cool

#   Exponential notation, i.e 10 ^ n where n is the value from the key
prefixes: dict[str, int] = {
    "kilo": 3,
    "hecto": 2,
    "deca": 1,
    "": 0,
    "deci": -1,
    "centi": -2,
    "milli": -3
}

units: dict[str, Unit] = {
    "mole": Unit.MOLE,
    "gram": Unit.GRAM,
    "atom": Unit.ATOM,
    "liter": Unit.LITER,
    "joule": Unit.JOULE,
    "kelvin": Unit.KELVIN,
    "celsius": Unit.CELSIUS,
    "particle": Unit.PARTICLE,
    "molecule": Unit.MOLECULE,
    "atmosphere": Unit.ATMOSPHERE,
    "torricelli": Unit.TORRICELLI
}


def unit_breakup(metric_unit: str) -> tuple[str, str]:
    """Breaks up a prefix and a unit into the prefix and unit individually"""

    prefix: str = ""

    #   Kilo, Hecto, Deca, Base, Deci, Centi, Milli
    #   4,      5,      4,  0,      4,  5,      5

    length: int = len(metric_unit)

    if length > 4:

        if metric_unit[0:5] == "milli":
            prefix = "milli"

        elif metric_unit[0:5] == "centi":
            prefix = "centi"

        elif metric_unit[0:5] == "hecto":
            prefix = "hecto"

    if length > 3:

        if metric_unit[0:4] == "kilo":
            prefix = "kilo"

        elif metric_unit[0:4] == "deca":
            prefix = "deca"

        elif metric_unit[0:4] == "deci":
            prefix = "deci"

    prefix_length: int = len(prefix)

    unit: str = ""

    unit_length: int = length - prefix_length

    #   Gram, Mole, Atmosphere, Liter, Kelvin, Celsius, Torricelli, Atom, Molecule, Particle, Joule
    #   4,      4,      10,     5,      6,      7,      10,         4,      8,      8           5

    if unit_length > 9:

        if metric_unit[prefix_length:prefix_length+10] == "atmosphere":
            unit = "atmosphere"

        elif metric_unit[prefix_length:prefix_length+10] == "torricelli":
            unit = "torricelli"

    if unit_length > 7:

        if metric_unit[prefix_length:prefix_length+8] == "molecule":
            unit = "molecule"

        elif metric_unit[prefix_length:prefix_length+8] == "particle":
            unit = "particle"

    if unit_length > 6:

        if metric_unit[prefix_length:prefix_length+7] == "celsius":
            unit = "celsius"

    if unit_length > 5:

        if metric_unit[prefix_length:prefix_length+6] == "kelvin":
            unit = "kelvin"

    if unit_length > 4:

        if metric_unit[prefix_length:prefix_length+5] == "liter":
            unit = "liter"

        elif metric_unit[prefix_length:prefix_length+5] == "joule":
            unit = "joule"

    if unit_length > 3:

        if metric_unit[prefix_length:prefix_length+4] == "gram":
            unit = "gram"

        elif metric_unit[prefix_length:prefix_length+4] == "mole":
            unit = "mole"

        elif metric_unit[prefix_length:prefix_length+4] == "atom":
            unit = "atom"

    #   I could've wrote all of this procedurally with a list instead. I'll recode it when I add a new unit.
    #   Yeah this needs a quick recode, it's much slower without a for loop break because of all the copy-pasted
    #   code and all the unnecessary if checks

    if unit == "":
        raise Exception("Unit Not In Accepted " + metric_unit)

    return prefix, unit
