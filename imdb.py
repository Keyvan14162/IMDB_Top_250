import sys
import requests
from bs4 import BeautifulSoup

counter = 1
movie_number = 250


def getMovies(url):
    global counter  # Bak unutma bunu

    response = requests.get(url)
    print(response)  # Don't need to write but i wrote

    html_content = response.content

    soup = BeautifulSoup(html_content, "html.parser")

    headers = []
    ratings = list()  # Same

    for i in soup.find_all("div", {"class": "lister-item-image float-left"}):
        for j in i.find_all("img"):
            headers.append(j.get("alt"))

    for i in soup.find_all("div", {"class": "inline-block ratings-imdb-rating"}):
        ratings.append(i.get("data-value"))

    for header, rating in zip(headers, ratings):
        if movie_number >= counter:
            sys.stdout.write(f"{counter} Header:{header} Rate:{rating}\n")
            counter += 1
        else:
            sys.exit(0)


if len(sys.argv) >= 3:  # Only 1 parameter plz
    sys.stderr.write("For help: python imdb.py help")
    sys.stderr.write("Ony 1 parameter allowed")
    sys.stderr.write("Use it like: python imdb.py 100 (You can only enter [0,250])")

elif len(sys.argv) == 2:  # Correct use
    if sys.argv[1] == "help":
        sys.stdout.write("You must have internet connection\nUse: imdb.py <number of top movies to show>\n")
        sys.stdout.write("You can only enter one parameter and parameter must be between 0 and 250")
        sys.exit(0)
    try:
        movie_number = int(sys.argv[1])

        if 0 > int(sys.argv[1]) or int(sys.argv[1]) > 250:
            raise ValueError

    except ValueError:
        sys.stderr.write("Only [0,250] integer values and help allowed")
        sys.exit(0)

    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")


elif len(sys.argv) == 1:  # When u entered 0 parameter or executed the program from an ide
    sys.stdout.write("Top 250 IMDB movies:\n")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=51&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=101&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=151&ref_=adv_nxt")
    getMovies("https://www.imdb.com/search/title/?groups=top_250&sort=user_rating,desc&start=201&ref_=adv_nxt")

# Trials that didn't worked
# for i in soup.find_all("a"):
#     print(i)
# print(soup.find_all("div", {"class":"lister-item-image float-left"}))
# print(soup.find_all("div", {"alt":""}))
