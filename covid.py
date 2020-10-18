from flask import Flask
import requests

app = Flask(__name__)

# TODO: create your app here
# Basic requirements:
# 1. From page displays list of countries
# 2. Every country is "clickable"
# 3. Clicking country takes us to a page with summary
# info for this countrie (total cases, total deaths etc.)
if __name__ == '__main__':
    countries = requests.get("https://api.covid19api.com/countries")
    tanzania_info = requests.get("https://api.covid19api.com/total/country/tanzania")
