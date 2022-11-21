class Calculator(object):

    def read(self):
        return input('Пример: ')


    def polska(self, ex):
        stack_list = []
        result = []

        for el in ex:
            if el.isdigit():
                result.append(el)
            elif el == '(':
                stack_list.append(el)
            elif el == ')':
                while stack_list and stack_list[-1] != '(':
                    result.append(stack_list.pop())
                stack_list.pop()
            elif el == "*" or el == "/":
                while stack_list and stack_list[-1] in ['*', '/']:
                    result.append(stack_list.pop())
                stack_list.append(el)
            elif el == "+" or el == "-":
                while stack_list and stack_list[-1] in ['+', '-', '*', '/']:
                    result.append(stack_list.pop())
                stack_list.append(el)

        while stack_list:
            result.append(stack_list.pop())

        return (result)

    def eval(self, string):
        temp = []

        for i in string:
            if i.isdigit():
                temp.append(int(i))
            elif i in ['+', '-', '*', '/']:
                b = temp.pop()
                a = temp.pop()
                if i == '+':
                    temp.append(a+b)
                elif i == '-':
                    temp.append(a-b)
                elif i == '*':
                    temp.append(a*b)
                elif i == '/':
                    temp.append(a/b)

        return temp

    def loop(self):
        line = self.read()

        while line != "quit":
            res_line = self.polska(line)
            value = self.eval(res_line)
            print(value)
            # Read next line of input
            line = self.read()
