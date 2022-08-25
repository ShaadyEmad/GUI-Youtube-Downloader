from pytube import YouTube
from tkinter import *
from tkinter import scrolledtext
from PIL import ImageTk, Image
import os


# Create window
window = Tk()
window.geometry('700x750')
window.resizable(False,False)
window.title("Youtube Downloader")

# put icon
window.iconbitmap("icon.ico")


# Create destination folder
username = os.getlogin()
destination = fr"C:\Users\{os.getlogin()}\Desktop\Youtube Downloder"
if not os.path.exists(destination):
    os.makedirs(destination)


# download
def download(destination):

    # Create result window
    result_window = Toplevel(window)
    result_window.title("Results")
    result_window.geometry("700x300")
    result_textbox = scrolledtext.ScrolledText(result_window ,width=80, height=30, font=("Times New Roman", 15))
    result_textbox.pack()

    # make list which has every link as element
    all_links = text_area.get("1.0", "end-1c")
    links = all_links.split()

    # Download video
    if (var_video.get() == 1):
        for i in links:
            try:
                # get url
                yt = YouTube(i)

                # download the file
                video = yt.streams.first()
                video.download(destination)

                # result of success
                result_textbox.insert(INSERT, f"-{yt.title}\n")
                result_textbox.insert(INSERT, "Done\n")
                result_textbox.insert(INSERT, "\n")

            except:
                result_textbox.insert(INSERT, f"-{ i}\n")
                result_textbox.insert(INSERT, "Error\n")
                result_textbox.insert(INSERT, "\n")

        result_textbox.insert(INSERT, "---Finish---\n")


    # Download Audio
    elif (var_audio.get() ==1):
        for i in links:
            try:
                # get url
                yt = YouTube(i)

                # extract only audio
                video = yt.streams.filter(only_audio=True).first()

                # destination to save file
                out_file = video.download(output_path=destination)

                # save the file
                base, ext = os.path.splitext(out_file)
                new_file = base + '.mp3'
                os.rename(out_file, new_file)

                # result of success
                result_textbox.insert(END, f"-{yt.title}\n")
                result_textbox.insert(END, "Done\n")
                result_textbox.insert(INSERT, "\n")

            except:
                result_textbox.insert(INSERT, f"-{ i}\n")
                result_textbox.insert(INSERT, "Error\n")
                result_textbox.insert(INSERT, "\n")

        result_textbox.insert(INSERT, "---Finish---\n")

    else :
        pass


# Define image
bg = Image.open("background.jpg")
bck = ImageTk.PhotoImage(bg)


# Create a label for background
bg_label = Label(window, image=bck)
bg_label.place(x=0, y=0)


# app title
app_title = Label(window, text="Youtube Downloader", font=("Helvetica", 35), fg="red").place(x=140, y=30)


text_area = scrolledtext.ScrolledText(window,width = 55, height = 20,font = ("Times New Roman",15))
text_area.grid(column = 0, pady = 140, padx = 70)


# create audio checkbox
var_audio = IntVar()
c_audio = Checkbutton(window, text="Audio", variable=var_audio, height=2, width=5, bg="#b7950b", font = ('Courier' ,'12', 'bold'))
c_audio.place(x=150 , y=600)


# create video checkbox
var_video = IntVar()
c_video = Checkbutton(window, text="Video", variable=var_video, height=2, width=5, bg="#b7950b", font = ('Courier' ,'12', 'bold'))
c_video.place(x=500 , y=600)


# create start button
start_button = Button(window, text="Start", bg='green', font=('Helvetica', '35', 'bold'),command=lambda: download(destination))
start_button.place(x=280 , y=650)

window.mainloop()