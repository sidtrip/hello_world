def max_element(input_list):
    if len(input_list) == 1:
        return input_list[0]
    elif input_list[0] > max_element(input_list[1:]):
        return input_list[0]
    else:
        return max_element(input_list[1:])


