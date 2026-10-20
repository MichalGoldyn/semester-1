from tkinter import *
from pgm_tools import *

file = input("Enter Relative Path: ")
image = readPGM(file)

"""Dimensions of Image"""
w = image[0]
h = image[1]

"""Dimensions of image in pixels"""
pixelDimensions = 2
pixelWidth = int(w/pixelDimensions)
pixelHeight = int(h/pixelDimensions)

scaledWidth = int(w*pixelDimensions)
scaledHeight = int(h*pixelDimensions)

"""Maximum Gray Value"""
maxGray = image[2]

root = Tk()
root.title("Matrix Display")
root.geometry(f"{scaledWidth}x{scaledHeight}")
c = Canvas(root, width = scaledWidth, height = scaledHeight)

"""     Outputs a GrayScale colour code     """
def colourCodes(grayValue):
    if grayValue >= 0 and grayValue <= maxGray:
        grayScaleValue = 255/maxGray
        tmp = int(grayValue * grayScaleValue)
        hexa = hex(tmp)
        cleanHexa = hexa[2:]
        if len(cleanHexa) != 2:
           cleanHexa = "0" + cleanHexa
        hexValue = f"#{cleanHexa}{cleanHexa}{cleanHexa}"

        return(hexValue)

"""     Outputs Coordinates of a pixel based on a grid that is definded       """
def pixelCoordinate(pixelX,pixelY):
    x1=0
    y1=0
    x2=0
    y2=0

    x1 = pixelX * pixelDimensions
    y1 = pixelY * pixelDimensions
    x2 = (pixelX+1) * pixelDimensions
    y2 = (pixelY+1) * pixelDimensions
    return x1, y1, x2, y2

#coords = pixelDrawer(1,3)
#c.create_rectangle(coords[0], coords[1], coords[2], coords[3], fill=colourCodes(0), outline="")

"""     Outputs the whole colour palette        """
def outputColourPalette():
    cInc = 0
    for y in range(pixelHeight):
        x1=0
        y1=0
        x2=0
        y2=0

        y1 = y * pixelDimensions
        y2 = (y+1) * pixelDimensions
        for x in range(pixelWidth):
            x1 = x * pixelDimensions
            x2 = (x+1) * pixelDimensions

            c.create_rectangle(x1, y1, x2, y2, fill=colourCodes(cInc), outline="")
            cInc +=1

"""     Draws out pixels at given coords and colour     """
def pixelDrawer(pixelCoordinates, colour):
    c.create_rectangle(pixelCoordinates[0], pixelCoordinates[1], pixelCoordinates[2], pixelCoordinates[3], fill=colourCodes(colour), outline="")


def outputPGM():
    heightCount = 0
    widthCount = 0
    imagePixels = image[3]
    for y in range(len(imagePixels)):
        for x in range(len(imagePixels[y])):
            pixelDrawer(pixelCoordinate(widthCount, heightCount), imagePixels[y][x])
            if widthCount == w - 1:
                widthCount = 0
                heightCount += 1
            else:
                widthCount +=1

            

outputPGM()

c.pack()
mainloop()