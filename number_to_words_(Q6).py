
def number_to_words(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    thousands = ["", "thousand"]

    def get_words(num):
        if num == 0:
            return "zero"
        words = []
        if num >= 1000:
            words.append(ones[num // 1000] + " thousand")
            num %= 1000
        if num >= 100:
            words.append(ones[num // 100] + " hundred")
            num %= 100
        if num >= 20:
            words.append(tens[num // 10])
            num %= 10
        elif num >= 10:
            words.append(teens[num - 10])
            num = 0
        if num > 0:
            words.append(ones[num])
        return " ".join(words)

    total_letters = 0
    for i in range(1, n + 1):
        words = get_words(i)
        words = words.replace(" ", "").replace("-", "") 
        total_letters += len(words)
    return total_letters


print(number_to_words(1000))
