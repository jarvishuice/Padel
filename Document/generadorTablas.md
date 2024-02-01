# Tablas para la base de datos ede padel 

+ el sistema esta realizado con le motor de base de datos postgresql en casod e adaptarlo a otro motor de base de datos deberia de cambiar las sentencias sql paara adaptarlo de igual forma se le anexa una diagrama de entidad rela el cual debe seguir rigurosamente 


```sql
-- public.bancos definition

-- Drop table

-- DROP TABLE public.bancos;

CREATE TABLE public.bancos (
	id varchar NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT bancos_pk PRIMARY KEY (id),
	CONSTRAINT bancos_un UNIQUE (nombre)
);

-- Permissions

ALTER TABLE public.bancos OWNER TO postgres;
GRANT ALL ON TABLE public.bancos TO postgres;


-- public.clientes definition

-- Drop table

-- DROP TABLE public.clientes;

CREATE TABLE public.clientes (
	ci varchar NOT NULL,
	nombre varchar NOT NULL,
	telefono varchar NOT NULL,
	correo varchar NULL,
	direccion varchar NULL,
	fecha_ingreso timestamp NOT NULL,
	url_imagen varchar NULL DEFAULT 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fpreviews.123rf.com%2Fimages%2Fylivdesign%2Fylivdesign2101%2Fylivdesign210102017%2F162572026-icono-de-cliente-estilo-de-esquema.jpg&tbnid=qyxQPn0J7Mtr0M&vet=12ahUKEwj9983x4_iDAxVpYTABHTF6B-UQMygEegUIARCAAQ..i&imgrefurl=https%3A%2F%2Fes.123rf.com%2Fphoto_162572026_icono-de-cliente-estilo-de-esquema.html&docid=ngLMwSLUgWLwdM&w=1300&h=1300&q=clientes&hl=es-419&client=firefox-b-e&ved=2ahUKEwj9983x4_iDAxVpYTABHTF6B-UQMygEegUIARCAAQ'::character varying,
	deuda numeric NOT NULL DEFAULT 0.0,
	id varchar NOT NULL,
	CONSTRAINT clientes_pk PRIMARY KEY (id),
	CONSTRAINT clientes_un UNIQUE (nombre),
	CONSTRAINT clientes_un_ci UNIQUE (ci)
);

-- Permissions

ALTER TABLE public.clientes OWNER TO postgres;
GRANT ALL ON TABLE public.clientes TO postgres;


-- public.conceptos_pagos definition

-- Drop table

-- DROP TABLE public.conceptos_pagos;

CREATE TABLE public.conceptos_pagos (
	id int4 NOT NULL,
	nombre varchar NOT NULL,
	descripcion varchar NULL,
	CONSTRAINT conceptos_pagos_pk PRIMARY KEY (id),
	CONSTRAINT conceptos_pagos_un UNIQUE (nombre)
);

-- Permissions

ALTER TABLE public.conceptos_pagos OWNER TO padel;
GRANT ALL ON TABLE public.conceptos_pagos TO padel;


-- public.pagos definition

-- Drop table

-- DROP TABLE public.pagos;

CREATE TABLE public.pagos (
	id varchar NOT NULL,
	fecha_pago timestamp NOT NULL,
	id_cliente varchar NULL
);

-- Permissions

ALTER TABLE public.pagos OWNER TO postgres;
GRANT ALL ON TABLE public.pagos TO postgres;


-- public.prueba definition

-- Drop table

-- DROP TABLE public.prueba;

CREATE TABLE public.prueba (
	id varchar NULL
);

-- Permissions

ALTER TABLE public.prueba OWNER TO postgres;
GRANT ALL ON TABLE public.prueba TO postgres;
GRANT ALL ON TABLE public.prueba TO padel;


-- public.tipos_usuarios definition

-- Drop table

-- DROP TABLE public.tipos_usuarios;

CREATE TABLE public.tipos_usuarios (
	id int4 NOT NULL,
	nombre varchar NOT NULL,
	CONSTRAINT tipos_usuarios_pk PRIMARY KEY (id)
);

-- Permissions

ALTER TABLE public.tipos_usuarios OWNER TO padel;
GRANT ALL ON TABLE public.tipos_usuarios TO padel;


-- public.plan_de_cuentas definition

-- Drop table

-- DROP TABLE public.plan_de_cuentas;

CREATE TABLE public.plan_de_cuentas (
	id varchar NOT NULL,
	metodo varchar NOT NULL,
	n_cuenta varchar NOT NULL,
	id_banco varchar NOT NULL,
	CONSTRAINT plan_de_cuentas_pk PRIMARY KEY (id),
	CONSTRAINT plan_de_cuentas_un UNIQUE (metodo, n_cuenta),
	CONSTRAINT plan_de_cuentas_fk FOREIGN KEY (id_banco) REFERENCES public.bancos(id)
);

-- Permissions

ALTER TABLE public.plan_de_cuentas OWNER TO postgres;
GRANT ALL ON TABLE public.plan_de_cuentas TO postgres;


-- public.usuarios definition

-- Drop table

-- DROP TABLE public.usuarios;

CREATE TABLE public.usuarios (
	id varchar NOT NULL,
	nombre varchar NOT NULL,
	cedula varchar NOT NULL,
	correo varchar NOT NULL,
	tipo_usuario int4 NOT NULL,
	"token" varchar NULL,
	status varchar NOT NULL DEFAULT 'inactivo'::character varying,
	"password" varchar NOT NULL,
	CONSTRAINT usuarios_pk PRIMARY KEY (id),
	CONSTRAINT usuarios_un UNIQUE (cedula),
	CONSTRAINT usuarios_fk FOREIGN KEY (tipo_usuario) REFERENCES public.tipos_usuarios(id)
);

-- Permissions

ALTER TABLE public.usuarios OWNER TO padel;
GRANT ALL ON TABLE public.usuarios TO padel;
INSERT INTO public.conceptos_pagos (id, nombre, descripcion) VALUES(1, 'PAGO PROVEDOR', 'PAgos a los provedores de bla blab bla ');
INSERT INTO public.conceptos_pagos (id, nombre, descripcion) VALUES(2, 'PAGO NOMINA', 'Descuento a la nonima ');
INSERT INTO public.conceptos_pagos (id, nombre, descripcion) VALUES(3, 'VENTA', 'vanta o alquiler ');
```
![img.png](img.png)