import os
import requests
from colorama import Fore

class Update:
    def __init__(self):
        # Get branch name
        self.folder_path = Update.getFolder()

        self.branch = os.popen(f'git -C {self.folder_path} rev-parse --abbrev-ref HEAD').read().split('\n')[0]
        
        self.getOnlineVersion()
        self.localVersion = Update.getLocalVersion(self.folder_path)

        self.formatedOnlineVersion = self.parseVersion(self.onlineVersion)
        self.formatedLocalVersion = self.parseVersion(self.localVersion)

        new_version_availiable = self.compareVersions()

        if not new_version_availiable:
            print(f'{Fore.YELLOW}No new version availiable{Fore.WHITE}')
            return

        print(f'''
            {Fore.GREEN}There is a new update availiable
            {Fore.YELLOW}Current version: {self.localVersion}
            {Fore.YELLOW}Newer version: {self.onlineVersion}
        {Fore.WHITE}''')
        
        self.updatePrompt()
        return

    def updatePrompt(self):
        ans=input(f'{Fore.YELLOW}>_ {Fore.CYAN}There is a new version of Cryptex availiable, do you want to update? (y/N) :{Fore.WHITE} ')

        if ans.lower() in ['y', 'yes']:
            os.system(f'git -C {self.folder_path} pull')
            print(f"{Fore.GREEN}Updated!{Fore.WHITE}")
            exit(0)

        print(f"{Fore.YELLOW}Not updating{Fore.WHITE}")
        return False
    
    def compareVersions(self):
        return self.formatedOnlineVersion > self.formatedLocalVersion

    def getOnlineVersion(self):
        user = 'SSGorg'
        url = f'https://raw.githubusercontent.com/{user}/Cryptex/{self.branch}/version'
        response = requests.get(url)
        self.onlineVersion = response.text.split('\n')[0]

    @staticmethod
    def getFolder():
        return os.path.abspath(os.path.dirname(__file__))

    @staticmethod
    def getFullLocalVersion(folder_path):
        with open(folder_path + '/../version', 'rt') as f:
            return f.read().split('\n')

    @staticmethod
    def getLocalVersion(folder_path):
        return Update.getFullLocalVersion(folder_path)[0]

    def parseVersion(self, versionString) -> str:
        formated = ''.join(versionString.split('.'))
        try:
            return int(formated)
        except ValueError:
            print(f'{Fore.RED}ERROR: Failed to get number from {versionString} formatted to {formated}')
            exit(1)
