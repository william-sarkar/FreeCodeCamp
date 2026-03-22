def verify_card_number(cardNumber):
    cardNumber = cardNumber.replace("-", "")
    cardNumber = cardNumber.replace(" ", "")
    sumOfRegular = 0
    sumOfDouble = 0
    for i in range(len(cardNumber)-2, -1, -2):
        double = int(cardNumber[i]) * 2
        if double > 9:
            double -= 9
        sumOfDouble += double
    for i in range(len(cardNumber)-1, -1, -2):
        sumOfRegular += int(cardNumber[i])
    totalSum = sumOfDouble + sumOfRegular
    if totalSum % 10 != 0:
        return "INVALID!"
    return "VALID!"

def verify_card_number2(cardNumber: str) -> str:
    # Step 1: Remove spaces and dashes
    cardNumber = cardNumber.replace("-", "").replace(" ", "")
    
    # Step 2: Initialize sums
    totalSum = 0
    n = len(cardNumber)
    
    # Step 3: Traverse digits from right to left
    for i in range(n - 1, -1, -1):
        digit = int(cardNumber[i])
        
        # Double every second digit (excluding check digit at far right)
        if (n - i) % 2 == 0:  # even position from the right
            digit *= 2
            if digit > 9:
                digit -= 9
        
        totalSum += digit
    
    # Step 4: Check validity
    return "VALID!" if totalSum % 10 == 0 else "INVALID!"

# print(verify_card_number("1234 5678 9012 3456"))
