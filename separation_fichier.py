from config import *

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