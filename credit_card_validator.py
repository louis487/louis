def validate_credit_card(card_number):
    # Remove spaces and dashes
    card_number = card_number.replace(' ', '').replace('-', '')

    # Check if the card number is all digits
    if not card_number.isdigit():
        return False

    # Implementing Luhn algorithm
    total = 0
    reverse_card_number = card_number[::-1]

    for i, digit in enumerate(reverse_card_number):
        n = int(digit)
        if i % 2 == 1:
            n *= 2
            if n > 9:
                n -= 9
        total += n

    return total % 10 == 0

# Example usage:
if __name__ == '__main__':
    card = '4539 1488 0343 6467'
    if validate_credit_card(card):
        print('Valid credit card number')
    else:
        print('Invalid credit card number')