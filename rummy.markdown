# Build a Simple Rummy Game with Reflex and GitHub!

This guide will help you build and deploy a fun, simple Rummy game web app using Python and Reflex. We'll make it super easy for anyone, even kids, to understand and play! You'll also learn how to put your game on GitHub for everyone to see.

## What You'll Need (Prerequisites)

Before we start, make sure you have these tools installed on your Windows computer:

*   **Python 3.11**: This is the programming language we'll use. Get it from [python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/).
*   **Node.js 18+**: This helps Reflex build the web part of our game. Download it from [nodejs.org](https://nodejs.org/dist/v20.17.0/node-v20.17.0-win-x64.zip).
*   **Git**: This is a tool to keep track of our code changes and share them on GitHub. Install it from [git-scm.com/download/win](https://git-scm.com/download/win).
*   **VSCode**: A great tool for writing code. Get it from [code.visualstudio.com](https://code.visualstudio.com/).
*   **Reflex Cloud Account**: This is where we'll put our game online. Sign up for free at [reflex.dev](https://reflex.dev).

## Let's Build Our Game! (Checklist)

Follow these steps to create your Rummy game:

### 1. Get Ready (Install Dependencies)

First, let's install some important software.

*   **Install Python 3.11**:
    *   Run the installer you downloaded. Make sure to check the box that says "Add Python to PATH" during installation!
    *   **Check if it worked:** Open your Command Prompt (CMD) and type:
        ```bash
        python --version
        ```
        You should see something like `Python 3.11.8` or `Python 3.11.9`.

*   **Install Node.js**:
    *   Unzip the Node.js file you downloaded to a simple location, like `C:\node-v20.17.0-win-x64`.
    *   **Tell your computer where Node.js is:** Open Command Prompt (CMD) and type:
        ```bash
        setx PATH "%PATH%;C:\node-v20.17.0-win-x64"
        ```
    *   **Check if it worked:** In a *new* Command Prompt window, type:
        ```bash
        node --version
        npm --version
        ```
        You should see versions like `v21.7.1` and `10.9.1`.

*   **Install Git**:
    *   Run the Git installer. You can usually click "Next" through the options.
    *   **Check if it worked:** Open Command Prompt (CMD) and type:
        ```bash
        git --version
        ```
        You should see a Git version number.

### 2. Make a Home for Your Game (Set Up Project Directory)

We need a special folder for our game.

*   **Create your game folder:** In your Command Prompt (CMD), go to where you want to save your game (e.g., `cd C:\Users\YourName\Desktop`) and type:
    ```bash
    mkdir rummy_game
    ```
    (If you already have a folder named `rummy_game`, you can skip this step!)

### 3. Create a Special Python Space (Set Up Virtual Environment)

This keeps our game's Python tools separate from other Python projects.

*   **Create the special space:** In Command Prompt (CMD), type:
    ```bash
    python -m venv rummy_game\venv
    ```

### 4. Get Reflex Ready (Install Reflex CLI)

Reflex is the magic tool that turns our Python code into a web game!

*   **Install Reflex:** In Command Prompt (CMD), type:
    ```bash
    rummy_game\venv\Scripts\pip.exe install --upgrade reflex
    ```
*   **Check if it's there:**
    ```bash
    rummy_game\venv\Scripts\pip.exe show reflex
    ```
    Look for `Version: 0.5.0+` (like `0.8.8`).

### 5. Get Gemini Ready (Install Gemini CLI)

Gemini can help us with code! (We used it to help debug the game).

*   **Check if Gemini is installed:**
    ```bash
    gemini --version
    ```
    If you see a version number (like `0.2.2`), you're good! If not, you might need to install it using `npm install -g @google/gemini-cli` and then authenticate by just typing `gemini` and following the browser steps.

### 6. Start Your Reflex Project! (Initialize Reflex App)

Now, let's tell Reflex to set up our game's basic files.

*   **Initialize your app:** In Command Prompt (CMD), type:
    ```bash
    cmd /c "cd rummy_game && venv\Scripts\reflex.exe init --template blank"
    ```
    This tells Reflex to create a blank game project inside your `rummy_game` folder.

*   **Check the game's files:** You should now see new files and folders inside your `rummy_game` folder, like `rummy_game\rummy_game.py` and `rxconfig.py`.

### 7. Write the Game Code!

We've already written the code for you! It makes a simple Rummy game with friendly colors and clear instructions.

*   **Open the game file:**
    ```bash
    notepad rummy_game\rummy_game\rummy_game.py
    ```
    (You can also open this file in VSCode: `code rummy_game\rummy_game\rummy_game.py`)

*   **Replace the code:** Copy all the game code from the GitHub repository's `rummy_game/rummy_game/rummy_game.py` file and paste it into your `notepad` (or VSCode) window, replacing everything that's already there. Save the file!

### 8. Test Your Game on Your Computer! (Local Test)

Let's see if our game works on your computer before putting it online.

*   **Run the game:** In Command Prompt (CMD), type:
    ```bash
    cmd /c "cd rummy_game && venv\Scripts\reflex.exe run"
    ```
    This will start your game!

*   **Play the game!** Open your web browser and go to `http://localhost:3000`.
    *   Look for the "Simple Rummy" title and the "How to Play" section.
    *   Try clicking "Start New Game".
    *   Can you draw a card? Can you discard a card? The game should tell you what to do!

### 9. Get Ready for Online (Generate Requirements File)

We need a list of all the special Python tools our game uses so Reflex Cloud knows what to install.

*   **Create the list:** In Command Prompt (CMD), type:
    ```bash
    rummy_game\venv\Scripts\pip.exe freeze > rummy_game\requirements.txt
    ```
*   **Check the list:** You can open `rummy_game\requirements.txt` with Notepad to see what's inside.

### 10. Put Your Game Online! (Deploy to Reflex Cloud)

Now, let's share your game with the world!

*   **Login to Reflex Cloud:** You'll need to tell Reflex who you are.
    ```bash
    reflex login
    ```
    This will open a web page for you to log in with your Google or GitHub account. After you log in, come back to the Command Prompt and press Enter.

*   **Deploy your game:** Once logged in, type this command. Remember to replace `YOUR_TOKEN_HERE` with the special token you got from your Reflex Cloud account settings (look for "Tokens" in your account settings on the Reflex website).
    ```bash
    cmd /c "cd rummy_game && venv\Scripts\reflex.exe deploy --app-name rummy_game --token YOUR_TOKEN_HERE --no-interactive"
    ```
    This might take a few minutes. When it's done, you'll see a special link (URL) to your game!

*   **Play your game online!** Go to the URL that Reflex gives you (it will look something like `https://rummy-game-gray-grass.reflex.run`).

### 11. Share Your Game on GitHub!

Let's put all your game's files on GitHub so you can share them easily.

*   **Initialize Git (if you haven't already):** In your main `rummy` folder (not `rummy_game`), type:
    ```bash
    git init
    ```
    (We already did this, so it might say "Reinitialized existing Git repository.")

*   **Tell Git about your GitHub home:** Replace `YOUR_GITHUB_REPO_URL` with the link to the empty GitHub repository you created (e.g., `https://github.com/YourUsername/your-game-name.git`).
    ```bash
    git remote add origin YOUR_GITHUB_REPO_URL
    ```
    (If you already added it, it might say "remote origin already exists.")

*   **Add all your game files:**
    ```bash
    git add .
    ```

*   **Save your changes (commit):**
    ```bash
    git commit -m "First version of my Simple Rummy game!"
    ```

*   **Send your game to GitHub!**
    ```bash
    git push -u origin master:main
    ```
    This sends all your game files to your GitHub repository. Now everyone can see your awesome game!

## Play the Game Online!

You can play the game online right now at: [https://rummy-game-gray-grass.reflex.run](https://rummy-game-gray-grass.reflex.run)

## Important Notes for Young Builders

*   **Reflex Versions:** We used Reflex version 0.5.0+ (like 0.8.8).
*   **Gemini Power:** Gemini helped us fix some tricky parts of the code!
*   **More Info:** You can learn more about Reflex at [reflex.dev/docs](https://reflex.dev/docs) and see more code examples at [github.dev/reflex-dev/reflex](https://github.dev/reflex-dev/reflex).

## What We Couldn't Do (Yet!)

Some cool features are a bit too tricky for this simple game right now:

*   **Moving Cards Around:** We can't drag and drop cards to rearrange them in your hand.
*   **Timers:** There's no clock ticking during the game.

But don't worry, your game is still super fun to play!
