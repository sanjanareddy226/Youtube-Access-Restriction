import comment_extract as CE
import sentimentYouTube as SYT
import nltk
import realtime_demo as x
nltk.download('punkt')
from urllib.request import urlopen
import urllib.request
import webbrowser

  
def main():
# EXAMPLE VideoId = 'tCXGJQYZ9JA'
    link = input("Enter Video : ")
    
#    link=H.my_form_post()
    i=0
    while(link[i]!='='):
        i=i+1
    id=link[i+1:]
    
	# Fetch the number of comments
	# if count = -1, fetch all comments
#    count = int(input("Enter no. of comments to extract : "))
    comments = CE.commentExtract(id, 100)
    possent=SYT.sentiment(comments)
    age=x.main()
    print('age is', age)
    print('positive content % is',possent)
    if(age>0 and age<5 and possent==100):
        webbrowser.open(link)
    elif(age>5 and age<10 and possent>90):
        webbrowser.open(link)
    elif(age>10 and age<15 and possent>80):
        webbrowser.open(link)
    elif(age>15 and age<18 and possent>75):
        webbrowser.open(link)
    elif(age>18):
        webbrowser.open(link)
    else:
        print('not accessible')
    # dosomething
        
        
    


if __name__ == '__main__':
	main()
