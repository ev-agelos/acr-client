"""Helper function to read/write user settings."""


import os
from configparser import ConfigParser


DOMAIN = 'https://rank.evagelos.me'
# settings.ini must live next to this file
SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             'settings.ini')

class ACPaths:
    """Paths for ac files that live in user's documents."""

    path =  os.path.expanduser('~/Documents/Assetto Corsa')
    log = os.path.join(path, 'logs/log.txt')

    @classmethod
    def last_setup(cls, car):
        return os.path.join(cls.path, 'setups/{}/generic/last.ini'.format(car))


def write_auth(section, **options):
    """Write user auth info to the settings.ini file."""
    parser = ConfigParser()
    parser.add_section(section)
    for key, value in options.items():
        parser.set('auth', key, str(value))
    with open(SETTINGS_FILE, 'w') as fob:
        parser.write(fob)


def read_auth():
    """Return user auth info from the settings.ini file."""
    parser = ConfigParser()
    if not all([parser.read(SETTINGS_FILE), parser.has_section('auth')] +
               [parser.has_option('auth', option)
                for option in ('user', 'token')]):
        return None
    return parser['auth']
