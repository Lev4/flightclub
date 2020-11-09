# import requests
import logging
import os
import pandas as pd

logging.basicConfig(level=logging.INFO)
fpth = os.path.join('FlightDeals.xlsx')


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.fpth = fpth

    def get_destination_data(self):
        df = pd.read_excel(self.fpth)
        # City IATA Code LowestPrice
        self.destination_data = df.to_dict('records')
        return self.destination_data

    # def update_destination_codes(self):
    #     for city in self.destination_data:
    #         new_data = {
    #             "price": {
    #                 "iataCode": city["iataCode"]
    #             }
    #         }
    #         response = requests.put(
    #             url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
    #             json=new_data
    #         )
    #         print(response.text)