"""
This script handles the command line interface using the python click library.
It uses the functions from the hue script to communicate with the hue bride.
"""
import click

from .util import *
from .hue import *


# Load the stored lights.
LIGHTS = load_light_data()


@click.group()
def cli():
    pass  # click entry point


@cli.command()
def all():
    """
    Lists all lights that are connected to the bridge with their id 
    and the name the name stored in the bridge. 

    This name is not the name that users use in this application. It is 
    the name the bridge uses.
    """
    data = get_all_lights()
    keys = data.keys()
    for key in keys:
        name = data.get(key).get("name")
        click.echo(f"{key}: {name}")


@cli.command()
@click.option('-l', '-light', 'light')
@click.option('-n', '-name', 'name')
def set(light, name):
    """
    Sets a name to a specific light. 
    @param light is the id
    @name is the name the users decides
    This is not the name stored in the bridge. The name in th ebridege will not be overwritten.

    The name is used as a better understandable identifier.

    After setting a name: 
    --------------
    $ hue set -light 3 -name desk
    --------------

    This name can be used: 
    --------------
    $ hue on -name desk
    --------------
    """
    LIGHTS[name] = int(light)
    save_light_data(LIGHTS)
    click.echo(f"Light {name} saved")


@cli.command()
def saved():
    """Shows a list of all lights that have been named using the @func set() function."""
    for light in LIGHTS.keys():
        click.echo(light)


@cli.command()
@click.option('-n', '-name', 'name')
def on(name):
    """Turns the light with given name on."""
    id = LIGHTS[name]
    turn_light(id)


@cli.command()
@click.option('-n', '-name', 'name')
def off(name):
    """Turns the light with given name off."""
    id = LIGHTS[name]
    turn_light(id, on=False)
