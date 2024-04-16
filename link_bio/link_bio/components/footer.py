import reflex as rx
import datetime
from link_bio.styles.sizes import Size
from link_bio.styles.colors import *

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="NoisyDevSVG.svg",
            height = Size.VERY_BIG.value,
            width = Size.ULTRA_BIG.value,
            alt='Logotipo de NoisyDev. Una \'ene\' y una \'de\' entre simbolo de menor y mayor'
        ),
        rx.hstack(
           rx.chakra.span(
                f'© 2023-{datetime.date.today().year}',
                font_size=Size.MEDIUM.value,
                color = TextColor.FOOTER.value
            ),
            rx.chakra.span(
                'NoisyDev by Agustin Muzi',
                font_size=Size.MEDIUM.value,
                color = Color.ALTERNATIVE.value
            ), 
            rx.chakra.span(
                'v1',
                font_size=Size.MEDIUM.value,
                color = TextColor.FOOTER.value
            ), 
            spacing='1'
        ),
        align="center",
        padding = Size.LARGE.value,
        height = '100%'
    )
    
