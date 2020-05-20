from plyer import notification
import requests
from bs4 import BeautifulSoup
import time

def notifyMe(ftitle, fmessage):
    notification.notify(
        title = ftitle,
        message = fmessage,
        app_icon = "D:/python/Projects/COVID-19 notification/try.ico",
        timeout = 8
    )

def getData(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    while True:
        # notifyMe("This is Title", "This is msg")
        myHtmlData = getData('https://www.mohfw.gov.in/')

        soup = BeautifulSoup(myHtmlData,'html.parser')
        # print(soup.prettify())
        myDataStr =""
        for tr in soup.find_all('tbody')[8].find_all('tr'):
            # print(tr.get('href'))
            myDataStr += tr.get_text()

        myDataStr = myDataStr[1:]
        itemList = myDataStr.split("\n\n")

        states = ['Madhya Pradesh', 'Delhi', 'Bihar']
        for item in itemList[0:22]:
            dataList = item.split('\n')
            if dataList[1] in states:
                print(dataList)
                nTitle = "Cases of COVID-19 "
                nMsg = f"STATE: {dataList[1]}: \n Indian Cases: {dataList[2]}  |   Foreign Cases: {dataList[3]}\n Cured: {dataList[4]}\n Deaths: {dataList[5]}" 
                notifyMe(nTitle, nMsg)
                time.sleep(2)
        print('''
                *****************************************
                *   PRESS ctrl + c to STOP the program  *
                *****************************************
                ''')

        time.sleep(3600)

 