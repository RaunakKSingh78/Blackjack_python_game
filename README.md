---

# Python Object-Oriented Blackjack

Welcome to my first Python project! This is a command-line implementation of the classic casino game **Blackjack** (21). Built entirely from scratch using **Object-Oriented Programming (OOP)** principles, this project helped me master key concepts like classes, instances, encapsulation, and game logic control flows.

---

## 🌟 Key Features

* **Fully Object-Oriented Design:** The game structure is split into logical real-world components (Cards, Decks, Hands, and Game loops).
* **Dynamic Ace Valuation:** Automatically checks your score and adjusts Ace values from 11 down to 1 if your hand is about to bust.
* **Authentic Dealer AI:** The dealer hides their first card on the deal and strictly follows standard casino rules (hitting on anything under 17 and standing on 17 or higher).
* **Multi-Round Sessions:** Input how many games you want to play upfront and play through a full series uninterrupted.

---

## 🏗️ Architecture & OOP Concepts Used

The code relies on four interconnected classes to model the game state accurately:

### 1. `Card`

Defines individual cards. Each card object contains unique properties for its **suit** (spades, diamonds, clubs, hearts) and its **rank** (A, 2-10, J, Q, K), alongside its numeric game value.

### 2. `Deck`

Constructs a complete standard 52-card deck using nested loops. It includes methods to `shuffle()` using Python's `random` module and `deal()` cards while handling deck depletion safely.

### 3. `Hand`

Manages the collection of cards held by either the player or the dealer. It handles:

* Calculating current total hand values.
* Managing the contextual Ace logic ($11 \rightarrow 1$).
* Evaluating whether the hand is an instant Natural Blackjack (21).
* Rendering the UI (including masking the dealer's face-down card).

### 4. `Game`

The orchestration engine. It controls user inputs (input error prevention for valid integer sessions), manages the hit/stand decision loops, tracks standard player actions, executes dealer rules, and evaluates win/loss/draw conditions.

---

## 🚀 How to Run the Game

### Prerequisites

Make sure you have Python installed on your machine (Python 3.x is recommended). No external libraries are required!

### Setup & Execution

1. **Clone this repository:**
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY_NAME.git

```


2. **Navigate into the project directory:**

```bash
   cd YOUR_REPOSITORY_NAME

```

3. **Run the script:**

```bash
   python blackjack.py

```

---

## 🎮 How to Play

1. Upon running the script, enter the number of game rounds you wish to play.
2. The initial hands will be dealt. Your hand value will show explicitly, while the Dealer's first card remains **HIDDEN**.
3. Type `h` or `hit` to draw another card, or `s` or `stand` to keep your current total.
4. If you bust (go over 21), you lose immediately.
5. Once you stand, the dealer reveals their hidden card and draws until their score hits 17 or greater.
6. Highest valid score under or equal to 21 wins!

---

## 📈 What I Learned

As my very first major Python milestone, this project helped me understand:

* How objects talk to each other (e.g., passing a `Card` popped from a `Deck` instance directly into a `Hand` instance's array).
* The importance of `try/except` blocks to handle invalid user inputs safely without crashing execution.
* Writing dry, reusable class functions (like `.get_value()` and `.check_winner()`) to keep game states organized.

---

### 📝 License

This project is open-source and free to use for educational purposes. Feel free to fork it, add features (like betting systems or splits), and make it your own!

---

### 💡 Tip for updating your repository:

Replace `YOUR_USERNAME` and `YOUR_REPOSITORY_NAME` in the clone command snippet above with your actual GitHub username and the exact repository name you choose!

