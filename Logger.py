import datetime

class logger:

    def __init__(self, pfad):
        self.now = datetime.datetime.now()
        self.pfad = pfad
        self.file = ""
        self.time = str(datetime.time(self.now.hour, self.now.minute, self.now.second))
        self.date = str(datetime.date.today())

                
    def log(self, wert, variable):
        if variable == False:
            wert = "\n" + "Variable Name was not Activate" + " | Value :" + str(wert)
        else:
            wert = "\n" + "Variable Name: " + str(variable) + " | Value: " + str(wert)
        self.file.writelines(wert)

    def start(self):
        msg = "\n" + "Start Logging | Date: " + self.date + " | Time: " + self.time

        print(self.file)
        self.file = open(self.pfad, "a")
        self.file.writelines("\n---------------------------------------------------------------------------------------------------")
        self.file.writelines(msg)
        self.file.writelines("\n---------------------------------------------------------------------------------------------------")

    def end(self):
        self.file.close()


#Tiny Logger Programm written from zProjoloN
#Please don't say it your's our something in this direction
#Here is how to use it. Very simple
# --------------------------------------- 

if __name__ == "__main__" :        
    print("Main ist starting")
    main = logger("Logger/Files/log/variables_log.txt")
    main.start()
    main.log("Hallo ich bin die erste zeile", "Str1")
    main.log("Hallo ich bin die zweit zeil", "Str2")
    main.end()
else:
    pass

# Logger() this class need the file directory where you want to save the log
# start() this function start the progress an creat the file. You have to use it !!!
# log() this function or write the value in the textfile i have file with .txt 
# end() this function close the file . You have to use it !!!
# Have fun with it 