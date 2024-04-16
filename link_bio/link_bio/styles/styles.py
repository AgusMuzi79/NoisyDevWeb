import reflex as rx
from .colors import *
from .sizes import *
# Styles

style = {
    'height':'100%',
    'min_height':'100vh',
    rx.button: {
        'width': '100%',
        'height': '100%',
        'display':'block',
        'padding': Size.SMALL.value,
        'border_radius': Size.DEFAULT.value,
        'background_color': Color.CONTENT.value,
        'color' :  TextColor.HEADER.value,
        '_hover': {
            'background_color': Color.SECONDARY.value,
            
        }
    },
    
    rx.link: {
        'text_decoration':  'none',
    },
    rx.avatar: {
        'padding' : '2px',
        'border' : '4px solid',
        'border_color' : Color.ALTERNATIVE.value
    },
    'font_family': 'Nunito',
    'background_color' :Color.BACKGROUND.value,
}

navbar_title_style = dict(
    font_family = 'Tilt Neon',
    font_size =  Size.LARGE.value,
)

title_style = dict (
    font_family = 'Nunito'
)

