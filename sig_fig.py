
class SigFig:

    __slots__ = "_value", "_num_of_sig_figs", "_sig_figs_start_index", "_crosses_decimal", "_decimal_index"

    #   Accepting only str for value because float doesn't offer the same amount of precision
    def __init__(self, value: str):

        self._value = value

        sig_fig_parsed: tuple[int, int, bool, int] = SigFig.parse_str(value)

        self._num_of_sig_figs = sig_fig_parsed[0]
        self._sig_figs_start_index = sig_fig_parsed[1]
        self._crosses_decimal = sig_fig_parsed[2]
        self._decimal_index = sig_fig_parsed[3]

    @staticmethod
    def parse_str(value: str) -> tuple[int, int, bool, int]:

        if len(value) == 0:

            raise Exception("Value is length 0")

        #   Because I'm bad at programming we're going to go with a simple scan approach.

        #   A decimal is fine here because due to the law of significant digits it's an absolute cheese.
        crosses_decimal: bool = False
        decimal_index: int = -1
        is_non_zero: list[int] = []

        for index, char in enumerate(value):

            if char == ".":

                crosses_decimal = True
                decimal_index = index

            elif char != "0":

                is_non_zero.append(index)

        is_non_zero.append(len(value) - 1)

        start_index: int = is_non_zero[0]

        num_sig_figs: int = is_non_zero[-1] - start_index + 1

        num_sig_figs -= int(start_index < decimal_index)

        return num_sig_figs, start_index, crosses_decimal, decimal_index
