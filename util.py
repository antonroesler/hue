"""This file conatins utilit functions to store and load data."""

import pickle

DATA_FILE = "./data/data.txt"


def load_light_data():
    """Loads data from the data file."""
    with open(DATA_FILE, "rb") as file:
        return pickle.load(file)


def save_light_data(data):
    """Saves data from the data file. Data must be complete. The file will be overwritten."""
    with open(DATA_FILE, "wb") as file:
        pickle.dump(data, file)
