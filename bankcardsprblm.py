def are_cards_equivalent(card1, card2):
    # Simulate the equivalence tester function
    # Replace this with the actual implementation of the equivalence tester
    # Return True if the cards are equivalent, False otherwise
    pass

def find_majority_element(cards):
    n = len(cards)

    # Base case: If there's only one card, return it as the majority element
    if n == 1:
        return cards[0]

    # Recursive case: Divide the cards into two halves
    mid = n // 2
    left_cards = cards[:mid]
    right_cards = cards[mid:]

    # Recursively find the majority elements in each half
    left_majority = find_majority_element(left_cards)
    right_majority = find_majority_element(right_cards)

    # Check if the majority element from the left half is the overall majority
    if are_cards_equivalent(left_majority, right_majority):
        return left_majority

    # Count the occurrences of the left and right majority elements
    left_majority_count = sum(1 for card in cards if are_cards_equivalent(card, left_majority))
    right_majority_count = sum(1 for card in cards if are_cards_equivalent(card, right_majority))

    # Return the majority element with the higher count
    if left_majority_count > n / 2:
        return left_majority
    elif right_majority_count > n / 2:
        return right_majority
    else:
        return None

def has_majority_set(cards):
    majority_element = find_majority_element(cards)
    if majority_element is not None:
        # Check if the majority element appears more than n/2 times
        majority_count = sum(1 for card in cards if are_cards_equivalent(card, majority_element))
        if majority_count > len(cards) / 2:
            return True
    return False

# Take input from the user
card_sequence = input("Enter the sequence of bank cards (space-separated): ")
cards = card_sequence.split()

if has_majority_set(cards):
    print("There is a set of more than n/2 equivalent bank cards.")
else:
    print("There is no set of more than n/2 equivalent bank cards.")

