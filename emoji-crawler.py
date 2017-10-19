# coding: utf-8
import requests
import json
from bs4 import BeautifulSoup

emoji_url = 'https://www.webpagefx.com/tools/emoji-cheat-sheet/'

emoji_request = requests.get(emoji_url)

emoji_html = emoji_request.text if emoji_request.status_code == 200 else ""

emoji_json = {}

if emoji_html != "":
    print emoji_html
    soup = BeautifulSoup(emoji_html)
    # write to README.md
    f = open('./README.md', 'a')
    md = ''
    for ul in soup.find_all('ul', class_='emojis'):
        emoji_type = ul['class'][0].capitalize()
        # f.write('## %s \n' % emoji_type)
        # f.write('<table>')
        md += '## %s \n<table>' % emoji_type
        index = 0
        tr = '<tr>'
        for span in ul.find_all('span', class_='name'):
            emoji_name = span.text
            index += 1
            if emoji_json.get(emoji_type, None) is not None:                
                emoji_json[emoji_type].append(emoji_name)
            else:
                emoji_json[emoji_type] = [emoji_name]
            
            if index % 3 == 0:
                tr += '<td>:%s: %s</td></tr><tr>' % (emoji_name, emoji_name)
            else:
                tr += '<td>:%s: %s</td>' % (emoji_name, emoji_name)
        tr += '</tr></table>\n\n'
        md += tr
    f.write(md)
    # write to emoji.json
    f = open('./emoji.json', 'w')
    f.write(json.dumps(emoji_json, ensure_ascii=False, indent=2))
else:
    print "emoji crowel error"
