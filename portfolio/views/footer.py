import reflex as rx
from portfolio.components.media import media
from portfolio.data import Data
from portfolio.styles.styles import Size


def footer(data: Data) -> rx.Component:
    return rx.vstack(
        rx.text(data.name),
        media(data.media),
        spacing=Size.SMALL.value
    )
