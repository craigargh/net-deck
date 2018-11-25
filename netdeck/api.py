import requests

BASE_URL = 'https://netrunnerdb.com'


def get_deck(deck_id):
    url = f'{BASE_URL}/api/2.0/public/deck/{deck_id}'

    return requests.get(url).json()


def get_decklist(decklist_id):
    url = f'{BASE_URL}/api/2.0/public/decklist/{decklist_id}'

    return requests.get(url).json()


def get_card(card_id):
    url = f'{BASE_URL}/api/2.0/public/card/{card_id}'

    return requests.get(url).json()


def get_cards():
    url = f'{BASE_URL}/api/2.0/public/cards'

    return requests.get(url).json()


def get_pack(pack_code):
    url = f'{BASE_URL}/api/2.0/public/pack/{pack_code}'

    return requests.get(url).json()


def get_packs():
    url = f'{BASE_URL}/api/2.0/public/packs'

    return requests.get(url).json()


def get_cycles():
    url = f'{BASE_URL}/api/2.0/public/cycles'

    return requests.get(url).json()
