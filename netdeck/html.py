


def generate(deck_name, card_paths):
    image_template = '<img src="../cards/{image_path}" width=240px/>'

    img_tags = [
        image_template.format(image_path=card_path)
        for card_path in card_paths
    ]

    html = '\n'.join(img_tags)

    return html
