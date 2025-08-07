# import section
import requests
import pandas
from bs4 import BeautifulSoup



response=requests.get("https://www.flipkart.com/apple-iphone-16-pink-128-gb/p/itmc2e910b4d0b1c?pid=MOBH4DQFWJVDRSHM&lid=LSTMOBH4DQFWJVDRSHMQYAA7N&marketplace=FLIPKART&fm=neo%2Fmerchandising&iid=M_8871a370-232a-4014-99d1-a7dae716e5ca_31_QBM1SMZJ3K19_MC.MOBH4DQFWJVDRSHM&ppt=hp&ppn=homepage&ssid=2r16kbmnv40000001742461093364&otracker=clp_pmu_v2_Apple%2BSmartphones_2_31.productCard.PMU_V2_Apple%2BiPhone%2B16%2B%2528Pink%252C%2B128%2BGB%2529_mobile-phones-store_MOBH4DQFWJVDRSHM_neo%2Fmerchandising_1&otracker1=clp_pmu_v2_PINNED_neo%2Fmerchandising_Apple%2BSmartphones_LIST_productCard_cc_2_NA_view-all&cid=MOBH4DQFWJVDRSHM")
# print(response)
soup=BeautifulSoup(response.content,'html.parser')
# print(soup)
names=soup.find_all('div',class_='_4rR01T')
[names]
for i in names[0:10]:
    d=i.get_text()
    name.append(d)
print(name)
