DROP TABLE IF EXISTS Users;
DROP TABLE IF EXISTS Passwords;

CREATE TABLE Users(
    id int,
    login varchar(256),
    money_amount int,
    card_number varchar(16),
    status varchar(16)
);

INSERT INTO Users VALUES(
    0, "admin", 1000, "4716510537135373", "active"
);
INSERT INTO Users VALUES(
    1, "Michael_Jordan", 0, "4916896052954357", "inactive"
);
INSERT INTO Users VALUES(
    2, "James_Harden", 579, "4556506620373585", "active"
);
INSERT INTO Users VALUES(
    3, "Idrak_Merzalizade", 111, "4532703678084565", "active"
);
INSERT INTO Users VALUES(
    4, "James_Franco", 947, "4641745614706825", "inactive"
);

CREATE TABLE Passwords(
    id int,
    password vartchar(256)
);

INSERT INTO Passwords VALUES(
    0, "BAGUVIX"
);
INSERT INTO Passwords VALUES(
    1, "12345"
);
INSERT INTO Passwords VALUES(
    2, "AEZAKMI"
);
INSERT INTO Passwords VALUES(
    3, "dsakfhOIUQHWEiuhasdas"
);
INSERT INTO Passwords VALUES(
    4, "HESOYAM"
);