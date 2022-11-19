class Triangle:
    angle_1 = None
    angle_2 = None
    angle_3 = None

    def __init__(self, angle_1, angle_2, angle_3):
        self.angle_1 = angle_1
        self.angle_2 = angle_2
        self.angle_3 = angle_3

    def check(self):
        if self.angle_1 < self.angle_2 + self.angle_3 and \
            self.angle_2 < self.angle_1 + self.angle_3 and \
                self.angle_3 < self.angle_1 + self.angle_2:
            print('Triangle initialized')
        else:
            print('Initialization failed')

    def check_nums(self):
        if self.angle_1 > 0 and self.angle_2 > 0 and self.angle_3 > 0:
            return True
        else:
            return False
