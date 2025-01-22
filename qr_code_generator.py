import qrcode
import os
import yaml

file_location = os.path.dirname(os.path.abspath(__file__))
with open(f"{file_location}/config.yaml", "r") as ymlfile:
    cfg = yaml.safe_load(ymlfile)
    base_url = cfg["baseURL"]

def generate_qr_code_from_folders():
    for folder in os.listdir(file_location + '/content'):
        loc = os.path.join(file_location, '/content/')
        loc = file_location + '/content/' + folder
        if os.path.isdir(loc):
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(base_url + folder)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")
            img.save(f"qr_codes/{folder}.png")
            print(f"QR code generated for {folder}")
        else:
            print(f"{loc} is not a folder")
if __name__ == "__main__":
    generate_qr_code_from_folders()
