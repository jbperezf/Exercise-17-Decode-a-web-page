import bs4, requests

url = "https://www.nytimes.com/"
r = requests.get(url)
r_html = r.text

soup = bs4.BeautifulSoup(r_html, "html.parser")
title = soup.find_all("h2", class_="esl82me0")

print([i.text for i in title])
