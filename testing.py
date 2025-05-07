from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tabulate import tabulate
import time

# Input locations
origin_city = "Bangalore"
destination_city = "Hyderabad"

# Selenium WebDriver setup
browser = webdriver.Chrome()
browser.get("https://www.cleartrip.com/")
wait_driver = WebDriverWait(browser, 20)

popup_close = wait_driver.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/div/div[2]/div/div[1]/div[2]"))
)
popup_close.click()

flight_tab = wait_driver.until(
    EC.element_to_be_clickable((By.XPATH, "/html/body/main/div/div[2]/div/div[1]/div[1]/div/div[2]/div/a[1]"))
)
flight_tab.click()

# From location
origin_input = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where from?']")))
origin_input.clear()
origin_input.send_keys(origin_city)
time.sleep(2)

origin_select = wait_driver.until(EC.element_to_be_clickable((By.XPATH, f"//ul//li//p[contains(text(), '{origin_city}')]")))
origin_select.click()

# To location
destination_input = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Where to?']")))
destination_input.clear()
destination_input.send_keys(destination_city)
time.sleep(2)

destination_select = wait_driver.until(EC.element_to_be_clickable((By.XPATH, f"//li//p[contains(text(), '{destination_city}')]/..")))
browser.execute_script("arguments[0].click();", destination_select)

# Calendar interaction
calendar_open = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div")))
browser.execute_script("arguments[0].click();", calendar_open)
time.sleep(10)

trip_type_tab = wait_driver.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div[1]')))
trip_type_tab.click()
time.sleep(2)

trip_round_option = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "//li[normalize-space()='Round trip']")))
trip_round_option.click()

# Dates
date_picker = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[1]")))
date_picker.click()

departure_date = wait_driver.until(EC.element_to_be_clickable((By.XPATH, '//div[@aria-label="Sun May 18 2025"]')))
departure_date.click()
time.sleep(1)

return_date = wait_driver.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[4]/div/div/div/div[4]/div[3]/div/div[2]/div[2]/div[3]/div[2]/div[1]')))
return_date.click()
time.sleep(1)

# Submit Search
search_flights_btn = wait_driver.until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/main/div/div/div/div[1]/div[1]/div/div[1]/div[2]/div/div[7]/button")))
search_flights_btn.click()

# Wait for result loading
time.sleep(10)

wait_driver.until(EC.presence_of_element_located((By.XPATH, '//*[contains(@class, "result") or contains(text(), "₹")]')))

# Try various flight result selectors
flight_result_blocks = None
for card_locator in [
    (By.XPATH, "//p[contains(@class, 'm-0 fs-6 fw-700 c-neutral-900 ta-right')]"),
    (By.XPATH, "//p[contains(@class, 'm-0 fs-2 fw-400 c-grey-70 ta-center lh-copy')]") 
]:
    try:
        wait_driver.until(EC.presence_of_all_elements_located(card_locator))
        flight_result_blocks = browser.find_elements(*card_locator)[:5]
        if flight_result_blocks:
            print(f"Found {len(flight_result_blocks)} flights with locator: {card_locator}")
            break
    except:
        continue

if not flight_result_blocks:
    print("No Flights Found")
    browser.quit()
    exit()

flight_details = []
flight_seen_set = set()

for flight_block in flight_result_blocks:
    try:
        try:
            route_text = flight_block.find_element(By.XPATH, './/*[contains(text(), "→") or contains(text(), "-")]').text
            start_point, end_point = route_text.split("→") if "→" in route_text else route_text.split("-")
            start_point, end_point = start_point.strip(), end_point.strip()
        except:
            start_point, end_point = origin_city, destination_city

        try:
            flight_duration = flight_block.find_element(By.XPATH, "//p[contains(@class, 'm-0 fs-2 fw-400 c-grey-70 ta-center lh-copy')]").text.strip()
        except:
            flight_duration = "N/A"

        try:
            airline_name = flight_block.find_element(By.XPATH, "//p[contains(@class, 'c-neutral-700 fs-1')]").text.strip()
        except:
            airline_name = "Unknown"

        try:
            flight_price = flight_block.find_element(By.XPATH, "//p[contains(@class, 'm-0 fs-6 fw-700 c-neutral-900 ta-right')]").text.strip()
        except:
            flight_price = "N/A"

        flight_signature = (airline_name, flight_duration, flight_price)

        if flight_signature not in flight_seen_set:
            flight_seen_set.add(flight_signature)
            flight_details.append([start_point, end_point, flight_duration, airline_name, flight_price])
    except NoSuchElementException:
        continue

# Display table
if flight_details:
    print(tabulate(flight_details, headers=["From", "To", "Duration", "Airline Name", "Price"], tablefmt="grid"))
else:
    print("No flights found.")

# Cleanup
browser.quit()