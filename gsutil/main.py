from driver import Gsutil

def main():
    cmd = "gsutil ls -l gs://data.visitdata.org/processed/vendor/foursquare/asof/"
    nameofSavingFile = "grouped.csv"
    gsutil = Gsutil(cmd,nameofSavingFile)
    gsutil.run()
    print("Complete")

if __name__ == '__main__':
    main()
