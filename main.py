from PIL import Image
import numpy as np

class ascii:
    def __init__(self, path, ratio):
        self.characters = [".","/","(","*","&","@","#","%"] # characters used to transform to ascii
        self.image = Image.open(path)
        self.greyscale = 0
        self.greyscaleArray = 0
        self.tablereduit = []
        self.result = open("test.txt","r+")
        self.ratio = ratio

    #convert the picture to a greyscaled version
    def convertToGrayscale(self):
        self.greyscale = self.image.convert("L")

    def getgreyscaleArray(self):
        #convert greyscale picture to array
        self.greyscaleArray = np.array(self.greyscale)
        # find the size of the picture with characters from the ratio
        # like if we have a 800x600px pic we can take the first pixel from every
        # rectangle of 5px length and 10px height to convert it to a character
        taillelong = len(np.array(self.greyscaleArray))/(self.ratio*2)
        taillelong = round(taillelong) if taillelong%2 else round(taillelong-1)

        for i in range(taillelong):
            taille = len(np.array(self.greyscaleArray[0]))/self.ratio
            taille = round(taille) if taille%2 else round(taille-1)
            self.tablereduit.append([]) # create a new line in the array to
                                        # detect when to create a new line in the txt doc
            for y in range(taille):
                # remap the numbers to fit between 0 and the numbers of (character-1) in the array
                # taking 1 out of ratio pixel
                self.tablereduit[i].append(round((
                    np.array(self.greyscaleArray[i*(self.ratio*2)][y*self.ratio])
                        *(len(self.characters)-1))/255))

    def toascii(self):
        for i in range(len(self.tablereduit)):
            self.result.write('\n') #create the new line in the txt doc

            for y in range(len(self.tablereduit[i])):
                #add the character to the txt
                self.result.write(self.characters[abs(self.tablereduit[i][y]-(len(self.characters)-1))])
        #closing the txt file
        self.result.close()


test1 = ascii("test.jpg", 5)
test1.convertToGrayscale()
test1.getgreyscaleArray()
test1.toascii()
