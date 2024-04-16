import reflex as rx
from link_bio.styles.colors import *
from link_bio.styles.styles import *

def title (title:str)  -> rx.Component:
    return rx.heading(
        title,
        color = TextColor.HEADER.value,
        style = title_style
    )