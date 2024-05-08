class Load:
    data = []

    @staticmethod
    def write(meetings, persons, pers_meetings):
        with open(meetings, encoding='utf-8') as f1:
            atributes = f1.readline()
            for line in f1:
                meeting_data = line.split(';')
                date = Date(meeting_data[1]).date
                meeting = Meeting(int(meeting_data[0]), date, meeting_data[2], [])
                Load.data.append(meeting)

        with open(persons, encoding='utf-8') as f2:
            atributes = f2.readline()
            users = {}
            for line in f2:
                user = line.split(';')
                user = User(int(user[0]), user[1], user[2], user[3], user[4], user[5])
                users[user.id]= user
        with open(pers_meetings, encoding='utf-8') as f3:
            atributes = f3.readline()
            for string in f3:
                id = string.split(';')
                for meeting in Load.data:
                    if int(id[0]) == meeting.id:
                        meeting.add_person(users[int(id[1])])

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
                if month in [1, 3, 5, 7, 8, 10, 12] and day <= 31:
                    self._date = date_string
                if month in [4, 6, 9, 11] and day <= 30:
                    self._date = date_string
            else:
                self._date = None
                print('ошибка')
        except ValueError:
            self._date = None
            print('ошибка')


class User:
    def __init__(self, id, nick_name, first_name=None, last_name=None, middle_name=None, gender=None):
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def __repr__(self):
        if self.gender is not None:
            return f"ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} {self.last_name} {self.middle_name} GENDER: {self.gender}"
        else:
            return f"ID: {self.id} LOGIN: {self.nick_name} NAME: {self.first_name} {self.last_name} {self.middle_name}"


class Meeting:
    lst_meeting = []

    def __init__(self, id, date, title, employees):
        self.id = id
        self.date = date
        self.title = title
        self.employees = employees
        Meeting.lst_meeting.append(self)

    def add_person(self, person):
        self.employees.append(person)

    @classmethod
    def count_meeting(cls, date):
        count = 0
        for meeting in cls.lst_meeting:
            if meeting.date == Date(str(date)).date:
                count += 1
        return count

    @classmethod
    def total(cls):
        total = 0
        for meeting in cls.lst_meeting:
            total += len(meeting.employees)
        return total

    def __repr__(self):
        return f"Рабочая встреча {self.id}\n{self.date} {self.title}\n{(employee for employee in self.employees)}"


Load.write('meetings.txt', 'persons.txt', 'pers_meetings.txt')
for item in Meeting.lst_meeting:
    print(item)
print(Meeting.total())
print(Meeting.count_meeting(Date('21.04.2020')))
