from PIL import Image
import os

file = input("Enter file to conver to greyscale ")
newFile = os.path.join( os.path.dirname(file), "grey-" + os.path.basename(file) )
colorImg = Image.open(file)
colorPixels = colorImg.load()
greyImg = Image.new("RGB",colorImg.size,"white")
greyPixels = greyImg.load()
for i in range(colorImg.size[0]):
    for j in range(colorImg.size[1]):
        pixel = colorPixels[i,j]
        luminosityPixel = int(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2])
        greyPixels[i,j] = (luminosityPixel,luminosityPixel,luminosityPixel)
greyImg.save(newFile)
print("Saved greyscale copy at", newFile)