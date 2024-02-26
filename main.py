import requests
import re
import urls

def find_phone_numbers(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        phone_numbers = re.findall(r'\b(?:8|\+7)?\s?\(?\d{3}\)?\s?(?:\d{3}|xxx)(?:-|\s)?(?:\d{2}|xx)(?:-|\s)?(?:\d{2}|xx)\b', response.text)

        return set(phone_numbers)
    except Exception as e:
        print(f"Error: {e}")
        return []
    
def showNumbers(url):
    phone_numbers = find_phone_numbers(url)
    print("Phone numbers found on", url, len(phone_numbers))
    for number in phone_numbers:
        print(number)

if __name__ == "__main__":
    for url in urls.urls:
        showNumbers(url)