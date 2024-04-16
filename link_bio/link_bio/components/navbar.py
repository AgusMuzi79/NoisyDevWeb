import reflex as rx
from link_bio.styles.sizes import Size as Size
from link_bio.styles.colors import Color as Color
from link_bio.styles.styles import *

def navbar () -> rx.Component:
    return rx.hstack(
        rx.box(
            rx.chakra.span('Noisy', color = Color.PRIMARY.value),
            rx.chakra.span('Dev', color = Color.ALTERNATIVE.value),
            style= navbar_title_style
        ),
        position = 'sticky',
        top = '0',
        bg =Color.CONTENT.value,
        padding_x = Size.BIG.value,
        padding_y = Size.DEFAULT.value,
        z_index = '999'
    )
