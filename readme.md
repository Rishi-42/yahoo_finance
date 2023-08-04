# Stock Price Notification Web Application

This is a web application that allows users to receive notifications when the price of a given stock reaches a certain threshold. Users can enter a stock ticker symbol and a price threshold, and the application will send a notification (email or text message) when the stock's price reaches or exceeds the specified threshold. The application uses the Yahoo Finance API to retrieve stock market data.

## Features

- Enter a stock ticker symbol and a price threshold.
- Specify the frequency to check the stock's price (e.g., hourly, daily, etc.).
- Choose the type of notification to receive (email, text message, etc.).

## Getting Started

### Prerequisites

- Python 3.x
- Flask
- SQLite

### Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/yahoo_finance.git
   cd yahoo_finance

2. **Install project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Start the development server**:

    ```bash
    fask --app app run
    ```

4. **Access the application in your web browser at** `http://localhost:5000`


## File Structure
```
yahoo_finance/
|-- instance/
|   |-- Finance.sqlite3
|-- static/
|   |-- css/
|   |-- js/
|-- templates/
|-- app.py
|-- models.py
|-- notification.py
|-- requirements.txt
|-- README.md
```
- instance: Contains the SQLite database (finance.db) for storing user preferences and notification data.
- static: Contains static assets such as CSS and JavaScript files.
- templates: Contains HTML templates for rendering the web pages.
- app.py: The main Flask application file.
- models.py: Defines the database models for user preferences.
- notification.py: Handles sending notifications to users.