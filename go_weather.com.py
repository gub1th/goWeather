#TEAM MEMBERS
'''
EMILY PAN - emilypan
JENNY DOAN - jdoan
DANIEL GUNAWAN - dgunawan
SAMHITHA SRINIVASAN - samhiths
'''

#PROJECT DESCRIPTION
'''
In this technologically driven world, many are forced to adapt to changes
or be left in the dust. Grandmas who grew up getting their weather news from 
the newspaper had to eventually adapt themselves to get news from the 
TV. However, getting news from the TV only requires the click of a few buttons, 
compared to getting your weather news from the internet. The Internet is full 
of so many things that a 70 year old grandma can't possibly pick up on in 
her lifespan. Thus, we introduce to you Go Weather.com, where we simplify 
the weather news process. Simply type in your city, and click "Get my weather
today!" to get your weather news. It's that easy! Grandmas all over the world 
no longer need to fret about working the Internet when they have this nifty 
tool for them! 
'''


from tkinter import *
import requests
from bs4 import BeautifulSoup

root = Tk()
root.geometry("500x300")
root.title(" Q&A ")


def getWeather(inp): 
    city = inp
 
    # create url
    url = "https://www.google.com/search?q="+"weather"+city
    
    # requests instance
    html = requests.get(url).content
    
    # getting raw data
    soup = BeautifulSoup(html, 'html.parser')


    # get the temperature
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    
    # this contains time and sky description
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    
    # format the data
    data = str.split('\n')
    time = data[0]
    sky = data[1]


    # list having all div tags having particular clas sname
    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    
    # particular list with required data
    strd = listdiv[5].text
    
    # formatting the string
    pos = strd.find('Wind')
    other_data = strd[pos:]

    return temp, time, sky, other_data

textLabelInit = ""
li = Label(text = textLabelInit, font="Arial 12", foreground="red")

def Take_input():
    INPUT = inputtxt.get("1.0", "end-1c")
    if len(INPUT) == 0:
        textLabelInit = 'Input is Empty! Enter Valid Input!'
        return
    else:
        textLabelInit = ""    
    temp, time, sky, other_data = getWeather(INPUT)
    Output.insert(END,  "\nTemperature: "+temp+ "\nTime:" + time+"\nSky Description:" + sky)

title = Label(text="Go Weather.com", font="Arial 30", foreground="green")



l = Label(text = "Enter in your city!", font="Arial 15")
inputtxt = Text(root, height = 3,
				width = 30,
				bg = "light yellow")

Output = Text(root, height = 7,
			width = 30,
			bg = "light cyan")

Display = Button(root, height = 2,
				width = 20,
				text ="Get my weather today!",
				command = lambda:Take_input())

title.pack()
l.pack()
li.pack()
inputtxt.pack()
Display.pack()
Output.pack()

mainloop()
