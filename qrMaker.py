import qrcode   # pip install qrcode
from PIL import ImageFont, ImageDraw, Image # pip install qrcode PIL

def qrMaker(spool,cwp):
    spool = spool
    cwp = cwp

    qr = qrcode.QRCode(version=2,
                       error_correction=qrcode.constants.ERROR_CORRECT_H,
                       )
    qr.add_data(spool)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(f'{spool}(二维码).png')
    # QR生成图片大小为300x300
    img = Image.open(f'{spool}(二维码).png')
    newimg = Image.new(mode="RGB", size=(325, 400), color=(255, 255, 255))
    newimg.paste(img, (0, 0))
    draw = ImageDraw.Draw(newimg)
    ttfront = ImageFont.truetype('msyh.ttc', 16)  # 字体文件msyh.ttc，需要查找下载

    draw.text((25, 350), 'SPOOL:'+spool, font=ttfront, fill="black")  # 文字位置，正文内容，文字RGB颜色，字体
    draw.text((25, 325), 'CWP:' + cwp, font=ttfront, fill="black")
    newimg.save(f'{spool}(二维码).png')




