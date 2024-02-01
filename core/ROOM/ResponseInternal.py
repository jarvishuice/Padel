from config.LOGS.LogsSystem import Logs
from core.Entities.ResponseINternalEntity import ResponseInternalEntity


class ResponseInternal() :
    def __init__ (self) -> None :
        pass

    @staticmethod
    def responseInternal(response: ResponseInternalEntity) -> ResponseInternalEntity:
        """

        :rtype: object
        :type response: ResponseInternalEntity
        """
        Logs.WirterTask(response.message)

        return response
