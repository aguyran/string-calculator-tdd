import re
def add(numbers: str) -> int:
    if numbers == "":
        return 0
    numbers_list = re.split(r"\\n|,|\n",numbers )
    return sum(int(number) for number in numbers_list)
