def get_fibonacci_number(position):
    if position == 0:
        return 0
    if position == 1:
        return 1
    return get_fibonacci_number(position - 2) + get_fibonacci_number(position-1)


def get_fibonacci_number_sequence(number):
    # base case (ignoring the zero from sequence according to test cases)
    if number == 0:
        return
    if number == 1:
        return [1,1]
    # recursive calls
    sequence = get_fibonacci_number_sequence(number - 1)
    # adding previous two from the sequence
    sequence.append(sequence[-1] + sequence[len(sequence) - 2])
    # [:number] cuts off the extra appended number at the end
    return sequence[:number]


if __name__ == "__main__":
    n = 7
    print(get_fibonacci_number(n))
    print(get_fibonacci_number_sequence(n))