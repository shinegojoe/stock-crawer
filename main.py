from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
import json
import requests
import threading



stockList = [
  # {'name': '元大台灣50', 'code': '0050'},
  # {'name': '元大中型100', 'code': '0051'},
  # {'name': '富邦科技', 'code': '0052'},
  # {'name': '元大電子', 'code': '0053'},
  # {'name': '元大台商50', 'code': '0054'},
  # {'name': '元大MSCI金融', 'code': '0055'},
  # {'name': '元大高股息', 'code': '0056'},
  # {'name': '富邦摩台', 'code': '0057'},
  # {'name': '元大寶滬深', 'code': '0061'},
  # {'name': 'BP上證50', 'code': '008201'},
  # {'name': '元大MSCI台灣', 'code': '006203'},
  # {'name': '富邦上証', 'code': '006205'},
  # {'name': '永豐臺灣加權', 'code': '006204'},
  # {'name': '元大上證50', 'code': '006206'},
  # {'name': 'FH滬深', 'code': '006207'},
  # {'name': '富邦台50', 'code': '006208'},
  # {'name': '元大台灣50正2', 'code': '00631L'},
  # {'name': '元大台灣50反1', 'code': '00632R'},
  # {'name': '富邦上証正2', 'code': '00633L'},
  # {'name': '富邦上証反1', 'code': '00634R'},
  # {'name': '國泰中國A50', 'code': '00636'},
  # {'name': '期元大S&P黃金', 'code': '00635U'},
  # {'name': '元大滬深300正2', 'code': '00637L'},
  # {'name': '元大滬深300反1', 'code': '00638R'},
  # {'name': '富邦深100', 'code': '00639'},
  # {'name': '期元大S&P石油', 'code': '00642U'},
  {'name': '富邦日本正2', 'code': '00640L'},
  {'name': '富邦日本反1', 'code': '00641R'},
  {'name': '富邦日本', 'code': '00645'},
  {'name': '群益深証中小', 'code': '00643'},
  # {'name': '元大S&P500', 'code': '00646'},
  # {'name': '元大S&P500正2', 'code': '00647L'},
  # {'name': '元大S&P500反1', 'code': '00648R'},
  # {'name': 'FH香港正2', 'code': '00650L'},
  # {'name': 'FH香港反1', 'code': '00651R'},
  # {'name': '國泰中國A50正2', 'code': '00655L'},
  # {'name': '國泰中國A50反1', 'code': '00656R'},
  # {'name': '富邦印度', 'code': '00652'},
  # {'name': '富邦印度正2', 'code': '00653L'},
  # {'name': '富邦印度反1', 'code': '00654R'},
  # {'name': '國泰日經225', 'code': '00657'},
  # {'name': '元大歐洲50', 'code': '00660'},
  # {'name': '元大日經225', 'code': '00661'},
  # {'name': '富邦NASDAQ', 'code': '00662'},
  # {'name': '國泰臺灣加權正2', 'code': '00663L'},
  # {'name': '國泰臺灣加權反1', 'code': '00664R'},
  # {'name': '富邦恒生國企正2', 'code': '00665L'},
  # {'name': '富邦恒生國企反1', 'code': '00666R'},
  # {'name': '富邦上証+R', 'code': '00625K'},
  # {'name': '群益深証中小+R', 'code': '00643K'},
  # {'name': '富邦臺灣加權正2', 'code': '00675L'},
  # {'name': '富邦臺灣加權反1', 'code': '00676R'},
  # {'name': '期元大S&P原油反1', 'code': '00673R'},
  # {'name': '期元大S&P黃金反1', 'code': '00674R'},
  # {'name': '國泰美國道瓊', 'code': '00668'},
  # {'name': '國泰美國道瓊反1', 'code': '00669R'},
  # {'name': '期富邦VIX', 'code': '00677U'},
  # {'name': '群益NBI生技', 'code': '00678'},
  # {'name': '元大美債20正2', 'code': '00680L'},
  # {'name': '元大美債20反1', 'code': '00681R'},
  # {'name': '富邦NASDAQ正2', 'code': '00670L'},
  # {'name': '富邦NASDAQ反1', 'code': '00671R'},
  # {'name': '期元大美元指數', 'code': '00682U'},
  # {'name': '期元大美元指正2', 'code': '00683L'},
  # {'name': '期元大美元指反1', 'code': '00684R'},
  # {'name': '群益臺灣加權正2', 'code': '00685L'},
  # {'name': '群益臺灣加權反1', 'code': '00686R'},
  # {'name': '兆豐藍籌30', 'code': '00690'},
  # {'name': '國泰20年美債正2', 'code': '00688L'},
  # {'name': '國泰20年美債反1', 'code': '00689R'},
  # {'name': '期街口S&P黃豆', 'code': '00693U'},
  # {'name': '富邦公司治理', 'code': '00692'},
  # {'name': '富邦恒生國企', 'code': '00700'},
  # {'name': '台新MSCI中國', 'code': '00703'},
  # {'name': '富邦歐洲', 'code': '00709'},
  # {'name': '國泰股利精選30', 'code': '00701'},
  # {'name': '國泰標普低波高息', 'code': '00702'},
  # {'name': 'FH彭博高收益債', 'code': '00710B'},
  # {'name': 'FH彭博新興債', 'code': '00711B'},
  # {'name': 'FH富時不動產', 'code': '00712'},
  # {'name': '期元大S&P日圓正2', 'code': '00706L'},
  # {'name': '期元大S&P日圓反1', 'code': '00707R'},
  # {'name': '期元大S&P黃金正2', 'code': '00708L'},
  # {'name': '元大台灣高息低波', 'code': '00713'},
  # {'name': '國泰中國A50+U', 'code': '00636K'},
  # {'name': '國泰日經225+U', 'code': '00657K'},
  # {'name': '國泰美國道瓊+U', 'code': '00668K'},
  # {'name': '群益道瓊美國地產', 'code': '00714'},
  # {'name': '期街口布蘭特正2', 'code': '00715L'},
  # {'name': '富邦美國特別股', 'code': '00717'},
  # {'name': '富邦臺灣優質高息', 'code': '00730'},
  # {'name': '第一金工業30', 'code': '00728'},
  # {'name': 'FH富時高息低波', 'code': '00731'},
  # {'name': '國泰RMB短期報酬', 'code': '00732'},
  # {'name': '富邦臺灣中小', 'code': '00733'},
  # {'name': '期元大道瓊白銀', 'code': '00738U'},
  # {'name': '國泰臺韓科技', 'code': '00735'},
  # {'name': '國泰新興市場', 'code': '00736'},
  # {'name': '國泰AI+Robo', 'code': '00737'},
  # {'name': '新光內需收益', 'code': '00742'},
  # {'name': '元大MSCI A股', 'code': '00739'},
  # {'name': '國泰中國A150', 'code': '00743'},
  # {'name': '中信中國50', 'code': '00752'},
  # {'name': '中信中國50正2', 'code': '00753L'},
  # {'name': '統一FANG+', 'code': '00757'},
  # {'name': '期街口道瓊銅', 'code': '00763U'},
  # {'name': '元大全球AI', 'code': '00762'},
  # {'name': '國泰北美科技', 'code': '00770'},
  # {'name': '新光投等債15+', 'code': '00775B'},
  # {'name': '新光中國政金綠債', 'code': '00774B'},
  # {'name': '富邦中証500', 'code': '00783'},
  # {'name': '國泰費城半導體', 'code': '00830'},
  # {'name': '元大US高息特別股', 'code': '00771'},
  # {'name': '台新全球AI', 'code': '00851'},
  # {'name': '新光中政金綠債+R', 'code': '00774C'},
  # {'name': '國泰美國道瓊正2', 'code': '00852L'},
  # {'name': '元大臺灣ESG永續', 'code': '00850'},
  # {'name': '元大全球未來通訊', 'code': '00861'},
  # {'name': '國泰US短期公債', 'code': '00865B'},
  # {'name': '國泰網路資安', 'code': '00875'},
  # {'name': '元大未來關鍵科技', 'code': '00876'},
  # {'name': '國泰永續高股息', 'code': '00878'},
  # {'name': '國泰台灣5G+', 'code': '00881'},
  # {'name': '中信中國高股息', 'code': '00882'},

]


class Crawer:
  def __init__(self):
    path = './chromedriver'
    self.browser = webdriver.Chrome(path)
    # self.url ="http://localhost:8080/api/stock"
    self.url ="http://167.179.80.227:8080/api/stock"



  def parseToInt(self, x):
    x = x.replace(",", "")
    return int(x)

  def postData(self, data):
    # url ="http://localhost:8080/api/stock"
    # url ="http://167.179.80.227:8080/api/stock"

    r = requests.post(self.url, data=data)
    print("response", r.json())
  
  def parseDate(self, date):
    date = date.split('/')
    return int(date[0]), int(date[1]), int(date[2])


  def parseData(self, tdList, name, code):
    y, m, d = self.parseDate(tdList[0].text)
    data = {
      "name": name,
      "code": code,
      "date": tdList[0].text,
      "year": y,
      "mon": m,
      "day": d,
      "allCount": self.parseToInt(tdList[1].text),
      "allMount": self.parseToInt(tdList[2].text),
      "open": float(tdList[3].text),
      "high": float(tdList[4].text),
      "low": float(tdList[5].text),
      "close": float(tdList[6].text),
      "delta": tdList[7].text,
      "stockCount": self.parseToInt(tdList[8].text)
    }
    jsonData = json.dumps(data)
    # print(jsonData)
    self.postData(jsonData)

  def getTable(self, name, code):
    table = self.browser.find_element_by_id('report-table')
    rows = table.find_element_by_tag_name('tbody').find_elements_by_tag_name('tr')
    for row in rows:
      # print(row)
      tdList = row.find_elements_by_tag_name('td')
      try:
        self.parseData(tdList, name, code)
      except Exception as e:
        print("name", name, "tdList", tdList)
        print("err", e)
        
        pass
      # sleep(1)
      # date = tdList[0].text
      # print(date)
      # for td in tdList:
      #   print(td.text)

  def getOneStock(self, form, searchBtn, name, code):
    dateSelect = form.find_element_by_id("d1")
    yearSelect = dateSelect.find_element_by_css_selector("select[name='yy']")
    monSelect = dateSelect.find_element_by_css_selector("select[name='mm']")
    s1 = Select(yearSelect)
    s2 = Select(monSelect)

    years = yearSelect.find_elements_by_tag_name('option')
    mons = monSelect.find_elements_by_tag_name('option')
    for y in years:
      val = y.get_attribute('value')
      print("year", val)
      s1.select_by_value(val)
      for m in mons:
        val = m.get_attribute('value')
        s2.select_by_value(val)
        searchBtn.click()
        sleep(5)
        try:
          self.getTable(name=name, code=code)
        except Exception as e:
          print(e)
          pass
      sleep(2)

  def run(self):
    url = "https://www.twse.com.tw/zh/page/trading/exchange/STOCK_DAY.html"
    self.browser.get(url)
    form = self.browser.find_element_by_class_name('main')
    # print(form)
    stockInput = form.find_element_by_tag_name('input')
    # stockInput.send_keys('0050')
    # sleep(3)
    searchBtn = form.find_element_by_class_name('search')
    for item in stockList:
      print(item)
      stockInput.clear()
      stockInput.send_keys(item["code"])
      sleep(3)
      self.getOneStock(form, searchBtn, item["name"], item["code"])
    # print('search btn', searchBtn)
    # searchBtn.click()
    # sleep(3)

    self.browser.close()

  def test(self):
    data = {
      "test": 123,
      "test2": 456
    }
    jsonData = json.dumps(data)

    # for i in range(10):
    #   threads.append(threading.Thread(target = self.postData, args = (jsonData,)))
    #   threads[i].start()

    # for i in range(1000):
    #   # self.postData(jsonData)
    #   threads = []

    #   for i in range(10):
    #     threads.append(threading.Thread(target = self.postData, args = (jsonData,)))
    #     threads[i].start()
    #   sleep(0.2)
    threads = []
    for i in range(5000):
      self.postData(jsonData)
      # sleep(1)

      # threads.append(threading.Thread(target = self.postData, args = (jsonData,)))
      # threads[i].start()
      # sleep(0.1)




def main():
  c = Crawer()
  c.run()
  # c.test()

main()