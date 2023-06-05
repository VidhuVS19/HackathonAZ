import requests
from selenium import webdriver
from bs4 import BeautifulSoup
import time

driver=webdriver.Chrome()

#Taking only 1 url for now(If it works, all urls will be read through the file and operated upon)
url="https://leetcode.com/problems/find-the-k-beauty-of-a-number/"

