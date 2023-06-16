# pip install qrcode
import qrcode

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=5,
    )
    
    qr.add_data(link)
    qr.make(fit=True)
    
    qr_image = qr.make_image(fill_color="black", back_color="white")
    
    qr_image.save("image.png")

link = input("Enter your link here: ")
generate_qr_code(link)