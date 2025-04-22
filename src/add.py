import re
from src.utils.delimiters import extract_delimter
from src.utils.check_negative_numbers import check_negative_numbers
from src.constants import DEFAULT_DELIMETER, GET_DELIMETER_REGEX


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = DEFAULT_DELIMETER

    if numbers.startswith("//"):
        inner_delimeter = extract_delimter(numbers)
        delimiter = delimiter + "|" + inner_delimeter
        match = re.match(GET_DELIMETER_REGEX, numbers)
        end_pos = match.end()
        numbers = numbers[end_pos:]

    numbers_list = re.split(rf"{delimiter}", numbers)
    check_negative_numbers(numbers_list)

    return sum(int(number) for number in numbers_list)
