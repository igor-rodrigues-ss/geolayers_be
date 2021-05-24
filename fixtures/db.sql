
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SET timezone TO 'America/Sao_Paulo';

CREATE EXTENSION IF NOT EXISTS postgis;

create schema tasks;
create schema layers;

create table tasks.save_layer(
	id UUID primary key,
	layer_name varchar(256),
	status varchar(20),
	"detail" text
);

CREATE TABLE layers.layer(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	nome varchar(256) NOT NULL
);

CREATE TABLE layers.properties(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	layer_id UUID NOT NULL,
	properties json NOT NULL,
	FOREIGN KEY (layer_id) REFERENCES layers.layer(id)
);

CREATE TABLE layers.geometries(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	layer_id UUID NOT NULL,
	properties_id UUID NOT NULL,
	geom geometry,
	FOREIGN KEY (layer_id) REFERENCES layers.layer(id),
	FOREIGN KEY (properties_id) REFERENCES layers.properties(id),
	CONSTRAINT geometry_4674 CHECK ((ST_SRID(geom) = 4674))
);

CREATE TABLE layers.styles(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	layer_id UUID NOT NULL,
	color VARCHAR(20) NOT NULL,
	fill BOOLEAN NOT NULL,
	FOREIGN KEY (layer_id) REFERENCES layers.layer(id)
);