-- Column names must be: origin and nb_fans
-- origin is the name of the country
-- nb_fans is the number of fans in this country
-- The result must be sorted by nb_fans in descending order
-- If two countries have the same number of fans, they must be sorted by their name in ascending order

SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC, origin ASC
;
