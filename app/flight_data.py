class FlightData:

    def __init__(self, price, origin_city, origin_airport, destination_city, destination_airport, out_date, return_date):
        self.price = price
        self.origin_city = origin_city
        self.origin_airport = origin_airport
        self.destination_city = destination_city
        self.destination_airport = destination_airport
        self.out_date = out_date
        self.return_date = return_date

    def check_weekend(self):
        """ Проверяет выходные """

        dts = datetime.strptime(self.out_date, '%Y-%m-%d')
        dte = datetime.strptime(self.return_date, '%Y-%m-%d')
        delta = dte - dts
        if 1 <= delta.days <= 2:
            if dts.weekday() in [4, 5]:
                return True
            else:
                return False
        else:
            return False
