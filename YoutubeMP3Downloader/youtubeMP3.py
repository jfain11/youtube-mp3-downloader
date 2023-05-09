from pytube import YouTube
from pytube import Playlist
from graphics import *
from graphicsButton import *


def main():

    # GUI
    win = GraphWin("YouTube MP3 Downloader", 900, 900)
    win.setBackground("light green")

    # Title Text
    titleText = Text(Point(450, 50), "YouTube MP3 Downloader")
    titleText.setStyle("bold")
    titleText.setSize(30)
    titleText.draw(win)

    # URL Entry Text
    entryText = Text(Point(450, 85), "Enter URL")
    entryText.setStyle("bold")
    entryText.setSize(15)
    # URL Entry Box
    urlEntry = Entry(Point(450, 120), 45)
    urlEntry.setSize(20)
    urlEntry.setFill("white")

    # Playlist Entry Text
    playlistEntryText = Text(Point(450, 170), "Enter Folder Name")
    playlistEntryText.setStyle("bold")
    playlistEntryText.setSize(15)
    # Playlist Entry Box
    playlistEntry = Entry(Point(450, 205), 45)
    playlistEntry.setSize(20)
    playlistEntry.setFill("white")

    # Download Button
    downloadButton = Button(450, 260, 40, 140)
    downloadButton.setWidth(4)
    downloadButton.setFill("white")
    # Download Button Text
    downloadButtonText = Text(Point(450, 260), "Begin Download")
    downloadButtonText.setStyle("bold")

    # Playlist Button
    playlistButton = Button(370, 130, 40, 140)
    playlistButton.setWidth(4)
    playlistButton.setFill("white")
    playlistButton.draw(win)
    # Playlist Button Text
    playlistButtonText = Text(Point(370, 130), "Playlist")
    playlistButtonText.setStyle("bold")
    playlistButtonText.draw(win)

    # Single Video Submit Button
    singleButton = Button(530, 130, 40, 140)
    singleButton.setWidth(4)
    singleButton.setFill("white")
    singleButton.draw(win)
    # Single Button Text
    singleButtonText = Text(Point(530, 130), "Single Song")
    singleButtonText.setStyle("bold")
    singleButtonText.draw(win)

    # Main Box
    borderBox = Rectangle(Point(20, 300), Point(880, 880))
    borderBox.setWidth(5)
    borderBox.setFill("white")
    borderBox.draw(win)

    # Main Text
    mainText1 = Text(Point(450, 380), "DOWNLOADING")
    mainText1.setStyle("bold")
    mainText1.setSize(30)

    mainText2 = Text(Point(450, 600), "ASDSADASDASD")
    mainText2.setStyle("bold")
    mainText2.setSize(15)

    mainText3 = Text(Point(450, 480), "0%")
    mainText3.setStyle("bold")
    mainText3.setSize(36)

    # MAIN LOOP
    selection = ""
    selectionMade = False
    while True:
        # Gets the click
        click = win.getMouse()
        if not selectionMade:

            # If user selects single song
            if singleButton.isClicked(click):
                selectionMade = True
                selection = "song"
                # Undraws the buttons
                singleButton.undraw()
                singleButtonText.undraw()
                playlistButton.undraw()
                playlistButtonText.undraw()

            # If user selects playlist
            if playlistButton.isClicked(click):
                selectionMade = True
                selection = "playlist"
                # Undraws the buttons
                singleButton.undraw()
                singleButtonText.undraw()
                playlistButton.undraw()
                playlistButtonText.undraw()

        # If the selection has been made
        if selectionMade:
            entryText.draw(win)
            urlEntry.draw(win)
            downloadButton.draw(win)
            downloadButtonText.draw(win)

            if selection == "playlist":
                playlistEntry.draw(win)
                playlistEntryText.draw(win)
            selectionMade = 0

        if selectionMade == 0:

            if downloadButton.isClicked(click):

                if selection == "playlist":

                    downloadButton.undraw()
                    downloadButtonText.undraw()

                    playlistURL = urlEntry.getText()
                    p = Playlist(playlistURL)
                    count = 1
                    length = len(p)

                    mainText1.setText(f"Downloading {length} Songs...")
                    mainText1.draw(win)

                    folderName = playlistEntry.getText()
                    mainText3.draw(win)
                    for video in p.videos:
                        percentage = round((count / length) * 100)

                        mainText3.setText(f"{percentage}%")

                        count += 1
                        video.streams.filter(only_audio=True).first().download(
                            r'C:\MusicMasterFolder' + '\\' + folderName)

                    mainText2.draw(win)
                    mainText2.setText(p.title + "\nPath: C:\MusicMasterFolder" + "\\" + folderName)


                elif selection == "song":
                    mainText1.setText("Downloading...")
                    mainText1.draw(win)

                    downloadButton.undraw()
                    downloadButtonText.undraw()
                    songURL = urlEntry.getText()
                    v = YouTube(songURL)

                    v.streams.filter(only_audio=True).first().download(r'C:\MusicMasterFolder')
                    mainText1.setText("Download Complete")

                    mainText2.draw(win)
                    mainText2.setText(v.title + "\n\nPath: C:\MusicMasterFolder")

                    # Restart Button 2
                    restart2Button = Button(450, 170, 40, 140)
                    restart2Button.setWidth(4)
                    restart2Button.setFill("white")
                    restart2Button.draw(win)

                    # Restart Button 2 Text
                    restartButton2Text = Text(Point(450, 170), "Main Menu")
                    restartButton2Text.setStyle("bold")
                    restartButton2Text.draw(win)

                    newClick = win.getMouse()
                    if restart2Button.isClicked(newClick):
                        win.close()
                        main()


if __name__ == '__main__':
    main()

