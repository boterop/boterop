import reflex as rx
from portfolio import data
from portfolio.styles.styles import BASE_STYLE, MAX_WIDTH, STYLESHEETS, EmSize, Size
from portfolio.views.about import about
from portfolio.views.extra import extra
from portfolio.views.footer import footer
from portfolio.views.header import header
from portfolio.views.info import info
from portfolio.views.tech_stack import tech_stack
from portfolio.views.languages import languages
from portfolio.views.quote import quote

DATA = data.data

title = DATA.title
description = DATA.description
image = DATA.image
locale = DATA.locale


def index() -> rx.Component:
    return rx.center(
        # rx.theme_panel(),
        rx.vstack(
            header(DATA),
            about(DATA.about),
            rx.divider(),
            languages(DATA.languages),
            tech_stack(DATA.technologies),
            info("Experience", DATA.experience),
            info("Projects", DATA.projects),
            info("Education", DATA.training),
            extra(DATA.extras),
            quote(),
            rx.divider(),
            footer(DATA),
            spacing=Size.MEDIUM.value,
            padding_x=EmSize.MEDIUM.value,
            padding_y=EmSize.BIG.value,
            max_width=MAX_WIDTH,
            width="100%",
        )
    )


app = rx.App(
    stylesheets=STYLESHEETS,
    style=BASE_STYLE,
    theme=rx.theme(appearance="dark", accent_color="cyan", radius="full"),
)

app.add_page(
    index,
    title=title,
    description=description,
    image=image,
    meta=[
        {"name": "og:title", "content": title},
        {"name": "og:description", "content": description},
        {"name": "og:image", "content": image},
        {"property": "og:locale", "content": locale},
    ],
)
