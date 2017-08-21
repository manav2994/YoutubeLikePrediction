
# Youtube Like Prediction

Being an open ended research problem, this approach was followed after doing the Literature Review. Youtube videos are still found long after they are initially submitted to the portal and prediction of like count becomes difficult. 585 videos were collected with the search query '**food**' using the YouTube Data API v3 out of which 100 were separated for testing. After following some previous work done in this area and considering the availability of limited data, Random forest Regressor was used for prediction of likes. Following features were used for training:

[**"channelAge","videoAge","viewCount","commentCount","favoriteCount","channel_commentCount","channel_subsriberCount","channel_ViewCount","likeCount"**,
*"channelViewCount/channeVideoCount","viewCount/videoAge","subscriberCount/channelVideoCount","channel_subsriberCount/channelAge"]*

These include both *derived* and **collected** features.


## Results:

* cross_val_score = [ 0.85541751  0.87433793  0.80681138  0.70352987  0.86366066] 
* Accuracy = **82.1%**

### Files Description

* data_collection.py - Run this script to collect videos/channels metadata [Default Query - Food]
```shell
python data_collection.py --q food
```
* featureDerive.py - Run this script to process data and derive features for training
```shell
python featureDerive.py
```
* train.py - Run this to perform traing and testing on the train and test data respectively
```shell
python train.py
```
* RandomForestRegressor - Model obtained after training
* processedFood.csv - Collected data

## References
1. Szabo, Gabor, and Bernardo A. Huberman. "Predicting the popularity of online content." Communications of the ACM 53.8 (2010): 80-88.
2. H. Jiang. "Predicting YouTube Views and Ratings using Conditional Random Fields."
3. Ayush1997. "YouTube-Like-predictor" Retrieved  from https://github.com/ayush1997/YouTube-Like-predictor
