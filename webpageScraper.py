import requests #a library for sending HTTP requests (fetching webpages from the internet, just like a browser does)
import re #re Python's built-in module for finding patterns inside text

def get_page_title(url, output_file):
    #with header to mimic a real browser/user and avoid being blocked by some websites
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    }
    response = requests.get(url, headers=headers, timeout=10) #HTTP GET request(same as typing the URL in Chrome and hitting Enter)+ attach mimic user header
    response.raise_for_status()

    match = re.search(r"<title>(.*?)</title>", response.text, re.IGNORECASE | re.DOTALL) #search for tile in html (capture everything between <title> and </title> tags)
    title = match.group(1).strip() if match else "No title found"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(title)

    print(f"Title: {title}")

get_page_title("https://www.justwatch.com/in/movies", "title.txt")