import reflex as rx
import random
from typing import List, Tuple

# Define a soft color palette
LIGHT_BLUE = "#ADD8E6"
LIGHT_GREEN = "#D4EDDA" # A softer green
LIGHT_YELLOW = "#FFF3CD" # A softer yellow
LIGHT_PINK = "#F8D7DA" # A softer pink
WHITE = "#FFFFFF"
BLACK = "#000000"
GRAY = "#E0E0E0" # A softer gray

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

class RummyState(rx.State):
    deck: List[Tuple[str, str]] = []
    discard_pile: List[Tuple[str, str]] = []
    player_hand: List[Tuple[str, str]] = []
    winner: bool = False
    turn_phase: str = "draw" # "draw" or "discard"

    def start_game(self):
        self.deck = [(rank, suit) for suit in SUITS for rank in RANKS]
        random.shuffle(self.deck)
        self.player_hand = [self.deck.pop() for _ in range(10)]
        self.discard_pile = [self.deck.pop()]
        self.winner = False
        self.turn_phase = "draw"

    def draw_from_deck(self):
        if self.turn_phase == "draw" and self.deck:
            self.player_hand.append(self.deck.pop())
            self.turn_phase = "discard"

    def draw_from_discard(self):
        if self.turn_phase == "draw" and self.discard_pile:
            self.player_hand.append(self.discard_pile.pop())
            self.turn_phase = "discard"

    def discard(self, card: Tuple[str, str]):
        if self.turn_phase == "discard":
            if card in self.player_hand:
                self.player_hand.remove(card)
                self.discard_pile.append(card)
                self.turn_phase = "draw"
                self.check_for_winner()

    def check_for_winner(self):
        if len(self.player_hand) == 0:
            self.winner = True

def card_component(card: Tuple[str, str], is_discardable: rx.Var[bool]):
    base_box_props = {
        "border": "1px solid #ccc",
        "padding": "20px 10px",
        "border_radius": "10px",
        "bg": WHITE,
        "width": "80px",
        "height": "120px",
        "display": "flex",
        "align_items": "center",
        "justify_content": "center",
        "box_shadow": "0px 2px 4px rgba(0,0,0,0.1)",
    }

    return rx.cond(
        is_discardable,
        rx.box(
            rx.text(f"{card[0]}{card[1]}", font_size="2em", color="black"),
            **base_box_props,
            on_click=lambda: RummyState.discard(card),
            cursor="pointer",
            opacity="1",
        ),
        rx.box(
            rx.text(f"{card[0]}{card[1]}", font_size="2em", color="black"),
            **base_box_props,
            cursor="default",
            opacity="0.7",
        )
    )

def player_hand(hand: List[Tuple[str, str]]):
    return rx.hstack(
        rx.foreach(
            hand,
            lambda card: card_component(
                card,
                is_discardable=(RummyState.turn_phase == "discard")
            )
        ),
        spacing="4"
    )

def discard_pile_component():
    return rx.box(
        rx.cond(
            RummyState.discard_pile,
            card_component(
                RummyState.discard_pile[-1],
                is_discardable=(RummyState.turn_phase == "draw")
            ),
            rx.text("No discard yet", color=BLACK)
        ),
        width="100px",
        height="150px",
        border="2px dashed " + GRAY,
        display="flex",
        align_items="center",
        justify_content="center",
        opacity=rx.cond(RummyState.turn_phase == "draw", "1", "0.5"),
        pointer_events=rx.cond(RummyState.turn_phase == "draw", "auto", "none"),
    )

def rules_accordion():
    return rx.accordion.root(
        rx.accordion.item(
            header="How to Play",
            content=rx.text(
                "This is a simple version of Rummy. The goal is to get rid of all your cards. On your turn, first draw a card from either the deck or the discard pile. Then, discard one card from your hand by clicking on it."
            ),
        ),
        collapsible=True,
        width="100%",
    )

def index():
    return rx.container(
        rx.vstack(
            rx.heading("Simple Rummy", size="9", color=BLACK),
            rules_accordion(),
            rx.button("Start New Game", on_click=RummyState.start_game, color_scheme="blue"),
            rx.cond(
                RummyState.winner,
                rx.heading("You Win!", size="8", color="green"),
                rx.vstack(
                    rx.text(
                        rx.cond(
                            RummyState.turn_phase == "draw",
                            "Draw a card from the deck or discard pile.",
                            "Discard a card from your hand."
                        ),
                        font_size="1.8em", # Make it more prominent
                        color=BLACK,
                        font_weight="bold"
                    ),
                )
            ),
            rx.heading("Your Hand", size="4", color=BLACK),
            player_hand(RummyState.player_hand),
            rx.hstack(
                rx.vstack(
                    rx.heading("Deck", size="4", color=BLACK),
                    rx.box(
                        rx.text("Draw", font_size="2em", color=BLACK),
                        width="100px",
                        height="150px",
                        border="2px solid " + BLACK,
                        display="flex",
                        align_items="center",
                        justify_content="center",
                        on_click=RummyState.draw_from_deck,
                        cursor="pointer",
                        opacity=rx.cond(RummyState.turn_phase == "draw", "1", "0.5"),
                        pointer_events=rx.cond(RummyState.turn_phase == "draw", "auto", "none"),
                        bg=LIGHT_BLUE # Soft color for deck
                    )
                ),
                rx.vstack(
                    rx.heading("Discard Pile", size="4", color=BLACK),
                    discard_pile_component()
                ),
                spacing="4"
            ),
            spacing="4",
            align="center"
        ),
        bg=LIGHT_GREEN, # Overall background color
        min_height="100vh", # Ensure background covers full height
        padding="20px"
    )

app = rx.App()
app.add_page(index)
