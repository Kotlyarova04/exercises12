class Load:
    data = []

    @staticmethod
    def write(ticket):
        with open(ticket, encoding='utf-8') as f:
            atributes = f.readline()
            for string in f:
                string = string.split(';')
                ticket = AirTicket(string[0], string[1], string[2], string[3], string[4], string[5], string[6],
                                   string[7])
                Load.data.append(ticket)


class AirTicket:
    def __init__(self, passenger_name, _from, to, date_time, flight, seat, _class, gate):
        self.passenger_name = passenger_name
        self._from = _from
        self.to = to
        self.date_time = date_time
        self.flight = flight
        self.seat = seat
        self._class = _class
        self.gate = gate

    def __repr__(self):
        return f'|{(self.passenger_name + " " * 16)[:16]}|{self._from} |{self.to}|{self.date_time}|' \
               f'{(self.flight + " " * 20)[:20]}|{(self.seat + " " * 4)[:4]}|{(self._class + " " * 3)[:3]}|' \
               f'{(self.gate + " " * 4)[:4]}|'


tickets = Load.write('tickets.txt')
print('-' * 79)
print('|     NAME       |FROM|TO |   DATE/TIME    |       FLIGHT       |SEAT|CLS|GATE|')
print('=' * 79)
for item in Load.data:
    print(item)
print('-' * 79)
