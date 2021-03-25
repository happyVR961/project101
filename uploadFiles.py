import dropbox 
import os 
class TransferData:
    def __init__(self, accessToken):
        self.accessToken = accessToken
    def uploadFile(self, fileFrom, fileTo):
        dbx = dropbox.Dropbox(self.accessToken)
        for root, dirs, files in os.walk(fileFrom)
        relative_path = os.path.relpath(local_path, fileFrom)
        dropbox_path = os.path.join(file_to, relative_path)
        with open(local_path, "rb") as f:
            dbx.files_upload(f.read(), dropbox_path, mode = WriteMode('overwrite'))
 def main():
     accessToken = "XisUVUztgA0AAAAAAAAAAaG0OM32SjA-7_kycX_x_5a4A-xcpk41aAqoKkepFhkG"
     data = TransferData(accessToken)
     fileFrom = input("Enter path from file that is to be uploaded: ")
     fileTo = input("Enter path to where file is to be uploaded: ")
     data.uploadFile(fileFrom, fileTo)
     print("File has been moved")
main()






