"""
class Data describes data and have 2 variants of data output
"""


class Data:
    def __init__(self, day, month, year):
        if int(day) < 1 or int(day) > 31:
            raise ValueError(f'{type(day).__name__} Day is not valid')
        if int(month) < 1 or int(day) > 12:
            raise ValueError(f'{type(month).__name__} Month is not valid')
        if int(year) < 1:
            raise ValueError(f'{type(year).__name__} Year is not valid')

        self.__monthstr=['January',
                         'February',
                         'March',
                         'April',
                         'May',
                         'June',
                         'July',
                         'August',
                         'September',
                         'October',
                         'November',
                         'December']
        self.__day = day
        self.__month = month
        self.__year = year

    def getdata(self, variant = 1):
        if variant == 1:
            return f'{self.__day} {self.__monthstr[int(self.__month)-1]} {self.__year}'
        if variant == 2:
            return f'{self.__day}-{self.__month}-{self.__year}'