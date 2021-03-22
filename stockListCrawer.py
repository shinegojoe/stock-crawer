from time import sleep
from selenium import webdriver


class StockListCrawer:
  def __init__(self):
    self.url = "https://www.twse.com.tw/zh/listed/listingProfile"
    path = './chromedriver'
    self.browser = webdriver.Chrome(path)
    self.browser.implicitly_wait(30)

  def getStock(self):
    stocks = self.browser.find_element_by_class_name("stocks")\
    .find_element_by_class_name("items")\
    .find_elements_by_tag_name("a")
    # for s in stocks:
    #   print(s.text)
    print(len(stocks))
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
      # print(val)
      if "http" not in val:
        print(val)
        c.click()
        sleep(1)
        self.getStock()
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

