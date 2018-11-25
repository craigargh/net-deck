import json

from netdeck import deck, images, html, image_maps


def build_deck(url):
    current_deck = deck.retrieve(url)

    card_paths = current_deck['paths']

    generate_html = html.generate(card_paths)

    deck_name = current_deck['name']

    with open(f'decks/{deck_name}.html', 'w+') as deck_file:
        deck_file.write(generate_html)


def build_cards_map():
    all_paths = image_maps.build()

    with open('image_paths.json', 'w+') as image_paths:
        json.dump(all_paths, image_paths, indent=4, sort_keys=True)


build_cards_map()
build_deck('https://netrunnerdb.com/en/deck/view/1201811')
build_deck('https://netrunnerdb.com/en/deck/view/752593')
build_deck('https://netrunnerdb.com/en/deck/view/1204622')
build_deck('https://netrunnerdb.com/en/deck/view/546597')

