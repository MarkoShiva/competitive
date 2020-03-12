def parse(s):                       # Not good implementation but still in case of limited number of characters is ok
    stack1 = []
    stack2 = []
    stack3 = []
    pair_open = ({"{": stack1, "(": stack2, "[": stack3})
    pair_close = ({"}": stack1, ")": stack2, "]": stack3})
    if string1[0] in pair_close.keys():
        return False
    for c in s:
        if c in pair_open.keys():
            pair_open[c].append(c)
        elif c in pair_close.keys():
            pair_close[c].pop()

    if len(stack1) == 0 and len(stack2) == 0 and len(stack3) == 0:
        return True
    else:
        return False

def lifo(s):
    stack = []                                      # proper implementation using single dict with mapped pairs and
                                                    # single stack
    pairs = ({"}": "{", ")": "(", "]": "["})
    if s[0] in pairs.keys():
        return False
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            val = stack.pop()
            if val != pairs[c]:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


# Example strings for checking whether the proper matching brackets are in place in string
string = "(kldksjaklf({)}klfjakss{}())"  # False string wrong order will pass for parse but not lifo
string1 = "(kldksjaklf(){klfjakss{}())"  # False string trailing {
string2 = "(kldksjaklf(){klfjakss{}(())"  # False string missing 2 brackets
string3 = "(kldksjaklf()klfjakss{}())"  # True string all of the brackets properly closed.


assert parse(string) == True            # If there are enough of matching brackets it will be true
assert parse(string1) == False
assert parse(string2) == False
assert parse(string3) == True

assert lifo(string) == False             # Proper checking via LIFO implementation with simple list.
assert lifo(string1) == False
assert lifo(string2) == False
assert lifo(string3) == True
