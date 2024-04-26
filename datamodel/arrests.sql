CREATE SCHEMA instance;

CREATE  TABLE instance.date_dimension ( 
	date_key             VARCHAR    NOT NULL   PRIMARY KEY,
	arrest_date          DATE       ,
	day                  INT       ,
	month                INT       ,
	quarter              INT       ,
	week                 INT       ,
	year                 INT       
 );

CREATE  TABLE instance.facts_arrest ( 
	arrest_key           BIGINT    NOT NULL   ,
	location_key         VARCHAR    NOT NULL   ,
	date_key             VARCHAR    NOT NULL   ,
	perpetrator_key      VARCHAR    NOT NULL   ,
	law_key              VARCHAR    NOT NULL   ,
	offense_key          VARCHAR    NOT NULL   ,
	police_department_key VARCHAR    NOT NULL   ,
	is_felony            BOOLEAN       ,
	is_misdemeanor       BOOLEAN       ,
	is_violation         BOOLEAN       ,
	arrest_count         INT       ,
	CONSTRAINT pk_facts_arrest PRIMARY KEY ( arrest_key, location_key, date_key, perpetrator_key, law_key, offense_key, police_department_key )
 );

CREATE  TABLE instance.law_dimension ( 
	law_key              VARCHAR    NOT NULL   PRIMARY KEY,
	law_code             VARCHAR       ,
	law_cat_cd           VARCHAR       
 );

CREATE  TABLE instance.location_dimension ( 
	location_key         VARCHAR    NOT NULL   PRIMARY KEY,
	arrest_boro          VARCHAR       ,
	arrest_precinct      INT       ,
	x_coord_cd           BIGINT       ,
	y_coord_cd           BIGINT       ,
	latitude             DECIMAL       ,
	longitude            DECIMAL       ,
	boro_precinct        VARCHAR       
 );

CREATE  TABLE instance.offense_dimension ( 
	offense_key          VARCHAR    NOT NULL   PRIMARY KEY,
	ky_cd                INT       ,
	ofns_desc            VARCHAR       
 );

CREATE  TABLE instance.perpetrator_dimension ( 
	perpetrator_key      VARCHAR    NOT NULL   PRIMARY KEY,
	age_group            VARCHAR       ,
	perp_sex             CHAR(1)       ,
	perp_race            VARCHAR       ,
	age_category         VARCHAR       
 );

CREATE  TABLE instance.police_department_dimension ( 
	police_department_key VARCHAR    NOT NULL   PRIMARY KEY,
	pd_cd                INT       ,
	pd_desc              VARCHAR       ,
	jurisdiction_code    INT       
 );
