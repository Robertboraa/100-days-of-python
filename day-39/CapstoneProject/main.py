from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

ORIGIN = "LON"

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()

destinations = data_manager.get_destination_data()
customers = data_manager.get_customer_emails()

for destination in destinations:
    flight = flight_search.check_flights(ORIGIN, destination["iataCode"])
    if flight and flight["price"] < destination["lowestPrice"]:
        fd = FlightData(
            price=flight["price"],
            origin_airport=flight["flyFrom"],
            destination_airport=flight["flyTo"],
            out_date=flight["local_departure"].split("T")[0],
            return_date=flight["local_arrival"].split("T")[0],
        )
        notification_manager.send_whatsapp(
            f"Low price alert! Only £{fd.price} to fly "
            f"from {fd.origin_airport} to {fd.destination_airport}.\n"
            f"Outbound: {fd.out_date}\nReturn: {fd.return_date}"
        )
        notification_manager.send_emails(
            customers,
            f"Low price alert! Only £{fd.price} to fly "
            f"from {fd.origin_airport} to {fd.destination_airport}.\n"
            f"Outbound: {fd.out_date}\nReturn: {fd.return_date}"
        )