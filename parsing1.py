string = "(kldksjaklf({)}klfjakss{}())"
string1 = "(kldksjaklf(){klfjakss{}())"
string2 = "(kldksjaklf(){klfjakss{}(())"
string3 = "(kldksjaklf()klfjakss{}())"

def parse(s):
    stack1 = []
    stack2 = []
    stack3 = []
    pair_open = ({"{": stack1, "(": stack2,"[": stack3})
    pair_close = ({"}": stack1, ")": stack2, "]": stack3})
    if string1[0] in pair_close.keys():
        return False
    for c in s:
        if c in pair_open.keys():
            pair_open[c].append(c)
        elif c in pair_close.keys():
            pair_close[c].pop()

    if len(stack1) == 0 and len(stack2) == 0 and len(stack3) == 0: return True
    else: return False

def lifo(s):
    stack = []
    pairs = ({"}": "{", ")": "(", "]": "["})
    if string1[0] in pairs.keys():
        return False
    for c in s:
        if c in pairs.values():
            stack.append(c)
        elif c in pairs.keys():
            val = stack.pop()
            if val != pairs[c]:
                return False
    if len(stack) == 0: return True
    else: return False


print(parse(string))
print(lifo(string))

