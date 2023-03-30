
create table if not exists provincias 
(
id integer primary key,
nombre varchar(100) not null,
letra varchar(2) not null
)
;


create table if not exists transferencias 
(
anio integer,
mes integer,
id_provincia integer,
cantidad numeric not null,
primary key (anio,mes,id_provincia),
foreign key (id_provincia) references provincias(id)
)
;
