from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification import NotificationManager, BOT_TOKEN, ADMIN_ID

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
flight_search = FlightSearch()
notification_manager = NotificationManager(BOT_TOKEN, ADMIN_ID)


ORIGIN_CITY_IATA = "MOW"

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))


for destination in sheet_data:

    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["IATA Code"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )

    if flight:
        if flight.price < destination["Lowest Price"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only RUB{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} to {flight.return_date}. "
            )
