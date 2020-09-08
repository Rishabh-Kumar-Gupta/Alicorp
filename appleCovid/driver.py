import pandas as pd
import requests

# Driver Class
class AllDataCSV:
    def __init__(self,csv_url,nameOfDownloadedFile, nameofSavingFile):
        self.nameofSavingFile = nameofSavingFile
        self.nameOfDownloadedFile = nameOfDownloadedFile
        self.csv_url = csv_url

    def csvDownloadFromUrl(self):
        req = requests.get(self.csv_url)
        url_content = req.content
        csv_file = open(self.nameOfDownloadedFile, 'wb')
        csv_file.write(url_content)
        csv_file.close()
        df = pd.read_csv(self.nameOfDownloadedFile)
        return [df, 200]

    def dateColumnIntoRow(self):
        df = self.csvDownloadFromUrl()[0]
        lst = list(df.columns[0:6])
        df = df.melt(id_vars=lst, var_name="Date", value_name="Value")
        return [df, 200]

    def saveToLocalMachine(self):
        df = self.dateColumnIntoRow()[0]
        df.to_csv(self.nameofSavingFile, index = False)
        return 200

    def run(self):
        self.saveToLocalMachine()
        print("Saved")
        return 200


