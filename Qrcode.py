import urllib
import urllib.request
import os
import sys
import tkinter as tk
# Use the following vCard v2.1 template.

VCARD_TEMPLATE = """BEGIN%3aVCARD%0d%0aVERSION%3a3.0%0d%0aN%3a%s%3b%s%0d%0aORG%3aThe+Telos+Alliance%0d%0aTITLE%3a%s%0d%0aEMAIL%3a%s%0d%0aTEL%3bTYPE%3dCELL%3a%2B%s%0d%0aTEL%3bTYPE%3dWORK%2cVOICE%3a%2B%s%0d%0aTEL%3bTYPE%3dHOME%2cVOICE%3a%2B%s%0d%0aNOTE%3aSkype%3A%s%0d%0aURL%3aTelosAlliance.com%0d%0aADR%3a%3b%3b1241+superior+Avenue+E%253bCleveland%253bOH%253b44114%253bUSA%0d%0aEND%3aVCARD%0A&addtext="""

VCARD_TEMPLATE = """BEGIN%3aVCARD%0d%0aVERSION%3a3.0%0d%0aN%3a%s%3b%s%0d%0aORG%3aThe+Telos+Alliance%0d%0aTITLE%3a%s%0d%0aEMAIL%3a%s%0d%0aTEL%3bTYPE%3dCELL%3a%s%0d%0aTEL%3bTYPE%3dWORK%2cVOICE%3a%s%0d%0aTEL%3bTYPE%3dmain%2cVOICE%3a%s%0d%0aNOTE%3aSkype%3A%s%0d%0aURL%3aTelosAlliance.com%0d%0aADR%3a%3b%3b1241+superior+Avenue+E%253bCleveland%253bOH%253b44114%253bUSA%0d%0aEND%3aVCARD%0A&addtext=""".replace('%','%%').replace('%%s', "%s")


def clear():
    global first_name
    first_name =fn.get()
    global last_name
    last_name = ln.get()
    global title
    title = tt.get()
    global mobile_number
    mobile_number = mobile.get()
    global direct_number
    direct_number = direct.get()
    global main_number
    main_number = main.get()


    btnRun['highlightbackground'] = 'blue'
    root.after(200, reset_color)
    root.destroy()

def reset_color():
    btnRun['highlightbackground'] = 'white'


def on_closing():
    print("closing...")
    root.destroy()
    sys.exit(0)


#setting up GUI

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_closing)
root.configure(background='lightgrey')

title = tk.Label(root, text="Generate contact QR code")
title.config(bg = 'lightgrey')

#input
fName = tk.Entry(root)
fn = tk.StringVar()
fName = tk.Entry(root, textvariable=fn)

lName = tk.Entry(root)
ln = tk.StringVar()
lName = tk.Entry(root, textvariable=ln)

ttl = tk.Entry(root)
tt = tk.StringVar()
ttl = tk.Entry(root, textvariable=tt)

mbl = tk.Entry(root)
mobile = tk.StringVar()
mbl = tk.Entry(root, textvariable=mobile)

dir = tk.Entry(root)
direct = tk.StringVar()
dir = tk.Entry(root, textvariable=direct)

mn = tk.Entry(root)
main = tk.StringVar()
mn = tk.Entry(root, textvariable=main)


ln.set("Enter Last Name")
fn.set("Enter First Name")
tt.set("Enter Job Title")
mobile.set("Enter Mobile Number")
direct.set("Enter Direct Number")
main.set("Enter Main Number")

#buttons
btnRun = tk.Button(root, text="Generate", command=clear)
btnRun.config(bg = 'lightgrey')

#packing
title.pack()

fName.pack()
lName.pack()
ttl.pack()
mbl.pack()
dir.pack()
mn.pack()

btnRun.pack()


root.geometry("550x400+200+150")
root.mainloop()

QR_CODE_TEMPLATE = "https://qrickit.com/api/qr.php?d=%s&txtcolor=FFFFFF&fgdcolor=000000&bgdcolor=FFFFFF&qrsize=300"


email = first_name + "." + last_name + "@telosalliance.com"
skype=last_name + "." +first_name

vcard = VCARD_TEMPLATE % (last_name,
                          first_name,
                          title,
                          email,
                          mobile_number,
                          direct_number,
                          main_number,
                          skype)

# Write the vCard to a file
'''out_filename = '.'.join([first_name + '-' + last_name, "vcf"])
out_file_hdl = open(out_filename, 'w')
out_file_hdl.write(vcard)
out_file_hdl.close()'''

# Generate a QR-Code
vcard_url = (QR_CODE_TEMPLATE % (vcard)).replace("\n", "").replace(" ", "%20")
print(vcard_url)
cnxn = urllib.request.urlopen(vcard_url)
qr_code = cnxn.read()
cnxn.close()
qr_filename = '.'.join([first_name + '-' + last_name, "png"])
with open(qr_filename, 'wb') as qr_file_hdl:
    qr_file_hdl.write(qr_code)
    print ("Created QR-code %s file." %(qr_filename))

os.system("open " + qr_filename)
