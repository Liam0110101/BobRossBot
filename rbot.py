"""START"""

# Import required modules
import praw
import time
import random
from datetime import datetime
# Defining time
now = datetime.now()
'''BOT'''

def bot():


    # BobRossBot_ v0.3 (cleaned up code)
    # Created by /u/whaliam
    # 6Ep96ck9@protonmail.com
    # Create Reddit instance
    # Setting variables
    print("Logging in...")

    reddit = praw.Reddit(user_agent='Bob Ross Bot v0.1',
                         client_id='mKkUYj3Ms9Cwfw',
                         client_secret='scnLMlK-DBnHQbl8N4FB-HKQvPY',
                         username='BobRossBot_',
                         password='6Ep96ck9')
    print("Welcome BobRossBot_ :)")
    print("Started: " + str(now))
    print("Loading quotes...")
    '''BOT|QUOTES''' # Enter quotes in the array below
    ross_quotes = \
        [
            " 'Trees cover up a multitude of sins.'",

            " 'Remember our Golden Rule: A thin paint sticks to a thick paint.' ",

            " 'And that makes it look like birch trees, isn't that sneaky? Heh. Ha. It's gorgeous.' ",

            " 'Be sure to use odorless paint-thinner. If it's not odorless, you'll find yourself working alone very, very quick.' ",

            " 'Let's just blend this little rascal here, ha! Happy as we can be.' ",

            " 'Clouds are very, very free.' ",

            " 'Decide where your little footy hills live.' ",

            " 'Shwooop. Hehe. You have to make those little noises, or it just doesn't work.' ",

            " 'Try to imagine that you are a tree. How do you want to look out here?' ",

            "  'You know me, I gotta put in a big tree.' ",

            " 'Gotta give him a friend. Like I always say 'everyone needs a friend'. ",

            "  'Any time ya learn, ya gain.' ",

            "  'Just put a few do-ers in there...' ",

            "  'Maybe in our world there lives a happy little tree over there.' ",

            "  'You can do anything you want to do. This is your world.' ",

            "  'You can put as many or as few as you want in your world.' ",

            " 'That's a crooked tree. We'll send him to Washington.' ",

            " 'I like to beat the brush.' ",

            " 'In painting, you have unlimited power. You have the ability to move mountains. You can bend rivers. But when I get home, the only thing I have power over is the garbage.' ",

            " 'You need the dark in order to show the light.' ",

            " 'Look around. Look at what we have. Beauty is everywhere—you only have to look to see it.' ",

            " 'There's nothing wrong with having a tree as a friend.' ",

            " 'There's nothing wrong with having a tree as a friend.' ",

            " 'They say everything looks better with odd numbers of things. But sometimes I put even numbers—just to upset the critics.' ",

            " 'How do you make a round circle with a square knife? That’s your challenge for the day.' ",

            " 'I remember when my Dad told me as a kid, ‘If you want to catch a rabbit, stand behind a tree and make a noise like a carrot. Then when the rabbit comes by you grab him.’ Works pretty good until you try to figure out what kind of noise a carrot makes…' ",

            " 'We tell people sometimes: we're like drug dealers, come into town and get everybody absolutely addicted to painting. It doesn't take much to get you addicted.' ",

            " 'The secret to doing anything is believing that you can do it. Anything that you believe you can do strong enough, you can do. Anything. As long as you believe. ",

            " 'Water's like me. It's laaazy ... Boy, it always looks for the easiest way to do things' ",

            " 'Oooh, if you have never been to Alaska, go there while it is still wild. My favorite uncle asked me if I wanted to go there, Uncle Sam. He said if you don't go, you're going to jail. That is how Uncle Sam asks you.' ",

            " 'I really believe that if you practice enough you could paint the 'Mona Lisa' with a two-inch brush.' ",

            " 'If I paint something, I don't want to have to explain what it is.' ",

            " 'We artists are a different breed of people. We're a happy bunch.' ",

            " 'We don't make mistakes. We just have happy accidents.' ",

            " 'We don't make mistakes. We just have happy accidents.' ",

            " 'You too can paint almighty pictures.' ",

            " 'Don’t forget to make all these little things individuals — all of them special in their own way.' ",

            " 'Talent is a pursued interest. Anything that you’re willing to practice, you can do.' ",

            " 'Make love to the canvas.' ",

            " 'Don’t forget to tell these special people in your life just how special they are to you.' ",

            " 'Just let go — and fall like a little waterfall.' ",

            " 'You can do anything you want to do. This is your world.' ",

            " 'You can have anything you want in the world — once you help everyone around you get what they want.' ",

            " 'If you do too much, it’s going to lose its effectiveness.' ",

            " 'This is happy place; little squirrels live here and play.' ",

            " 'Remember how free clouds are. They just lay around in the sky all day long' ",

            " 'That’s where the crows will sit. But we’ll have to put an elevator to put them up there because they can’t fly, but they don’t know that, so they still try.' ",

            " 'We don’t really know where this goes — and I’m not sure we really care.' ",

            " 'Go out on a limb — that’s where the fruit is.' ",

            " 'Isn’t it fantastic that you can change your mind and create all these happy things?' ",

            " 'It’s life. It’s interesting. It’s fun.' ",

        ]
    '''BOT|IMAGES''' # Enter Imgur links in the array below
    ross_images = \
        [
            " [Here's a random painting :)](https://imgur.com/gallery/q2GEp) ",
            " [Here's a random painting :)](https://imgur.com/gallery/XJUfQ) ",
            " [Here's a random painting :)](https://imgur.com/gallery/L0rLs) ",
            " [Here's a random painting :)](https://imgur.com/gallery/m58x4xS) ",
            " [Here's a random painting :)](https://imgur.com/gallery/r6xblZg) ",
            " [Here's a random painting :)](https://imgur.com/gallery/mT1DRVY) ",
            " [Here's a random painting :)](https://imgur.com/gallery/Xy1sA) ",
            " [Here's a random painting :)](https://imgur.com/gallery/hc3HO) ",
            " [Here's a random painting :)](https://imgur.com/gallery/3Xfh1) ",
            " [Here's a random painting :)](https://imgur.com/gallery/8USdT) ",
            " [Here's a random painting :)](https://imgur.com/gallery/CE5blh5) ",
            " [Here's a random painting :)](https://imgur.com/gallery/m7ymyYp) ",
            " [Here's a random painting :)](https://imgur.com/gallery/2ECwjYr) ",
            " [Here's a random painting :)](https://imgur.com/gallery/kK1Zr) ",
            " [Here's a random painting :)](https://imgur.com/gallery/qs6Xd) ",
            " [Here's a random painting :)](https://imgur.com/gallery/DJ4zL) ",
            " [Here's a random painting :)](https://imgur.com/gallery/xWBUI8S) ",
            " [Here's a random painting :)](https://imgur.com/gallery/hM7ls6K) ",
            " [Here's a random painting :)](https://imgur.com/gallery/P6L9y) ",
            " [Here's a random painting :)](https://imgur.com/a/BP7kB) ",
            " [Here's a random painting :)](https://i.imgur.com/gyuNg8j.jpg) ",
            " [Here's a random painting :)](https://imgur.com/7RmtwPK) ",
            " [Here's a random painting :)](https://i.imgur.com/sgJbHNS.jpg) ",
            " [Here's a random painting :)](https://imgur.com/a/tMF0C) ",
            " [Here's a random painting :)](https://i.imgur.com/1qytrLH.jpg) ",
            " [Here's a random painting :)](https://i.imgur.com/BezhUOU.jpg) ",
            " [Here's a random painting :)](https://imgur.com/gallery/fzQkm) ",
            " [Here's a random painting :)](https://imgur.com/a/jSPlu) ",
            " [Here's a random painting :)](https://imgur.com/a/e01ND) ",
            " [Here's a random painting :)](https://imgur.com/a/oeGZ6) ",
            " [Here's a random painting :)](https://imgur.com/w4nER2N) ",
            " [Here's a random painting :)](https://i.imgur.com/7b44qgF.jpg) ",
            " [Here's a random painting :)](https://i.imgur.com/7b44qgF.jpg) ",
            " [Here's a random painting :)](https://imgur.com/L48F2T6) ",
            " [Here's a random painting :)](https://imgur.com/iYytETj) "
        ]

    '''YOUTUBE URLS'''
    youtube_links = \
    [
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=lLWEXRAnQd0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=VlucWfTUo1A) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=dNEp3hoHSDI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=oh5p5f5_-7A) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=kasGRkfkiPM) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=pw5ETGiiBRg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=L5bXkI0-pEg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=I-ousb8-SD0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=UQ-RTZCOQn0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=BW2wKKFvH1g) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=XZmdzfvXRuw) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=vgbMONXc9Cs) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=HCsCatvigtw) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=enutOy-nsZk) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=LygUyAb78oY) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=VnZEpic2UzU) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=zxj3xLDNxo0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=PutvF_P4588) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=8ysFkNYwhAE) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=qTDQt_PdlYc) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=kJFB6rH3z2A) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=TohG7F8M3Ls) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=DFSIQNjKRfk) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=nJGCVFn57U8) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=IEQWfszfRlA) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=mEU0stNfkxI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=RInDWhYceLU) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=0FYfo94qefg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=qx2IsmrCs3c) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=qXElmiqzcI0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=DFQlu6eqrBo) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=MHJB0IBnuD4) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=OFKFUJ9eDNs) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=Ugiwi8uizpg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=4KYxkqlzyqM) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=Qj6lMtnCt8o) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=wrbGlR22K0Q) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=RrBsbqO9aqI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=eTEKGOi6SVg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=GzSqjyQUPZQ) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=O6L5YPt9CeU) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=zoTeyliLn5o) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=aA8RhtaWACA) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=Da4SPyh1ATM) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=uEUMVwc4o5U) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=UOziR7PoVco) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=vrAMRxBB5KI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=NcVeRlPu_5w) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=Vx6v47gHBWM) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=OJ_xqtvZf3o) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=8P-YeoTmVrw) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=1s58rW0_LN4) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=lzODyJS2ZIg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=Wj-3ct7RvAI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=KYlM2zJnNWY) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=DqhzxdkdQS0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=jfCsew_mz7A) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=gMEZp47VKC0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=iRMsb9Vf7GM) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=4XxClvPZ1RE) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=fBh1nA4pMDY) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=loAzRUzx1wI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=AGhXEPfp-W4) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=GhOGZMpPUSE) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=tWoInh2USOs) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=530_cVmexiI) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=6evqNlOO7Bw) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=o2cjLA_wgIk) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=miJ19Kz_i3Y) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=OHSm8kLE7js) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=kNZssD9zWlw) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=RqtDliGeyTg) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=lSeRrm5ZK9c) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=puGk2iFvvp0) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=EVQcDEiJh2o) ",
    " [Here's a link to a random video of me painting](https://youtube.com/watch?v=0pwoixRikn4) "

    ]

    '''BOT|REDIRECT URLS''' # Enter Redirect/Information URL(S) in the strings below
    code = "|| [code](https://github.com/whaliam/BobRossBot) ||💻[feedback](https://www.reddit.com/user/BobRossBot_/comments/7ikvn5/feedback_3_and_code/)"
    username = "BobRossBot_"
    # Set subreddit parameters
    subreddit = reddit.subreddit("all")

    print("Searching for instances of 'Bob Ross...'")

    # Set comment parameters
    for comment in subreddit.stream.comments():


        if re.search("bob ross", comment.body, re.IGNORECASE):
            time.sleep(5)
            ross_reply = random.choice(ross_quotes) + str("||") + random.choice(youtube_links) + str("||") + random.choice(ross_images)
            print("comment found!")
            print("preparing quote")
            comment.reply(ross_reply)
            print(ross_reply)
            print("replied with quote!")
            print("starting cooldown")
            print(str(now))
            print("cooldown")
            time.sleep(10)

# Created by /u/whaliam
# 6Ep96ck9@protonmail.com

'''GUI'''
#Start GUI
from tkinter import *

'''GUI|MAINMENU'''

# Create main window
root = Tk()
menu = Menu(root)
root.config(menu=menu)

'''GUI RESIZEABLE ROOT WINDOW''' # Credit: The Internet


def createWidgets(self):
    top=self.winfo_toplevel()
    top.rowconfigure(0, weight=1)
    top.columnconfigure(0, weight=1)
    self.rowconfigure(0, weight=1)
    self.columnconfigure(0, weight=1)
    self.quit = Button(self, text='Quit', command=self.quit)
    self.quit.grid(row=0, column=0, sticky=Tk.N+Tk.S+Tk.E+Tk.W)


def __init__(self, master=None):
    Tk.Frame.__init__(self, master)
    self.grid(sticky=Tk.N + Tk.S + Tk.E + Tk.W)
    self.createWidgets()


'''GUI|SUBMENU1'''
# Create menu
# First submenu
submenu = Menu(menu)
menu.add_cascade(label="Bot", menu=submenu)
submenu.add_separator()
submenu.add_command(label="Start Bot", command=bot)
submenu.add_separator()

'''GUI|SUBMENU2'''

# Second submenu
submenu2 = Menu(root)
menu.add_cascade(label="Settings", menu=submenu2)
submenu2.add_separator()
submenu2.add_command(label="Exit", command=exit)
submenu2.add_separator()

'''GUI|TITLE'''
root.title("Bob Ross Bot")

"""GUI|START-BUTTON"""
button1 = Button(root, text="Start Bot...", bg="Red", fg="White", command=bot,)
button1.grid(row=0, column=0, padx=10, pady=10, sticky=S + W)

'''GUI|CANVAS
Canvas0 = Canvas(root, bg="White", height=500, width=500, relief=GROOVE)
Canvas0.grid(rowspan=4, columnspan=4, padx=10, pady=10, sticky=E + W)'''

'''GUI|TEXTBOX
Textbox0 = Text(root, height=500, width=500)
Textbox0.grid(rowspan=4, columnspan=4, padx=10, pady=10, sticky=E + W)
Textbox0.insert(END, ross_reply)'''


'''GUI|STATUSBAR'''
statusbar = Label(root, text="Times Replied...", bd=1, relief=SUNKEN, anchor=W, bg='Red', fg='White')
statusbar.grid(columnspan=4, row=6, padx=10, pady=10, sticky=S+ E + W)

# Loop GUI
root.mainloop()

'''END'''
