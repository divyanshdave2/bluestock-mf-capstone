# Data Dictionary

## dim_fund

|## dim_fund

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | TEXT | Unique AMFI scheme code |
| fund_house | TEXT | Asset Management Company (AMC) name |
| scheme_name | TEXT | Official mutual fund scheme name |
| category | TEXT | Fund category (Equity, Debt, Hybrid, etc.) |
| sub_category | TEXT | Fund sub-category (Large Cap, Mid Cap, Small Cap, Liquid, etc.) |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Date when the fund was launched |
| benchmark | TEXT | Benchmark index used for performance comparison |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| exit_load_pct | REAL | Exit load charged on redemption (%) |
| min_sip_amount | REAL | Minimum SIP investment amount (₹) |
| min_lumpsum_amount | REAL | Minimum lump sum investment amount (₹) |
| fund_manager | TEXT | Name of the fund manager |
| risk_category | TEXT | Risk category (Low, Moderate, High, Very High) |
| sebi_category_code | TEXT | SEBI classification code for the scheme |

## fact_nav

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | TEXT | Fund identifier |
| date | DATE | NAV date (business day) |
| nav | REAL | Net Asset Value in INR |

## fact_transactions

| Column Name | Data Type | Description |
|------------|------------|------------|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | TEXT | AMFI scheme code |
| transaction_type | TEXT | SIP, Lumpsum, or Redemption |
| amount_inr | REAL | Transaction amount in INR |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | T30 or B30 city classification |
| age_group | TEXT | Investor age category (18-25, 26-35, etc.) |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income in lakh INR |
| payment_mode | TEXT | UPI, Net Banking, Mandate, or Cheque |
| kyc_status | TEXT | KYC verification status (Verified/Pending) |

## fact_performance

| Column Name | Data Type | Description |
|------------|------------|------------|
| amfi_code | TEXT | AMFI scheme code |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Asset Management Company (AMC) |
| category | TEXT | Fund category (Equity, Debt, Hybrid, etc.) |
| plan | TEXT | Direct or Regular plan |
| return_1yr_pct | REAL | 1-year return percentage |
| return_3yr_pct | REAL | 3-year CAGR return percentage |
| return_5yr_pct | REAL | 5-year CAGR return percentage |
| benchmark_3yr_pct | REAL | 3-year benchmark return percentage |
| alpha | REAL | Excess return over benchmark |
| beta | REAL | Sensitivity to market movements |
| sharpe_ratio | REAL | Risk-adjusted return metric |
| sortino_ratio | REAL | Downside risk-adjusted return metric |
| std_dev_ann_pct | REAL | Annualized standard deviation (volatility) |
| max_drawdown_pct | REAL | Maximum decline from peak value |
| aum_crore | REAL | Assets Under Management (₹ Crore) |
| expense_ratio_pct | REAL | Annual expense ratio (%) |
| morningstar_rating | INTEGER | Fund rating (1–5 stars) |
| risk_grade | TEXT | Risk classification of the fund |