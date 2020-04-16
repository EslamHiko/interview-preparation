'''
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
'''
def emit_starting_at(s, i):
    """
    when we see ->     3[...]
    we pass in this i  ^        that's the one at the start
    and return this one      ^  that's the one after the closing bracket
    """
    numstr = ""
    while s[i].isdigit():
        numstr += s[i]
        i += 1
    # currently on an opening bracket -- move past it
    i += 1

    chunk = ""
    while s[i] != ']':
        if s[i].isdigit():
            i, added = emit_starting_at(s, i)
            chunk += added
        else:
            chunk += s[i]
            i += 1
    # return position past the closing bracket
	# multiply the string rather than repeatedly processing it
    return i+1, chunk*int(numstr)


class Solution:
    def decodeString(self, s: str) -> str:
        # modify the string so that the full string is one nested expr
        s = "1[" + s + ']'
        return emit_starting_at(s, 0)[1]
