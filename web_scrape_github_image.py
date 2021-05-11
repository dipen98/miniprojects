import requests as rq
from bs4 import BeautifulSoup as bs

github_user = input("Enter Github user: ")

url = 'https://github.com/'+github_user

r = rq.get(url) 

if r.status_code == 200:
    print("request Successfull")
    print("fetching Profile pic link....")
    soup = bs(r.content,'html.parser')
    profile_image = soup.find('img',{'alt':'Avatar'})['src']
    print(profile_image)
else:
    print("Inavlid request, check username")
    