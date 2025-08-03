"""
display "Wikipedia Search"
get title
while title
    try
        page = wikipedia.page
        display page.title, wikipedia.summary, page.url
    except wikipedia.exceptions.DisambiguationError as e
        display "We need a more specific title. Try one of the following, or a new search:"
        display e.options

    except wikipedia.exceptions.PageError
        display Page id title does not match any pages.

    except Exception as e
        display An unexpected error occurred e

    get title
display "Thank you."
"""
import wikipedia

print("Wikipedia Search")
title = input("Enter page title: ").strip()

while title:
    try:
        page = wikipedia.page(title, auto_suggest=False)
        print(page.title)
        print(wikipedia.summary(title, auto_suggest=False))
        print(page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # Ask for next input
    title = input("\nEnter another page title (or press Enter to quit): ").strip()

print("Thank you.")
