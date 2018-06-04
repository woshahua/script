import os
import re
import urllib.request

def download_pdf(link, location, name):
    try:
        response = urllib.request.urlopen(link)
        file = open(os.path.join(location, name), "wb")
        file.write(response.read())
        file.close()
    except urllib.request.HTTPError:
        print(">>> Error 404: cannot be downloaded\n")
        # send error out
        raise


if __name__ == "__main__":

    link = "http://www.cs.toronto.edu/~hinton/absps/NatureDeepReview.pdf"
    location = "C:\\Users\\wohan\\Desktop"
    name = "neuralDeepReview.pdf"

    download_pdf(link, location, name)
