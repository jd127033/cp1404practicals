"""
Wikipedia API task
Cameron Lane
Estimated Finish time: 25 min
Finish time: 20 min
"""

import wikipedia


def main():
    """"""
    page_title = input("Enter page title: ").strip()
    while page_title:
        display_page_details(page_title)
        page_title = input("Enter page title: ").strip()
    print("Thank you!")


def display_page_details(page_title):
    """"""
    try:
        page = wikipedia.page(page_title, auto_suggest=False)
        print(page.title)
        print(page.summary)
        print(page.url)
        print()
    except wikipedia.exceptions.PageError:
        print(f'Page id "{page_title}" does not match any pages. Try another id!')
        print()
    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)
        print()


main()
