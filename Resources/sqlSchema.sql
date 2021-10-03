-- Create tables for Project3 Weather Events
-- Before creating any tables, drop the tables if the already exsists
Drop TABLE wine_df;


--create table for the data
CREATE TABLE wine_df(
	type varchar  NOT NULL,
	fixed acidity decimal NOT NULL,
	volatile acidity decimal  NOT NULL, 
	citric acid decimal NOT NULL, 
	residual sugar decimal NOT NULL, 
	chlorides decimal NOT NULL,
	free sulfur dioxide decimal NOT NULL, 
	total sulfur dioxide decimal NOT NULL, 
	density decimal NOT NULL, 
	pH decimal NOT NULL,
	sulphates decimal NOT NULL,
	alcohol decimal NOT NULL,
	quality integer NOT NULL,
	class integer NOT NULL,
	name varchar NOT NULL 
);


 
