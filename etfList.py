from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import json
import requests


def main():
  path = './chromedriver'
  browser = webdriver.Chrome(path)
  url = "https://www.twse.com.tw/zh/page/ETF/list.html"
  browser.get(url)
  tbody = browser.find_element_by_tag_name('tbody')
  trList = tbody.find_elements_by_tag_name('tr')
  data = []
  for tr in trList:
    tdlist = tr.find_elements_by_tag_name('td')
    # print(tdlist[0].text)
    name = tdlist[2].text
    code = tdlist[1].text
    data.append({
      "name": name,
      "code": code
    })
  for d in data:
    print(d)

  browser.close()


main()