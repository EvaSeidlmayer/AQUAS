




def average_text_length(strings):
    # Step 1: Compute the length of each string
    lengths = [len(string) for string in strings]

    # Step 2: Sum all the lengths
    total_length = sum(lengths)

    # Step 3: Divide the total length by the number of strings
    if len(strings) == 0:
        return 0  # To handle division by zero if the list is empty
    average_length = total_length / len(strings)

    return average_length


# Example usage:
strings = ["hello", "world", "Python", "is", "great"]
print(average_text_length(strings))  # Output: 4.8
