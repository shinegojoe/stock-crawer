from time import sleep
from selenium import webdriver
import requests
import json


class StockListCrawer:
  def __init__(self):
    self.url = "https://www.twse.com.tw/zh/listed/listingProfile"
    self.postUrl = "http://167.179.80.227:3002/api/stockList"
    # self.postUrl = "http://localhost:3002/api/stockList"

    path = './chromedriver'
    self.browser = webdriver.Chrome(path)
    self.browser.implicitly_wait(30)

  def writeLog(self, e):
    print(e)
    with open("error.log", "a") as f:
      f.write("\n")
      f.write(str(e) + '\n')

  def addStock(self, category, code, name):
    data = {
      "category": category,
      "code": code,
      "name": name
    }
    # print(data)
    try:
      jsonData = json.dumps(data)
      # print(jsonData)
      r = requests.post(self.postUrl, json=data)

      # resp = requests.post(self.postUrl, data=jsonData)
      print(r.json())
    except Exception as e:
      self.writeLog(e)

  def getStock(self, category):
    stocks = self.browser.find_element_by_class_name("stocks")\
    .find_element_by_class_name("items")\
    .find_elements_by_tag_name("a")
    for s in stocks:
      # print(s.text)
      data = s.text.split(' ')
      if len(data) >=2:
        code = data[0]
        name = data[1]
      else:
        code = data[0]
        name = ""
      # print(code, name)
      self.addStock(category, code, name)
    # print(len(stocks))
    back = self.browser.find_element_by_class_name("back")
    back.click()
    sleep(1)

  def run(self):
    self.browser.get(self.url)
    stockListLink = self.browser.find_element_by_class_name("stock-code-browse")
    stockListLink.click()
    sleep(1)
    stk = self.browser.find_element_by_id("popup").find_element_by_class_name("stk")
    categoryList = stk.find_elements_by_tag_name("a")
    for c in categoryList:
      val = c.get_attribute("data-val")
      category = c.text
      print("category", category)
      if "http" not in val:
        print(val)
        c.click()
        sleep(1)
        try:
          self.getStock(category)
        except Exception as e:
          self.writeLog(e)
      # print(c)
      # c.click()
      # sleep(1)
      # stocks = self.browser.find_element_by_class_name("stocks")\
      # .find_element_by_class_name("items")\
      # .find_elements_by_tag_name("a")
      
      # for s in stocks:
      #   print(s.text)
      # back = self.browser.find_element_by_class_name("back")
      # back.click()
      # sleep(1)

     

    sleep(3)
    self.browser.close()




def main():
  crawer = StockListCrawer()
  crawer.run()

if __name__ == "__main__":
  main()

