import reflex as rx
from portfolio.components.heading import heading
from portfolio.styles.styles import Size


def tech_stack(technologies: list[str]) -> rx.Component:
    return rx.vstack(
        heading("Main Technologies"),
        rx.flex(
            *[
                rx.badge(
                    rx.box(
                        class_name=technology.icon,
                        font_size="24px"
                    ),
                    rx.text(technology.name),
                    size="2"
                )
                for technology in technologies
            ],
            wrap="wrap",
            spacing=Size.SMALL.value
        ),
        spacing=Size.DEFAULT.value
    )
