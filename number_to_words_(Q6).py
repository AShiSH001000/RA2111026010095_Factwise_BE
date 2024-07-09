def number_letter_counts():
    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    hundred = "hundred"
    thousand = "thousand"
    
    and_word = "and"
    
    def letter_count(n):
        if n == 0:
            return 0
        if n < 10:
            return len(units[n])
        elif 10 < n < 20:
            return len(teens[n-10])
        elif n == 10 or n >= 20 and n < 100:
            return len(tens[n // 10]) + len(units[n % 10])
        elif n < 1000:
            count = len(units[n // 100]) + len(hundred)
            if n % 100 != 0:
                count += len(and_word) + letter_count(n % 100)
            return count
        elif n == 1000:
            return len(units[1]) + len(thousand)
        return 0

    total_count = 0
    for i in range(1, 1001):
        total_count += letter_count(i)
    
    return total_count

number_letter_counts()
