import reflex as rx
from portfolio.components.media import media
from portfolio.data import Data
from portfolio.styles.styles import Size


def footer(data: Data) -> rx.Component:
    made = "Portfolio made with"
    return rx.hstack(
        rx.vstack(
            rx.text(data.name),
            media(data.media),
            spacing=Size.SMALL.value,
        ),
        rx.center(
            rx.hstack(
                rx.text(made),
                rx.badge(
                    rx.box(class_name="devicon-reflex-plain", font_size="24px"),
                    rx.text("Reflex"),
                    size="2",
                ),
            ),
            width="100%",
        ),
        width="100%",
    )
