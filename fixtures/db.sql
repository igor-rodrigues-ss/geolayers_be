
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
SET timezone TO 'America/Sao_Paulo';

CREATE EXTENSION IF NOT EXISTS postgis;


CREATE TABLE layer(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	nome varchar(256) NOT NULL
);

CREATE TABLE layer_properties(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	layer_id UUID NOT NULL,
	propertie json NOT NULL,
	FOREIGN KEY (layer_id) REFERENCES layer(id)
);

CREATE TABLE layer_geometries(
	id UUID DEFAULT uuid_generate_v4() PRIMARY KEY,
	layer_id UUID NOT NULL,
	propertie_id UUID NOT NULL,
	geometry geometry,
	FOREIGN KEY (layer_id) REFERENCES layer(id),
	FOREIGN KEY (propertie_id) REFERENCES layer_properties(id),
	CONSTRAINT geometry_4674 CHECK ((ST_SRID(geometry) = 4674))
);