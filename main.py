import numpy as np
import pandas as pd

from requests_html import HTMLSession
from bs4 import BeautifulSoup  # 引入库BeautifulSoup
import re

session = HTMLSession()


def GetAllPageNums(URL):  # 获得大页面的数量
    r2 = session.get(URL)
    h2 = r2.html.find('span.pageinfo', first=True).html
    soup2 = BeautifulSoup(h2, 'lxml')
    PageNums = soup2.find_all('span', attrs={'class': 'pageinfo'})[0].find_all('strong')[0].text
    return PageNums

def GetContentCity(Hrefs):
    listcity = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        TextContent = TextContent[5:35]
        city =str(re.findall(r'[\u4e00-\u9fa5]{2}市[\u4e00-\u9fa5]{2}县|[\u4e00-\u9fa5]{2}市|[\u4e00-\u9fa5]{2}市[\u4e00-\u9fa5]{2}县[\u4e00-\u9fa5]{2}乡|[\u4e00-\u9fa5]{2}市[\u4e00-\u9fa5]{2}区[\u4e00-\u9fa5]{2}村', TextContent))  # 获取发生的市区
        listcity.append(city)
    return listcity

def GetContentDay(Hrefs):
    listday = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        day = str(re.findall(r'\d{1,}月\d{1,}日', TextContent))  # 获取发生的月日
        listday.append(day)
    return listday


def GetContentTime(Hrefs):
    listtime = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        time = str(re.findall(r'\d{1,}时\d{1,}分', TextContent))  # 获取火灾的时间
        listtime.append(time)
    return listtime


def GetContentSavetime(Hrefs):
    listStime = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        Savetime = str(re.findall(r'\d{1,}[分|多][钟|分钟]', TextContent))  # 获取火灾的时间
        listStime.append(Savetime)
    return listStime


def GetContentEar(Hrefs):
    listear = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        ear = str(re.findall(r'约{0,}\d{1,}平方[米|千米]', TextContent))  # 获取面积
        listear.append(ear)
    return listear


def GetContentpeople(Hrefs):
    listpeople = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        people = str(re.findall(r'\d{1,}[人|名][\u4e00-\u9fa5]{0,3}', TextContent))  # 获取救援人数
        listpeople.append(people)
    return listpeople


def GetContentsurvivor(Hrefs):
    listsurvivor = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'text2'})[0].text
        survivor = str(re.findall(r'[\u4e00-\u9fa5]{0,5}伤亡[\u4e00-\u9fa5]{0,3}', TextContent))  # 获取伤亡情况
        listsurvivor.append(survivor)
    return listsurvivor


def GetContentnewtime(Hrefs):
    listnewtime = []
    for each in Hrefs:
        r3 = session.get(each)
        h3 = r3.html.find('div.content2', first=True).html
        soup3 = BeautifulSoup(h3, 'lxml')
        TextContent = soup3.find_all('div', attrs={'class': 'info2'})[0].text
        newtime = str(re.findall(r'\d{4}\-\d{2}\-\d{2}', TextContent))  # 获取伤亡情况
        listnewtime.append(newtime)
    return listnewtime


PageNums = GetAllPageNums('http://www.jx-fire.gov.cn/fire/huozaipujiu/')

i = 1

n = 0


j = str(i)

Alllistcity = []
Alllistday = []
Alllisttime = []
Alllistsavetime = []
Alllistear = []
Alllistpeople = []
Alllistsurvivor = []
Alllistnewstime=[]

while i<= int (PageNums) :
    number = 0
    url = 'http://www.jx-fire.gov.cn/fire/huozaipujiu/' + 'list_' + '4' + '_' + str(i) + '.html'
    r1 = session.get(url)
    h1 = r1.html.find('div.listcontent', first=True).html
    soup = BeautifulSoup(h1, 'lxml' )
    Hrefs = []
    # 获取每一页的新闻数
    News = soup.find_all('div', attrs={'class': 'listcontent'})[0].find_all('li')  # 获取每个class=listcontent的div标签内的a标签的href
    NewsNum = len(News)
    for x in range(NewsNum):
        hrefs = soup.find_all('div', attrs={'class': 'listcontent'})[0].find_all('a')[x]['href']  # 获取每个class=listcontent的div标签内的a标签的href
        Hrefs.append(hrefs)
    while number < len(Hrefs):
        Hrefs[number] = 'http://www.jx-fire.gov.cn/' + Hrefs[number]
        number = number + 1
    city = GetContentCity(Hrefs)
    day = GetContentDay(Hrefs)
    time = GetContentTime(Hrefs)
    savetime = GetContentSavetime(Hrefs)
    ear = GetContentEar(Hrefs)
    people = GetContentpeople(Hrefs)
    survivor = GetContentsurvivor(Hrefs)
    newtime = GetContentnewtime(Hrefs)
    Alllistcity.append(city)
    Alllistday.append(day)
    Alllisttime.append(time)
    Alllistsavetime.append(savetime)
    Alllistear.append(ear)
    Alllistpeople.append(people)
    Alllistsurvivor.append(survivor)
    Alllistnewstime.append(newtime)
    i = i + 1
    print(i)

Alllistcity=list(np.ravel(Alllistcity))
Alllistday=list(np.ravel(Alllistday))
Alllisttime=list(np.ravel(Alllisttime))
Alllistsavetime=list(np.ravel(Alllistsavetime))
Alllistear=list(np.ravel(Alllistear))
Alllistpeople=list(np.ravel(Alllistpeople))
Alllistsurvivor=list(np.ravel(Alllistsurvivor))
Alllistnewstime=list(np.ravel(Alllistnewstime))
df = pd.DataFrame( {'city':Alllistcity,'newstime':Alllistnewstime,'fireday': Alllistday, 'time': Alllisttime, 'Savetime': Alllistsavetime, 'ear': Alllistear, 'people': Alllistpeople,'survivor': Alllistsurvivor})
df = df.set_index('fireday')  # 指定index，去除生成的index
df.to_excel('C:\\Users\\42454\\Desktop\\智慧消防信息采集.xlsx')  # 我直接写入到当前文件夹
print('ok')