-- Create roles (users)
CREATE USER taskly_user WITH PASSWORD 'taskly_password';
CREATE USER tasks_user WITH PASSWORD 'tasks_password';
CREATE USER users_user WITH PASSWORD 'users_password';

-- Create databases
CREATE DATABASE taskly OWNER taskly_user;
CREATE DATABASE tasks_db OWNER tasks_user;
CREATE DATABASE users_db OWNER users_user;

-- Connect to each database and grant permissions
\connect taskly

GRANT ALL PRIVILEGES ON DATABASE taskly TO taskly_user;

\connect tasks_db

GRANT ALL PRIVILEGES ON DATABASE tasks_db TO tasks_user;

\connect users_db

GRANT ALL PRIVILEGES ON DATABASE users_db TO users_user;

-- Ensuring future privileges
ALTER DATABASE taskly SET search_path TO public;
ALTER DATABASE tasks_db SET search_path TO public;
ALTER DATABASE users_db SET search_path TO public;
