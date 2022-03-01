import dropbox

class TransferData(object):
    def _init_(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.BC-pgFK6LIIVDE_4FwI_NHZY6qCwk5N8xg0Sxg06-u3LIVFWZelL4OKcCndcfNgLq01bxR3FzGIjpPtFVNZ04Y75IUCamSuw'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path: ")
    file_to = input("Enter the dropbox file path: ")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)
    print("Transfered successfully.")

if __name__ == '__main__':
    main()