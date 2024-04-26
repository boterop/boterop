import reflex as rx
from portfolio.services.zen_service import ZenService
from portfolio.styles.styles import Size


def quote() -> rx.Component:
    quote: dict
    [quote] = ZenService().get_quote()
    element = f'<center>{quote["h"]}</center>'
    return rx.center(
        rx.link(
            rx.html(element),
            href=ZenService().ZEN_URL,
            underline="hover",
            color_scheme="bronze",
            is_external=True,
        ),
        width="100%",
    )
