import datetime

class Date:
    mnth = ['янв', 'фев', 'мар', 'апр', 'май', 'июн', 'июл', 'авг', 'сен', 'окт', 'ноя', 'дек']
    def __init__(self, date_string):
        self._date = None
        self.date = date_string

    def __repr__(self):
        if self._date:
            return self._date
        else:
            print('ошибка')
            return 'None'
    @property
    def date(self):
        if self._date is not None:
            day, month, year = self._date.split('.')
            return f"{int(day)} {Date.mnth[int(month) - 1]} {int(year)} г."
        else:
            return self._date

    @date.setter
    def date(self, date_string):
        day, month, year = date_string.split('.')
        try:
            day = int(day)
            month = int(month)
            year = int(year)
            if 1 <= day <= 31 and 1 <= month <= 12 and 0 <= year:
                if month == 2 and year % 4 == 0 and day <= 29:
                    self._date = date_string
                if month == 2 and year % 4 != 0 and day <= 28:
                    self._date = date_string
                if month in [1,3,5,7,8,10,12] and day <= 31:
                    self._date = date_string
                if month in [4,6,9,11] and day <= 30:
                    self._date = date_string
            else:
                self._date = None
                print('ошибка')
        except ValueError:
            self._date = None
            print('ошибка')

    def to_timestamp(self):
        if self._date is not None:
            day, month, year = self._date.split('.')
            date1 = datetime.date(int(year), int(month), int(day))
            start = datetime.date(1970,1,1)
            delta = date1 - start
            return int(delta.days*24*60*60)
        else:
            return None

    def __lt__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() < other.to_timestamp()
        return False

    def __le__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() <= other.to_timestamp()
        return False

    def __eq__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() == other.to_timestamp()
        return False

    def __ne__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() != other.to_timestamp()
        return False

    def __gt__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() > other.to_timestamp()
        return False

    def __ge__(self, other):
        if self._date is not None and other._date is not None:
            return self.to_timestamp() >= other.to_timestamp()
        return False





d1 = Date('07.12.2021')
print(d1.date)
d1.date = '14.02.2022'
print(d1.date)
print(d1.to_timestamp())
d2 = Date('32.14.2020')
print(d2.date)
d2.date = '29.02.2021'
print(d2)
d2.date = '29.02.2020'
print(d2.date)
if d1 < d2:
    print('YES')
else:
    print('NO')
print(d1 >= d2)
print(d1 != Date('01.01.2023'))
print(d1 <= d2)
