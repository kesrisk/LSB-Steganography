from tkinter import *
fields = ('folder_name', 'message')
Image_link = None

def makeform(root, fields):
   entries = {}
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=22, text=field+": ", anchor='w')
      ent = Entry(row)
      ent.insert(0 ," ")
      row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
      lab.pack(side = LEFT)
      ent.pack(side = RIGHT, expand = YES, fill = X)
      entries[field] = ent
   return entries

def get_image_message():
    global Image_link
    print(name.get())
    Image_link = "new_limk"
    return "I'm back"

root = Tk()
# ents = makeform(root, fields)
# root.bind('<Return>', (lambda event, e = ents: fetch(e)))
row = Frame(root)
lab_name = Label(row, width=22, text='Name'+": ", anchor='w')
name = Entry(row)
name.insert(0 ," ")
row.pack(side = TOP, fill = X, padx = 5 , pady = 5)
lab_name.pack(side = LEFT)
name.pack(side = RIGHT, expand = YES, fill = X)

b1 = Button(root, text = 'Final Balance', command=get_image_message)
b1.pack(side = LEFT, padx = 5, pady = 5)

print(Image_link)

root.mainloop()