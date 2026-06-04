-- 1. Top 5 funds by 3-year return
SELECT scheme_name, return_3yr_pct
FROM fact_performance
ORDER BY return_3yr_pct DESC
LIMIT 5;

-- 2. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;

-- 3. Total transactions
SELECT COUNT(*) AS total_transactions
FROM fact_transactions;

-- 4. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 5. Transactions by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 6. Top states by transaction count
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 7. Average transaction amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 8. Highest Sharpe ratio funds
SELECT amfi_code, sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 9. Total funds by category
SELECT category, COUNT(*)
FROM dim_fund
GROUP BY category;

-- 10. Maximum NAV
SELECT MAX(nav)
FROM fact_nav;