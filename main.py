from urllib.request import urlopen
from bs4 import BeautifulSoup


url = "https://www.github.com/apePetrus"
page = urlopen(url)

html_bytes = page.read()
html = html_bytes.decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
username = soup.find("span", {"class", "p-name vcard-fullname d-block overflow-hidden"})

print(username.string)