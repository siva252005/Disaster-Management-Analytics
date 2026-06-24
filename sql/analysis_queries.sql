-- Top 10 Countries by Disaster Count
SELECT Country,
COUNT(*) AS Total_Disasters
FROM disasters
GROUP BY Country
ORDER BY Total_Disasters DESC
LIMIT 10;

-- Disaster Type Distribution
SELECT Disaster_Type,
COUNT(*) AS Total_Disasters
FROM disasters
GROUP BY Disaster_Type
ORDER BY Total_Disasters DESC;

-- Top Countries by Deaths
SELECT Country,
SUM(Deaths) AS Total_Deaths
FROM disasters
GROUP BY Country
ORDER BY Total_Deaths DESC
LIMIT 10;

-- Top Countries by Economic Loss
SELECT Country,
SUM(Total_Damages_USD) AS Total_Damage
FROM disasters
GROUP BY Country
ORDER BY Total_Damage DESC
LIMIT 10;

-- Economic Loss by Disaster Type
SELECT Disaster_Type,
SUM(Total_Damages_USD) AS Total_Damage
FROM disasters
GROUP BY Disaster_Type
ORDER BY Total_Damage DESC;

-- Severity Distribution
SELECT Severity,
COUNT(*) AS Total
FROM disasters
GROUP BY Severity;

-- Decade-wise Trend
SELECT Decade,
COUNT(*) AS Total_Disasters
FROM disasters
GROUP BY Decade
ORDER BY Decade;

-- Average Deaths by Disaster Type
SELECT Disaster_Type,
ROUND(AVG(Deaths),2) AS Avg_Deaths
FROM disasters
GROUP BY Disaster_Type
ORDER BY Avg_Deaths DESC;

-- Top 5 Deadliest Events
SELECT Country,
Disaster_Type,
Deaths
FROM disasters
ORDER BY Deaths DESC
LIMIT 5;
