#!/usr/bin/python3
"""Defines the Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Represent a place.

    Attributes:
        user_id (str): The User id.
        city_id (str): The City id.
        name (str): The name of the place.
        number_rooms (int): The number of rooms of the place.
        number_bathrooms (int): The number of bathrooms of the place.
        price_by_night (int): The price by night of the place
        latitude (float): The latitude of the place.
        longitude (float): The longitude of the place.
        max_guest (int): The maximum number of guests of the place.
        amenity_ids (list): A list of Amenity ids.
        description (str): The description of the place.
    """

    city_id = ""
    user_id = ""
    name = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    description = ""
