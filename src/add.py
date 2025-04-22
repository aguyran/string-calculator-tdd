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
    negative_numbers=[]
    for i in numbers_list:
        if int(i) < 0:
            negative_numbers.append(i)
    if negative_numbers:
        raise Exception(f"negative numbers not allowed {','.join(negative_numbers)}")
   
        
    return sum(int(number) for number in numbers_list)
