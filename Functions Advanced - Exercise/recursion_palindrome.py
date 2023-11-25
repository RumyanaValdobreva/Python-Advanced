def palindrome(word, index=0):
    if index >= len(word) // 2:
        return f"{''.join(word)} is a palindrome"

    start = word[index]
    end = word[-1 - index]

    if not start == end:
        return f"{''.join(word)} is not a palindrome"
    return palindrome(word, index + 1)


print(palindrome("abcba", 0))