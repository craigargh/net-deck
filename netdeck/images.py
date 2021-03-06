import os
import string


def card_paths(deck_config):
    return [
        card_path(card)
        for card in deck_config['cards']
        for _ in range(card['qty'])
    ]


def card_path(card):
    cycle_dir = format_path(card['cycle_position'], card['cycle_name'])

    if card['pack_type'] == 'data_pack':
        pack_dir = format_path(card['pack_position'], card['pack_name'])
    else:
        pack_dir = ''

    card_dir = format_path(card['card_position'], card['card_title'], digits=3, title_case=True)
    file_name = card_dir + '.jpg'

    return os.path.join(cycle_dir, pack_dir, file_name)


def format_path(position, name, digits=2, title_case=False):
    position_string = f'{position}'.rjust(digits, '0')

    if name == 'Dai V':
        position_string = '005'

    if name == "Na'Not'K":
        name = 'Na_Not_k'

    elif title_case:
        if "'" in name:
            name = string.capwords(name)
        else:
            name = name.title()

        if ' In ' in name:
            name = name.replace(' In ', ' in ')

        if 'Of The' in name:
            name = name.replace('Of The', 'of the')

    name = name \
        .replace("'", "_") \
        .replace('&', "_") \
        .replace(':', ' -') \
        .replace('"', '') \
        .replace('é', 'e') \
        .replace('à', 'a')

    return f"{position_string} - {name}" \
        .replace(' ', '%20')
