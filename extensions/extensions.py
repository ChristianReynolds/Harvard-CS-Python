#get input, # separate based on . , compare to locate and print
def main():
    x=input("File name: ")
    if "." in x :
        c,y = x.lower().strip().rsplit('.',1)
        filecheck(y)
    else:
        print("application/octet-stream")


def filecheck(p):
    match p:
        case "jpeg" | "jpg":
            print("image/jpeg")
        case "pdf":
            print("application/pdf")
        case "gif":
            print("image/gif")
        case "png":
            print("image/png")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:
            print("application/octet-stream")






main()


