from bs4 import BeautifulSoup

html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="utf-8">
        <title>My test page</title>
    </head>
    <body>
        <div class="panel1">
            <img src="images/test1.png" alt="Image test 1">
            <img src="images/test2.png" alt="Image test 2">
        </div>
        <div class="panel2">
            <img src="images/test1.png" alt="Image test 1">
            <img src="images/test2.png" alt="Image test 2">
        </div>
    </body>
</html>

"""

# Declare Object with lxml parser (pip install lxml)
soup = BeautifulSoup(html, "lxml")

# Get all img element
img = soup.find_all("img")

print([elem for elem in img])

