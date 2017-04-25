import feedparser


def get_news():
    try:
      host = "feeds.bbci.co.uk"
      path = "/news/world/rss.xml"
      rss_url = 'http://' + host + path
      rss = feedparser.parse(rss_url)

      #try for rss.entries[:4]:
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

      newsfeed = rss.entries[0]['title'] + '.  ' + rss.entries[0]['description'] + '.  ' + rss.entries[1]['title'] + '.  ' + rss.entries[1]['description'] + '.  ' + rss.entries[2]['title'] + '.  ' + rss.entries[2]['description'] + '.   '

      # print newsfeed
      newsfeed = newsfeed.encode('utf-8')

      # Today's news from BBC
      news = 'And now, The latest stories from the World section of the BBC News.  ' + newsfeed


    except:
        news = "sorry i could not get in contact with bbc news, no news, is good news, right?. have a great day"

    return news
