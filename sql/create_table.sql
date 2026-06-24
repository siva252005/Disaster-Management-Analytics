USE disaster_db;

CREATE TABLE disasters (
id INT AUTO_INCREMENT PRIMARY KEY,
Year INT,
Disaster_Type VARCHAR(50),
Country VARCHAR(100),
Region VARCHAR(100),
Continent VARCHAR(50),
Deaths INT,
Injured INT,
Affected BIGINT,
Total_Affected BIGINT,
Total_Damages_USD BIGINT,
Decade INT,
Severity VARCHAR(20),
Damage_Category VARCHAR(20)
);
