from PyFiles.imports import *

def splitvideoimages(videopath, outputpath):  #TODO: Traduire
    """
    Load a video and extract all the frames
    :param videopath:
    :param outputpath:
    :return:
    """
    statuswin = tk.Tk()
    lab = Label(statuswin, text="Splitting Images...").pack()
    vid = cv2.VideoCapture(videopath)
    currentframe = 0
    # frame count
    while True:
        # reading from frame
        ret, frame = vid.read()
        if ret:
            currentframe += 1
        else:
            break

    framecount = currentframe
    progre = Progressbar(statuswin, length=200, mode='determinate')
    progre.pack()
    progre["maximum"] = framecount
    vid.release()
    cv2.destroyAllWindows()

    vid = cv2.VideoCapture(videopath)
    currentframe = 0
    while True:
        # reading from frame
        ret, frame = vid.read()

        if ret:
            progre["value"] = currentframe
            statuswin.update()
            # if video is still left continue creating images
            name = Path.joinpath(Path(outputpath), str(currentframe) + '.png')

            # writing the extracted images
            cv2.imwrite(str(name), frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    vid.release()
    cv2.destroyAllWindows()
    statuswin.destroy()
