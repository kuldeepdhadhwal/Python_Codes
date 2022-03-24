# make a logger file
import time

def get_timestamp():
#     for the timestamps
    t = time.localtime()
    return time.strftime('%Y-%m-%d %H:%M:%S', t)

def openLogger(path):
#     modes can be changed
    file = open(path,'w+')
    return file

# calling logger
file = openLogger('/home/kuldeep/Documents/test/first.txt')

def add(file):
    t = get_timestamp()
    file.write(str(t) + " " + "Initalize the function" +"\n")
    a ,b= 20, 10
    file.write(str(a+b) + "\n")
    t = get_timestamp()
    file.write(str(t)+  " " + "End the function" + "\n")
    
def closeLogger(file):
    file.close()
    
add(file)
closeLogger(file)
