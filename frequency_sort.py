def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    limited = [[i, 0] for i in range(0, 53)]
    for c in s:
        if c == " ":
            limited[52][1] += 1
        elif c.isupper():
            limited[26 + ord(c) - ord('A')][1] += 1
        else:
            limited[ord(c) - ord('a')][1] += 1

    limited.sort(reverse=True, key=lambda x: x[1])
    return "".join([chr(ord('a') + c)*v if c<=25 else chr(ord('A') + c - 26)*v if c<52 else " " for c, v in limited])


print(frequencySort("  he"))
