# https://leetcode.com/problems/longest-common-prefix/submissions/1242171329/

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    prefix = ""

    list = sorted(strs)

    first = list[0]
    last = list[-1]

    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return prefix
        prefix += first[i]

    return prefix

print(longestCommonPrefix(["dag","dacar","dar"]))


