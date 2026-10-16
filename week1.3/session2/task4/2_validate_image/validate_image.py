# Week 1.3, Session 2: Validate image

# Open a pgm image
# You could handle file errors with try/except

# Read the file content

# Store the width, the height, and the maximum gray value

# For each pixel, check if the pixel value is between 0 and the maximum gray value inclusive

# Check if the widths and heights are the same as specified

# 4. Print the final verdit.
#  Print `Valid image` if the widths, the heights are the same, and all pixel values between 0 and the maximum gray value inclusive
#  Print `Invalid width` if the widths are different
#  Print `Invalid height` if the heights are different
#  Print `Invalid pixel values` if any pixel values is less than 0 and greater than the maximum gray value
import sys

with open("week1.3/session2/task4/images/invalid_pixels.pgm", "r") as img:
# Read the file content
    imageInfo = [x.rstrip("\n") for x in img]
    dim = imageInfo[1].split()
    width = int(dim[0])
    height = int(dim[1])
    maxGInfo = int(imageInfo[2])
    actImg = [x.replace(" ", "") for x in imageInfo[3: ]]
    imgWidth = len(actImg[0])
    imgHeight = len(actImg)

    print(actImg)

    if imgWidth != width:
        print("Invalid width")
        sys.exit()
    elif imgHeight != height:
        print("Invalid Height")
        sys.exit()

    pxlCheck = [x.split() for x in imageInfo[3:]]
    invalidGS = False
    for i in pxlCheck:
        for y in i:
            if int(y) < 0 or int(y) > maxGInfo:
                invalidGS = True
                break
        if invalidGS == True:
            break

    if imgWidth == width and imgHeight == height and invalidGS == False:
        print("Valid Image")
    elif invalidGS == True:
        print("Invalid pixel values")