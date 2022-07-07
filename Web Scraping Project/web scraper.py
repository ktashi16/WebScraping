import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:/Users/dolma/Downloads/chromedriver_win32/chromedriver.exe")
driver.get("https://oxylabs.io/blog")
results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for element in soup.findAll(attrs='css-16nzj3b esl9i4u1'):
    name = element.find('h5')
    if name not in results:
        results.append(name.text)
df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')