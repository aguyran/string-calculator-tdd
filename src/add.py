import re
from src.utils.delimiters import get_delimter_and_modified_string
from src.utils.check_negative_numbers import check_negative_numbers
from src.constants import DEFAULT_DELIMITIR


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = DEFAULT_DELIMITIR
    delimiter, new_numbers = get_delimter_and_modified_string(numbers, delimiter)
    numbers_list = re.split(rf"{delimiter}", new_numbers)
    check_negative_numbers(numbers_list)

    return sum(int(number) for number in numbers_list)
