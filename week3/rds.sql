USE hasandb;
-- DROP TABLE titanic;
CREATE TABLE titanic (
	PassengerId int NULL,
    Survived int NULL,
    Pclass int NULL,
    Name text NULL,
    Sex text NULL,
    Age double NULL,
    SibSp int NULL,
    Parch int NULL,
    Ticket text NULL,
    Fare double NULL,
    Cabin text NULL,
    Embarked text NULL
);
LOAD DATA LOCAL INFILE '~/Downloads/titanic.csv' INTO TABLE titanic
FIELDS TERMINATED BY ',' -- csv
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS; -- ignore first line as header