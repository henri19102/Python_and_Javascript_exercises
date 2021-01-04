from PIL import Image
from bs4 import BeautifulSoup as bs
import requests, os, re
from io import BytesIO

def get_all_images(url):
    soup = bs(requests.get(url).content, 'lxml')
    images = []
    for img in soup.findAll('img'):
        images.append(img.get('src'))
    return images

def download(url):
    pathname = "images"
    # if path doesn't exist, make that path dir
    if not os.path.isdir(pathname):
        os.makedirs(pathname)
    response = requests.get(url, stream=True)
    filename = os.path.join(pathname, url.split("/")[-1])
    new_file = filename.split(".")[0]
    try:
        g = re.search(r'/([\w_-]+[.](jpg|jpeg|gif|png))$', url)
        if g:
            img = Image.open(BytesIO(response.content)).convert('RGB')
            if img.height > 300 or img.width > 300:
                get_pixels = img.height * img.width
                #if get_pixels > 4021248:
                if get_pixels > 1000:
                    width = round(img.width)
                    height = round(img.height)
                    size = (int(width/2), int(height/2))
                    img = img.resize((size), Image.BOX)
                    new_file = new_file + "_resized"
                img.save(new_file + ".jpg")
    except Image.UnidentifiedImageError as error:
        print(format(error))

def main():
    url = input("Enter URL to extract files from: ")
    imgs = get_all_images(url)
    for img in imgs:
        download(img)

if __name__ == "__main__":
    main()