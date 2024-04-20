import reflex as rx
from portfolio.data import Extra

from portfolio.styles.styles import Size


def glow_card(extra: Extra) -> rx.Component:
    card = rx.card(
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

    return rx.stack(
        rx.script(src="/scripts/glow_card_script.js"),
        rx.html("<article data-glow><div data-glow></div></article>"),
    )
