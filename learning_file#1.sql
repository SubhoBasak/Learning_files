# chose the database
-- USE sql_store;

# select all data from the customers table where customer_id is 1 and the rows will be ordered by the city names
-- SELECT * FROM customers WHERE customer_id = 1 ORDER BY city;

# select the first_name, last_name, points and points added with 10000000, and show all the records in those columns
# in the output from the customer tabel
-- SELECT first_name, last_name, points, points+10000000 FROM customers;

# select first_name, last_name, points and (points+10)*100 and show all the values but the (points+10)*100 column name will be show as
# 'discount factor'
-- SELECT
--	first_name,
--	last_name,
--	points,
--  (points+10)*10 AS 'discount factor'
-- FROM customers;

# return unique values in the selected columns
-- SELECT DISTINCT state FROM customers;

# ===================================================================================

-- USE sql_store;

-- SELECT name, unit_price, unit_price*1.1 AS new_price FROM products;

# ===================================================================================

-- SELECT * FROM customers WHERE points > 3000;

-- SELECT * FROM customers WHERE state = 'VA';

# <> select all without the mentioned one
-- SELECT * FROM customers WHERE state <> 'va';

-- SELECT * FROM customers WHERE state != 'va';

-- SELECT * FROM customers WHERE birth_date > '1990-01-01';

# =====================================================================

-- Get the orders placed this year

-- SELECT * FROM orders WHERE order_date >= '2019-01-01';

# =====================================================================

-- SELECT * FROM customers WHERE birth_date >= '1990-01-01' AND points > 1000;

# Multiplication has always a higher priority, for that AND is evaluats first and then OR.
# Or we can use parentheses for easy understand
-- SELECT * FROM customers WHERE birth_date > '1990-01-01' OR points > 1000 AND state = 'va';

-- SELECT * FROM customers WHERE NOT(birth_date > '1990-01-01' OR points > 1000 AND state = 'va');
# equavalent expression
-- SELECT * FROM customers WHERE birth_date <= '1990-01-01' AND points <= 1000 OR state != 'va';

-- SELECT * FROM order_items WHERE order_id = 6 AND unit_price*quantity > 30;

# ================================================================

-- SELECT * FROM customers WHERE state = 'va' OR state = 'ga' OR state = 'fl'
# Or equavalent query
-- SELECT * FROM customers WHERE state IN ('va', 'ga', 'fl')
# And the same query with NOT opreator
-- SELECT * FROM customers WHERE state NOT IN ('va', 'ga','fl')

-- SELECT * FROM products WHERE quantity_in_stock IN (49, 38, 72)

# BETWEEN function

-- SELECT * FROM customers WHERE points >= 1000 AND points <= 3000
# equavalent query
-- SELECT * FROM customers WHERE points BETWEEN 1000 AND 3000
# In this second case BETWEEN function check the range between the given values including them also

# We also can check date range using the BETWEEN function. And the date should be given as a string
# And the format should be 'yyyy-mm-dd'
-- SELECT * FROM customers WHERE birth_date BETWEEN '1990-01-01' AND '2000-01-01'

# '%' - for any number of character
-- SELECT * FROM customers WHERE last_name LIKE 'b%'
-- SELECT * FROM customers WHERE last_name LIKE 'brush%'
-- SELECT * FROM customers WHERE last_name LIKE '%b%'
-- SELECT * FROM customers WHERE last_name LIKE '%y'

# '_' - for single number of character
-- SELECT * FROM customers WHERE last_name LIKE '_____y'
-- SELECT * FROM customers WHERE last_name LIKE 'b____y'

-- SELECT * FROM customers WHERE address LIKE '%TRAIL%' OR address LIKE '%AVENUE%'

-- SELECT * FROM customers WHERE phone LIKE '%9'
-- SELECT * FROM customers WHERE phone NOT LIKE '%9'

-- SELECT * FROM customers WHERE last_name LIKE '%field%'
# equavalent query using regular expression
-- SELECT * FROM customers WHERE last_name REGEXP 'field'

-- SELECT * FROM customers WHERE first_name REGEXP 'elka|ambur'
-- SELECT * FROM customers WHERE last_name REGEXP 'ey$|on$'
-- SELECT * FROM customers WHERE last_name REGEXP '^my|se'
# equavalent queries
-- SELECT * FROM customers WHERE last_name REGEXP 'B[r|u]'
-- SELECT * FROM customers WHERE last_name REGEXP 'br|bu'
-- SELECT * FROM customers WHERE last_name REGEXP 'b[ur]'

-- SELECT * FROM customers WHERE phone IS NULL
# This will not work
-- SELECT * FROM customers WHERE phone = NULL

# Sort the records bsed on given column z to a
-- SELECT * FROM customers ORDER BY first_name DESC

-- SELECT * FROM customers ORDER BY state, first_name
-- SELECT * FROM customers ORDER BY state DESC, first_name

-- SELECT first_name, last_name, 10 AS points FROM customers ORDER BY points, first_name
# In the following query 1 and 2 represent the 1st and 2nd column
-- SELECT first_name, last_name, 10 AS points FROM customers ORDER BY 1, 2

-- SELECT * FROM order_items WHERE order_id = 2 ORDER BY quantity*unit_price DESC
-- SELECT *, quantity*unit_price AS total_price FROM order_items WHERE order_id = 2 ORDER BY total_price DESC

-- SELECT * FROM customers ORDER BY points DESC LIMIT 3

-- SELECT * FROM orders
-- SELECT * FROM orders JOIN customers ON orders.customer_id = customers.customer_id
-- SELECT order_id, first_name, last_name FROM orders JOIN customers ON orders.customer_id = customers.customer_id

# If we execute the following query it will occure an error
-- SELECT order_id, customer_id, first_name, last_name FROM orders JOIN customers ON orders.customer_id = customers.customer_id
# The right way to get the expected output we have to use the following query
-- SELECT order_id, orders.customer_id, first_name, last_name FROM orders JOIN customers ON orders.customer_id = customers.customer_id
# Instead of orders.customer_id, we also can write customers.customer_id, because in both table the custoemr_id is same

-- SELECT order_id, orders.customer_id, first_name, last_name FROM orders JOIN customers ON orders.customer_id = customers.customer_id
# The equavalent short query of the above query is :
-- SELECT order_id, any_new_short_name.customer_id, first_name, last_name FROM orders any_new_short_name JOIN customers new_name ON any_new_short_name.customer_id = new_name.customer_id

-- SELECT order_id, p.product_id, quantity, o_i.unit_price FROM order_items o_i JOIN products p ON o_i.product_id = p.product_id

-- SELECT * FROM order_items oi JOIN sql_inventory.products p ON oi.product_id = p.product_id

-- USE sql_inventory;
-- SELECT * FROM products p JOIN sql_store.order_items oi ON p.product_id = oi.product_id

-- USE sql_hr;
-- SELECT * FROM employees;

-- SELECT e.employee_id, e.first_name, m.first_name AS manager FROM employees e JOIN employees m ON e.reports_to = m.employee_id



