# Driver
import io
import subprocess
import pandas as pd

class Gsutil:

    def __init__(self,cmd,nameofSavingFile):
        self.cmd = cmd
        self.nameofSavingFile = nameofSavingFile

    def latestVersion(self):
        direct_output = subprocess.check_output(self.cmd, shell=True).decode('utf-8')
        latestVer = direct_output.strip().split("\n")
        dic = {}
        line = latestVer[-1]
        string = line.strip()
        lst = string.split("/")
        newlst = lst[-2].split("-")
        dic[newlst[0]] = string
        laV = ""
        for key in dic:
            lsV = dic[key]
        print("Latest Version : ", lsV)
        return lsV

    def csvFileDownload(self):
        lsV = self.latestVersion()
        csvfileCMD = "gsutil ls -l "
        grpl = []

        cmd = csvfileCMD + lsV
        direct_output = subprocess.check_output(cmd, shell=True).decode('utf-8')
        out = direct_output.split("\n")

        l = []
        for i in out:
            lst = i.split("  ")
            l.append(lst[-1])
        l = l[:-2]


        for string in l:
            if "grouped" in string:
                grpl.append(string)

        cmd = "gsutil cat "
        try:
            cmd = cmd + grpl[0]
            direct_output = subprocess.check_output(cmd, shell=True).decode("utf-8")
            data = io.StringIO(direct_output)
            df = pd.read_csv(data, sep=",")
            print("Success 0")

            n = 2
            # n = len(grpl)
            for i in range(1,n):
                cmd = "gsutil cat "
                cmd = cmd + grpl[i]
                direct_output = subprocess.check_output(cmd, shell=True).decode("utf-8")
                data = io. StringIO(direct_output)
                newDF = pd. read_csv(data, sep=",")
                try:
                    df = pd.concat([df,newDF])
                except SystemError:
                    print("Either DF's columns not similar or Syntax error.")
                print("Success " , i)
            print("DF created")
            return df

        except IndexError:
            print("Index Error")

    def saveToLocalMachine(self):
        try:
            df = self.csvFileDownload()
        except ValueError:
            print("Something went wrong!")
        df.to_csv(self.nameofSavingFile,index = False)
        print("Saved.")
        return 200
    def run(self):
        self.saveToLocalMachine()

