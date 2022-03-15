import pyqrcode as qr
import pypng as png
import io


url = qr.create("+258850143767")
#url = QRCode(content=b"Eusébio Simango", error='H', version=3, mode='binary')
print(url)
with open ('kkk.png', 'w') as fstream:
    url.png('kkk.png', scale=5)
    url.png('kkk.png', scale=5)
    buffer = io.BytesIO()

		
