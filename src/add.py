import re


def add(numbers: str) -> int:
    if numbers == "":
        return 0
    delimiter = "\\n|,|\n"
    if numbers.startswith("//"):
        inner_delimiter = re.match(r"//([\s\S]*)[\n|\\n]", numbers).group(1)
        delimiter = delimiter + "|" + inner_delimiter
        
        match = re.match(r"//(.*)\n", numbers)
        end_pos = match.end()
        numbers = numbers[end_pos:]
    numbers_list = re.split(rf"{delimiter}", numbers)
    return sum(int(number) for number in numbers_list)
