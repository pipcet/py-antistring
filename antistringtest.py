# we use str(0)[0:0] for the empty string, rather than "", because string constants are overloaded
# in antistring.py

# str[::sign] is str if sign is 1, the reversed string if sign is -1

# this is incredibly dumb and slow

class FreeString:
    def letters(self):
        sign = 1
        res = []
        for string in self.stack:
            for letter in string[::sign]:
                res.append([letter,sign])
            sign = -sign
        return res

    def normalize(self):
        letters = self.letters()

        i = 0
        while i < len(letters)-1:
            if i == -1:
                i = 0
            if (letters[i][0] == letters[i+1][0] and
                letters[i][1] != letters[i+1][1]):
                letters = letters[0:i] + letters[i+2:]
                i = i-1
            else:
                i += 1

        sign = 1
        string = str(0)[0:0]
        stack = []
        for l in letters:
            if l[1] == sign:
                string += l[0]
            else:
                stack += [string[::sign]]
                sign = -sign
                string = l[0]
        if letters != []:
            stack += [string[::sign]]
        else:
            stack = [str(0)[0:0], str(0)[0:0]]

        if len(stack)%2 == 1:
            stack += [str(0)[0:0]]

        res = FreeString()
        res.stack = stack

        return res

    def __add__(self, b):
        st0 = self.stack
        st1 = b.stack

        if len(st0) % 1 != 0:
            Error()

        if len(st1) % 1 != 0:
            Error()

        res = FreeString()
        res.stack = st0 + st1

        return res.normalize()

    def __neg__(self):
        res = FreeString();
        res.stack.append(str(0)[0:0])
        res.stack += self.stack
        res.stack.append(str(0)[0:0])

        return res.normalize()

    def __sub__(self, b):
        return self + (-b)

    def __str__(self):
        n = self.normalize()
        assert len(n.stack) == 2 and n.stack[1] == ""
        return n.stack[0]

    def __repr__(self):
        sign = str(0)[0:0]
        res = str(0)[0:0]
        for string in self.stack:
            res += sign+string
            if sign==str("-"):
                sign=str("+")
            else:
                sign=str("-")
        return res

    def __init__(self, string=None):
        if string is None:
            self.stack = []
        else:
            self.stack = [string, str(0)[0:0]]

print "hi"
print repr(-"hi")
print ("hi" + "there")
print repr("hi" + "there" + "there")
print repr("hi" + "there" - "there")
print repr("hi" - "there" + "there")
print repr("hi" + "there" - "there" + "where")
print repr("hi" + "there" - "where" + "there")
print "hi"-"there"
