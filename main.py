from datetime import datetime, timedelta
from src.data_manager import DataManager
from src.flight_search import FlightSearch
from src.notification import NotificationManager
from src.config import BOT_TOKEN, ADMIN_ID

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager(BOT_TOKEN, ADMIN_ID)


ORIGIN_CITY_IATA = "MOW"

tomorrow = datetime.now() + timedelta(days = 1)
six_month_from_today = datetime.now() + timedelta(days = (6 * 30))

for destination in sheet_data:

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        from_time = tomorrow,
        to_time = six_month_from_today
    )

    if flight:
        if flight.price < destination["Lowest Price"]:
            notification_manager.send_sms(
                message = f"""Внимание низкая цена! 
                        Перелет из {flight.origin_city}-{flight.origin_airport} 
                        в {flight.destination_city}-{flight.destination_airport} за {flight.price} рублей.\n
                        Даты: {flight.out_date} - {flight.return_date}. """
            )
