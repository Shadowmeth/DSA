class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        else:
            return None

    def read(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None


class Linter:
    def __init__(self):
        self.stack = Stack()

    def lint(self, text):
        while self.stack.read():
            self.stack.pop()

        matching_braces = {"(": ")", "[": "]", "{": "}"}
        for char in text:
            if char in matching_braces.keys():
                self.stack.push(char)
            elif char in matching_braces.values():
                if not self.stack.read():
                    return char + " does not have opening brace"
                else:
                    popped_opening_brace = self.stack.pop()
                    if char != matching_braces.get(str(popped_opening_brace)):
                        return char + " has mismatched opening brace"
        # if we get to end of line and the stack isn't empty
        if self.stack.read():
            return self.stack.read() + " does not have closing brace"
        return True

linter = Linter()
print(linter.lint("(var x = 2;"))

def reverse_string(string):
    stack = Stack()
    for c in string:
        stack.push(c)
    reversed = ""
    while stack.read():
        reversed += stack.pop()
    return reversed

print(reverse_string("abcde"))

