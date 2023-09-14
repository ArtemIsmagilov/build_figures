SELECT p.name_product, c.name_category
FROM product as p
LEFT JOIN category as c
ON p.category_id = c.id ;
