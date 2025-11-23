import requests

API_KEY = "9b607251ea994d7499934f65d2963ab0"  

def get_news(topic, language):
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": topic,
        "language": language,
        "sortBy": "publishedAt",
        "apiKey": API_KEY
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        print("Error fetching news:", response.status_code)
        return

    data = response.json()
    articles = data.get("articles", [])

    if not articles:
        print("No news found for this topic.")
        return

    print(f"\n🔹 TOP NEWS ABOUT: {topic.upper()}\n")
    for i, article in enumerate(articles[:5], start=1):
        print(f"{i}. {article['title']}")
        print(article['url'])
        print()


def smart_news_assistant():
    print("=== SMART NEWS ASSISTANT ===")

    while True:
        topic = input("\nEnter topic you want news about (or type exit): ")
        if topic.lower() == "exit":
            print("Goodbye!")
            break

        print("\nChoose language:")
        print("1. English")
        print("2. Hindi")
        print("3. Marathi")

        lang_choice = input("Enter 1/2/3: ")

        lang_map = {"1": "en", "2": "hi", "3": "mr"}
        language = lang_map.get(lang_choice, "en")

        get_news(topic, language)


# Run the assistant
smart_news_assistant()