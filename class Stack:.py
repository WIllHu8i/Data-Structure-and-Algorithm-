class Stack:
    def __init__(self):
        self._items = []
    def is_empty(self):
        if len(self._items)==0:
            return True
        else:
            return False
        #return not bool(self._items) if that list is empty, bool will return False else True
    def push(self,item):
        self._items.append(item)
    def pop(self):
        return self._items.pop()
    def peek(self):
        return self._items[-1]
    def size(self):
        return len(self._items)
    def __str__(self):
        return self._items


def rev_string(my_str):
    string = Stack()
    rev_str = ""
    for character in my_str:
        string.push(character)
    while string.is_empty() is False:
        rev_str+=string.pop()
    return rev_str

print(rev_string("willhh"))

def par_checker(parentheses):
    stack = Stack()
    for par in parentheses:
        if par=="(":
            stack.push(par)
        else:
            if stack.is_empty():
                return False
            else:
                stack.pop()
    return stack.is_empty()
        
print(par_checker("((()))"))  # expected True
print(par_checker("((()()))"))  # expected True
print(par_checker("(()"))  # expected False
print(par_checker(")("))  # expected False



def balance_checker(parentheses):
    stack = Stack()
    for par in parentheses:
        if par in "({[":
            stack.push(par)
        else:
            if stack.is_empty():
                return False
            elif par==")" and stack.peek()=="(":
                stack.pop()
            elif par=="}" and stack.peek()=="{":
                stack.pop()
            elif par=="]" and stack.peek()=="[":
                stack.pop()
            else:
                return False
    return stack.is_empty()

            

print(balance_checker('{({([][])}())}'))
print(balance_checker('[{()]'))


def divide_by_2(decimal_num):
    stack = Stack()
    while decimal_num>0:
        remainder = decimal_num%2
        decimal_num = decimal_num//2
        stack.push(remainder)
    binary = ""
    while not stack.is_empty():
        binary+=str(stack.pop())
    return binary

print(divide_by_2(42))
print(divide_by_2(31))


def base_converter(decimal_num, base):
    digits = "0123456789ABCDEF"
    rem_stack = Stack()

    while decimal_num > 0:
        rem = decimal_num % base
        rem_stack.push(rem)
        decimal_num = decimal_num // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string

print(base_converter(25, 8))
print(base_converter(25, 16))
