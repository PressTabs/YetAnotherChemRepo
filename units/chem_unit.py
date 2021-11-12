from unit import Unit
from metric_prefix import MetricPrefix


class ChemUnit:

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

    __slots__ = "_prefix", "_unit", "_abbr_representation", "_representation"

    def __init__(self, chem_unit: str):






    def __repr__(self) -> str:


