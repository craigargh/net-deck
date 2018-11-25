import json

from netdeck import api


def retrieve(deck_url):
    [*_, deck_id] = deck_url.split('/')

    deck = api.get_deck(deck_id)

    with open('image_paths.json', 'r') as image_paths_file:
        cards_map = json.load(image_paths_file)

    return build_deck_details(deck, cards_map)


def build_deck_details(deck, cards_map):
    deck_data = deck['data'][0]

    deck_cards = []

    for card_id, qty in deck_data['cards'].items():
        image_location = cards_map[card_id]

        for _ in range(qty):
            deck_cards.append(image_location)

    return {
        'name': deck_data['name'],
        'paths': deck_cards
    }
