-- Sql script that lists all bands with Glam rock
-- As their main style, ranked by their longevity
SELECT band_name, (split - formed) AS lifespan
FROM metal_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC;
