import requests
from bs4 import BeautifulSoup


def getStackTags(number):
    getTags = f"https://stackoverflow.com/tags?page={number}"

    data = requests.get(getTags)
    data = BeautifulSoup(data.text, "lxml")

    tags = data.find_all("div", {"class": "s-card"})
    tagInfo = []
    for a in tags:
        let = a.find("a", {"class": "post-tag"})
        tagName = let.text
        link = "https://stackoverflow.com" + let["href"]
        desc = a.find("div", {"class": "v-truncate4"}).text
        questions = (a.find("div", class_="mt-auto grid jc-space-between fs-caption fc-black-400").find("div",
                                                                                                        class_="grid--cell").text)

        tagInfo.append({"tagName": tagName.strip(), "link": link, "description": desc.strip(),
                        "quesCount": questions.split(" ")[0]})

    return tagInfo
