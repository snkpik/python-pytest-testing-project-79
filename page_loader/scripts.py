import os
import requests
def url_to_filename(url: str, type=".html"):
    new_url = url.replace("https://", "").replace("http://", "")
    result = ""
    for char in new_url:
        if char.isalnum():
            result += char
        else:
            result += "-"

    return result + type


def download(url: str, path: str = os.getcwd()) -> str:
    filename = url_to_filename(url)
    new_file_path = os.path.join(path, filename)
    request = requests.get(url, allow_redirects=True, timeout=(3, 7))
    data = request.content
    with open(new_file_path, "wb") as file:
        file.write(data)

    return new_file_path

