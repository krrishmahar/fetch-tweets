def write_tweets(file_path, tweets):
    with open(file_path, 'w', encoding="utf-8") as f:
        f.write('## Some Tweets\n\n')
        for tweet in tweets:
            f.write("```bash"+ "\n")
            f.write("Tweet:" + f'{tweet['text']}' + "\n")
            f.write(f"\t\t\t\t\t\t - {tweet['time']}" + "\n")
            f.write("```" + "\n")


def update_readme():
    with open('recent_tweets.md', 'r', encoding="utf-8") as ra:
        recent_tweets = ra.read()

    with open('test.md', 'r', encoding="utf-8") as readme:
        readme_content = readme.read()

    start_marker = '<!-- TWEETS -->'
    end_marker = '<!-- /TWEETS -->'

    # Locate the positions of the markers
    start_idx = readme_content.find(start_marker) + len(start_marker)
    end_idx = readme_content.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        raise ValueError("Markers not found in README file")


    # Ensure only the section between the markers is updated
    updated_content = (readme_content[:start_idx].strip() + "\n\n" +
                       recent_tweets.strip() + "\n" +
                       readme_content[end_idx:].strip())

    with open('test.md', 'w', encoding="utf-8") as readme:
        readme.write(updated_content)
