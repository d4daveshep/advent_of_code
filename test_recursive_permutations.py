import pytest

# Generate permutations using recursion
def generate(permutation:list, elements:list, positions:list):

    if len(permutation) == len(elements):

        for it in permutation:
            print(it, end=' ')
        print()

    else:

        for i in range(0, len(elements)):

            if positions[i]:
                continue

            # Set the position (taken), append the element
            positions[i] = True
            permutation.append(elements[i])

            generate(permutation, elements, positions)

            # Remove the element, reset the position (available),
            permutation.pop()
            positions[i] = False

def test_generate_permutations():
    elements = ["BB", "CC", "DD", "EE", "HH", "JJ"]
    permutation = []

    positions = [False] * len(elements)

    print("\nPermutations")
    generate(permutation, elements, positions)