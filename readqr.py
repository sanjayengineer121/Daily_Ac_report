from PIL import Image
from tkinter import *
from pyzbar.pyzbar import decode
from tkinter import filedialog
from tkinter.filedialog import askopenfilename
import customtkinter
import cv2

#result = decode(Image.open('qr.png'))
#print(result)

root = customtkinter.CTk() 
root.title("QR Code DECODER")
root.iconbitmap('img/scan.ico')
root.geometry(f"{1100}x{580}")
msg=""
def decode():
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    

#result = decode(Image.open(filename))
    image = cv2.imread(filename)
    detector = cv2.QRCodeDetector()

    # detect and decode
    data, vertices_array, binary_qrcode = detector.detectAndDecode(image)

    # if there is a QR code
    # print the data
    if vertices_array is not None:
        print("QRCode data:")
        print(data)
        msg=data

        
        text_box = Text(
            root,
            height=12,
            width=40
        )
        text_box.pack(expand=True)
        text_box.insert('end', msg)

#print(msg)
def clear_all():
	quit()



#my_button = Button(root, text="Create QR Code", command=create_code)
#my_button.pack(pady=20)

my_button = customtkinter.CTkButton(master=root, text="CHOOSE QR FILE TO DECODE QR", command=decode)
my_button.pack( pady=20)

my_button2 = customtkinter.CTkButton(master=root, text="QUIT",text_color="red",fg_color="yellow", command=clear_all)
my_button2.pack()

#text_box.config(state='disabled')

#my_label = Label(root, text='QR IS HERE')
#my_label.pack(pady=20)

root.mainloop()

