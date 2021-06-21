from PIL import Image
im = Image.open("X.png")
newim = im.resize((140,140))
newim.save("resizedX.png")