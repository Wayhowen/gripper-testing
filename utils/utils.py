def input_getter(allowed_values, type_to_convert):
    try:
        result = type_to_convert(input())
    except ValueError:
        result = None
    if allowed_values:
        while result not in allowed_values:
            print("Wrong input provided, please try again")
            result = type_to_convert(input())
    return result
