import re
from src.constants import GET_DELIMITIR_REGEX


def extract_delimter(numbers: str) -> str:
    return re.match(GET_DELIMITIR_REGEX, numbers).group(1)


def get_delimter_and_modified_string(
    numbers: str,
    delimiter: str,
) -> str:
    final_delimiter = delimiter
    if numbers.startswith("//"):
        inner_delimiter  = extract_delimter(numbers)
        final_delimiter = f"{delimiter}|{inner_delimiter }"
        match = re.match(GET_DELIMITIR_REGEX, numbers)
        end_pos = match.end()
        numbers = numbers[end_pos:]
    return final_delimiter, numbers
