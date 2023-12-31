-- drop table titanic;
CREATE TABLE titanic (
	PassengerId int NULL,
    Survived int NULL,
    Pclass int NULL,
    Name text NULL,
    Sex text NULL,
    Age numeric NULL,
    SibSp int NULL,
    Parch int NULL,
    Ticket text NULL,
    Fare numeric NULL,
    Cabin text NULL,
    Embarked text NULL
);

COPY titanic FROM 's3://{bucket}/{file}'
CREDENTIALS 'aws_iam_role=arn:aws:iam::{account-id}:role/{role-name}'
DELIMITER ','
EMPTYASNULL
BLANKSASNULL
IGNOREHEADER 1
REMOVEQUOTES;

-- debug
-- select * from stl_load_errors
-- order by starttime desc

