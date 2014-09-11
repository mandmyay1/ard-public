from PIL import Image
import os

file = input("Enter file to conver to greyscale ")
newFile = os.path.join( os.path.dirname(file), "grey-" + os.path.basename(file) )
img = Image.open(file)
pixels = img.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        pixel = pixels[i,j]
        luminosityPixel = int(0.21 * pixel[0] + 0.72 * pixel[1] + 0.07 * pixel[2])
        pixels[i,j] = (luminosityPixel,luminosityPixel,luminosityPixel)
img.save(newFile)
print("Saved greyscale copy at", newFile)