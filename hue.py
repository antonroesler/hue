""" This script contains all the API connections to the hue system. """

import requests
import json
import os

# Key and IP-address are stored as environment variables
KEY = os.environ['HUE_KEY']
IP = os.environ['HUE_BRIDGE_IP']

ADDRESS = f"http://{IP}/api/{KEY}/"


def get_all_lights():
    """
    Returns all devices that are accsessible via the connected bridge. 
    Returns a dict.
    """
    url = f"{ADDRESS}lights"
    response = requests.get(url)
    data = json.loads(response.text)
    return data


def turn_light(id, on=True):
    """
    Turns a specific light on/off. The id, that is used by the bridge, is required.
    To turn the light off, the on parameter must be set to False.
    """
    body = '{"on":false}'
    if on:
        body = '{"on":true}'
    url = f"{ADDRESS}lights/{id}/state"
    response = requests.put(url, data=body)
    return response
