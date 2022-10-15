import os
import requests

class Update:
    def __init__(self, branch):
        self.branch = branch

    def run(self) -> bool:
        self.getFolder()
        self.getOnlineVersion(f'https://raw.githubusercontent.com/SSGorg/Cryptex/{self.branch}/version')
        self.getLocalVersion()
        print(self.onlineVersion, self.localVersion)

        self.onlineVersion = self.parseVersion(self.onlineVersion)
        self.localVersion = self.parseVersion(self.localVersion)
        print(self.onlineVersion, self.localVersion)

        new_version_availiable = self.compareVersions()

        if not new_version_availiable:
            print('No new version availiable')
            return False
        
        ans=input('>_ There is a new version of Cryptex availiable, do you want to update? (Y/n) : ')
        if 'n' in ans.lower():
            print('Not updating')
            return False

        os.system(f'git -C {self.folder_path} pull')
        return True

    def compareVersions(self):
        return self.onlineVersion > self.localVersion

    def getOnlineVersion(self, url):
        response = requests.get(url)
        self.onlineVersion = response.text.split('\n')[0]

    def getFolder(self):
        self.folder_path = os.path.abspath(os.path.dirname(__file__))

    def getLocalVersion(self):
        with open(self.folder_path + '/../version', 'rt') as f:
            self.localVersion = f.read().split('\n')[0]

    def parseVersion(self, versionString) -> str:
        formated = ''.join(versionString.split('.'))
        try:
            return int(formated)
        except ValueError:
            print(f'ERROR: Failed to get number from {versionString} formatted to {formated}')
            exit(1)
