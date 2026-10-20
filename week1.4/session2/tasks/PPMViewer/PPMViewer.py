from PPMTools import *
from tkinter import *


file = input("Enter Relative Path: ")
image = readPMM(file)

"""Dimensions of Image"""
w = image[0]
h = image[1]

"""Dimensions of image in pixels"""
pixelDimensions = 10
pixelWidth = int(w/pixelDimensions)
pixelHeight = int(h/pixelDimensions)

scaledWidth = int(w*pixelDimensions)
scaledHeight = int(h*pixelDimensions)

"""Maximum Value"""
maxval = image[2]

root = Tk()
root.title("Matrix Display")
root.geometry(f"{scaledWidth}x{scaledHeight}")
c = Canvas(root, width = scaledWidth, height = scaledHeight)

"""     Returns rgb decimal channel to hexa     """
def colourCodes(rgbValue):
    if rgbValue >= 0 and rgbValue <= maxval:
        rgbScaleValue = 255/maxval
        tmp = int(rgbValue * rgbScaleValue)
        hexa = hex(tmp)
        cleanHexa = hexa[2:]
        if len(cleanHexa) != 2:
           cleanHexa = "0" + cleanHexa

        return(cleanHexa)

"""     Hexa byte combiner into hex colour code     """
def combineHexa(x, y, z):
    hexValue = f"#{x}{y}{z}"
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
    c.create_rectangle(pixelCoordinates[0], pixelCoordinates[1], pixelCoordinates[2], pixelCoordinates[3], fill=colour, outline="")


def outputPMM():
    heightCount = 0
    widthCount = 0
    imagePixels = image[3]
    for x in range(len(imagePixels)):
        hexColour = combineHexa(colourCodes(int(imagePixels[x][0])), colourCodes(int(imagePixels[x][1])), colourCodes(int(imagePixels[x][2])))
        pixelDrawer(pixelCoordinate(widthCount, heightCount), hexColour)
        if widthCount == w - 1:
            widthCount = 0
            heightCount += 1
        else:
            widthCount +=1

            
outputPMM()


c.pack(expand=True, fill=BOTH)
mainloop()


