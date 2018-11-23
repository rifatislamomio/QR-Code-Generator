import pyqrcode

def generateQrCode(code,file_name):
    code = str(code)                       #converting to string
    q = pyqrcode.create(code)
    file_name = str(file_name)+".png"    #adding extension

    q.png(file_name,scale=6)            #genering a png file

    print("Generated!...")






if __name__ == "__main__":
    code = input("Enter the contents of the qr code: ")
    file_name = input("Enter the file name: ")
    generateQrCode(code,file_name)