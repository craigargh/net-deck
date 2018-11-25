from netdeck import deck, images, html

current_deck = deck.retrieve('https://netrunnerdb.com/en/deck/view/752593')
card_paths = images.card_paths(current_deck)

generate_html = html.generate('test_deck', card_paths)

deck_name = current_deck['name']

with open(f'decks/{deck_name}.html', 'w+') as deck_file:
    deck_file.write(generate_html)
