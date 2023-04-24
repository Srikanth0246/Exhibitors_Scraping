import requests
import csv
from bs4 import BeautifulSoup

file=open('Company Url.csv','w',newline='',encoding="utf-8")
csvwriter=csv.writer(file)
csvwriter.writerow(['Company Name','URL'])
header={
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding':'gzip, deflate',
        'accept-language':'en-US,en;q=0.9'
        }

URL='https://exhibitor.expowest.com/ew23/Public/Exhibitors.aspx?ID=1074263'
responses = requests.get(URL,headers=header)

html=BeautifulSoup(responses.content,"html.parser")
def geturl(specific):
    URL='https://exhibitor.expowest.com/ew23/Public/'+specific
    responses = requests.get(URL,headers=header)
    html=BeautifulSoup(responses.content,"html.parser")

    CompanyURL=html.find('a',attrs={'id':'BoothContactUrl'})
    if CompanyURL == None:
        return 'Na'
    x=CompanyURL.find('i')
    x.decompose()
    url=CompanyURL.string

    return url

Companynames=html.find_all('a',attrs={'class':'exhibitorName'})

j=0

for i in Companynames:
    companyname=i.string
    url=geturl(i['href'])
    csvwriter.writerow([companyname,url])
    j+=1
    print(j)
