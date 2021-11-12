
class SigFig:

    __slots__ = "_value", "_num_of_sig_figs", "_sig_figs_start_index"

    def __init__(self, value: float or str):

        self._value: float = float(value)

        number: str = str(value)

        crosses_decimal: bool = False

        for char_index in range(len(number)):

            char: str = number[char_index]

            if char is not "0":

                self._sig_figs_start_index = char_index
                break

        end_index: int = len(number) - 1

        while end_index > self._sig_figs_start_index:

            char: str = number[end_index]

            if char is ".":

                crosses_decimal = True

            elif char is not "0":

                break

            end_index -= 1

        self._num_of_sig_figs = end_index - self._sig_figs_start_index + 1 - int(crosses_decimal)

    def set_num_of_sig_figs(self, num: int) -> None:

        self._num_of_sig_figs = num

    def __add__(self, other):

        if not isinstance(other, SigFig) and type(other) is str or float:

            other_num: SigFig = SigFig(other)




