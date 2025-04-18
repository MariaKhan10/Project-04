import os

def main():
    i = 0
    path = "C:/Users/Al-Rehman COMputers/Pictures/Saved Pictures/"
    for filename in os.listdir(path):
        mydest = "image" + str(i) + ".jpg"
        my_source = path + filename
        mydest = path + mydest
        os.rename(my_source, mydest)
        i += 1

if __name__ == "__main__":
    main()
