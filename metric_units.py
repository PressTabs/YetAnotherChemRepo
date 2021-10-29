
abbr_prefix: dict[str, float] = {
    "G": 1 * (10 ** 9),
    "M": 1 * (10 ** 6),
    "k": 1 * (10 ** 3),
    "h": 1 * (10 ** 2),
    "da": 1 * (10 ** 1),
    "": 1 * (10 ** 0),
    "d": 1 * (10 ** -1),
    "c": 1 * (10 ** -2),
    "m": 1 * (10 ** -3),
    "q": 1 * (10 ** -6),  # Micro
    "n": 1 * (10 ** - 9)
}

#   When generating table will list this as True (i.e the default standard)
#   Too lazy to code the non-abbreviated units today so we use this for now.
abbr_unit: dict[str, int] = {
    "mol": 0,
    "g": 1,
    "L": 2,
    "C": 3,
    "K": 4,
    "atm": 5,
    "torr": 6
}
