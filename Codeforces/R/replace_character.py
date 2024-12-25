from collections import Counter

t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())  # Convert string to list

    # Count frequencies of characters
    freq = Counter(s)

    # Find the least and most frequent characters
    low = min(range(n), key=lambda i: (freq[s[i]], s[i]))
    high = max(range(n), key=lambda i: (freq[s[i]], s[i]))

    # Replace least frequent character with most frequent character
    s[low] = s[high]

    # Print the modified string
    print("".join(s))