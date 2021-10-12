import qrcode

class QRcode:
    def touch_img_qr(code):
        img = qrcode.make(f'778=205610002={code}')
        type(img)  # qrcode.image.pil.PilImage
        img.save(f"{code}.png")
var = os.argv[1]
QRcode.touch_img_qr(var)
