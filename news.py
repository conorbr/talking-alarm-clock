# Bitcoin Price Index Module
#
# import requests
# import json
# from newsapi.sources import Sources
#
# s = Sources(API_KEY="1ad1dcfe53bd46099344d09a2f2575d3")
#
#
#

# print s.all()
# print s.information().all_categories()
# json = s.get()



# request = requests.get("https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=1ad1dcfe53bd46099344d09a2f2575d3")
# if request.status_code == 200:
#     obj = json.loads(request.text)
#     req_obj = obj[0][1]
#     print request
#     print req_obj
#     print obj
# else:
#     print "Failed to retrieve news Response returned code " + str(request.response_code)
#     print "failed"

import feedparser


def get_news():
    try:
      host = "feeds.bbci.co.uk"
      path = "/news/world/rss.xml"
      rss_url = 'http://' + host + path
      rss = feedparser.parse(rss_url)

      #for entry in rss.entries[:4]:
      #    print entry['title']
      #    print entry['description']
      #
      #print rss.entries[0]['title']
      #print rss.entries[0]['description']
      #print rss.entries[1]['title']
      #print rss.entries[1]['description']
      #print rss.entries[2]['title']
      #print rss.entries[2]['description']
      #print rss.entries[3]['title']
      #print rss.entries[3]['description']

      newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.  ' + rss.entries[3]['title'] + '.  ' + rss.entries[3]['description'] + '.  '

      # print newsfeed
      newsfeed = newsfeed.encode('utf-8')

      # Today's news from BBC
      news = 'And now, The latest stories from the World section of the BBC News.  ' + newsfeed


    except:
        news = "sorry i could not get in contact with bbc news, no news, is good news, right?. have a great day"

    return news
