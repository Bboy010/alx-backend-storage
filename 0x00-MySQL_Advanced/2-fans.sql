-- Column names must be: origin and nb_fans
-- nb_fans is the number of fans in this country
SELECT origin, COUNT(*) AS nb_fans
FROM metal_bands
GROUP BY origin
ORDER BY nb_fans DESC, origin ASC;
