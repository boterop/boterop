import reflex as rx
from portfolio.components.icon_button import icon_button
from portfolio.data import Media
from portfolio.styles.styles import Size


def media(data: Media) -> rx.Component:
    return rx.flex(
        rx.flex(
            icon_button(
                "mail",
                f"mailto:{data.email}",
                data.email,
                True,
                rx.button(
                    rx.icon("copy", color="white", size=16),
                    on_click=rx.set_clipboard(data.email),
                    variant="ghost",
                ),
            ),
        ),
        rx.hstack(
            icon_button("file-text", data.cv),
            icon_button("github", data.github),
            icon_button("linkedin", data.linkedin),
            icon_button("message-circle", data.whatsapp),
            spacing=Size.SMALL.value,
        ),
        spacing=Size.SMALL.value,
        flex_direction=["column", "column", "row"],
    )
