from typing import Any

from pydantic import BaseModel



class ResponseInternalEntity(BaseModel):
    """
    :var status :bool
    :var message :str
    :var response :Any
    """
    status:bool
    message: str
    response: Any
