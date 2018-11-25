from netdeck import api


def retrieve(deck_url):
    [*_, deck_id] = deck_url.split('/')

    deck = api.get_deck(deck_id)

    card_ids = deck['data'][0]['cards'].keys()

    cards = [
        api.get_card(card_id)
        for card_id in card_ids
    ]

    packs = api.get_packs()

    cycles = api.get_cycles()

    return build_deck_details(deck, cards, packs, cycles)


def build_deck_details(deck, cards, packs, cycles):
    pack_map = make_packs_map(packs)
    card_map = make_cards_map(cards)
    cycles_map = make_cycles_map(cycles)

    deck_data = deck['data'][0]

    deck_cards = []

    for card_id, qty in deck_data['cards'].items():
        card = card_map[card_id]

        pack_id = card['pack_code']
        pack = pack_map[pack_id]

        cycle_id = pack['cycle_id']
        cycle = cycles_map[cycle_id]

        full_card_info = {
            'qty': qty,
            **card,
            **pack,
            **cycle,
        }

        deck_cards.append(full_card_info)

    return {
        'name': deck_data['name'],
        'cards': deck_cards
    }


def make_packs_map(packs):
    return {
        pack['code']: pack_details(pack)
        for pack in packs['data']
    }


def pack_details(pack_data):
    pack_type = 'data_pack' if pack_data['size'] == 20 else 'big_box'

    return {
        'pack_name': pack_data['name'],
        'pack_position': pack_data['position'],
        'cycle_id': pack_data['cycle_code'],
        'pack_type': pack_type,
    }


def make_cards_map(cards):
    return {
        card['data'][0]['code']: card_details(card)
        for card in cards
    }


def card_details(card):
    card_data = card['data'][0]

    return {
        'card_title': card_data['title'],
        'pack_code': card_data['pack_code'],
        'card_position': card_data['position']
    }


def make_cycles_map(cycles):
    return {
        cycle['code']: cycle_details(cycle)
        for cycle in cycles['data']
    }


def cycle_details(cycle):
    cycle_name = cycle['name']

    if cycle_name == 'Core Set':
        cycle_name = 'Core'

    return {
        'cycle_name': cycle_name,
        'cycle_code': cycle['code'],
        'cycle_position': cycle['position'],
    }
