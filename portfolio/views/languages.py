import reflex as rx
from portfolio.data import Language
from portfolio.components.heading import heading
from portfolio.styles.styles import Size


def languages(langs: list[Language]) -> rx.Component:
    return rx.vstack(
        heading("Linguistic Proficiency"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(lang.icon, font_size="18px"),
                    rx.text(lang.name),
                    variant="outline",
                    radius="large",
                    size="2",
                )
                for lang in langs
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
    )
