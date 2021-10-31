from unit import Unit

#   Won't support abbreviations for now cus I'm cool

#   Exponential notation, i.e 10 ^ n where n is the value from the key ("" wont be included)
prefixes: dict[str, int] = {
    "kilo": 3,
    "hecto": 2,
    "deca": 1,
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

#   ^^^ These are the only dictionaries that need to be edited

#   This block of code will run on import so that the unit_breakup works efficiently. And some this only needs to be
#   done once per run it's overall a benefit given a large enough dataset, plus it makes the algorithm easier to
#   read

prefix_lengths: list[int] = [len(prefix) for prefix in prefixes]
unit_lengths: list[int] = [len(unit) for unit in units]

unique_prefix_lengths: list[int] = [length for counter, length in enumerate(prefix_lengths) if length not in prefix_lengths[:counter]]
unique_unit_lengths: list[int] = [length for counter, length in enumerate(unit_lengths) if length not in unit_lengths[:counter]]

unique_prefix_lengths.sort()
unique_unit_lengths.sort()

unique_prefix_lengths.reverse()
unique_unit_lengths.reverse()


def unit_breakup(metric_unit: str) -> tuple[str, str]:
    """Breaks up a prefix and a unit into the prefix and unit individually"""

    prefix: str = ""

    length: int = len(metric_unit)

    for prefix_length in unique_prefix_lengths:

        if length > prefix_length - 1:

            possible_prefix: str = metric_unit[0:prefix_length]

            if prefixes.get(possible_prefix) is not None:

                prefix = possible_prefix
                break

    prefix_length: int = len(prefix)

    for unit_length in unique_unit_lengths:

        if length > unit_length - 1:

            possible_unit: str = metric_unit[prefix_length:length]

            if units.get(possible_unit) is not None:

                return prefix, possible_unit

    raise Exception("Unit Not In Accepted " + metric_unit)
