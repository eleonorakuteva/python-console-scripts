def generate_vector_with_given_length(length: int) -> list:
    return [None] * length

def generate01(idx, vector):
    if idx == len(vector):
        print(*vector, sep='')
        return
    for bit in range(2):
        vector[idx] = bit
        generate01(idx + 1, vector)


print("Generating all 0/1 combinations in given vector.")
len_vector = int(input("Enter the length of the vector: "))
curr_vector = generate_vector_with_given_length(len_vector)
generate01(0, curr_vector)


# print("\n", "Generating all 0/1 combinations in one byte:")
# EMPTY_BYTE = generate_vector_with_given_length(8)
# generate01(0, EMPTY_BYTE)