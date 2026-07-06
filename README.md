# python-internship
CodeAlpha Python internship
# 🐍 Python Tasks

A collection of four beginner-friendly Python tasks covering core programming concepts — loops, dictionaries, file handling, and more.

---

## 📋 Table of Contents

- [Task 1 — Hangman Game](#task-1--HangmanGame)
- [Task 2 — Stock Portfolio Tracker](#task-2--StockTracker)
- [Task 3 — Task Automation Scripts](#task-3--TaskAutomation)-
  - - [Task 3a — Task Automation Scripts](#task-3a--Movefolders)
  - - [Task 3b — Task Automation Scripts](#task-3b--exyractemail)
  - - [Task 3c — Task Automation Scripts](#task-3c--webpageScraper)
- [Task 4 — Basic Chatbot](#task-4--chatbot)
- [Requirements](#requirements)
- [How to Run](#how-to-run)

---

## Task 1 — Hangman Game

A classic word-guessing game played entirely in the console.

**Features**
- 5 predefined words with hints
- ASCII gallows that builds with each wrong guess
- Maximum 6 incorrect guesses
- Input validation and replay option

**Concepts used:** `random`, `while` loop, `if-else`, strings, lists

**Run:**
```bash
python HangmanGame.py
```

**Sample output:**
```
========================================
         HANGMAN
========================================
  Hint: A popular programming language
  The word has 6 letters.

       -----
       |   |
           |
  Word: _ _ _ _ _ _
  Guess a letter: p
  'P' is in the word!
```

---

## Task 2 — Stock Portfolio Tracker

A simple tracker that calculates the total value of a user's stock holdings.

**Features**
- Hardcoded price dictionary (`APPL`, `TSLA`, `GOGL`, etc.)
- User inputs stock symbol and quantity
- Displays per-stock value and total portfolio value
- Optionally saves results to a `.txt` or `.csv` file

**Concepts used:** dictionary, `input()`/`output`, arithmetic, file handling

**Run:**
```bash
python StockTracker.py
```

**Sample output:**
```
Enter stock symbol (or 'done' to finish): APPL
Enter quantity: 5
Enter stock symbol (or 'done' to finish): TSLA
Enter quantity: 2

--- Portfolio Summary ---
APPL   x5   @ $180   =  $900.00
TSLA   x2   @ $250   =  $500.00
Total investment: $1400.00
```

---

## Task 3 — Task Automation Scripts

Three standalone automation scripts for common repetitive tasks.

### 3a — Move JPG Files
Scans a source folder and moves all `.jpg` files into a new destination folder, creating it if it doesn't exist.

```bash
python movefolders.py
```

**Concepts used:** `os`, `shutil`

---

### 3b — Extract Emails
Reads a `.txt` file, finds all email addresses using a regex pattern, and saves them to a new file.

```bash
python extractemail.py
```

**Concepts used:** `re`, file handling

---

### 3c — Webpage Title Scraper
Fetches a fixed URL and extracts the page `<title>`, then saves it to a text file.

```bash
python webpageScraper.py
```

**Concepts used:** `requests`, file handling

---

## Task 4 — Basic Chatbot

A rule-based chatbot that responds to common phrases via keyword matching.

**Features**
- Recognises greetings, questions, and farewells
- Friendly fallback response for unknown input
- Runs in a continuous loop until the user says goodbye

**Concepts used:** `if-elif`, functions, loops, `input()`/`output`

**Run:**
```bash
python chatbot.py
```

**Sample output:**
```
Chatbot: Hello! I'm ready to chat. Type 'bye' to exit.
You: hello
Chatbot: Hi there! How can I help you?
You: how are you
Chatbot: I'm doing great, thanks for asking!
You: bye
Chatbot: Goodbye! Have a great day!
```

---

## Requirements

- Python 3.7 or higher
- Project 3c only requires the `requests` library:

```bash
pip install requests
```

No other external dependencies.

---

## How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/python-mini-projects.git
   cd python-mini-projects
   ```

2. **Run any project directly**
   ```bash
   python hangman.py
   python stock_tracker.py
   python chatbot.py
   ```

3. **For the automation scripts**, update the folder paths or file names inside the script before running.

---

## 📁 Project Structure

```
python-mini-tasks/
│
├── hangman.py            # Task 1
├── stock_tracker.py      # Task 2
├── move_jpgs.py          # Task 3a
├── extract_emails.py     # Task 3b
├── scrape_title.py       # Task 3c
├── chatbot.py            # Task 4
└── README.md
```

---

