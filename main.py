import pickle

#class Paraglider():
#    def __init__ (self,eier):
#        self.sele = 'viktig'
#        self.kamera = 'digg å ha'
#        self.eier = eier



def saveobject(obj1,obj2,filename):  #lagrer obj1 og obj2 til 'filename'
    with open(filename, 'wb') as output:
        pickle.dump(obj1, output, pickle.HIGHEST_PROTOCOL)
        pickle.dump(obj2, output, pickle.HIGHEST_PROTOCOL)

def loadobject(filename):
    with open(filename, 'rb') as input:
        variable1 = pickle.load(input)
        print variable1.eier
        variable2 = pickle.load(input)
        print variable2.eier
        return (variable1,variable2)



#obj1 = Paraglider('Håkon')
#obj2 = Paraglider('Voss HPGK')
#filename = 'heioghaa_1'

#saveobject(obj1,obj2,filename)
#obj1 = None
#obj2 = None

#print(obj1)
#print(obj2)

[variable1,variable2] = loadobject(filename)  #<- slik loades filene.
