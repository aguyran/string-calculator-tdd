import re
from src.constants import GET_DELIMETER_REGEX

def extract_delimter(numbers: str) -> str:
    return re.match(GET_DELIMETER_REGEX, numbers).group(1)

def get_delimter(numbers: str) -> str:
    if numbers.startswith("//"):
        return extract_delimter(numbers)
