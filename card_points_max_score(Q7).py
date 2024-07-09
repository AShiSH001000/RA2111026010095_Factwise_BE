
def max_score(cardPoints, k):
    n = len(cardPoints)
    total_sum = sum(cardPoints)
    if k >= n:
        return total_sum
    
    window_sum = sum(cardPoints[:n - k])
    min_window_sum = window_sum
    
    for i in range(n - k, n):
        window_sum += cardPoints[i] - cardPoints[i - (n - k)]
        min_window_sum = min(min_window_sum, window_sum)
    
    return total_sum - min_window_sum

def main():
    # Input cardPoints as a space-separated string of integers
    cardPoints_str = input("CardPoints separated by spaces: ")
    cardPoints = list(map(int, cardPoints_str.split()))
    
    # Input k as an integer
    k = int(input(" k: "))
    
    result = max_score(cardPoints, k)

    print(f"{result}")

if __name__ == "__main__":
    main()
