import reflex as rx
from link_bio.styles.colors import *

def link_icon(icon, url: str) -> rx.Component:
    return rx.link(
        rx.icon(
            tag = icon, 
            color = TextColor.HEADER.value,
            alt = icon
        ),
        href=url,
        is_external = True,  
    )