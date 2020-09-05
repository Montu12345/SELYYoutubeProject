
#importing all libraries
from youtube_api import YouTubeDataAPI
from youtube_transcript_api import YouTubeTranscriptApi
import pandas as pd
import numpy as np
import datetime

#keeps a tally of how many words are in a list
def word_count(list):
    counts = dict()
    words = list

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
    
#number of videos to search for; returns a dictionary
number_of_results = 100
#api key = value
api_key = "VALUE" 
yt = YouTubeDataAPI(api_key)

#search for top 100 videos sorted by relevance between jan 1 2019 and jun 30 2019
searches_2019 = yt.search(q='no equipment workout', max_results=number_of_results, order_by='relevance', published_after=datetime.datetime.timestamp(datetime.datetime(2019,1,1)), published_before=datetime.datetime.timestamp(datetime.datetime(2019,6,30)))

#converts data into a pandas dataframe
df_searches_2019 = pd.DataFrame(searches_2019)

#print data for videos
pd.options.display.max_rows = 100
df_searches_2019.to_string(index = False)
df_searches_2019.iloc[:,0].tolist()
df_searches_2019

#gets more information about the videos based on the video's video_id
searches_2019_more_info = []
video_id_2019 = df_searches_2019.iloc[:,0]
for i in range(0, number_of_results):
    searches_2019_more_info_singluar = yt.get_video_metadata(video_id_2019[i], part=['statistics','snippet'])
    searches_2019_more_info_singluar['number'] = i
    searches_2019_more_info.append(searches_2019_more_info_singluar)

#converts data into a pandas dataframe and prints it out
searches_2019_more_info = pd.DataFrame(searches_2019_more_info)
searches_2019_more_info

#process of counting how many times either nothing is in the description, or the words "Para, Paralympic, Adaptive, Adapted, Disabled, Disability, Differently abled, Disability friendly, Wheelchair Accessible, and Inclusive" appeard.
#search is case sensitive, so also did lowercase search
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
    if (not video_description_2019[i].strip()):
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

#running the word_count function on list of video_tag, prints out the key (word) and the value (number of times the name appeared)
word_count_tag_2019 = word_count(video_tag_list_2019)
for key, value in word_count_tag_2019.items():
    print(key)
    #print(value)

#running the word_count function on video_description, prints out 
word_count_description_2019 = word_count(video_description_list_2019)
sorted_word_count_description_2019 = sorted(word_count_description_2019.items(), key=lambda x: x[1])
df_sorted_word_count_2019 = pd.DataFrame(sorted_word_count_description_2019)
pd.options.display.max_rows = 5500
df_sorted_word_count_2019.head(5300)

#search for top 100 videos sorted by relevance between jan 1 2020 and jun 30 2020
searches_2020 = yt.search(q='no equipment workout', max_results=number_of_results, order_by='relevance', published_after=datetime.datetime.timestamp(datetime.datetime(2020,1,1)), published_before=datetime.datetime.timestamp(datetime.datetime(2020,6,30)))

#converts data into a pandas dataframe
df_searches_2020 = pd.DataFrame(searches_2020)

#print data for videos
pd.options.display.max_rows = 100
df_searches_2020

#gets more information about the videos based on the video's video_id
searches_2020_more_info = []
video_id_2020 = df_searches_2020.iloc[:,0]
for i in range(0, number_of_results):
    searches_2020_more_info_singluar = yt.get_video_metadata(video_id_2020[i], part=['statistics','snippet'])
    searches_2020_more_info_singluar['number'] = i
    searches_2020_more_info.append(searches_2020_more_info_singluar)

#converts data into a pandas dataframe and prints it out
searches_2020_more_info = pd.DataFrame(searches_2020_more_info)
pd.options.display.max_rows = 100
searches_2020_more_info

#process of counting how many times either nothing is in the description, or the words "Para, Paralympic, Adaptive, Adapted, Disabled, Disability, Differently abled, Disability friendly, Wheelchair Accessible, and Inclusive" appeard.
#search is case sensitive, so also did lowercase search
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

#running the word_count function on list of video_tag, prints out the key (word) and the value (number of times the name appeared)
word_count_tag_2020 = word_count(video_tag_list_2020)
for key, value in word_count_tag_2020.items():
    #print(key)
    print(value)

#running the word_count function on video_description, prints out 
word_count_description_2020 = word_count(video_description_list_2020)
sorted_word_count_description_2020 = sorted(word_count_description_2020.items(), key=lambda x: x[1])
df_sorted_word_count = pd.DataFrame(sorted_word_count_description_2020)
pd.options.display.max_rows = 5100
df_sorted_word_count.head(5100)

#gathering subtitles of the videos
transcript_list = []

#checks if videos have subtitles, throws error when video does not have subtitles
for i in range(0, 100):
    print(i)
    transcript_2020 = YouTubeTranscriptApi.get_transcript(video_id_2020[i])
    transcript_list.append(transcript_2020)
    
print (transcript_list)


transcript_list_2019 = []
#checks if videos have subtitles, throws error when video does not have subtitles
for i in range(0, 100):
    print(i)
    transcript_2019 = YouTubeTranscriptApi.get_transcript(video_id_2019[i])
    #searches_2020_more_info_singluar['number'] = i
    transcript_list_2019.append(transcript_2019)
    #transcript_list.append("AKSDJFLKJSDFLKJASD;FKJAS;LDKFJALS;DKJF;LAKSDJF;LAKSDJF;LKASDJF")

print (transcript_list_2019)
