import reflex as rx
from link_bio.styles.colors import Color as Color
from link_bio.styles.sizes import *


def link_button(icon: str, text : str, url : str) -> rx.Component:
    return rx.link(
        rx.button(
            rx.hstack(
                rx.icon(
                    tag = icon,
                    width = Size.BIG.value,
                    height = Size.BIG.value,
                    alt = icon
                ),
                text,
            )
        ),
        href=url,
        is_external = True,
        width = '100%',
        
    )

    
