-- This file contains the definitions of the tables used in the application
--
-- User table
create table user(u_id serial primary key, u_name varchar(20), u_lastName varchar(20), u_age integer,
 u_address varchar(50), u_location varchar(20), u_email varchar(30), u_password)