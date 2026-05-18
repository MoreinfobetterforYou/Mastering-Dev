import requests as req
import json
import easygui as gui
import os

def ask_user() -> tuple[str, int]:
    while True:
        try:
            query = gui.enterbox(msg = "Enter the image you want to download: ", title="GUI")
            number_Of_images = gui.enterbox(msg = "Enter the number of images you want: (Min = 1, Max = 80)", title = "GUI", default=1)
            if not query:
                gui.msgbox(msg="Enter an image you want !!!", title="GUI")
                continue
            number_Of_images = int(number_Of_images)
            if number_Of_images > 80 or number_Of_images < 1:
                gui.msgbox("Enter a valid number of pages !!!!")
                continue
            else:
                return query, number_Of_images
        except (ValueError, TypeError):
            print("Enter a valid number of pages")

query, number_Of_images = ask_user()
API_key = "API_KEY"
url = "https://api.pexels.com/v1/search"
params = {
    "query": query,
    "per_page": number_Of_images
}
headers = {
    "Authorization": API_key
}
response_from_img_api = req.get(url, params=params, headers = headers)

if response_from_img_api.status_code == 200:
    currentDirectory = os.getcwd()
    newFolderPath = os.path.join(currentDirectory, f"{query.strip().lower()}")
    os.mkdir(newFolderPath, exist_ok = True)
    data = response_from_img_api.json()
    try:
        with open(f"{os.path.join(newFolderPath, f"{query.strip().lower()}")}.json", "r") as file:
            database = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        database = []

    database.append(data)
    with open(f"{os.path.join(newFolderPath, f"{query.strip().lower()}")}.json", "w") as file:
        json.dump(database, file, indent=4)
    for photo in data['photos']:
        print(f"ID: {photo['id']}, Photographer: {photo['photographer']}")
        image_url = photo["src"]["original"]
        image_Req = req.get(image_url)
        if image_Req.status_code == 200:
            fileName = f"{photo['id']}.jpg"
            with open(f"{os.path.join(newFolderPath, fileName)}", "wb") as file:
                file.write(image_Req.content)
            print(f"The file has been downloaded: {fileName}")
        else:
            print(f"Failed to access the photos from API")
else:
    print("Failed to access photos from the API")