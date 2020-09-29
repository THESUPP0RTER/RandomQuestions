def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    mapping = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
    }
    result, i = 0, 0
    while i < (len(s) - 1):
        if mapping[s[i + 1]] > mapping[s[i]]:
            result += (mapping[s[i + 1]] - mapping[s[i]])
            i += 2
        else:
            result += mapping[s[i]]
            i += 1
    return result if i >= len(s) else result + mapping[s[i]]