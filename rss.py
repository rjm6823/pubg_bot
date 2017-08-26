import feedparser

url = 'https://steamcommunity.com/games/578080/rss/'


def most_recent():
    entries = feedparser.parse(url).entries
    for item in entries:
        if 'Update' in item['title']:
            return item


def check_new():
    # Read most recent update from storage file
    with open('./last_update.txt', 'r') as file:
        last_update = file.readline()

    # Check what the last update is
    last = most_recent()
    if last['title'] == last_update:
        return False

    # Set new most recent update
    with open('./last_update.txt', 'w') as file:
        file.write(last['title'])
    return most_recent()
