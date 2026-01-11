#!/bin/bash
set -e

echo "Initializing database on first container run..."

psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER --dbname "$POSTGRES_DB" <<-EOSQL
	CREATE USER ${DB__USER} WITH PASSWORD '${DB__PASSWORD}';
	ALTER DATABASE ${POSTGRES_DB} OWNER TO ${DB__USER};
EOSQL

  