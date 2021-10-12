import qrcode
import sys
import os

code = sys.argv[1]
def touch_img_qr(code):
    img = qrcode.make(f'778=205610002={code}')
    type(img)  # qrcode.image.pil.PilImage
    img.save(f"/var/www/html/{code}.png")
        
    print(code)
    
touch_img_qr(code)
           
