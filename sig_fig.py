class SigFig:
    __slots__ = "_value", "_num_of_sig_figs", "_sig_figs_start_index", "_crosses_decimal", "_decimal_index", "_negative"

    #   Accepting only str for value because float doesn't offer the same amount of precision
    def __init__(self, value: str):

        self._value = value

        sig_fig_parsed: tuple[int, int, bool, int, bool] = SigFig.parse_str(value)

        self._num_of_sig_figs = sig_fig_parsed[0]
        self._sig_figs_start_index = sig_fig_parsed[1]
        self._crosses_decimal = sig_fig_parsed[2]
        self._decimal_index = sig_fig_parsed[3]
        self._negative = sig_fig_parsed[4]

    def get_value(self) -> str:

        return self._value

    def get_num_of_sig_figs(self) -> int:

        return self._num_of_sig_figs

    def get_crosses_decimal(self) -> bool:

        return self._crosses_decimal

    def get_decimal_index(self) -> int:

        #   Will return -1 if decimal not found.
        return self._decimal_index

    @staticmethod
    def parse_str(value: str) -> tuple[int, int, bool, int, bool]:

        if len(value) == 0:
            raise Exception("Value is length 0")

        #   Because I'm bad at programming we're going to go with a simple scan approach.

        #   A decimal is fine here because due to the law of significant digits it's an absolute cheese.
        crosses_decimal: bool = False
        decimal_index: int = -1
        is_non_zero: list[int] = []
        is_negative: bool = False

        for index, char in enumerate(value):

            if char == ".":

                crosses_decimal = True
                decimal_index = index

            elif char == "-":

                is_negative = True

            elif char != "0":

                is_non_zero.append(index)

        is_non_zero.append(len(value) - 1)

        start_index: int = is_non_zero[0]

        num_sig_figs: int = is_non_zero[-1] - start_index + 1

        num_sig_figs -= int(start_index < decimal_index)

        return num_sig_figs, start_index, crosses_decimal, decimal_index, is_negative

    @staticmethod
    def add(base, other: float or str or int):

        if isinstance(other, int) or isinstance(other, float):
            return SigFig(f"{float(base.get_value) + other}")

        base_sig_fig: SigFig = base if isinstance(base, SigFig) else SigFig(base)
        other_sig_fig: SigFig = other if isinstance(other, SigFig) else SigFig(other)

        base_digits_right: int = len(base_sig_fig.get_value()) - base.get_decimal_index() - 1 if base.get_crosses_decimal else 0
        other_digits_right: int = len(other_sig_fig.get_value()) - other_sig_fig.get_decimal_index() - 1 if other_sig_fig.get_crosses_decimal else 0

        return SigFig(f"{round(float(base.get_value()) + float(other_sig_fig.get_value()), min(base_digits_right, other_digits_right))}")

    def __add__(self, other: float or str or int):

        return SigFig.add(self, other)

    def __radd__(self, other: float or str or int):

        return SigFig.add(self, other)

    @staticmethod
    def multiply(base, other: float or str or int):

        if isinstance(other, int) or isinstance(other, float):

            return SigFig(f"{float(base.get_value) * other}")

        base_sig_fig: SigFig = base if isinstance(base, SigFig) else SigFig(base)
        other_sig_fig: SigFig = other if isinstance(other, SigFig) else SigFig(other)

        #   Implement SigFig round function :>
        return SigFig(f"{float(base_sig_fig.get_value()) * float(other_sig_fig.get_value())}")
