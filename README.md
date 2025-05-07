# ✈️ Cleartrip Flight Scraper with Selenium

This project is a Python script that uses **Selenium WebDriver** to automate searching for **round-trip flights** between two Indian cities (e.g., Bangalore → Hyderabad) on [Cleartrip](https://www.cleartrip.com). The script extracts flight details such as duration, airline, and price, and displays them in a tabular format using the `tabulate` library.

---

## 🚀 Features

- Automatically opens the Cleartrip website
- Handles popups and navigates to the flight booking tab
- Enters origin and destination cities
- Selects departure and return dates
- Scrapes flight data (airline, duration, and price)
- Displays results in a table format

---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.7+
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and added to PATH
- Selenium
- Tabulate

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/cleartrip-flight-scraper.git
cd cleartrip-flight-scraper


## 📂 Project Structure

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate



---

## 🛠️ Requirements

Make sure you have the following installed:

- Python 3.7+
- Google Chrome browser
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) installed and added to PATH
- Selenium
- Tabulate

---

## 📦 Installation

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/cleartrip-flight-scraper.git
cd cleartrip-flight-scraper


##Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

#install Dependencies

pip install -r requirements.txt


##requirements

pip install selenium tabulate


##Run the script

python flight_scraper.py

##Output

+------------+-------------+-----------+-----------------+----------+
| From       | To          | Duration  | Airline Name    | Price    |
+------------+-------------+-----------+-----------------+----------+
| Bangalore  | Hyderabad   | 1h 25m    | Indigo Airlines | ₹4,293   |
| ...        | ...         | ...       | ...             | ...      |
+------------+-------------+-----------+-----------------+----------+



