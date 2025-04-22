def check_negative_numbers(numbers: list[str]) -> None:
    negative_numbers = []
    for number in numbers:
        if int(number) < 0:
            negative_numbers.append(number)

    if negative_numbers:
        raise Exception(f"negative numbers not allowed {','.join(negative_numbers)}")
