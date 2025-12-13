# proxy-based-credit-scoring

## Credit Scoring Business Understanding

Credit risk is defined as the possibility that a borrower will fail to meet their contractual repayment obligations, resulting in financial loss to the lender. In the context of Buy-Now-Pay-Later (BNPL) services, effective credit risk assessment is essential to balance financial inclusion with portfolio stability. This project focuses on developing a proxy-based credit scoring model using alternative transaction data, in line with modern credit risk practices described by the World Bank, HKMA, and Basel II frameworks.

## Basel II Accord and the Importance of Interpretability

The Basel II Capital Accord emphasizes accurate risk measurement, internal model governance, transparency, and auditability in credit risk modeling. Under Basel II, banks are required to demonstrate how credit risk estimates—such as probability of default—are derived, validated, and monitored over time. This regulatory focus necessitates the use of models that are not only predictive but also interpretable and well-documented.

As highlighted in Basel-aligned credit risk literature and industry guidelines, interpretable models allow financial institutions to explain credit decisions to regulators, internal risk committees, and customers. Consequently, this project prioritizes structured feature engineering, clear assumptions, and traceable modeling decisions to ensure regulatory compliance, model stability, and operational trustworthiness.

## Necessity and Risks of a Proxy Default Variable

The dataset used in this project does not include an explicit loan default or repayment outcome variable. According to World Bank and HKMA guidelines on alternative credit scoring, when traditional default labels are unavailable, it is acceptable to construct proxy risk indicators using behavioral data, provided their limitations are clearly acknowledged.

To address this gap, a proxy target variable is created using customer engagement patterns derived from Recency, Frequency, and Monetary (RFM) analysis. Customers exhibiting low transaction frequency, low monetary value, and long periods of inactivity are classified as high-risk proxies, reflecting a higher likelihood of disengagement and potential repayment risk.

However, reliance on proxy variables introduces business and modeling risks. The proxy may incorrectly label temporarily inactive but creditworthy customers as high-risk, or fail to capture external socioeconomic factors affecting repayment capacity. As a result, predictions generated from this model should be used as a decision-support tool rather than a sole determinant for credit approval, consistent with best practices recommended in alternative credit scoring frameworks.

## Trade-offs Between Interpretable and Complex Models in a Regulated Context

Credit risk modeling involves a fundamental trade-off between interpretability and predictive performance. Traditional scorecard-based approaches, such as Logistic Regression combined with Weight of Evidence (WoE), are widely adopted in regulated financial institutions due to their transparency, robustness, and strong regulatory acceptance. These models enable clear interpretation of feature impacts, facilitate model validation, and align closely with Basel II expectations.

In contrast, more complex machine learning models, such as Gradient Boosting, can achieve superior predictive accuracy by capturing non-linear relationships and complex interactions within the data. However, their limited interpretability, increased validation complexity, and higher governance burden make them less suitable as primary decision engines in tightly regulated environments.

In practice, many financial institutions adopt a balanced approach: interpretable models are used for core credit decisioning, while complex models are employed selectively to enhance risk monitoring or support secondary analyses. This project reflects that philosophy by evaluating both model types while maintaining a strong emphasis on explainability and regulatory alignment.