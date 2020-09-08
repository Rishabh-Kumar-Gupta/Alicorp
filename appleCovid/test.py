import pytest

from driver import AllDataCSV
from main import urlFinder

def fix():
    # csv_url = "https://covid19-static.cdn-apple.com/covid19-mobility-data/2016HotfixDev8/v3/en-us/applemobilitytrends-2020-09-05.csv"
    csv_url = urlFinder()
    nameOfDownloadedFile = 'downloaded.csv'
    nameOfSavingFile = "save.csv"
    obj = AllDataCSV(csv_url, nameOfDownloadedFile, nameOfSavingFile)
    return obj


class TestClass:

    def test1(self):
        # pytest.skip("Skipping")
        obj = fix()
        res = obj.csvDownloadFromUrl()
        assert res[1] == 200

    def test2(self):
        # pytest.skip("Skipping")
        obj = fix()
        res = obj.csvDownloadFromUrl()
        assert res[1] == 200

    def test3(self):
        # pytest.skip("Skipping")
        obj = fix()
        code = obj.saveToLocalMachine()
        assert code == 200
    def test4(self):
        # pytest.skip("Skipping")
        obj = fix()
        code = obj.run()
        assert code == 200

        