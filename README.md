# Binance Futures Testnet Trading Bot
## Overview
---
A Python-based trading bot for placing MARKET and LIMIT orders on Binance Futures Testnet.
The application provides a simple command-line interface (CLI) for order placement and includes input validation, logging, and error handling.
---
## Features
* Place MARKET orders
* Place LIMIT orders
* Support for BUY and SELL orders
* Command Line Interface (CLI)
* Input validation
* Exception handling
* API request and response logging
---
## Project Structure
```text
trading_bot/
│
├── bot/
│   ├── client.py
│   ├── orders.py
│   ├── validators.py
│   └── logging_config.py
│
├── cli.py
├── requirements.txt
├── README.md
└── .env
```
---
## Requirements
* Python 3.x
* Binance Account
* Binance Futures Testnet API Credentials
---
## Installation
### Clone the Repository
```bash
git clone <repository-url>
cd trading_bot
```
### Create a Virtual Environment
```bash
python -m venv venv
```
### Activate the Virtual Environment
Windows:
```bash
venv\Scripts\activate
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
---
## Environment Variables
Create a `.env` file in the project root directory:
```env
BINANCE_API_KEY=your_api_key
BINANCE_SECRET_KEY=your_secret_key
```
---
## Running the Application
```bash
python cli.py
```
### Example Input
```text
Enter Symbol (e.g. BTCUSDT): BTCUSDT
Enter Side (BUY/SELL): BUY
Enter Order Type (MARKET/LIMIT): MARKET
Enter Quantity: 0.001
```
---
## Validation
The application validates:
* Order side (BUY/SELL)
* Order type (MARKET/LIMIT)
* Quantity greater than zero
* Price requirement for LIMIT orders
---

