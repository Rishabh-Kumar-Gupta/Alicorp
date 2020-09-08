# Main Class
from driver import AllDataCSV
import requests
import json
import io


def urlFinder():
    url = "https://covid19-static.cdn-apple.com/covid19-mobility-data/current/v3/index.json"
    page = requests.get(url)
    res = page.text
    r = json.loads(res)
    url = "https://covid19-static.cdn-apple.com" + r['basePath'] + r['regions']['en-us']['csvPath']
    return url

def main():
    nameOfDownloadedFile = 'downloaded.csv'
    nameOfSavingFile = "save.csv"
    url = "https://covid19.apple.com/mobility"
    # csv_url = "https://covid19-static.cdn-apple.com/covid19-mobility-data/2016HotfixDev8/v3/en-us/applemobilitytrends-2020-09-05.csv"
    csv_url = urlFinder()
    obj = AllDataCSV(csv_url, nameOfDownloadedFile, nameOfSavingFile)
    obj.run()

if __name__=="__main__":
    main()

