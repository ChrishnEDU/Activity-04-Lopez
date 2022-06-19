import cv2
import os


print("Mode:")
print("    1. Fixed Path \n    2. Provided Path")
ch = int(input("\nInput: "))
#----Fixed flag Path
if ch == 1:
    ffp = "TAKO.jpg"
    img = cv2.imread(ffp, 1)
    #----Display Image & Cleanup
    cv2.imshow("A WILD TAKO APPEARED!", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
#----User Provided Path
elif ch == 2:
    #----Input Image prov
    print("\nWhen i say WAH you say ___?")
    prov = input("Enter: ")
    flag = str(prov+".jpg")
    #----Display Image & Cleanup
    if os.path.exists(flag):
        img = cv2.imread(flag,1)
        if prov == "WAH":
            cv2.imshow("WAH!", img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()          
    else:
        print("Invalid answer! System Terminated.")
else:
    print("Invalid Mode! System Terminated.")
