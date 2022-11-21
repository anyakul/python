class Runner(object):

    def eval(self, str):
        value = 0
        lst = [int(i) for i in str.split(" ")]

        for i in range(len(lst)-1):
            perc = lst[i] + (lst[i] * ((11) / 100))  
      
            if lst[i + 1] > lst[i] and lst[i + 1] <= perc:
                value += 1
            else:
                value = 0

        if value == len(lst) - 1:
            print('Да, спортсмен успеет подготовиться к соревнованиям')

        else:
            print('Нет, спортсмен неуспеет подготовиться к соревнованиям')

        return value

    def loop(self):
        line = input()
        value = self.eval(line)
        print(value)
