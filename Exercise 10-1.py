def nested_sum(input_nested):
    element_sum = 0
    for element in input_nested:
        element_sum += sum(element)

    print(element_sum)



nested_sum([[2], [1, 2]])