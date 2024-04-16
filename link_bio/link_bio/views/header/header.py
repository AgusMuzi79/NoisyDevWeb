import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.styles.sizes import Size
from link_bio.styles.colors import *
from link_bio.styles.fonts import *
from link_bio.constants.constants_urls import *


def header () -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(
                src='Cara.jpeg', 
                size = '8', 
                radius='full',
            ),
            rx.vstack(
                rx.heading(
                    'Agustin Muzi',
                    size='7',
                    color = TextColor.HEADER.value,
                    font_family = Font.TEXT.value,
                ),
                rx.text(
                    '@noisydev',
                    margin_top = Size.ZERO.value,
                    margin_bottom = Size.SMALL.value,
                    color = Color.ALTERNATIVE.value 
                ),
                rx.hstack (
                    link_icon('instagram', INSTAGRAM_NOISYDEV),
                    link_icon('github', GITHUB_NOISYDEV),
                    link_icon('twitter', TWITTER_NOISYDEV),
                    link_icon('linkedin', LINKEDIN),
                    link_icon('music-2', TIKTOK_NOISYDEV),
                    align='center',
                    spacing='3'
                ),
                spacing='0',
                align_items='start'  
            ), 
            align='center',
        ),
        
        rx.text(
            '''Hola! Soy Agus, estoy actualmente estudiando
            desarrollo web para ser fullstack developer en la UNICEN.
            Hago diseño web en Python utilizando Reflex. Aqui podras encontrar
            todos mis enlaces de interes Bienvenid@!''',
            color = TextColor.BODY.value,
        ),
        align_items='start', 
        margin = Size.SMALL.value
    )    
        
        
        
        
        
        
        
        
    