#importing all libraries
from youtube_api import YouTubeDataAPI
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import numpy as np
import datetime

#function to keep tally of the words; returns dictionary
def word_count(list):
    counts = dict()
    words = list

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
#number of videos to be looked at
number_of_results = 100
#api key
api_key = "AIzaSyBh1BfQLT2YryYTx1rolUXaiLprhTTiXKk" 
yt = YouTubeDataAPI(api_key)

#search for videos between jan 1 2019 and jun 30 2019
searches_2019 = yt.search(q='home exercise', max_results=number_of_results, order_by='relevance', published_after=datetime.datetime.timestamp(datetime.datetime(2019,1,1)), published_before=datetime.datetime.timestamp(datetime.datetime(2019,6,30)))

#print(searches)
df_searches_2019 = pd.DataFrame(searches_2019)
df_searches_2019.head(5)

searches_2019_more_info = []
video_id_2019 = df_searches_2019.iloc[:,0]
for i in range(0, number_of_results):
    searches_2019_more_info_singluar = yt.get_video_metadata(video_id_2019[i], part=['statistics','snippet'])
    searches_2019_more_info_singluar['number'] = i
    searches_2019_more_info.append(searches_2019_more_info_singluar)
    
searches_2019_more_info = pd.DataFrame(searches_2019_more_info)
searches_2019_more_info.head(5)

None_2019 = 0
Para_2019 = 0
para_2019 = 0
Paralympic_2019 = 0 
paralympic_2019 = 0 
Adaptive_2019 = 0
adaptive_2019 = 0
Adapted_2019 = 0
adapted_2019 = 0
Disabled_2019 = 0
disabled_2019 = 0
Disability_2019 = 0
disability_2019 = 0
Differently_abled_2019 = 0
differently_abled_2019 = 0
Disability_friendly_2019 = 0
disability_friendly_2019 = 0
Wheelchair_accessible_2019 = 0
wheelchair_accessible_2019 = 0
Inclusive_2019 = 0
inclusive_2019 = 0

video_title_2019 = searches_2019_more_info.iloc[:,4]
video_description_2019 = searches_2019_more_info.iloc[:,5]

for i in range(0, number_of_results):
    if (not video_description_2020[i].strip()):
        None_2019 += 1

for i in range(0, number_of_results):
    if ("Para" in (video_description_2019[i] or video_title_2019[i])):
        Para_2019 += 1
for i in range(0, number_of_results):
    if ("para" in (video_description_2019[i] or video_title_2019[i])):
        para_2019 += 1
        
for i in range(0, number_of_results):
    if ("Paralympic" in (video_description_2019[i] or video_title_2019[i])):
        Paralympic_2019 += 1
for i in range(0, number_of_results):
    if ("paralympic" in (video_description_2019[i] or video_title_2019[i])):
        paralympic_2019 += 1
        
for i in range(0, number_of_results):
    if ("Adaptive" in (video_description_2019[i] or video_title_2019[i])):
        Adaptive_2019 += 1
for i in range(0, number_of_results):
    if ("adaptive" in (video_description_2019[i] or video_title_2019[i])):
        adaptive_2019 += 1
        
for i in range(0, number_of_results):
    if ("Disabled" in (video_description_2019[i] or video_title_2019[i])):
        Disabled_2019 += 1
for i in range(0, number_of_results):
    if ("disabled" in (video_description_2019[i] or video_title_2019[i])):
        disabled_2019 += 1
        
for i in range(0, number_of_results):
    if ("Disability" in (video_description_2019[i] or video_title_2019[i])):
        Disability_2019 += 1
for i in range(0, number_of_results):
    if ("disability" in (video_description_2019[i] or video_title_2019[i])):
        disability_2019 += 1

for i in range(0, number_of_results):
    if ("Differently_abled" in (video_description_2019[i] or video_title_2019[i])):
        Differently_abled_2019 += 1
for i in range(0, number_of_results):
    if ("differently_abled" in (video_description_2019[i] or video_title_2019[i])):
        differently_abled_2019 += 1
        
for i in range(0, number_of_results):
    if ("Disability_friendly" in (video_description_2019[i] or video_title_2019[i])):
        Disability_friendly_2019 += 1
for i in range(0, number_of_results):
    if ("disability_friendly" in (video_description_2019[i] or video_title_2019[i])):
        disability_friendly_2019 += 1
        
for i in range(0, number_of_results):
    if ("Wheelchair_accessible" in (video_description_2019[i] or video_title_2019[i])):
        Wheelchair_accessible_2019 += 1
for i in range(0, number_of_results):
    if ("wheelchair_accessible" in (video_description_2019[i] or video_title_2019[i])):
        wheelchair_accessible_2019 += 1

for i in range(0, number_of_results):
    if ("Inclusive" in (video_description_2019[i] or video_title_2019[i])):
        Inclusive_2019 += 1
for i in range(0, number_of_results):
    if ("inclusive" in (video_description_2019[i] or video_title_2019[i])):
        inclusive_2019 += 1
        
print ("2019 None:", None_2019)

print ("2019 Para:", Para_2019)
print ("2019 para:", para_2019)

print ("2019 Paralympic:", Paralympic_2019)
print ("2019 paralympic:", paralympic_2019)

print ("2019 Adaptive:", Adaptive_2019) 
print ("2019 adaptive:", adaptive_2019)

print ("2019 Adapted:", Adapted_2019)
print ("2019 adapted:", adapted_2019)

print ("2019 Disabled:", Disabled_2019)
print ("2019 disabled:", disabled_2019)

print ("2019 Disability:", Disability_2019)
print ("2019 disability:", disability_2019)

print ("2019 Differently_abled:", Differently_abled_2019)
print ("2019 differently_abled:", differently_abled_2019)

print ("2019 Disability_friendly:", Disability_friendly_2019)
print ("2019 differently_abled:", differently_abled_2019)

print ("2019 Wheelchair_accessible:", Wheelchair_accessible_2019)
print ("2019 wheelchair_accessible:", wheelchair_accessible_2019)

print ("2019 Inclusive:", Inclusive_2019)
print ("2019 inclusive:", inclusive_2019)

#putting all words in the description into a list (words separated by " ")
video_description_list_2019 = []
for i in range(0, number_of_results):
    description_2019 = video_description_2019[i].split(' ')
    video_description_list_2019 = video_description_list_2019 + (description_2019)

#putting all words in the video tag into a list (words separated by "|")
video_tag_2019 = searches_2019_more_info.iloc[:,12]
video_tag_list_2019 = []
for i in range(0, number_of_results):
    tag_2019 = video_tag_2019[i].split("|")
    video_tag_list_2019 = video_tag_list_2019 + (tag_2019)
#print (word_list_description)
#print (word_list_video_tag)

#running the word_count function on list of video_tag and video description, prints out if the number count is > 1
word_count_tag_2019 = word_count(video_tag_list_2019)
for key, value in word_count_tag_2019.items():
    if word_count_tag_2019[key] > 1:
        print(key, value)
        
word_count_description_2019 = word_count(video_description_list_2019)
for key, value in word_count_description_2019.items():
    if word_count_description_2019[key] > 1:
        print(key, value)
        
sorted_word_count_tag_2019 = sorted(word_count_tag_2019.items(), key=lambda x: x[1])
print(sorted_word_count_tag_2019)

sorted_word_count_description_2019 = sorted(word_count_description_2019.items(), key=lambda x: x[1])
print(sorted_word_count_description_2019)

#conducting search on youtube. sorting by relevance, videos publised between jan 1st 2020 and jun 30 2020
searches_2020 = yt.search(q='home exercise', max_results=number_of_results, order_by='relevance', published_after=datetime.datetime.timestamp(datetime.datetime(2020,1,1)), published_before=datetime.datetime.timestamp(datetime.datetime(2020,6,30)))

#converting searches (list) into pandas dataframe 
df_searches_2020 = pd.DataFrame(searches_2020)
#df_search.head(100)

#for i in range(0, number_of_results):
   # print(asdfh_search.iloc[:,4][i]);
   
#using youtube video video_id to get more information about the video
searches_2020_more_info = []
video_id_2020 = df_searches_2020.iloc[:,0]
for i in range(0, number_of_results):
    searches_2020_more_info_singluar = yt.get_video_metadata(video_id_2020[i], part=['statistics','snippet'])
    searches_2020_more_info_singluar['number'] = i
    searches_2020_more_info.append(searches_2020_more_info_singluar)
    
#converting to pandas dataframe
searches_2020_more_info = pd.DataFrame(searches_2020_more_info)
pd.options.display.max_rows = 100
searches_2020_more_info.iloc[:,5]
print(searches_2020_more_info)

#searching how many times the following keywords appear in the title or description of a video
None_2020 = 0
Para_2020 = 0
para_2020 = 0
Paralympic_2020 = 0 
paralympic_2020 = 0 
Adaptive_2020 = 0
adaptive_2020 = 0
Adapted_2020 = 0
adapted_2020 = 0
Disabled_2020 = 0
disabled_2020 = 0
Disability_2020 = 0
disability_2020 = 0
Differently_abled_2020 = 0
differently_abled_2020 = 0
Disability_friendly_2020 = 0
disability_friendly_2020 = 0
Wheelchair_accessible_2020 = 0
wheelchair_accessible_2020 = 0
Inclusive_2020 = 0
inclusive_2020 = 0

video_title_2020 = searches_2020_more_info.iloc[:,4]
video_description_2020 = searches_2020_more_info.iloc[:,5]

#if myString.strip():
   # print("it's not an empty or blank string")
#else:
  #  print("it's an empty or blank string")
for i in range(0, number_of_results):
    if (not video_description_2020[i].strip()):
        None_2020 += 1

for i in range(0, number_of_results):
    if ("Para" in (video_description_2020[i] or video_title_2020[i])):
        Para_2020 += 1
for i in range(0, number_of_results):
    if ("para" in (video_description_2020[i] or video_title_2020[i])):
        para_2020 += 1
        
for i in range(0, number_of_results):
    if ("Paralympic" in (video_description_2020[i] or video_title_2020[i])):
        Paralympic_2020 += 1
for i in range(0, number_of_results):
    if ("paralympic" in (video_description_2020[i] or video_title_2020[i])):
        paralympic_2020 += 1
        
for i in range(0, number_of_results):
    if ("Adaptive" in (video_description_2020[i] or video_title_2020[i])):
        Adaptive_2020 += 1
for i in range(0, number_of_results):
    if ("adaptive" in (video_description_2020[i] or video_title_2020[i])):
        adaptive_2020 += 1
        
for i in range(0, number_of_results):
    if ("Disabled" in (video_description_2020[i] or video_title_2020[i])):
        Disabled_2020 += 1
for i in range(0, number_of_results):
    if ("disabled" in (video_description_2020[i] or video_title_2020[i])):
        disabled_2020 += 1
        
for i in range(0, number_of_results):
    if ("Disability" in (video_description_2020[i] or video_title_2020[i])):
        Disability_2020 += 1
for i in range(0, number_of_results):
    if ("disability" in (video_description_2020[i] or video_title_2020[i])):
        disability_2020 += 1

for i in range(0, number_of_results):
    if ("Differently_abled" in (video_description_2020[i] or video_title_2020[i])):
        Differently_abled_2020 += 1
for i in range(0, number_of_results):
    if ("differently_abled" in (video_description_2020[i] or video_title_2020[i])):
        differently_abled_2020 += 1
        
for i in range(0, number_of_results):
    if ("Disability_friendly" in (video_description_2020[i] or video_title_2020[i])):
        Disability_friendly_2020 += 1
for i in range(0, number_of_results):
    if ("disability_friendly" in (video_description_2020[i] or video_title_2020[i])):
        disability_friendly_2020 += 1
        
for i in range(0, number_of_results):
    if ("Wheelchair_accessible" in (video_description_2020[i] or video_title_2020[i])):
        Wheelchair_accessible_2020 += 1
for i in range(0, number_of_results):
    if ("wheelchair_accessible" in (video_description_2020[i] or video_title_2020[i])):
        wheelchair_accessible_2020 += 1

for i in range(0, number_of_results):
    if ("Inclusive" in (video_description_2020[i] or video_title_2020[i])):
        Inclusive_2020 += 1
for i in range(0, number_of_results):
    if ("inclusive" in (video_description_2020[i] or video_title_2020[i])):
        inclusive_2020 += 1

#difference between Para and para exists --> case sensitive
print ("2020 None", None_2020)

print ("2020 Para:", Para_2020)
print ("2020 para:", para_2020)

print ("2020 Paralympic:", Paralympic_2020)
print ("2020 paralympic:", paralympic_2020)

print ("2020 Adaptive:", Adaptive_2020) 
print ("2020 adaptive:", adaptive_2020)

print ("2020 Adapted:", Adapted_2020)
print ("2020 adapted:", adapted_2020)

print ("2020 Disabled:", Disabled_2020)
print ("2020 disabled:", disabled_2020)

print ("2020 Disability:", Disability_2020)
print ("2020 disability:", disability_2020)

print ("2020 Differently_abled:", Differently_abled_2020)
print ("2020 differently_abled:", differently_abled_2020)

print ("2020 Disability_friendly:", Disability_friendly_2020)
print ("2020 differently_abled:", differently_abled_2020)

print ("2020 Wheelchair_accessible:", Wheelchair_accessible_2020)
print ("2020 wheelchair_accessible:", wheelchair_accessible_2020)

print ("2020 Inclusive:", Inclusive_2020)
print ("2020 inclusive:", inclusive_2020)

#putting all words in the description into a list (words separated by " ")
video_description_list_2020 = []
for i in range(0, number_of_results):
    description_2020 = video_description_2020[i].split(' ')
    video_description_list_2020 = video_description_list_2020 + (description_2020)

#putting all words in the video tag into a list (words separated by "|")
video_tag_2020 = searches_2020_more_info.iloc[:,12]
video_tag_list_2020 = []
for i in range(0, number_of_results):
    tag_2020 = video_tag_2020[i].split("|")
    video_tag_list_2020 = video_tag_list_2020 + (tag_2020)




#sort_orders = sorted(orders.items(), key=lambda x: x[1])
#print (word_list_description)
#print (word_list_video_tag)

word_count_tag_2020 = word_count(video_tag_list_2020)
for key, value in word_count_tag_2020.items():
    if word_count_tag_2020[key] > 1:
        print(key, value)

word_count_description_2020 = word_count(video_description_list_2020)

for key, value in word_count_description_2020.items():
    if word_count_description_2020[key] > 1:
        print(key, value)

sorted_word_count_tag_2020 = sorted(word_count_tag_2020.items(), key=lambda x: x[1])
print(sorted_word_count_tag_2020)

sorted_word_count_description_2020 = sorted(word_count_description_2020.items(), key=lambda x: x[1])
print(sorted_word_count_description_2020)

#get_video_comments(video_id, get_replies=True, max_results=None, next_page_token=False, parser=<function parse_comment_metadata>, part=['snippet'], **kwargs)

comments_2020 = []
for i in range(0, 1):
    comments = yt.get_video_comments(df_searches_2020.iloc[:,0][i],False, None, part=['snippet'], searchTerms="health")
    #as_comments['number'] = i
    comments_2020.append(comments)

#asdfh_comments = pd.DataFrame(asdf_comments)
#print(asdfh_comments.iloc[:,0])

#print(comments_2020)
asdfh_comments = pd.DataFrame(comments_2020)
#pd.options.display.max_columns = 30
pd.set_option('display.max_colwidth', -1)
asdfh_comments.head(1)

transcript_list = []
for i in range(0, number_of_results):
    transcript_2020 = YouTubeTranscriptApi.get_transcript(video_id_2020[i])
    #searches_2020_more_info_singluar['number'] = i
    transcript_list.append(transcript_2020)
