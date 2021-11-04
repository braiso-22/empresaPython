create database empresa;
use empresa;

create table departamento(
codigo integer primary key,
nombre text,
presupuesto real
);

create table empleado(
SSN integer primary key,
Nombre text,
Apellido text,
Departamento integer, foreign key (Departamento) references departamento(Codigo));

