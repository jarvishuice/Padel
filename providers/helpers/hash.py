from jwt import encode,decode
from jwt import exceptions
import datetime

from config.LOGS.LogsSystem import Logs
from config.keys.credentialKeys import CredentialKeys
from fastapi.responses import JSONResponse
class HashHelper:
    __key = None
    __algoritmo = "HS256"
    def __init__(self):
        self.__key = CredentialKeys().getKeysUser

    def expireDate(self,days:int) :
        date = datetime.datetime.now()
        newDate =  date + datetime.timedelta(days)
        return newDate
    def crearToken(self,data:dict):
        token = encode(payload={**data,"exp": self.expireDate(1)}, key=self.__key, algorithm= self.__algoritmo)
        print(token)
        return token
    def validarToken(self,token,output=False):
        try:
            if output:
                decode(token, key=self.__key, algorithms=[ self.__algoritmo ])
        except exceptions.DecodeError as e :
            Logs.Error(f"error al decodificar Token  detail [{e}]")
            return JSONResponse(conten={"message": "Token invalido"},status_code=401)
        except exceptions.ExpiredSignatureError as e:
            Logs.Error(f"token expirado detail [{e}]")
            return JSONResponse(conten={"message": "Token Expirado"},status_code=401)
    def cifrar(self, text: str) :
        hash:str = encode(payload={"clave":text},key=self.__key,algorithm=self.__algoritmo)
        return hash


