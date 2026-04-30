# 5 KEY RESEARCH QUESTIONS - FORTUNE 500 ANALYSIS
## Formulated for Descriptive Statistics Methods

---

## **QUESTION 1: Profitability vs. Size Relationship**

**Research Question:**
"Is there a strong linear relationship between company revenue and profit?"

**Hypothesis:**
- Larger revenues should drive proportionally higher profits

**Statistical Methods Applied:**
- Simple Linear Regression: `Profits = β₀ + β₁(Revenues)`
- Pearson Correlation coefficient
- Significance test (t-test, p-value)
- R² metric (coefficient of determination)

**Univariate Component:**
- Distribution of Revenues (histogram, box plot)
- Distribution of Profits (histogram, box plot)
- Descriptive statistics (mean, median, std dev, skewness)

**Expected Output:**
- Regression equation with coefficients
- Correlation strength (r value)
- Statistical significance (p < 0.05 or p < 0.001)
- R² explaining percentage of variance explained
- Residual analysis showing fit quality

**Business Question:** "For every $1 billion increase in revenue, how much profit increase can we expect?"

---

## **QUESTION 2: Revenue Stability & Market Performance**

**Research Question:**
"Which companies/metrics show the highest revenue volatility, and how does revenue stability affect market value?"

**Hypothesis:**
- Companies with stable revenues should have more stable market values
- Revenue changes correlate strongly with market value changes

**Statistical Methods Applied:**
- Univariate analysis: Variance, coefficient of variation, range, IQR
- Multivariate correlation analysis
- Scatter plot analysis with trend identification
- Segment analysis (grouping by performance)

**Univariate Component:**
- Distribution of Revenue Changes (% change)
- Identify outliers and extreme values
- Calculate dispersion metrics

**Multivariate Component:**
- Correlation matrix: Revenue Change vs. Market Value
- Scatter plot with fitted trend line
- Identify segments: Stable vs. Volatile companies

**Expected Output:**
- Correlation coefficient between revenue stability and market value
- Distribution of revenue changes across companies
- Identification of stable vs. volatile performers
- Insights on which company categories are most volatile

**Business Question:** "If revenue drops 10%, what happens to market value on average?"

---

## **QUESTION 3: Employee Efficiency**

**Research Question:**
"Do companies with more employees generate proportionally higher revenues? (Do larger workforces lead to higher revenue per employee?)"

**Hypothesis:**
- Company size (employees) should correlate with total revenue
- BUT: Revenue per employee might not scale linearly

**Statistical Methods Applied:**
- Derived metric: Revenue per Employee = Revenues / Employees
- Simple Linear Regression: `Revenue per Employee = f(Number of Employees)`
- Univariate analysis of efficiency metrics
- Segment analysis by company size

**Univariate Component:**
- Distribution of Revenue per Employee
- Distribution of Profit per Employee
- Identify efficiency outliers (highly efficient vs. inefficient)

**Multivariate Component:**
- Scatter plot: Company Size vs. Revenue per Employee
- Show negative/weak correlation (surprising insight)
- Identify high-efficiency outliers

**Expected Output:**
- Revenue per Employee statistics (mean, median, range)
- Profit per Employee statistics
- Regression slope showing relationship (likely weak)
- R² showing low explanatory power (size ≠ efficiency)
- Identification of most efficient companies

**Business Question:** "Is bigger always better? What makes some companies more efficient than others?"

**Key Insight:** Management quality and strategy matter more than headcount

---

## **QUESTION 4: Market Value Predictability**

**Research Question:**
"How well can we predict a company's market value from its financial metrics (revenues, profits, assets)?"

**Hypothesis:**
- Market value should be highly predictable from financial fundamentals
- Strong relationship: Financial metrics → Market Valuation

**Statistical Methods Applied:**
- Multiple Linear Regression: `Market Value = β₀ + β₁(Revenue) + β₂(Profits) + β₃(Assets)`
- Train-Test Split (80% training, 20% testing)
- 5-Fold Cross-Validation
- Model Performance Metrics: R², RMSE, MAE
- Residual Diagnostics:
  - Normality test (Shapiro-Wilk)
  - Homoscedasticity check
  - Linearity verification
- Overfitting detection (compare train vs test R²)

**Univariate Component:**
- Distribution of Market Value
- Identify if Market Value is normally distributed
- Check for outliers

**Multivariate Component:**
- Correlation matrix: All predictors vs. Market Value
- Identify multicollinearity issues
- Select best predictor combination

**Model Validation:**
- Train R² vs. Test R² comparison
- Cross-validation R² with confidence intervals
- Residual distribution analysis
- Q-Q plot for normality
- Residuals vs. Predicted plot for homoscedasticity

**Expected Output:**
- Multiple regression equation with coefficients
- R² > 0.80 (excellent prediction)
- Cross-validation results showing model robustness
- Residual diagnostics confirming assumptions met
- RMSE error values for prediction accuracy

**Business Question:** "Can we reliably predict market value from basic financial statements?"

**Success Criteria:** R² > 0.80 with validated assumptions

---

## **QUESTION 5: Performance Ranking Changes**

**Research Question:**
"What are the temporal patterns in company rankings? How volatile are Fortune 500 positions year-over-year?"

**Hypothesis:**
- Companies maintain relatively stable rankings
- BUT: Significant volatility exists, especially for mid-tier companies

**Statistical Methods Applied:**
- Temporal/Time Series Analysis:
  - Rank change metric: `Rank Change = Previous Rank - Current Rank`
  - Distribution analysis of rank changes
  - Segment analysis by current ranking position
- Univariate analysis of change metrics
- Correlation: Revenue Change vs. Rank Change vs. Profit Change

**Univariate Component:**
- Distribution of Rank Changes (histogram)
- Central tendency: Mean, median rank change
- Dispersion: Std dev, range of rank changes
- Identify distribution shape (normal, skewed)

**Time Series Component:**
- Histogram of rank changes showing frequency distribution
- Performance categories: Significant improvement, moderate, decline, etc.
- Analysis by company segment:
  - Top 20 companies (average rank change)
  - Middle 460 companies (average rank change)
  - Bottom 20 companies (average rank change)
- Correlation: Changes in revenue vs. changes in rank

**Multivariate Component:**
- Scatter plot: Revenue Change vs. Profit Change
- Show correlation between different types of changes
- Identify divergent companies (high revenue growth but profit decline, etc.)

**Expected Output:**
- Distribution of rank changes with statistics
- Percentage of companies that improved vs. declined
- Performance volatility by company segment
- Correlation between revenue changes and rank changes
- Identification of movers vs. stable performers

**Business Question:** "Is a company's Fortune 500 position guaranteed, or is it dynamic?"

**Key Insight:** ~40% improve, ~40% decline, positions are highly dynamic

---

## INTEGRATION TABLE

| Question | Primary Method | Secondary Method | Validation | Time |
|----------|---|---|---|---|
| Q1 | Simple Regression | Correlation | Residual plots | 1.5 min |
| Q2 | Multivariate Correlation | Segment analysis | Scatter plots | 1.5 min |
| Q3 | Regression (efficiency) | Univariate stats | Outlier analysis | 1.0 min |
| Q4 | Multiple Regression | Cross-validation | Residual diagnostics | 2.0 min |
| Q5 | Time Series analysis | Distribution analysis | Segment comparison | 1.0 min |
| | | | **Total** | **8.0 min** |

---

## METHODOLOGY ALIGNMENT

✅ **Univariate Statistics:** Q1, Q2, Q3, Q5
- Histograms, box plots, distributions
- Mean, median, variance, skewness, kurtosis

✅ **Multivariate Statistics:** Q2, Q4, Q5
- Correlation matrices, scatter plots
- Heatmaps, pair-wise relationships

✅ **Linear Regression:** Q1, Q3, Q4
- Simple regression (Q1, Q3)
- Multiple regression (Q4)
- Coefficient interpretation, R² values

✅ **Model Validation:** Q4
- Train-test split, cross-validation
- Residual analysis, assumption checking
- Normality, homoscedasticity tests

✅ **Time Series Analysis:** Q5
- Ranking changes, temporal patterns
- Distribution of changes, segment analysis
- Year-over-year comparisons

---

## PRESENTATION FLOW SUGGESTION

1. **Start (1 min):** Introduce dataset and 5 questions
2. **Q1 (1.5 min):** Revenue-Profit relationship (simple regression)
3. **Q2 (1.5 min):** Revenue stability (multivariate analysis)
4. **Q3 (0.5 min):** Employee efficiency (surprising insight)
5. **Q4 (2 min):** Market value prediction (regression + validation) [Main focus]
6. **Q5 (1 min):** Ranking dynamics (time series)
7. **Conclude (0.5 min):** Summary and implications

---

**Generated:** April 30, 2026  
**For Presentation:** May 5, 2026  
**Status:** Ready for analysis execution
