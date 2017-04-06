"""
    ===========
    Description
    ===========
    This is a simple Socrata configuration module, you might have to create
    a robust config module for Socrata or populate this file with multiple configurations
    depending on your needs and expose them.

    This is how a public API URL looks like:
      https://data.cityofchicago.org/resource/alternative-fuel-locations.json?

    let's split it into what node-socrata receives as parameters.
    HOST_DOMAIN = https://data.cityofchicago.org
    DATASET = alternative-fuel-locations

    Connection setup for socrata:
      client = Socrata(HOST_DOMAIN, TOKEN, username="", password="")

    TOKEN is something that you generated with a Socrata developer,
    create one here: https://dev.socrata.com/

    username and password are only required for creating or modifying data.
    An application token isn't strictly required (can be None),
    but queries executed from a client without an application token will
    be sujected to strict throttling limits. To create a bare-bones client:
      client = Socrata(HOST_DOMAIN, None)
"""
from sodapy import Socrata

HOST_DOMAIN = 'data.cityofchicago.org'

DATASETS = {
  'ALT_FUEL_LOCATIONS': 'alternative-fuel-locations'
}

def getChicagoAlternativeFuelLocations(limit):
  client = Socrata(HOST_DOMAIN, None)
  return client.get(DATASETS['ALT_FUEL_LOCATIONS'], limit=limit)