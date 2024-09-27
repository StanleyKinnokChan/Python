import tableauserverclient as TSC
import pandas as pd
from pathlib import Path
from datetime import datetime
import sys

current_date = datetime.now().strftime("%Y-%m-%d")
current_date_short = datetime.now().strftime("%Y%m%d")

class Tableau_Server(object):
    def __init__(self,token_name, personal_access_token,site_id,url, https = False):
        # authorize 
        print(f"Today is {current_date}\n")
        print(f"Login to the site: {site_id}......\n")
        tableau_auth = TSC.PersonalAccessTokenAuth(token_name, personal_access_token, site_id)
        server = TSC.Server('https://eu-west-1a.online.tableau.com/', use_server_version=True)
        server.auth.sign_in(tableau_auth)
        server.use_highest_version() # make sure to use the same api version as server
        server.server_info.get()

        self.server = server


    def download_wb(self,filepath,*args):

        print("Finding workbooks......\n")
        all_workbooks = list(TSC.Pager(self.server.workbooks))
        workbook = None
        print('-'*50)
        for wb_name in args:

            print(f"  Target workbook: {wb_name}")
            #check if the target workbook has already been downloaded
            wb_name_nospace = wb_name.replace(" ","")
            existing_file_name = f"{wb_name_nospace}_{current_date_short}.twbx"
            existing_file_path = filepath.joinpath(existing_file_name)
            if existing_file_path.exists():
                print(f"\n  Workbook already exists: {existing_file_path}")

            else:
                for wb in all_workbooks:
                    if wb.name == wb_name:
                        print(f"\n  Workbook Found in server. Start downloading '{wb.name}' | {wb.id}......")
                        file_path = self.server.workbooks.download(wb.id, filepath=filepath)
                        file_path = Path(file_path)

                        # check download successfully to target location
                        if file_path.exists():
                            print(f"\n  Downloaded the workbook to target location: {file_path}.")

                            # Get the current date in the desired format
                            new_file_name = f"{file_path.stem}_{current_date_short}{file_path.suffix}"
                            new_file_path = file_path.parent.joinpath(new_file_name)
                            
                            # if new path.exists, rename the file
                            if not new_file_path.exists():
                                file_path.rename(new_file_path)
                                print(f"\n  Workbook is renamed to: {new_file_path}")
                        else:
                            print("\n  Failed! Workbook name cannot be found in the server. Please check the dashboard's name in the server and you request")

                        break
            print('-'*50)
        print('\nProcess Finished. You can now close the window.')

def main():

    if len(sys.argv) > 1:
        filepath = Path(sys.argv[1])
    else:
        # path to the directory where the dashboard will be saved
        filepath=Path(r"<Path>")

    workbook_list = ["workbook_name_1","workbook_name_2",>]

    token_name = '<personal_access_token_name>'
    personal_access_token = '<personal_access_token_secret>'
    site_id = '<site_name>'
    url = '<server_url>'

    # Login to server
    ts = Tableau_Server(token_name,personal_access_token,site_id,url)
    
    # download a workbook
    ts.download_wb(filepath,*workbook_list)

if __name__ == '__main__':
    main()