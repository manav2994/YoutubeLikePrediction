#!/usr/bin/python
#precogtask
# -*- coding: utf-8 -*-

from apiclient.discovery import build
#from apiclient.errors import HttpError
#from oauth2client.tools import argparser # removed by Dongho
import argparse
import csv
import unidecode
import pycountry
import random


def youtube_search(options):
	# Call the search.list method to retrieve results matching the specified
	
	pageToken=""
	# create a CSV output for video list    
	csvFile = open('rawData.csv','w')
	csvWriter = csv.writer(csvFile)
	csvWriter.writerow(["title","videoId","description","channelId","channelTitle","ChannelPublishedAt","videoPublishedAt","viewCount","likeCount","dislikeCount","commentCount","favoriteCount","duration","caption","licensedContent","channel_videoCount","channel_subscriberCount","channel_commentCount","channel_ViewCount","country"])
	
	#Enter you API key here
	DEVELOPER_KEY = "AIzaSyAgzszK84rYUM0ErWSdtiV-tyNGqGB3xFg"
	YOUTUBE_API_SERVICE_NAME = "youtube"
	YOUTUBE_API_VERSION = "v3"
	count =0 
	#For loop to specify the number of pages
	for i in range(0,20):
		youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

		search_response = youtube.search().list(q=options.q, part="id,snippet", pageToken= pageToken, maxResults=options.max_results, order = "viewCount").execute()

		videos = []
		channels = []
		playlists = []

	
	
		for search_result in search_response.get("items", []):
			if search_result["id"]["kind"] == "youtube#video":
				title = search_result["snippet"]["title"]
				title = unidecode.unidecode(title)
				channelId = search_result["snippet"]["channelId"]
				publishedAt = search_result["snippet"]["publishedAt"]
				description = search_result["snippet"]["description"]
				description = unidecode.unidecode(description)
				videoId = search_result["id"]["videoId"]
				video_response = youtube.videos().list(id=videoId,part="statistics, contentDetails").execute()
				#dimension = video_response["contentDetails"]["dimension"]
				#definition = video_response["contentDetails"]["definition"]
				#videoStats
				for video_result in video_response.get("items",[]):
					duration = video_result["contentDetails"]["duration"]
					if video_result["contentDetails"]["caption"] == "True":
						caption = 1
					else:
						caption = 0
					if video_result["contentDetails"]["licensedContent"] == "True":
						licensedContent =  1
					else:
						licensedContent =  0	

					viewCount = video_result["statistics"]["viewCount"]
					if 'likeCount' not in video_result["statistics"]:
						likeCount = 0
					else:
						likeCount = video_result["statistics"]["likeCount"]
					if 'dislikeCount' not in video_result["statistics"]:
						dislikeCount = 0
					else:
						dislikeCount = video_result["statistics"]["dislikeCount"]
					if 'commentCount' not in video_result["statistics"]:
						commentCount = 0
					else:
						commentCount = video_result["statistics"]["commentCount"]
					if 'favoriteCount' not in video_result["statistics"]:
						favoriteCount = 0
					else:
						favoriteCount = video_result["statistics"]["favoriteCount"]
				

				#channel Stats
				channelResults = youtube.channels().list(part="snippet, statistics", id=channelId).execute()
				channelTitle = channelResults["items"][0]["snippet"]['title']
				ChannelPublishedAt = channelResults["items"][0]["snippet"]["publishedAt"]
				if 'country' not in channelResults["items"][0]["snippet"]:
					country = 0
				else:	
					c = channelResults["items"][0]["snippet"]["country"]
					country = pycountry.countries.get(alpha_2= c)
					country = country.name
				if 'viewCount' not in channelResults["items"][0]["statistics"]:
					channel_ViewCount = 0
				else:
					channel_ViewCount = channelResults["items"][0]["statistics"]["viewCount"]
				if 'commentCount' not in channelResults["items"][0]["statistics"]:
					channel_commentCount = 0
				else:
					channel_commentCount = channelResults["items"][0]["statistics"]["commentCount"]
				if 'subscriberCount' not in channelResults["items"][0]["statistics"]:
					channel_subscriberCount = 0
				else:
					channel_subscriberCount = channelResults["items"][0]["statistics"]["subscriberCount"]
				if 'videoCount' not in channelResults["items"][0]["statistics"]:
					channel_videoCount = 0
				else:
					channel_videoCount = channelResults["items"][0]["statistics"]["videoCount"]		

				if count == 30:
					k = random.randint(0,4)
					#Enter you API keys here
					devKeys = ["AIzaSyAtwN1cSa0A20aKRmUUsTVb0teStkzqkcY", "AIzaSyBnzWtgUAaKzXn--CWHHvCSE6CTH_TgDuA", "AIzaSyBEwAbwqJMST6rZsM_wIQukAKrQhH4Ttog", "AIzaSyAIgXTnpjPNXC1fdQHBNWvlykPovud9frA"]
					DEVELOPER_KEY = devKeys[k]
					count = 0 
					pageToken = search_response["nextPageToken"]
				count +=1
				
				print(i)
				csvWriter.writerow([title,videoId,description,channelId,channelTitle,ChannelPublishedAt,publishedAt,viewCount,likeCount,dislikeCount,commentCount,favoriteCount,duration,caption,licensedContent,channel_videoCount,channel_subscriberCount,channel_commentCount,channel_ViewCount,country])
		

	csvFile.close()

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Search on YouTube')
	parser.add_argument("--q", help="Search term", default="Food")
	parser.add_argument("--max-results", help="Max results", default=50)
	args = parser.parse_args()
	youtube_search(args)

