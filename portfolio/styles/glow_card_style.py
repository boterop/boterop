import reflex as rx

glow_card_style = {
    ":root": {
        "--backdrop": "hsl(0 0% 60% / 0.12)",
        "--radius": 14,
        "--border": 3,
        "--backup-border": "var(--backdrop)",
        "--size": 200,
    },
    "article:first-of-type": {
        "--base": 80,
        "--spread": 500,
        "--outer": 1,
    },
    "article:last-of-type": {
        "--outer": 1,
        "--base": 220,
        "--spread": 200,
    },
}
