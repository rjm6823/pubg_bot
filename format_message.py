import re


def replace_html_tags(text):
    """Replaces breaks and list items with newlines"""
    replace = re.compile('<br>|<li>')
    return re.sub(replace, '\n', text)


def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)


def format_notes(item):
    title = '__**' + item['title'] + '**__ - '
    date = item['published'] + '\n'
    desc = remove_html_tags(replace_html_tags(item['description'])) + '\n'
    link = '<' + item['link'] + '>'
    return title + date + desc + link
