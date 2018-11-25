def generate(card_paths):
    img_tags = [
        img(card_path)
        for card_path in card_paths
    ]

    html = '\n'.join(img_tags)

    return html


def img(card_path):
    image_template = '<img src="../cards/{image_path}" width=240px/>'
    image_template.format(image_path=card_path)
