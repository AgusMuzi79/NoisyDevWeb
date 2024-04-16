import reflex as rx
from link_bio.components.navbar import navbar
from link_bio.components.footer import footer
from link_bio.views.header.header import header
from link_bio.views.body.body import links
from link_bio.styles.styles import *
from link_bio.styles.sizes import *
from link_bio.styles.stylesheets import *

class State(rx.State):
    pass
    

def index() -> rx.Component:
    return rx.box(
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                links(),
                max_width = '600px',
                width = '100%',
                align='center',
                margin_y= Size.DEFAULT.value,
            ),
        ),
        footer()
    )

app = rx.App(
    style=style, 
    stylesheets = STYLESHEETS
)
app.add_page(
    index,
    title = 'NoisyDev',
    description = '',
    image = '/NoisyDevJPG.jpg'
    
)