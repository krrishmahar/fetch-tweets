import os
import time

from config import Config
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common import ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from datetime import datetime
from dotenv import load_dotenv


load_dotenv()
os.environ['PATH'] = '/Driver/'

# setting driver headless via chrome.Options
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless=new") 
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(options=chrome_options)

def email_validation():
    email = os.getenv('TWITTER_EMAIL')
    try:
        email_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
        )
        email_element.send_keys(email)
        email_element.send_keys(Keys.ENTER)
    except ElementNotInteractableException:
        # Email field not found, proceed without entering email
        pass

def user_signin():
    user = os.getenv('TWITTER_USERNAME')
    password = os.getenv('TWITTER_PASSWORD')
    driver.get(f'https://x.com/{user}/')
    username = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'r-30o5oe'))
    )
    username.send_keys(user, Keys.ENTER)

    email_validation()

    # Find the password field and enter the password
    password_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.NAME, 'password'))
    )

    password_element.send_keys(password, Keys.ENTER)

    # Wait for the tweets to load
    time.sleep(6)

    # Get the page source
    page_source = driver.page_source
    driver.quit()

    return page_source


def parse_data(source, tweet_limit=Config.TWEET_LIMIT):
    soup = BeautifulSoup(source, 'html.parser')
    # Find all tweet articles
    tweet_articles = soup.find_all('article', {'role': 'article'})
    parsed_tweets = []
    tweet_count = 1

    # Extract information from each tweet article
    for tweet in tweet_articles:
        if tweet_count > int(tweet_limit):
            break
        # Try to find the tweet text
        tweet_text_div = tweet.find('div', {'data-testid': 'tweetText'})
        tweet_text_parts = []
        if tweet_text_div:
            for element in tweet_text_div.find_all(['span', 'img'], recursive=True):
                if element.name == 'span':
                    tweet_text_parts.append(element.get_text())
                elif element.name == 'img':
                    alt_text = element.get('alt', '')
                    tweet_text_parts.append(alt_text)
            tweet_text = ' '.join(tweet_text_parts)
            tweet_count += 1
        else:
            tweet_text = 'No tweet text found'

        # Try to find the tweet's timestamp
        time_tag = tweet.find('time')
        if time_tag:
            timestamp = time_tag['datetime']
            # Parse and format the timestamp
            parsed_timestamp = datetime.fromisoformat(timestamp)
            formatted_timestamp = parsed_timestamp.strftime(r'%d/%m/%Y')
        else:
            formatted_timestamp = 'No timestamp found'

        parsed_tweets.append({'time': formatted_timestamp, 'text': tweet_text})

    return parsed_tweets
