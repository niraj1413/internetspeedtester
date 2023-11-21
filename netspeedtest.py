from tkinter import *
import speedtest

def speedchecker():
    sp = speedtest.Speedtest()
    sp.get_servers()
    down = str(round(sp.download()/(10**6), 3)) + "mbps"
    up = str(round(sp.upload()/(10**6), 3)) + "mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp_test = Tk()

sp_test.title("INTERNET SPEED TEST")
sp_test.geometry("500x650")
sp_test.config(bg="blue")

# Label for the title
title_label = Label(sp_test, text="INTERNET SPEED TEST", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
title_label.place(x=60, y=40, height=50, width=380)

# Label for downloading speed
download_label = Label(sp_test, text="DOWNLOADING SPEED", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
download_label.place(x=60, y=130, height=50, width=380)

# Label to display downloading speed
lab_down = Label(sp_test, text="00", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
lab_down.place(x=60, y=200, height=50, width=380)

# Label for uploading speed
upload_label = Label(sp_test, text="UPLOADING SPEED", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
upload_label.place(x=60, y=290, height=50, width=380)

# Label to display uploading speed
lab_up = Label(sp_test, text="00", font=("Time New Roman", 20, "bold"), bg="blue", fg="white")
lab_up.place(x=60, y=380, height=50, width=380)

# Button to check speed
button = Button(sp_test, text="CHECK SPEED", font=("Time New Roman", 20, "bold"), relief=RAISED, bg="red", command=speedchecker)
button.place(x=60, y=460, height=50, width=380)

sp_test.mainloop()
