from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time

def get_comments(video_url, num_comments):
    driver = webdriver.Chrome()  
    driver.get(video_url)
    
    SCROLL_PAUSE_TIME = 2
    comments = []

    # Scroll down until we get enough comments
    while len(comments) < num_comments:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(SCROLL_PAUSE_TIME)

        comment_elements = driver.find_elements(By.XPATH, '//*[@id="content-text"]')
        for comment_element in comment_elements:
            comments.append(comment_element.text)
            if len(comments) >= num_comments:
                break
    
    driver.quit()
    return comments

# URL of the YouTube video and number of comments to scrape
video_url = "https://www.youtube.com/watch?v=J0Z_QrLXPK0"
num_comments = 1000  # Number of comments you want to scrape

comments = get_comments(video_url, num_comments)

# Save comments to Excel
df = pd.DataFrame(comments, columns=['Comment'])
df.to_excel('youtube_comments.xlsx', index=False)
print("Data saved to youtube_comments.xlsx")
