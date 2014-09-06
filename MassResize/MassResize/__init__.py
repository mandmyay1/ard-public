from PIL import Image

basewidth = 400
img = Image.open("C:\\Users\\Adam\\Pictures\\441bjhri4m_198024463.jpg")
wpercent = basewidth/float(img.size[0])
hsize = int(float(img.size[1])*float(wpercent))
newimg = img.resize( (basewidth,hsize), Image.ANTIALIAS )
newimg.save( "C:\\Users\\Adam\\Pictures\\441bjhri4m_198024463-test.jpg")