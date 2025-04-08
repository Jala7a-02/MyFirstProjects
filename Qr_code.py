import qrcode
import qrcode.constants

def ganerate_QrCode(text , filename) :

    qr  = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 7 ,
        border = 2
    )


    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "white" , back_color = "black")
    img.save(f"{filename}.png")

url = input("enter the text or url you would like to convert into QrCode\n")
ganerate_QrCode(url,"Arba")