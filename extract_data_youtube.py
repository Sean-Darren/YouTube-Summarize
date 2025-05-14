import sys #for reading command-line input
import re #to extract the video ID from the link
import requests #to fetech the data from the web
import bs4 #will use to take the title of Youtube Video using the <title> tag
from youtube_transcript_api import YouTubeTranscriptApi #to take the subtitle 

#Extract Video ID
def extractID(link):
    ID_url = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", link)
    if ID_url:
        print("Video ID: ", ID_url.group(1))
        return ID_url.group(1)  # return ID
    else:
        raise ValueError("Invalid Youtube URL")

#Extract title and channel
def extractTitleChannel(link):
    raw = requests.get(link);
    #Create BeatifulSoup Object
    tag = bs4.BeautifulSoup(raw.text, features="html.parser");
    title_video = tag.find("title").text;
    channel_video = tag.find("span", {"itemprop": "author"}).find("link", {"itemprop": "name"})["content"]

    return title_video, channel_video;

def extractTranscripts(id):
    try:
        transcript_raw = YouTubeTranscriptApi.get_transcript(id, languages=[]); #take the english transcripts
        transcript_full = ' '.join([i['text'] for i in transcript_raw]); #join from seperate text into sentence

        return transcript_full
    
    #Handle when Error Extracting Transcripts
    except Exception as e:
            print(f"Error getting transcripts: {e}")
            return None

