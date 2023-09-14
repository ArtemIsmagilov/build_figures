-- https://www.trustradius.com/vertical-specific

DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS product;

CREATE TABLE category (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_category VARCHAR
);

CREATE TABLE product (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name_product VARCHAR,
category_id INTEGER,
FOREIGN KEY (category_id) REFERENCES category(id)
);


INSERT INTO category(name_category) VALUES
('3D Modeling Software'),
('Agriculture Software'),
('Animation Software'),
('Apparel Software'),
('Assisted Living Software'),
('Auto Repair Software'),
('Automotive Software Solutions'),
('Aviation Software'),
('Awards Management Software'),
('Banking Software'),
('Car Rental Software'),
('Clinical Data Management Systems'),
('Emergency Notification System')
;

INSERT INTO product(name_product, category_id) VALUES
('Onshape', 1),
('Onshape', 2),
('SketchUp', 2),
('Autodesk Inventor', 2),
('Farmbrite', 3),
('ruumi', 3),
('Adobe After Effects', 5),
('Adobe Animate', 5),
('Vue.ai', 5),
('Awardco', NULL),
('Forma, now part of Snapchat', 6),
('Fullbay', 6),
('OnShift', 7),
('Fullbay', 7),
('Awards Network', NULL),
('Submittable', 8),
('Vision Media', NULL),
('Submittable', 9),
('SurveyMonkey Apply', 9),
('Evalato', 9),
('Acclaim Awards (aka AcclaimWorks)', NULL)
;













