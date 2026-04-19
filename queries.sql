SELECT category, COUNT(*) AS product_count
FROM amazon_ecommerce
GROUP BY category
ORDER BY product_count DESC;

SELECT category, AVG(price) AS average_price
FROM amazon_ecommerce
GROUP BY category
ORDER BY average_price DESC;

SELECT category, product_id, AVG(rating) AS average_rating
FROM amazon_ecommerce
GROUP BY category, product_id
ORDER BY category,average_rating DESC;

WITH ranked_products AS (
    SELECT category, product_id, 
    AVG(rating) AS average_rating,
    SUM(review_count) AS total_reviews,
    ROW_NUMBER() OVER (PARTITION BY category ORDER BY AVG(rating) DESC, SUM(review_count) DESC) AS rank
    FROM amazon_ecommerce
    GROUP BY category, product_id
)

SELECT * FROM ranked_products
WHERE rank <= 5