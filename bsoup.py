import requests
from bs4 import BeautifulSoup
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return str(arr)


if __name__ == '__main__':
    app.run(debug=True)




 
page = requests.get('https://seattle.craigslist.org/d/apartments-housing-for-rent/search/apa') # Getting page HTML through request
soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsou
links = soup.find_all('div', attrs={'class': "result-info"})
otherlink  = soup.find_all('img')
img_link = soup.find_all('div', attrs={'class': "content"})


newArr = []
print(otherlink)
# print(links)
 # Selecting all of the anchors with titles
 # Keep only the first

# for item in otherlink:

#     try: 
#         newArr.append({
#             'img': item.find('img', attrs={'class': "loading"}).get('src')    
#         })

#     except:
#         pass

# print(newArr)

for item in links:
    try: 
        arr.append({
            'address': item.find('span', attrs={'class': "result-hood"}).text,
            'housePrice': item.find('span', attrs={'class': 'result-price'}).text,
            'beds':item.find('span', attrs={'class': 'housing'}).text.strip().replace(" ","").replace("\n",""),
           
        })

    except:
        pass
 
# print(arr)
# print(arr) # Display the innerText of each anchorHouston
# print(links)"result-info"
# find('span', attrs={'class': "result-meta"})
# class="result-meta"arr.append(an)


