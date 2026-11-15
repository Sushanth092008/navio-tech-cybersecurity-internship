# Minor Project 1: Cybersecurity Risk Assessment Framework for Small Businesses

A Python command-line tool that helps a small business catalogue cyber risks, score likelihood and impact, rank risks, and export an assessment as JSON or CSV.

## Scope from the allocation brief

- Research common SME risks such as phishing, ransomware, and insider threats.
- Develop a risk assessment model informed by the NIST Cybersecurity Framework.
- Rank threats using severity and impact.
- Recommend mitigations such as firewalls, MFA, and employee training.
- Provide case-study scenarios for validation.
- Document findings and SME best practices.

## Requirements

- Python 3.10+
- No third-party packages required.

## Run

From this directory:

```bash
python risk_assessment.py
python risk_assessment.py --format csv --output risk-register.csv
python risk_assessment.py --format json --output risk-register.json
python risk_assessment.py --list
```

## Scoring method

Likelihood and impact are each rated from 1 (lowest) to 5 (highest). Inherent risk score = likelihood × impact (range 1–25).

- 1–4: Low
- 5–9: Moderate
- 10–16: High
- 17–25: Critical

These thresholds are a simple educational model, not an official NIST scoring scale. NIST CSF 2.0 is used to organize outcomes across Govern, Identify, Protect, Detect, Respond, and Recover; it does not prescribe this numeric formula.

## Validation

Run tests:

```bash
python -m unittest discover -s tests -v
```

The included risk register and case-study scenarios are illustrative sample data, not results from a real client assessment.
