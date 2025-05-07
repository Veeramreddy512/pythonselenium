# Cleartrip Flight Scraper

This Python script automates the process of searching for round-trip flights on [Cleartrip.com](https://www.cleartrip.com) using Selenium, extracts details of the top few flights, and displays the results in a tabular format.

## 🚀 Features

- Automates round-trip flight search using Chrome.
- Inputs source (`Bangalore`) and destination (`Hyderabad`) cities.
- Selects custom departure and return dates.
- Scrapes flight results (Airline, Duration, Price).
- Displays results in a clean table using the `tabulate` library.

---

## 🧰 Requirements

- Python 3.x
- Google Chrome
- [ChromeDriver](https://sites.google.com/a/chromium.org/chromedriver/) (must match your Chrome version)
- Python packages:
  - `selenium`
  - `tabulate`

You can install the required packages using:

```bash
pip install selenium tabulate
