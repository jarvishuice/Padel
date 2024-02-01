
import configparser
class PathSystem:
    """
      que contiene las rutas de directorios a utilizar por el sistema
      :var root :str:  path de  crisostomo
      :var logs :str: path de los logs de  crisostomo
      :var assets str: path de los assets
      :var libros str: path de los libros
    """
    config = configparser.ConfigParser()
    config.read('config.ini')
    root = "/home/jarvis/PycharmProjects/Padel/"
    logs = "/home/jarvis/PycharmProjects/Padel/Logs/"
    assets = f'{root}/assets/'
    def __init__(self) -> object:
        pass

    def getRoot(self) -> str: return self.root
    def getLogs(self) -> str: return self.logs
    def getAssets (self) -> str: return self.assets

    def setRoot(self,path:str) -> str:
         self.root = path
         return self.root

y = PathSystem()
print(y.root)