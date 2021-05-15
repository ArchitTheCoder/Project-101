import os
from os.path import relpath
import dropbox

from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    
    def upload_files(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)
        for root, dirs, files in os.walk(file_from):
            for file_name in files:
                local_path = os.path.join(root, file_name)
                relative_path = os.path.relpath(local_path, file_from)
                dbxpath = os.path.join(file_to, relative_path)
            
                with open(local_path, "rb") as f:
                    dbx.files_upload(f.read(), dbxpath, mode = WriteMode("overwrite"))

def main():
    access_token = "3xK4-zIywnsAAAAAAAAAAQWzMlFC4JefQNOBpsNTxLrgn3rvEPyZqTajGLmkLjQK"

    transferData = TransferData(access_token)
    file_from = str(input("Enter the folder path to transfer: "))
    # C:\Users\archi\Downloads\School Videos
    file_to = str(input("Enter the full path to dropbox: "))
    # C:\Users\archi\Dropbox\Test

    transferData.upload_files(file_from, file_to)
    print("File has been moved")

main()