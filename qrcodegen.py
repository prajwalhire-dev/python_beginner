#importing the pyqrcode for this script
import pyqrcode
from pyqrcode import QRCode #importing QRCode

#string which represents the qr code
s = "https://github.com/prajwalhire-dev"

#generate the qr code
url = pyqrcode.create(s)

#create and save the file w.r.t extension 
url.svg("mygithub.svg", scale = 8)