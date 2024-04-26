import reflex as rx
from portfolio.data import Extra

from portfolio.styles.styles import Size


def glow_card(extra: Extra) -> rx.Component:
    return rx.box(
        rx.box(
            custom_attrs={"data-glow": ""},
        ),
        rx.link(
            rx.flex(
                rx.text.strong(extra.title),
                rx.text(
                    extra.description,
                    size=Size.SMALL.value,
                    color_scheme="gray",
                ),
                direction="column",
                spacing="1",
            ),
            href=extra.url,
            width="100%",
            height="100%",
            is_external=True,
        ),
        class_name="glow-card",
        custom_attrs={"data-glow": ""},
    )
