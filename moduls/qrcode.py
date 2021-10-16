import qrcode


class QRcode:
    '''Генерация qr-кода'''

    def touch_img_qr(code):
        '''Генерация qr-кода для считывания'''

        img = qrcode.make(f'778=205610002={code}')
        type(img)
        img.save(f"/home/sammy/certificat/qrimg/{code}.png")
