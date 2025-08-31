import reflex as rx

config = rx.Config(
    app_name="rummy_game",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)