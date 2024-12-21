from tkinter import *
import requests
import io
from urllib.request import urlopen
from PIL import ImageTk, Image
import webbrowser


class NewsApp:

    def __init__(self):
        # Fetch data
        try:
            self.data = requests.get(
                'https://newsapi.org/v2/top-headlines?country=in&apiKey=c3c60e5e707d438cb8a5d88bd9ecba55'
            ).json()
        except Exception as e:
            print("Error fetching news:", e)
            self.data = {'articles': []}  # Fallback to empty data

        # Check if articles are available
        if 'articles' not in self.data or not self.data['articles']:
            print("No articles found in the API response.")
            self.data['articles'] = [{'title': 'No News Available',
                                       'description': 'Please check your internet connection or API key.',
                                       'urlToImage': 'https://globaleducation.s3.ap-south-1.amazonaws.com/globaledu/no-image.png',
                                       'url': ''}]

        # Initial GUI load
        self.load_gui()
        # Load first news item
        self.load_news_item(0)

    def load_gui(self):
        self.root = Tk()
        self.root.geometry('350x600')
        self.root.resizable(0, 0)
        self.root.configure(background='black')

    def load_news_item(self, index):
        self.root.title('Satyam Headlines📰')

        # Clear screen for the new news item
        self.clear()

        try:
            # Fetch and paste image
            img_url = self.data['articles'][index]['urlToImage']
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)
        except:
            img_url = 'https://globaleducation.s3.ap-south-1.amazonaws.com/globaledu/no-image.png'
            raw_data = urlopen(img_url).read()
            im = Image.open(io.BytesIO(raw_data)).resize((350, 250))
            photo = ImageTk.PhotoImage(im)

        # Display
        label = Label(self.root, image=photo)
        label.image = photo  # Keep a reference to avoid garbage collection
        label.pack()

        # Print news heading
        heading = Label(self.root, text=self.data['articles'][index]['title'], bg='black', fg='white', wraplength=350,
                        justify='center')
        heading.pack(pady=(10, 20))
        heading.config(font=('verdana', 15))

        # Print news details
        details = Label(self.root, text=self.data['articles'][index]['description'], bg='black', fg='white',
                        wraplength=350, justify='center')
        details.pack(pady=(2, 20))
        details.config(font=('verdana', 12))

        # Buttons frame
        frame = Frame(self.root, bg='black')
        frame.pack(expand=True, fill=BOTH)

        # Previous button
        if index != 0:
            prev = Button(frame, text='Prev', width=16, height=3, command=lambda: self.load_news_item(index - 1))
            prev.pack(side=LEFT)

        # Read button
        read = Button(frame, text='Read More', width=16, height=3,
                      command=lambda: self.open_link(self.data['articles'][index]['url']))
        read.pack(side=LEFT)

        # Next button
        if index != len(self.data['articles']) - 1:
            next = Button(frame, text='Next', width=16, height=3, command=lambda: self.load_news_item(index + 1))
            next.pack(side=LEFT)

        self.root.mainloop()

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()

    def open_link(self, url):
        if url:
            webbrowser.open(url)
        else:
            print("No URL available for this article.")


obj = NewsApp()
