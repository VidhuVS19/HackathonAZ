from selenium import webdriver
from bs4 import BeautifulSoup
import time
import re

driver=webdriver.Chrome()

#url="https://leetcode.com/problemset/all/?page="
# Define the base URL and pattern for the pages
base_url = "https://leetcode.com/problemset/all/?page="  
url_pattern = r"leetcode\.com/problemset/all/\?page=/\d+" 

# List to store all extracted hrefs
all_hrefs = []

# Loop through the pages
for page_number in range(1, 55):  # Replace the range values with the desired page numbers
    # Construct the URL for the current page
    url = base_url + str(page_number)
    driver.get(url)

    #To wait a few seconds to give time for the page to load
    time.sleep(7)

    #Extract page source using BeautifulSoup
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # Find all <a> elements with a certain pattern in their href attribute
    pattern = r'leetcode\.com/problems/' 
    regex = re.compile(pattern)
    try:
        a_elements = soup.find_all('a', href=regex)
    except:
        #print("ERROR-1")
        pass

    hrefs = [a.get('href') for a in a_elements]
    all_hrefs.extend(hrefs)

#To avoid duplicates
all_hrefs2=list(set(all_hrefs))

# Create a new text file
filename = "leetcode.txt"
with open(filename, "w") as file:
# Write the href attribute of each <a> element to the file
    for href in all_hrefs2:
        try:
            file.write(href + "\n")
        except:
            pass

#Quit the webdriver
driver.quit()