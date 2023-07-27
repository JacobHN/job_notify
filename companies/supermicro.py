from bs4 import BeautifulSoup as bs
import requests
import os
# from notifypy import Notify
import time
import db

class supermicro:
    company = 'SuperMicro'
    def run(self):
        flag = False
        headers = {
            'User-Agent': 'Mozilla/5.0'
            }
        url = "https://jobs.supermicro.com/search/?q=&q2=&alertId=&locationsearch=&shifttype=&title=&department=software&location=&date="
        r = requests.get(url, headers = headers)
        soup = bs(r.content, "html.parser")
        items = soup.find("tbody").find_all("tr", {"class": "data-row"})
        for item in items:
            id = int(item.find("td", {"class": "colShifttype hidden-phone"}).find("span", {"class": "jobShifttype"}).string)
            job = item.find("td", {"class": "colTitle"})\
                        .find("span", {"class": "jobTitle hidden-phone"})\
                        .find("a")
            title = job.string
            hlink = "https://jobs.supermicro.com" + job.get('href')
            if(not db.exist(self.company, id)):
                print("new job")
                db.addItem(self.company, id, title, hlink)
                flag = True
            elif db.exist(self.company, id):
                return flag
        # if flag:
        #     notification = Notify()
        #     notification.title = "tallgeese is here bitch"
        #     notification.message = "check the site ye ass"
        #     notification.audio = "sounds/uwu.wav"
        #     notification.send()
        #  time.sleep(30)