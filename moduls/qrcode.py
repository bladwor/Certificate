import qrcode

class QRcode:
    def touch_img_qr(code):
        img = qrcode.make(f'778=205610002={code}')
        path = ('/var/www/html/')
        type(img)
        img.save(f"/var/www/html/{code}.png")
        img.save(f"{code}.png")
        
        print(code)
