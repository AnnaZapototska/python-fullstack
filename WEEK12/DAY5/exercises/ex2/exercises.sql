-- 1
-- SELECT * FROM customer;

-- 2
-- SELECT first_name || ' ' || last_name AS full_name FROM customer;

-- 3
-- SELECT DISTINCT create_date FROM customer;

-- 4
-- SELECT * FROM customer ORDER BY first_name DESC;

-- 5
-- SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate ASC;
-- 6
-- SELECT address, phone FROM address WHERE district = 'Texas';
-- 7
-- SELECT *
-- FROM film
-- WHERE film_id IN (15, 150);

-- 8
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'Twilight';

-- 9
-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title LIKE 'Twe%';

-- 10
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC
-- LIMIT 10;

-- 11
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10
-- LIMIT 10;
-- not sure about next solution without limit
-- SELECT film_id, title, description, release_year, rental_rate
-- FROM film
-- ORDER BY rental_rate ASC
-- OFFSET 10 ROWS FETCH NEXT 10 ROWS ONLY;


-- 12
-- SELECT c.first_name, c.last_name, p.amount, p.payment_date 
-- FROM customer c 
-- INNER JOIN payment p 
-- ON c.customer_id = p.customer_id 
-- ORDER BY c.customer_id ASC;

-- 13
-- SELECT f.title 
-- FROM film f 
-- WHERE f.film_id NOT IN 
-- (SELECT DISTINCT i.film_id FROM public.inventory i);

-- 14
-- SELECT c.city, co.country 
-- FROM city c 
-- INNER JOIN country co 
-- ON c.country_id = co.country_id;

-- 15
-- SELECT c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date, s.staff_id 
-- FROM customer c 
-- INNER JOIN payment p 
-- ON c.customer_id = p.customer_id 
-- INNER JOIN staff s 
-- ON p.staff_id = s.staff_id 
-- ORDER BY s.staff_id ASC;
