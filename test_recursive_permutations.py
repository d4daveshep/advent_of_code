from dataclasses import dataclass


# Generate permutations using recursion
@dataclass
class State:
    permutation: list
    current_flow: int
    cumulative_flow: int
    mins_remaining: int


def generate(permutation: list, elements: list, positions: list, state: State):
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

            #  check state here ?

            generate(permutation, elements, positions, state)

            # Remove the element, reset the position (available),
            permutation.pop()
            positions[i] = False


def test_generate_permutations():
    elements = ["AA", "BB", "CC", "DD", "EE", "HH", "JJ"]
    permutation = ["AA"]

    positions = [False] * len(elements)
    positions[0] = True

    state = State(permutation, 0, 0, 30)

    print("\nPermutations")
    generate(permutation, elements, positions, state)
