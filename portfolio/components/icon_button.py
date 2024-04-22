import reflex as rx

from reflex.components.radix.themes.base import Theme


def icon_button(
    icon: str,
    url: str,
    text="",
    solid=False,
    child="",
    class_name="",
) -> rx.Component:
    background = "cyan-600" if solid else "transparent"
    border = "border-0" if solid else "border"
    border_color = "transparent" if solid else "cyan-700"
    color = "white" if solid else "cyan-500"
    print(Theme.get_props())
    return rx.flex(
        rx.link(
            rx.flex(
                rx.icon(icon, class_name=f"stroke-{color}"),
                rx.container(text, class_name="pt-0.5"),
                spacing="2" if text != "" else "0",
                class_name="text-white text-sm font-medium",
            ),
            href=url,
            is_external=True,
        ),
        child,
        class_name=f"items-center h-8 px-3 py-1 rounded-full border-{border_color} bg-{background} {class_name} {border}",
        spacing="3",
    )
