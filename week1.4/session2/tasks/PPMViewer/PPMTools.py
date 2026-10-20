


def readPMM( filename ):
    ''' 
    Read a named PMM file and store the data in a tuple.
    Input: filename string
    Output: tuple of PGM image data
    '''

    with open(filename,"rb") as f:    # read in the file
        data = f.readlines()
        
    pixelData = [line for line in data[3:]] # clean the space-separated data, skip the first line
    specData = [line.strip().split() for line in data[1:3]]

    
    width = int(specData[0][0]) # store the data - compare to the text in the file
    height = int(specData[0][1])
    max_gray = int(specData[1][0])
    #pixels = [[pixelData[i][j] for j in range(len(pixelData[i]))] for i in range(len(pixelData))]
    #pixels = [x for x in pixelData[0]]
    pixels = [[int(pixelData[0][x]), int(pixelData[0][x+1]), int(pixelData[0][x+2])] for x in range(0, len(pixelData[0]), 3)] 

    
    return width,height,max_gray,pixels   # tuple of PGM data
