import datetime
import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
#Fix
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
#Insert file name

driver = webdriver.Chrome(ChromeDriverManager().install())

url = "https://www.agoda.com/th-th/search?guid=5c77e50d-bab3-4a69-ac67-b90e8d5c3bd6&asq=xi4DHjbYz3ZzG7B%2FqYMjyZufa9Vwpz6XltTHq4n%2B9gNZKis4UREXeechLsPNI3YYh8GU%2FSLJhm7FJCISRDF9Kl3F0M0v%2FgujhgMWDATnAyW9M%2FWcU5pJP1GKC%2Ba9AVZs%2FfPpQOKjWhNk5%2BxrvuDpR2Q%2FDuO4Ycd3tHzVRGE03t%2Btr8t%2FDbzpMXRg8RvFY3Be5W64vLOBuh44LB9a%2FDpckOpLAc7kNmnLw6qMMZIQMy0%3D&city=8584&tick=638140028982&locale=th-th&ckuid=e3a9b81b-2af9-45b5-a1b6-7aada956d24d&prid=0&currency=THB&correlationId=9a9ade24-9afe-42ec-bc54-889b52758a34&analyticsSessionId=-6509936149616115943&pageTypeId=107&realLanguageId=22&languageId=22&origin=TH&cid=1891472&tag=db22e9db-2204-0721-cb3a-2acdba0c3274&userId=e3a9b81b-2af9-45b5-a1b6-7aada956d24d&whitelabelid=1&loginLvl=0&storefrontId=3&currencyId=6&currencyCode=THB&htmlLanguage=th-th&cultureInfoName=th-th&machineName=sg-pc-6g-acm-web-user-b7fb5db5-9hvvp&trafficGroupId=5&sessionId=f0akjqvbn0ywwn1shmho44ts&trafficSubGroupId=122&aid=82361&useFullPageLogin=true&cttp=4&isRealUser=true&mode=production&browserFamily=Chrome&checkIn=2023-03-31&checkOut=2023-04-01&rooms=1&adults=1&children=0&priceCur=THB&los=1&textToSearch=%E0%B8%9E%E0%B8%B1%E0%B8%97%E0%B8%A2%E0%B8%B2&travellerType=0&familyMode=off&hotelAccom=34,37&productType=-1"
driver.get(url)


soup = BeautifulSoup(driver.page_source,'html.parser')

url_lis = [ "https://www.agoda.com/"+x['href'] for x in soup.find_all('a',{'class':'PropertyCard__Link'})]
name_lis = [ x['aria-label'] for x in soup.find_all('a',{'class':'PropertyCard__Link'})]
loc_lis = []
map_lis = []
rate_lis = []
review_lis = []
num_review_lis = []

for i in url_lis: 
    print(i)
    driver.get(i)

    soupx = BeautifulSoup(driver.page_source,'html.parser')
    """
    try:
        name = soupx.find('h1',{"class":'HeaderCerebrum__Name'}).text 
        name_lis.append(name)
        print(name)
    except: 
        name_lis.append("ไม่มี")
        print("ไม่มี")
"""
    try:
        loc = soupx.find('div',{'class':'HeaderCerebrum__Location'}).text
        loc_lis.append(loc)
        print(loc)
    except: 
        loc_lis.append("ไม่มี")
        print("ไม่มี")

    rate = soupx.find('h4',{'class':'Typographystyled__TypographyStyled-sc-j18mtu-0'})
    rate_lis.append(str(rate).replace('<h4 class="Typographystyled__TypographyStyled-sc-j18mtu-0 gouaKT kite-js-Typography">',"").replace("</h4>",""))
    print(str(rate).replace('<h4 class="Typographystyled__TypographyStyled-sc-j18mtu-0 gouaKT kite-js-Typography">',"").replace("</h4>",""))

    review = soupx.find('span',{'class':'Spanstyled__SpanStyled-sc-16tp9kb-0'}).text
    review_lis.append(review)
    print(review)


    num_review = soupx.find('div',{'class':'review-basedon'}).find('span').text 
    num_review_lis.append(num_review)
    print(num_review)


df = pd.DataFrame()
df['Title'] = name_lis 
df['URL'] = url_lis 
df['Location'] = loc_lis 
df['Rating'] = rate_lis 
df['Total Review'] = num_review_lis 
df['Review'] = review_lis

df.to_excel("Hotel.xlsx")