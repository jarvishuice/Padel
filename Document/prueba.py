import http.client

conn = http.client.HTTPConnection("localhost:8010")

conn.request("GET", "/Padel/Productos/filter/almacen/0")

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))