import urllib.request as r
import bs4
urls = ["https://www.4399.com/flash"]
for url in urls:
    resp = r.urlopen(url)

    html = resp.read().decode('gb2312')

    bs = bs4.BeautifulSoup(html,'html.parser')

    lis = bs.select(".n-game>li")

    for li in lis:
        name = li.select("a>b")[0].text
        type = li.select("em>a")[0].text
        date = li.select("em")[-1].text

        with open('data.csv', 'a', encoding='utf-8') as f:
            f.write(f'{name},{type},{date}\n')

    a = bs.select("#pagg>a")[-1]

    if a.text == "下一页":
        next_url = "https://www.4399.com" + a.attrs['href']

        print(next_url)

        urls.append(next_url)