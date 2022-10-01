import requests 
import xml.etree.ElementTree as ET 

# url of news rss feed 
RSS_FEED_URL = "http://www.hindustantimes.com/rss/topnews/rssfeed.xml"	

def loadRSS(): 
	''' 
	utility function to load RSS feed 
	'''
	# create HTTP request response object 
	resp = requests.get(RSS_FEED_URL) 

	# return response content 
	return resp.content 

def parseXML(rss): 
	''' 
	utility function to parse XML format rss feed 
	'''
	# create element tree root object 
	root = ET.fromstring(rss) 

	# create empty list for news items 
	newsitems = [] 

	# iterate news items 
	for item in root.findall('./channel/item'): 
		news = {} 

		# iterate child elements of item 
		for child in item: 

			# special checking for namespace object content:media 
			if child.tag == '{http://search.yahoo.com/mrss/}content': 
				news['media'] = child.attrib['url'] 
			else: 
				news[child.tag] = child.text.encode('utf8') 
		newsitems.append(news) 

	# return news items list 
	return newsitems 

def topStories(): 
	''' 
	main function to generate and return news items 
	'''
	# load rss feed 
	rss = loadRSS() 

	# parse XML 
	newsitems = parseXML(rss) 
	return newsitems 
