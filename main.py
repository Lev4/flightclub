from datetime import datetime, timedelta
from app.data_manager import DataManager
from app.flight_search import FlightSearch
from app.notification import NotificationManager
from config import BOT_TOKEN, ADMIN_ID

data_manager = DataManager()

data_package = {
    "sheet_data": data_manager.get_destination_data(),
    "flight_search": FlightSearch(),
    "notification_manager": NotificationManager(BOT_TOKEN, ADMIN_ID),
    "ORIGIN_CITY_IATA": "MOW",
    "tomorrow": datetime.now() + timedelta(days = 1),
    "six_month_from_today": datetime.now() + timedelta(days = (6 * 30)),
}


def search_flights(data_pack, period):
    for destination in data_pack["sheet_data"]:

        if period == "long":
            flight = data_pack["flight_search"].check_flights(
                data_pack["ORIGIN_CITY_IATA"],
                destination["IATA Code"],
                from_time = data_pack["tomorrow"],
                to_time = data_pack["six_month_from_today"]
            )
        else:
            flight = data_pack["flight_search"].check_flights_short(
                data_pack["ORIGIN_CITY_IATA"],
                destination["IATA Code"],
                from_time = data_pack["tomorrow"],
                to_time = data_pack["six_month_from_today"]
            )

        if flight:
            if flight.price < destination["Lowest Price"]:
                msg = ""
                if flight.check_weekend_plus():
                    msg += "Выходные плюс 1! \n"
                elif flight.check_weekend():
                    msg += "Выходные!\n"

                msg += f"Перелет из {flight.origin_city}-{flight.origin_airport} "
                msg += f"в {flight.destination_city}-{flight.destination_airport} за {flight.price} рублей.\n"
                msg += f"Даты: {flight.out_date} ({flight.out_date_weekday}) - {flight.return_date} ({flight.return_date_weekday}).\n"
                msg += f"Продолжительность {flight.duration_days} д"

                data_pack["notification_manager"].send_sms(
                    message = msg
                )


search_flights(data_package, "short")

