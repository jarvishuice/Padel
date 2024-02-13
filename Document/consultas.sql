/* obtiene iel nuevo di para los conceptos de pagos */
SELECT max(id) + 1 as nuevoID FROM conceptos_pagos ;
/*==================================================== */


/* ===Descuento e producto del inventario============*/
update inventario set cantidad = ((select cantidad
from inventario where id_producto  = '0')-0.2)
where id_producto ='0'
/*==================================================*/