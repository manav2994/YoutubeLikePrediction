#!/usr/bin/python
#precogTask

import numpy as np
import csv as csv
import pandas as pd
import re
file = csv.reader(open('unprocessedFood.csv', 'r'))
fileOut = open('processedFood', 'w')

#1title,2videoId,3description,4channelId,5channelTitle,6ChannelPublishedAt,7videoPublishedAt,
#8viewCount,9 likeCount,10dislikeCount,11commentCount,12favoriteCount,13duration,14caption,
#15 licensedContent,16channel_videoCount, 17 channel_subscriberCount,
#18channel_commentCount, 19channel_ViewCount, 20country


data = []
newData = [] 

for row in file:
		data.append(row)

#Features collected as well as derived features list
header = ["videoID","channelAge","videoAge","viewCount","commentCount","favoriteCount","channel_commentCount","channel_subsriberCount","channel_ViewCount","likeCount","channelViewCount/channeVideoCount","viewCount/videoAge","subscriberCount/channelVideoCount","channel_subsriberCount/channelAge"]
newData.append(header)

for i in range(1, len(data)):
	a  = data[i][5]
	b = re.split('-',a)
	#Change using current Date
	d = re.split('T',b[2])
	channelAge = (2017-int(b[0]))*365 + (20 - int(b[1])) + int(d[0])

	a1  = data[i][6]
	b1 = re.split('-',a1)
	#Change using current Date
	d1 = re.split('T',b1[2])
	videoAge = (2017-int(b1[0]))*365 + (20 - int(b1[1])) + int(d1[0])


	if int(data[i][15]) == 0:
		data[i][15] =1

	if int(channelAge) == 0:
		channelAge = 1
	file
	if int(videoAge) == 0:
		videoAge = 1

	if int(data[i][15]) == 0:
		data[i][15] =1

	if int(data[i][9]) ==0:
		data[i][9] =1

	y = [data[i][1],int(channelAge),int(videoAge),int(data[i][7]),int(data[i][10]),int(data[i][11]),int(data[i][17]),int(data[i][16]), int(data[i][18]),int(data[i][8]), int(int(data[i][18])/int(data[i][15])), int(int(data[i][7])/int(videoAge)),  int(int(data[i][16])/int(data[i][15])), int(int(data[i][16])/int(channelAge))]
	newData.append(y)

#writing dataframe to csv
df = pd.DataFrame(newData, columns = header)
df.to_csv(fileOut, sep=',', encoding='utf-8')


