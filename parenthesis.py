# taking n as an input
n = int(input("Input: n = "))
# initialize result as empty list for further use
result = []

# declaring function


def parentheses(left, right, strs):
    if right == n & left == n:
        result.append(strs)
        return
    if left < n:
        parentheses(left + 1, right, strs + "(")
    if right < left:
        parentheses(left, right + 1, strs + ")")


# calling function parentheses
parentheses(0, 0, "")
print("Output: ", result)
