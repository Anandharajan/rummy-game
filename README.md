# Simple Rummy Game

This is a simple, single-player Rummy card game built with [Reflex](https://reflex.dev/). The goal is to get rid of all your cards by forming melds.

## How to Play

1.  Click the "Start New Game" button.
2.  The game will tell you when to draw a card and when to discard.
3.  Draw a card by clicking on the deck or the discard pile.
4.  Discard a card from your hand by clicking on it.
5.  The game ends when you have no cards left in your hand.

## Setup and Installation

### Prerequisites

*   Python 3.11
*   Node.js 18+
*   Git

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd rummy
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    *   **Windows (PowerShell):** `.\venv\Scripts\Activate.ps1`
    *   **Windows (Git Bash):** `source venv/Scripts/activate`
    *   **macOS/Linux:** `source venv/bin/activate`

4.  **Install the dependencies:**
    ```bash
    pip install -r rummy_game/requirements.txt
    ```

## Running the Game Locally

To run the game locally, execute the following command from the `rummy_game` directory:

```bash
reflex run
```

The app will be available at `http://localhost:3000`.

## Deployment

This app can be deployed to [Reflex Cloud](https://reflex.dev/docs/hosting/deploying-to-reflex-cloud/).

1.  **Login to Reflex Cloud:**
    ```bash
    reflex login
    ```

2.  **Deploy the app:**
    ```bash
    reflex deploy
    ```
