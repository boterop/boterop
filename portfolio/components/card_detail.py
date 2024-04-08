import reflex as rx
from portfolio.data import Extra

from portfolio.styles.styles import IMAGE_HEIGHT, Size


def card_detail(extra: Extra) -> rx.Component:
    return rx.card(
        rx.link(
            rx.flex(
                rx.text.strong(extra.title),
                rx.text(extra.description, size=Size.SMALL.value, color_scheme="gray"),
                direction="column",
                spacing="1",
            ),
            href=extra.url,
        ),
        width="100%",
        is_external=True,
    )
