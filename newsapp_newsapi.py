import requests
import sys
url = "https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=737789fe16034754838ae50314d79738"
response = requests.get(url)

if response.status_code == 200:
    news_data = response.json()
else:
    print("An error has occured")
    
print("Welcome to the News App\nPlease choose an option:\n1. Show all headlines\n2.Search by keyword\n3.Filter by category\n4.Exit")

while True: 
    choice = input("Enter your choice: ")

    if choice == '1':
        for article in news_data['articles']:
            print(f"{article['title']} - {article['source']['name']}")
    elif choice == '2':
        keyword = input("Enter a keyword: ")
        results = [article for article in news_data['articles'] if keyword.lower() in article['title'].lower()]
        if results:
            for article in results:
                print(f"{article['title']} - {article['source']['name']}")
        else:
            print("No results found.")
    elif choice == '3':
        category = input("Enter a category: ")
        if category in ['business', 'entertainment', 'general', 'health', 'science', 'technology']:
            url = f"https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey=737789fe16034754838ae50314d79738"
            response = requests.get(url)
            if response.status_code == 200:
                news_data = response.json()
                for article in news_data['articles']:
                    print(f"{article['title']} - {article['source']['name']}")
            else:
                print("An error has occured")
        else:
            print("Invalid category.")
    elif choice == '4':
        print("Thank you for using the News App. Have a nice day!")
        break 
        sys.exit("User chose to exit.")
    else:
        print("Invalid choice.")
