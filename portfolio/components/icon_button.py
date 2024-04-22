import reflex as rx


def icon_button(
    icon: str,
    url: str,
    text="",
    solid=False,
    child="",
    class_name="",
) -> rx.Component:
    background = f"bg-{'cyan-600' if solid else 'transparent'}"
    return rx.flex(
        rx.link(
            rx.flex(
                rx.icon(icon, color="white"),
                rx.container(text, class_name="pt-0.5"),
                spacing="2" if text != "" else "0",
                class_name="text-white text-sm font-bold",
            ),
            href=url,
            is_external=True,
        ),
        child,
        class_name=f"items-center px-3 py-1 rounded-full {background} {class_name}",
        spacing="3",
    )
