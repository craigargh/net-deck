from netdeck import api, images


def build():
    cards = retrieve()['cards']

    return {
        card['card_id']: images.card_path(card)
        for card in cards
    }


def retrieve():
    cards = api.get_cards()
    packs = api.get_packs()
    cycles = api.get_cycles()

    return build_deck_details(cards, packs, cycles)


def build_deck_details(cards, packs, cycles):
    pack_map = make_packs_map(packs)
    card_map = make_cards_map(cards)
    cycles_map = make_cycles_map(cycles)

    cards_map = []

    for card_id, card_data in card_map.items():
        pack_id = card_data['pack_code']
        pack = pack_map[pack_id]

        cycle_id = pack['cycle_id']
        cycle = cycles_map[cycle_id]

        full_card_info = {
            'qty': 1,
            'card_id': card_id,
            **card_data,
            **pack,
            **cycle,
        }

        cards_map.append(full_card_info)

    return {
        'cards': cards_map
    }


def make_packs_map(packs):
    return {
        pack['code']: pack_details(pack)
        for pack in packs['data']
    }


def pack_details(pack_data):
    is_data_pack = pack_data['size'] and 19 <= pack_data['size'] <= 20

    pack_type = 'data_pack' if is_data_pack else 'big_box'

    return {
        'pack_name': pack_data['name'],
        'pack_position': pack_data['position'],
        'cycle_id': pack_data['cycle_code'],
        'pack_type': pack_type,
    }


def make_cards_map(cards):
    cards = cards['data']

    return {
        card['code']: card_details(card)
        for card in cards
    }


def card_details(card_data):
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

    if 'Core Set' in cycle_name:
        cycle_name = cycle_name.replace('Core Set', 'Core')

    return {
        'cycle_name': cycle_name,
        'cycle_code': cycle['code'],
        'cycle_position': cycle['position'],
    }
