create role system_serv_one with login password 'serv_one123';
create database service_one with owner = system_serv_one encoding = 'UTF8' connection limit = -1;
alter database service_one set time zone 'Europe/Moscow';
grant all on database service_one to system_serv_one;
revoke all on database service_one from public;
revoke create on schema public from public;