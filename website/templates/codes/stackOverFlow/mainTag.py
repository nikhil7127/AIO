import requests
from bs4 import BeautifulSoup


def mainTags(tagName, option="Votes"):
    url = f"https://stackoverflow.com/questions/tagged/{tagName}?tab={option}&page=1"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")

    questions = soup.find_all("div", class_="question-summary")

    main_list = []

    for a in questions:
        stats = a.find("div", class_="votes").text.split()[0].strip()
        ans = a.find("div", class_="status").text.split("a")[0].strip()
        views = a.find("div", class_="views").text.strip()
        let = a.find("a", class_="question-hyperlink")
        question = let.text.strip()
        question_link = "https://stackoverflow.com" + let["href"]
        description = a.find("div", class_="excerpt").text.strip()
        tags = a.find("div", class_="tags").find_all("a", class_="post-tag")
        question_tags = []
        for tag in tags:
            question_tags.append((tag.text, "https://stackoverflow.com" + tag["href"]))

        main_list.append(
            {"votes": stats, "answer": ans, "views": views, "question": question, "question_link": question_link,
             "description": description, "tags": question_tags})
    return main_list, tagName
