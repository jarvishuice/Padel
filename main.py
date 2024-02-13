from typing import Annotated
from fastapi import FastAPI,Depends
from fastapi.security import OAuth2PasswordBearer
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config

from ROUTE.Clientes.ClientesRouter import CLIENTES
import uvicorn
from ROUTE.user.userRouter import USER
from ROUTE.Pagos.conceptosRouter import CONCEPTOS
from ROUTE.Finance.financeRouter import FINANCE
from ROUTE.Ordenes.ordenesRouter import ORDENES
from ROUTE.Productos.ProductosRouter import PRODUCTOS

origins = ["*"]
app =FastAPI(title="Padel ",version="1.0",openapi_url="/localhost",logger="info",logs_paths="/home/munay/MUNAYSYSTEM2.1DAO/APP/")

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(PRODUCTOS)
app.include_router(ORDENES)
app.include_router(USER)
app.include_router(CLIENTES)
app.include_router(FINANCE)
app.include_router(CONCEPTOS)

if __name__ == '__main__':
    configServer: Config = uvicorn.Config("main:app",port=8010,log_level="info",reload=False,host="0.0.0.0")
    server = uvicorn.Server(configServer)
    server.run()