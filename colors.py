class Colors:
    darkGray = (26, 31, 40)
    green = (166, 255, 167)
    red = (255, 167, 166)
    orange = (255, 105, 64)
    yellow = (250, 234, 62) 
    purple = (200, 64, 255)
    cyan = (64, 255, 200)
    blue = (64, 81, 255)   

    @classmethod
    def getCellColors(cls):
        return [cls.darkGray, cls.green, cls.red, cls.orange, cls.yellow, cls.purple, cls.cyan, cls.blue] 