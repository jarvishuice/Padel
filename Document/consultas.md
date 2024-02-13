# consultas del sistema 

1.  generador de id  para los conceptos de pagos
```sql 

SELECT max(id) + 1 as nuevoID FROM conceptos_pagos ;



```
2. Descuento del inventario 
```sql 
update inventario set cantidad = ((select cantidad 
from inventario where id_producto  = '0')-0.2) 
where id_producto ='0'
```