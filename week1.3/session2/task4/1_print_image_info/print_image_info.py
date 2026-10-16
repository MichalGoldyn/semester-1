# Week 1.3, Session 2: Print PGM image info

# Open a pgm image file
# You can use the relative path ../images/filename
# You could handle file errors with try/except.
try:
    with open("week1.3/session2/task4/images/feep.pgm", "r") as img:
    # Read the file content
        imageInfo = [x.rstrip("\n") for x in img]
        dim = imageInfo[1].split()
        print(f"Dimensions: {dim[0]} x {dim[1]}")
        print(f"Max Gray Value: {imageInfo[2]}")
except:
    print("File Dosent Exist")
# print image dimension (i.e., Dimensions: width x height pixels)

# print max gray value (i.e., Max Gray Value: max_gray_value)