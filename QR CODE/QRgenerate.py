#library
import qrcode
# example data
data = "https://meme-wars-grp2.netlify.app/"
# output file name
filename = "qr1.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)