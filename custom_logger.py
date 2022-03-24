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
    
def read_from_warehouse(opt,arg,file):
    try:
        t = get_timestamp()
        file.write(str(t) + " " + "entered into read from warehouse function" +"\n")
        df_record_count = spark.read.csv(org)
        file.write(str(t) + " "+ str(df_record_count.count()) + "\n")
        file.write(str(t) + " " + "Exit from read from warehouse function" +"\n")
        return df_record_count
    except Exception as e:
        t = get_timestamp()
        file.write(str(t)+  " " + str(e) + "\n")
        print(e)
        
def closeLogger(file):
    file.close()
    
add(file)
closeLogger(file)
