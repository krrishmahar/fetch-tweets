from scrapper import user_signin, parse_data 
from update_README import write_tweets, update_readme
import time
if __name__ == "__main__":
    start = time.time()
    data = user_signin()
    tweets = parse_data(data)

    write_tweets('recent_tweets.md', tweets)
    update_readme()
    end = time.time()
    print(end-start)

