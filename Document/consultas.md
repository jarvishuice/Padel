# consultas del sistema 
#### Este documento contiene las consultas empleadas por el core para las operaciones del sistema 

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
3. Inventario actual 
```sql
/*=====================================================
 *              Inventario actual                     *
 * ====================================================*/
select p.nombre ,p.precio,p.costo ,p.id,i.cantidad 
from productos p 
inner join inventario i  on  i.cantidad =i.cantidad 
where p.id = i.id_producto 
--=======================================================
```