""" DAY 13
Given an integer k and a string s, find the length of the longest substring that contains 
at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

##########

Two pointers, left and right
Traverse the right as far as we can go while satisfying the condition. Keep track of the longest substr.
When the condition no longer holds, increment the left counter until it does once again.

"""

def longest_substr_k_distinct(s: str, k: int) -> str:
    if not s or k < 1:
        return ""

    N = len(s)
    left, right = 0, 1
    longest_substr = s[0]
    char_freqs = {s[0]: 1}
    distincts = 1

    while right < N:
        # process the rightmost char
        if s[right] in char_freqs:
            char_freqs[s[right]] += 1
        else:
            # it is a new character
            char_freqs[s[right]] = 1
            distincts += 1

            # if we are over the allowed number of distincts, need to increment left
            while distincts > k:
                char_freqs[s[left]] -= 1
                if char_freqs[s[left]] == 0:
                    distincts -= 1
                    del char_freqs[s[left]]
                left += 1
            
        # update longest, if needed
        candidate_substr = s[left:right+1]
        if len(candidate_substr) > len(longest_substr):
            longest_substr = candidate_substr

        right += 1

    return longest_substr


# TEST CASES
assert longest_substr_k_distinct("abcba", 2) == "bcb"
assert longest_substr_k_distinct("abcba", 1) == "a"  # ambiguous, but now it sticks to the first one.
assert longest_substr_k_distinct("abcba", 0) == ""
assert longest_substr_k_distinct("abcba", -10) == ""
assert longest_substr_k_distinct("xyzabcbbbbcbcacbwertyuidgkgkhabcp", 2) == "bcbbbbcbc"
assert longest_substr_k_distinct("axyzabcbbbbcbcacbwertyuidgkgkhacbp", 3) == "abcbbbbcbcacb"
