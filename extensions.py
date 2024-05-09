a = str(input("File name: "))
a = a.lower()
a = a.replace(" ","")
if a.endswith(".gif"):
    print("image/gif")

elif a.endswith(".jpeg"):
    print("image/jpeg")

elif a.endswith(" .jpeg "):
    print("image/jpeg")

elif a.endswith(".jpg"):
    print("image/jpeg")

elif a.endswith(".png"):
    print("image/png")

elif a.endswith(".pdf"):
    print("application/pdf")

elif a.endswith(".zip"):
    print("application/zip")

elif a.endswith(".txt"):
    print("text/plain")

else:
    print("application/octet-stream")
