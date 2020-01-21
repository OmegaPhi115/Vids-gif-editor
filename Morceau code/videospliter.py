from core import *


def splitvideoimages(videopath, outputpath):
    """
    Load a video and extract all the frames
    :param videopath:
    :param outputpath:
    :return:
    """
    vid = cv2.VideoCapture(videopath)
    currentframe = 0
    while True:
        # reading from frame
        ret, frame = vid.read()

        if ret:
            # if video is still left continue creating images
            name = Path(outputpath, str(currentframe) + '.png')

            # writing the extracted images
            cv2.imwrite(name, frame)

            # increasing counter so that it will
            # show how many frames are created
            currentframe += 1
        else:
            break

    # Release all space and windows once done
    vid.release()
    cv2.destroyAllWindows()

def analyseimage(imagepath, outputpath, framenum=""):
    """

    :param imagepath:
    :param outputpath:
    :param framenum:
    :return:
    """
    frame = {
        "frame": framenum,
        "size": "",
        "pink": [],
        "white": []
    }
    ima = Image.open(imagepath)
    (x, y) = ima.size
    frame["size"] = (x, y)
    output_image = Image.new("RGB", (int(x / 2), int(y / 2)))

    for j in range(0, y):
        for i in range(0, x):
            pixel = ima.getpixel((i, j))
            if colorinterval(pixel, (220, 0, 90), (255, 10, 120)): #  if pink
                frame['pink'].append((i // 2, j // 2))

    #TODO: SAVE THE DIC
    with open(Path(outputpath, str(framenum) + '.txt')) as framefile:
        framefile.write(frame)

    os.remove(imagepath)

class videoconvert:
    def __init__(self, file_path):
        if file_path[-3:] == "mp4":
            self.video_init(file_path)
        elif file_path[-3:] == "txt":
            readbitmap(file_path)

    def video_init(self, video):
        self.video = video
        self.framecount = 0
        vid = cv2.VideoCapture(self.video)
        while 1:
            ret, frame = vid.read()
            if ret:
                self.framecount += 1
            else:
                break

def createbitmap():
    pass

def converttoimages(vide):
    global maintext
    maintext.config(text="Init")
    mainprogress = Progressbar(root, length=200, maximum=3, mode='determinate')
    mainprogress.grid(row=1, column=0, padx=5, pady=5)
    sublabel = Label(root, text="Creating temp directory")
    sublabel.grid(row=2, column=0)
    root.update()

    #pool = ThreadPool(50)

    # creating a folder named data
    temp_folder_path = Path(data_folder, 'temp')
    if not overidespliting:
        while os.path.exists(temp_folder_path):
            root.update()
            # for files in os.walk(temp_folder_path):
            #     os.remove(files)
            sublabel.config(text="Please delete " + str(temp_folder_path))
        os.makedirs(temp_folder_path)

    #counting frames
    sublabel.config(text="Counting frames...")
    root.update()

    currentframe = 0
    framecount = 0
    vid = cv2.VideoCapture(vide)
    while 1:
        ret, frame = vid.read()
        if ret:
            framecount += 1
        else:
            break

    maintext.config(text='Spliting frames')
    mainprogress["value"] = 1
    sublabel = Label(root, text="")
    sublabel.grid(row=2, column=0)
    subprogress = Progressbar(root, length=200, maximum=framecount, mode='determinate')
    subprogress.grid(row=3,column=0, padx=5, pady=5)
    root.update()

    # frame
    if (overidespliting) or (test_data_folder == ""):
        vid = cv2.VideoCapture(vide)
        currentframe = 0
        while True:

            # reading from frame
            ret, frame = vid.read()

            if ret:
                # if video is still left continue creating images
                name = './data/temp/' + str(currentframe) + '.png'

                # writing the extracted images
                cv2.imwrite(name, frame)

                # increasing counter so that it will
                # show how many frames are created
                currentframe += 1
                sublabel.config(text='Creating: ' + name)
                subprogress["value"] = currentframe
                root.update()
            else:
                break

        # Release all space and windows once done
        vid.release()
        cv2.destroyAllWindows()
    else:
        copy_tree(str(test_data_folder), str(temp_folder_path))

    #now we halve the resolutions of the images
    maintext.config(text='Analizing frames')
    mainprogress["value"] = 2
    sublabel.config(text='Compressing frame: ')
    subprogress["value"] = 0
    root.update()
    iaa = 0

    def frameana(imapa, framenum):
        frame = {
            "frame": framenum,
            "size": "",
            "pink": []
        }
        ima = Image.open(imapa)
        (x, y) = ima.size
        frame["size"] = (x, y)
        output_image = Image.new("RGB", (int(x / 2), int(y / 2)))

        for i in range(0, x, 2):
            for j in range(0, y, 2):
                pixel = ima.getpixel((i, j))
                if colorinterval(pixel, (220, 0, 90), (255, 10, 120)):
                    frame['pink'].append((i // 2, j // 2))

        os.remove(imapa)
        return frame

    video = []
    while iaa <= 20:
        sublabel.config(text='Analizing frame: ' + str(iaa))
        subprogress["value"] = iaa
        root.update()
        video.append(frameana(Path(temp_folder_path, str(iaa) + ".png"), iaa))
        iaa += 1



    with open(Path(data_folder, "test.txt"), "w") as outfile:
        outfile.write(str(video))


    # imap = []
    # while iaa <= framecount:
    #     imap.append(Path(temp_folder_path, str(iaa) + ".png"))
    #     iaa += 1
    #
    # video = []
    # for fram in imap:
    #     video.append()

    #video = pool.map(frameana, imap)



    #os.removedirs(temp_folder_path)

def readbitmap(file):
    with open(Path(data_folder, "test.txt"), "r") as outfile:
        bitmap = ast.literal_eval(outfile.read())

    def heatmapfull(bitmap, index, randge=0, anchor="m"):
        (x, y) = bitmap[0]["size"]
        output_image = Image.new("RGB", (x, y))

        frametoadd = [index]
        lowrange = index - int(randge / 2)
        highrange = index + int(randge / 2)
        for i in range(lowrange, highrange):
            frametoadd.append(i)

        for frameindex in frametoadd:
            for pinkpixel in bitmap["pink"]:
                output_image.putpixel(pinkpixel, (255, 0, 100))

        output_image.show()
    heatmapfull(bitmap, 10, 5)

#video = [frame1, frame2, ...]

#frame = {
# frame: framenum
# pink: [pinkpixel1coo, pinkpixel2coo, ...]}


