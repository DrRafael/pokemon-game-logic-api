# Object-Oriented Pokemon Battle Logic with PokeAPI Integration

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Requests](https://img.shields.io/badge/Requests-2.31%2B-green.svg)](https://requests.readthedocs.io/)
[![pyTelegramBotAPI](https://img.shields.io/badge/TelegramBotAPI-4.12%2B-blue.svg)](https://github.com/eternnoir/pyTelegramBotAPI)

An Object-Oriented Programming (OOP) Telegram bot demonstrating class inheritance, dynamic battle mechanics, and REST API integration with **PokeAPI**.

---

## 🚀 Key Features

* **REST API Integration**: Fetches real-time Pokemon artwork and forms from `PokeAPI` with error handling and request timeouts.
* **OOP Inheritance & Polymorphism**: Extends base `Pokemon` class into specialized subclasses (`Wizard`, `Fighter`) with distinct attack modes.
* **Telegram Bot UI**: Interactive turn-based battles invoked via message replies (`/attack`) and commands (`/go`).
* **Session State Handling**: Maps active Telegram users to their respective Pokemon instances.

---

## 🛠️ Tech Stack

* **Language**: Python 3.10+
* **Framework**: pyTelegramBotAPI
* **HTTP Client**: Requests
* **External API**: PokeAPI

---

## ⚙️ Configuration & Setup

### 1. Clone the repository
git clone https://github.com/DrRafael/pokemon-game-logic-api.git
cd pokemon-game-logic-api

### 2. Install dependencies
pip install -r requirements.txt

### 3. Configure Credentials
Copy `config.py.example` to `config.py` and insert your Telegram Bot Token:
```python
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
