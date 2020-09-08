import pytest
from driver import Gsutil

class TestClass:

    def fix(self):
        cmd = "gsutil ls -l gs://data.visitdata.org/processed/vendor/foursquare/asof/"
        nameofSavingFile = "grouped.csv"
        return Gsutil(cmd, nameofSavingFile)

    def test1(self):
        # pytest.skip("Skipping")
        obj = self.fix()
        lsV = obj.latestVersion()
        # assert 0

        assert len(lsV) > 0

    def test2(self):
        # pytest.skip("Skipping")
        obj = self.fix()
        df = obj.csvFileDownload()
        assert str(type(df)) == "<class 'pandas.core.frame.DataFrame'>"

    def test3(self):
        # pytest.skip("Skipping")
        obj = self.fix()
        res = obj.saveToLocalMachine()
        assert res == 200

