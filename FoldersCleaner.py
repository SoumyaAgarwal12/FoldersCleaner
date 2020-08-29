import os

# --------------------All files in particular folder of os will store in variable "files"--------------
files = os.listdir()
# --------------------Remove particular file----------------------
files.remove("FoldersCleaner.py")
# print(files)

# ---------------------Create Folder if not Exist-----------------------------
def createfolder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

# ---------------------Move Files----------------------------
def move(folder_name,files):
    for f in files:
        os.replace(f,f"{folder_name}/{f}")

if __name__ == '__main__':

    # ---------------------Function call for creating folder---------------------------
    createfolder("Jpg Files")
    createfolder("Png Files")
    createfolder("HTML files")
    createfolder("JS Files")
    createfolder("Pdf Files")
    createfolder("Others")

    imgJpg = [".jpg"]
    jpg = [file for file in files if os.path.splitext(file)[1].lower() in imgJpg]
    # print(jpg)

    imgPng = [".png"]
    png = [file for file in files if os.path.splitext(file)[1].lower() in imgPng]
    # print(png)

    htmlExt = [".htm",".html"]
    html = [file for file in files if os.path.splitext(file)[1].lower() in htmlExt]
    # print(html)

    jsExt = [".js"]
    js = [file for file in files if os.path.splitext(file)[1].lower() in jsExt]
    # print(js)

    pdfExt = [".pdf"]
    pdf = [file for file in files if os.path.splitext(file)[1].lower() in pdfExt]
    # print(pdf)

    otherExt = [file for file in files if file not in jpg and file not in png and file not in html and file not in js and file not in pdf and os.path.isfile(file)]
    # print(otherExt)
    
    # ---------------------Function call for moving folder---------------------------
    move("Jpg Files",jpg)
    move("Png Files",png)
    move("HTML Files", html)
    move("Js Files",js)
    move("Pdf Files",pdf)
    move("Others",otherExt)

#=============================================================THANK YOU=================================================================
#===================================================Reference "Code With Harry"========================================================
