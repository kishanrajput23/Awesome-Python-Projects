values = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000 } #this dictionary contains roman number and their values in decimal

def RomanNumeralToDecimal(romanNumeral):
    sum = 0
    for i in range(len(romanNumeral) - 1):
        left_part = romanNumeral[i]
        right_part = romanNumeral[i + 1]
        if values[left_part] < values[right_part]:
            sum -= values[left_part]
        else:
            sum += values[left_part]
    sum += values[romanNumeral[-1]]
    return sum

s = input()
answer = RomanNumeralToDecimal(s)
print(answer)
