#import computer vision library, handles opening the camera and setting size of frame and converting color image to grayscale
import cv2

# import the library for reading qr codes, we just use the decode function from this library
import pyzbar.pyzbar as pyzbar



# define type comparison function
def typecomp1(x,y):
    #damage modifiers for normal attacker
    if x[1] == 'normal' and y[1] in ["normal", "fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "psychic","bug", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == "normal" and y[1] in ["rock", "steel",]:
        return 0.5
    elif x[1] == "normal" and y[1] == "ghost":
        return 0
    #damage modifiers for fire attacker
    elif x[1] == 'fire' and y[1] in ["normal", "elec","fight","poison", "ground", "fly", "psychic", "ghost", "dark", "fairy"]:
        return 1.0
    elif x[1] == "fire" and y[1] in ["fire", "water", "rock", "dragon"]:
        return 0.5
    elif x[1] == "fire" and y[1] in ["grass","ice", "bug", "steel"]:
        return 2.0
    #damage modifiers for water attacker
    elif x[1] == "water" and y[1] in ["normal", "elec","ice","fight", "poison", "fly", "psychic", "bug", "ghost", "dark", "steel", "fairy"]:
        return 1
    elif x[1] == "water" and y[1] in ["water", "grass", "dragon"]:
        return 0.5
    elif x[1] == "water" and y[1] in ["fire", "ground", "rock"]:
        return 2.0
    #damage modifiers for electric attacker
    elif x[1] == "elec" and y[1] in ["normal", "fire", "ice", "fight", "poison", "psychic", "bug", "rock", "ghost", "dark", "steel", "fairy"]:
        return 1
    elif x[1] == "elec" and y[1] in ["elec", "grass", "dragon"]:
        return 0.5
    elif x[1] == "elec" and y[1] in ["water", "fly",]:
        return 2
    elif x[1] == "elec" and y[1] == "ground":
        return 0
    #damage modifiers for grass attacker
    elif x[1] == "grass" and y[1] in ["normal", "elec", "ice", "fight", "psychic", "ghost", "dark", "fairy"]:
        return 1
    elif x[1] == "grass" and y[1] in ["fire", "grass", "poison", "fly", "bug", "dragon", "steel"]:
        return 0.5
    elif x[1] == "grass" and y[1] in ["water", "ground", "rock"]:
        return 2.0
    #damage modifiers for ice attacker
    elif x[1] == "ice" and y[1] in ["normal", "elec", "fight", "poison", "psychic", "bug", "rock", "ghost", "fairy"]:
        return 1.0
    elif x[1] == "ice" and y[1] in ["fire", "water", "ice", "steel"]:
        return 0.5
    elif x[1] == "ice" and y[1] in ["grass", "ground", "fly", "dragon"]:
        return 2
    #damage modifiers for fighting attacker
    elif x[1] == "fight" and y[1] in ["fire", "water", "elec", "grass", "fight", "ground", "dragon"]:
        return 1.0
    elif x[1] == "fight" and y[1] in ["poison", "fly", "psychic", "bug", "fairy"]:
        return 0.5
    elif x[1] == "fight" and y[1] in ["normal", "ice", "rock", "dark", "steel"]:
        return 2
    elif x[1] == "fight" and y[1] == "ghost":
        return 0
    #damage modifiers for poison attacker
    elif x[1] == "poison" and y[1] in ["normal", "fire", "water", "elec", "ice", "fight", "fly", "psychic", "bug", "dragon", "dark"]:
        return 1
    elif x[1] == "poison" and y[1] in ["poison", "ground", "rock", "ghost"]:
        return 0.5
    elif x[1] == "poison" and y[1] in ["grass", "fairy"]:
        return 2.0
    elif x[1] == "poison" and y[1] == "steel":
        return 0
    #damage modifiers for ground attacker
    elif x[1] == "ground" and y[1] in ["normal", "water", "ice", "fight", "ground", "psychic", "ghost", "dragon", "dark", "fairy"]:
        return 1
    elif x[1] == "ground" and y[1] in ["grass", "bug"]:
        return 0.5
    elif x[1] == "ground" and y[1] in ["fire", "poison", "steel"]:
        return 2.0
    elif x[1] == "ground" and y[1] == "fly":
        return 0
    #damage modifiers for fly attacker
    elif x[1] == "fly" and y[1] in ["normal", "fire", "water", "ice", "poison", "ground", "fly", "psychic", "ghost", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == "fly" and y[1] in ["elec", "rock", "steel"]:
        return 0.5
    elif x[1] == "fly" and y[1] in ["grass", "fight","bug"]:
        return 2.0
    #damage modifiers for psychic attackers
    elif x[1] == "psychic" and y[1] in ["normal","fire", "water", "elec", "grass", "ice", "ground", "fly", "bug", "rock", "ghost", "dragon", "fairy"]:
        return 1.0
    elif x[1] == "psychic" and y[1] in ["psychic", "steel"]:
        return 0.5
    elif x[1] == "psychic" and y[1] in ["fight", "poison"]:
        return 2.0
    elif x[1] == "psychic" and y[1] == "dark":
        return 0
    #damage modifiers for bug attackers
    elif x[1] == "bug" and y[1] in ["normal", "water", "elec", "ice", "ground", "bug", "rock", "dragon"]:
        return 1.0
    elif x[1] == "bug" and y[1] in ["fire", "fight", "poison", "fly", "ghost", "steel", "fairy"]:
        return 0.5
    elif x[1] == "bug" and y[1] in ["grass","psychic", "dark"]:
        return 2.0
    #damage modifiers for rock attackers
    elif x[1] == "rock" and y[1] in ["normal", "water", "elec", "grass", "poison", "psychic", "rock", "ghost", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == 'rock' and y[1] in ["fight", "ground", "steel"]:
        return 0.5
    elif x[1] == "rock" and y[1] in ["fire", "ice", "fly", "bug"]:
        return 2.0
    #damage modifiers for ghost attackers
    elif x[1] == "ghost" and y[1] in ["fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "bug", "rock", "dragon", "steel", "fairy"]:
        return 1.0
    elif x[1] == "ghost" and y[1] == "dark":
        return 0.5
    elif x[1] == "ghost" and y[1] == ["psychic", "ghost"]:
        return 2.0
    elif x[1] == "ghost" and y[1] == "normal":
        return 0
    #damage modifiers for dragon attackers
    elif x[1] == "dragon" and y[1] in ["normal", "fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "psychic", "bug", "rock", "ghost", "dark"]:
        return 1.0
    elif x[1] == "dragon" and y[1] == "steel":
        return 0.5
    elif x[1] == "dragon" and y[1] == "dragon":
        return 2.0
    elif x[1] == "dragon" and y[1] == "fairy":
        return 0
    #damage modifiers for dark attackers
    elif x[1] == "dark" and y[1] in ["normal", "fire", "water", "elec", "grass", "ice", "poison", "ground", "fly", "bug", "rock", "dragon", "steel"]:
        return 1.0
    elif x[1] == "dark" and y[1] in ["fight", "dark", "fairy"]:
        return 0.5
    elif x[1] == "dark" and y[1] in ["psychic", "ghost"]:
        return 2.0
    #damage modifiers for steel attackers
    elif x[1] == "steel" and y[1] in ["normal", "grass", "fight", "poison", "ground", "fly", "psychic", "bug", "ghost", "dragon", "dark"]:
        return 1.0
    elif x[1] == "steel" and y[1] in ["fire", "water", "elec", "steel"]:
        return 0.5
    elif x[1] == "steel" and y[1] in ["ice","rock", "fairy"]:
        return 2.0
    #damage modifiers for fairy attackers I really like the term fairy attackers
    elif x[1] == "fairy" and y[1] in ["normal", "water", "elec", "grass", "ice", "ground", "fly", "psychic", "bug", "rock", "ghost", "fairy"]:
        return 1.0
    elif x[1] == "fairy" and y[1] in ["fire", "poison", "steel"]:
        return 0.5
    elif x[1] == "fairy" and y[1] in ["fight", "dragon", "dark"]:
        return 2.0
    
#define type comparison2    
def typecomp2(x,y):
    #damage modifiers for normal attacker
    if x[1] == 'normal' and y[2] in ["normal", "fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "psychic","bug", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == "normal" and y[2] in ["rock", "steel",]:
        return 0.5
    elif x[1] == "normal" and y[2] == "ghost":
        return 0
    #damage modifiers for fire attacker
    elif x[1] == 'fire' and y[2] in ["normal", "elec","fight","poison", "ground", "fly", "psychic", "ghost", "dark", "fairy"]:
        return 1.0
    elif x[1] == "fire" and y[2] in ["fire", "water", "rock", "dragon"]:
        return 0.5
    elif x[1] == "fire" and y[2] in ["grass","ice", "bug", "steel"]:
        return 2.0
    #damage modifiers for water attacker
    elif x[1] == "water" and y[2] in ["normal", "elec","ice","fight", "poison", "fly", "psychic", "bug", "ghost", "dark", "steel", "fairy"]:
        return 1
    elif x[1] == "water" and y[2] in ["water", "grass", "dragon"]:
        return 0.5
    elif x[1] == "water" and y[2] in ["fire", "ground", "rock"]:
        return 2.0
    #damage modifiers for electric attacker
    elif x[1] == "elec" and y[2] in ["normal", "fire", "ice", "fight", "poison", "psychic", "bug", "rock", "ghost", "dark", "steel", "fairy"]:
        return 1
    elif x[1] == "elec" and y[2] in ["elec", "grass", "dragon"]:
        return 0.5
    elif x[1] == "elec" and y[2] in ["water", "fly",]:
        return 2
    elif x[1] == "elec" and y[2] == "ground":
        return 0
    #damage modifiers for grass attacker
    elif x[1] == "grass" and y[2] in ["normal", "elec", "ice", "fight", "psychic", "ghost", "dark", "fairy"]:
        return 1
    elif x[1] == "grass" and y[2] in ["fire", "grass", "poison", "fly", "bug", "dragon", "steel"]:
        return 0.5
    elif x[1] == "grass" and y[2] in ["water", "ground", "rock"]:
        return 2.0
    #damage modifiers for ice attacker
    elif x[1] == "ice" and y[2] in ["normal", "elec", "fight", "poison", "psychic", "bug", "rock", "ghost", "fairy"]:
        return 1.0
    elif x[1] == "ice" and y[2] in ["fire", "water", "ice", "steel"]:
        return 0.5
    elif x[1] == "ice" and y[2] in ["grass", "ground", "fly", "dragon"]:
        return 2
    #damage modifiers for fighting attacker
    elif x[1] == "fight" and y[2] in ["fire", "water", "elec", "grass", "fight", "ground", "dragon"]:
        return 1.0
    elif x[1] == "fight" and y[2] in ["poison", "fly", "psychic", "bug", "fairy"]:
        return 0.5
    elif x[1] == "fight" and y[2] in ["normal", "ice", "rock", "dark", "steel"]:
        return 2
    elif x[1] == "fight" and y[2] == "ghost":
        return 0
    #damage modifiers for poison attacker
    elif x[1] == "poison" and y[2] in ["normal", "fire", "water", "elec", "ice", "fight", "fly", "psychic", "bug", "dragon", "dark"]:
        return 1
    elif x[1] == "poison" and y[2] in ["poison", "ground", "rock", "ghost"]:
        return 0.5
    elif x[1] == "poison" and y[2] in ["grass", "fairy"]:
        return 2.0
    elif x[1] == "poison" and y[2] == "steel":
        return 0
    #damage modifiers for ground attacker
    elif x[1] == "ground" and y[2] in ["normal", "water", "ice", "fight", "ground", "psychic", "ghost", "dragon", "dark", "fairy"]:
        return 1
    elif x[1] == "ground" and y[2] in ["grass", "bug"]:
        return 0.5
    elif x[1] == "ground" and y[2] in ["fire", "poison", "steel"]:
        return 2.0
    elif x[1] == "ground" and y[2] == "fly":
        return 0
    #damage modifiers for fly attacker
    elif x[1] == "fly" and y[2] in ["normal", "fire", "water", "ice", "poison", "ground", "fly", "psychic", "ghost", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == "fly" and y[2] in ["elec", "rock", "steel"]:
        return 0.5
    elif x[1] == "fly" and y[2] in ["grass", "fight","bug"]:
        return 2.0
    #damage modifiers for psychic attackers
    elif x[1] == "psychic" and y[2] in ["normal","fire", "water", "elec", "grass", "ice", "ground", "fly", "bug", "rock", "ghost", "dragon", "fairy"]:
        return 1.0
    elif x[1] == "psychic" and y[2] in ["psychic", "steel"]:
        return 0.5
    elif x[1] == "psychic" and y[2] in ["fight", "poison"]:
        return 2.0
    elif x[1] == "psychic" and y[2] == "dark":
        return 0
    #damage modifiers for bug attackers
    elif x[1] == "bug" and y[2] in ["normal", "water", "elec", "ice", "ground", "bug", "rock", "dragon"]:
        return 1.0
    elif x[1] == "bug" and y[2] in ["fire", "fight", "poison", "fly", "ghost", "steel", "fairy"]:
        return 0.5
    elif x[1] == "bug" and y[2] in ["grass","psychic", "dark"]:
        return 2.0
    #damage modifiers for rock attackers
    elif x[1] == "rock" and y[2] in ["normal", "water", "elec", "grass", "poison", "psychic", "rock", "ghost", "dragon", "dark", "fairy"]:
        return 1.0
    elif x[1] == 'rock' and y[2] in ["fight", "ground", "steel"]:
        return 0.5
    elif x[1] == "rock" and y[2] in ["fire", "ice", "fly", "bug"]:
        return 2.0
    #damage modifiers for ghost attackers
    elif x[1] == "ghost" and y[2] in ["fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "bug", "rock", "dragon", "steel", "fairy"]:
        return 1.0
    elif x[1] == "ghost" and y[2] == "dark":
        return 0.5
    elif x[1] == "ghost" and y[2] == ["psychic", "ghost"]:
        return 2.0
    elif x[1] == "ghost" and y[2] == "normal":
        return 0
    #damage modifiers for dragon attackers
    elif x[1] == "dragon" and y[2] in ["normal", "fire", "water", "elec", "grass", "ice", "fight", "poison", "ground", "fly", "psychic", "bug", "rock", "ghost", "dark"]:
        return 1.0
    elif x[1] == "dragon" and y[2] == "steel":
        return 0.5
    elif x[1] == "dragon" and y[2] == "dragon":
        return 2.0
    elif x[1] == "dragon" and y[2] == "fairy":
        return 0
    #damage modifiers for dark attackers
    elif x[1] == "dark" and y[2] in ["normal", "fire", "water", "elec", "grass", "ice", "poison", "ground", "fly", "bug", "rock", "dragon", "steel"]:
        return 1.0
    elif x[1] == "dark" and y[2] in ["fight", "dark", "fairy"]:
        return 0.5
    elif x[1] == "dark" and y[2] in ["psychic", "ghost"]:
        return 2.0
    #damage modifiers for steel attackers
    elif x[1] == "steel" and y[2] in ["normal", "grass", "fight", "poison", "ground", "fly", "psychic", "bug", "ghost", "dragon", "dark"]:
        return 1.0
    elif x[1] == "steel" and y[2] in ["fire", "water", "elec", "steel"]:
        return 0.5
    elif x[1] == "steel" and y[2] in ["ice","rock", "fairy"]:
        return 2.0
    #damage modifiers for fairy attackers I really like the term fairy attackers
    elif x[1] == "fairy" and y[2] in ["normal", "water", "elec", "grass", "ice", "ground", "fly", "psychic", "bug", "rock", "ghost", "fairy"]:
        return 1.0
    elif x[1] == "fairy" and y[2] in ["fire", "poison", "steel"]:
        return 0.5
    elif x[1] == "fairy" and y[2] in ["fight", "dragon", "dark"]:
        return 2.0
    
# define stabcheck

def stabcheck1(x):
    if x[1] == x[5]:
        return 1.5
    else:
        return 1.0
# define stabcheck
def stabcheck2(x):
    if x[1] == x[6]:
        return 1.5
    else:
        return 1.0
    
# define modifier
def modifier(x,y):
    return(float(stabcheck1(x))*(float(stabcheck2(y)))*(float(typecomp1(x,y)))*(float(typecomp2(x,y))))

# define dmg
def dmg(x,y):
    if x[2] == 'phys':
        print(((((2*float(x[13]))+10)/250)*(float(x[8])/float(y[5]))*(float(x[3]))+2)*(float(modifier(x,y)))
    elif x[2] == 'spec':
        print(((((2*float(x[13]))+10)/250)*(float(x[10])/float(y[7]))*(float(x[3]))+2)*(float(modifier(x,y)))
    else:
        print(float(x[3]))
           

# initialize our strings to empty strings, these evaluate to false in python if you do bool("") for example
string1 = ""
string2 = ""

#set up video capture of the webcam
cap = cv2.VideoCapture(0)

#auto detect the width and height of camera in pixels, not actually used in this code but good to know
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# set up while loop that makes camera turn on as long as condition(True) is true or until break
while True:
    
    #cap.read returns a return value to let you know if camera is working as well as series of frames.
    ret, frame = cap.read()
    #convert the frame to grayscale so there's less data to deal with
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # show the "frame" on your computer so you can see what's happening
    cv2.imshow('frame', gray)
    
    
    #pyzbar decodes any qr codes it sees and returns a list
    decodedObjects = pyzbar.decode(gray)
    
    #we iterate through each object in the list and access it's data attribute which is the byte version of the string contained on the qr code
    for obj in decodedObjects:
        #print('obj.data is :', obj.data)
        # we convert the byte data to the string type and call it decodedData
        decodedData = str(obj.data)
        # printing values just to see what's happening under the hood, you can probably get rid of these
        #print('decodedData is :', decodedData)
        #print('string1 is: ', string1)
        #print('string2 is: ', string2)
        
        # if neither string is empty we want to run your comparison and return value
        if string1 != "" and string2 != "":
                arr1 = string1.split(",")
                arr2 = string2.split(",")
                #calling dmg calls other related nested functions and prints the damage dealt we can alter the output to include more info if we want
                dmg(arr1,arr2)
                #since we got the info we needed out of the print statement we can reset the program to the initial conditions
                string1 = ""
                string2 = ""
        
        
        #if both strings are empty we want to assign the decodedData to our first string if that string has enough commas to be an attack
        if string1 == "" and string2 == "" and decodedData.count(",") > 11:
            string1 = decodedData
            #print("STRING1 is ", string1)
        # if string one is not empty then we want to assign the decodedData to our second string    
        elif string1 != "" and string2 =="" and string1 != decodedData and decodedData !="":
            string2 = decodedData
            #print("STRING2 is ", string2)
            
            
    # if you press q you will break out of the while loop that keeps the camera streaming       
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#releases capturing of video        
cap.release()
# destroys the window created for viewing the camera
cv2.destroyAllWindows()
