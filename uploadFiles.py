import dropbox
import os
import shutil

class TransferData(object):
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)


def main():
    accessToken = 'BkMOFwm3Py8AAAAAAAAAAb5NSv7ntVIllO33gAqt4DLQKA5xnbHlYJyyY5MwFx_k'
    transfer_data = TransferData(accessToken)

    file_from = input('Enter the file name:')
    file_to = input('Enter the file name to upload:')

    transfer_data.upload_file(file_from,'/' + file_to)

    # for root,dirs,files in os.walk('backup', topdown=True):
    #     for name in files:
    #         print(os.path.join(name))
    #         print(os.path.join(root,name))

main()