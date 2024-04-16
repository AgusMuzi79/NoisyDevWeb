import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.styles.sizes import Size 
from link_bio.components.title import title
from link_bio.styles.styles import *
from link_bio.constants.constants_urls import *

def links() -> rx.Component:
    return rx.vstack(
        title(
            'Redes Sociales',
        ),
        link_button(
            'instagram',
            'NoisyDev',
            INSTAGRAM_NOISYDEV
        ),
        link_button(
            'twitter',
            'Twitter', 
            TWITTER_NOISYDEV
        ),
        link_button(
            'youtube',
            'Youtube', 
            YOUTUBE_NOISDEV
        ),
        
        title(
            'Contacto',
        ),
        link_button(
            'inbox',
            'agusmuzi79@gmail.com',
            f'mailto:{EMAIL_PERSONAL}'
        ),
        link_button(
            'linkedin',
            'LinkedIn',
            LINKEDIN
        ),
        title(
            'Recursos'
        ),
        link_button(
            'github',
            'Github', 
            GITHUB_NOISYDEV
        ),
        link_button(
            'book_user',
            'Notion CV',
            NOTION_CV
        ),
        margin = Size.ZERO.value,
        padding = Size.SMALL.value,
        width = '100%',
        height = '100%'
    )
    
