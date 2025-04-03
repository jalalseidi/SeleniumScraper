from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome browser open after execution
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

# Open Python events page
driver.get("https://www.python.org/events/")

# Extract event data
events = driver.find_elements(By.CSS_SELECTOR, ".list-recent-events.menu li")

# Store extracted data in a dictionary
event_dict = []
for event in events:
    event_name = event.find_element(By.TAG_NAME, "a").text
    event_date = event.find_element(By.TAG_NAME, "time").text

    event_dict.append({"name": event_name, "time": event_date})

# Print the dictionary
print(event_dict)

# Close the browser
driver.quit()
