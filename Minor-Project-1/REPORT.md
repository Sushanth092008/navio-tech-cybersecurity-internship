# Project Report
## Cybersecurity Risk Assessment Framework for Small Businesses

**Student:** Sushanth G  
**Internship:** NavioTech Solution  
**Project:** Minor Project 1  
**Status:** Initial implementation and illustrative validation

## 1. Introduction

Small and medium enterprises (SMEs) rely on email, cloud applications, endpoints, and customer records but may have limited cybersecurity resources. This project provides a repeatable way to catalogue common cyber threats, estimate their likelihood and impact, rank them, and select practical mitigations.

## 2. Objectives

- Identify common SME threats including phishing, ransomware, insider misuse, weak passwords, unpatched software, and device loss.
- Use a transparent likelihood-impact scoring method.
- Organize recommended controls using the NIST Cybersecurity Framework (CSF) 2.0 functions.
- Export a ranked risk register for review.

## 3. Methodology

Each risk is described by an identifier, threat, affected asset, likelihood, impact, NIST CSF function mapping, and mitigation actions. Likelihood and impact are rated from 1 to 5. The score is calculated as:

**Risk score = Likelihood × Impact**

| Score | Rating |
|---:|---|
| 1–4 | Low |
| 5–9 | Moderate |
| 10–16 | High |
| 17–25 | Critical |

This is a project-defined educational scale, not a scale prescribed by NIST. Scores should be calibrated with business owners and supported by evidence before operational use.

## 4. Framework alignment

- **Govern:** establish cybersecurity responsibilities and policies.
- **Identify:** understand assets, business context, and risks.
- **Protect:** implement safeguards such as MFA, backups, patching, and access control.
- **Detect:** monitor suspicious activity and security events.
- **Respond:** coordinate containment, communication, and incident handling.
- **Recover:** restore systems and services after disruption.

The NIST CSF functions are used as an organizing framework; the numeric scoring formula is separately defined by this project.

## 5. Illustrative risk register

The program includes six sample risk scenarios. These are hypothetical examples for software demonstration, not findings from a real SME.

| Threat | Likelihood | Impact | Score | Rating |
|---|---:|---:|---:|---|
| Phishing / business email compromise | 4 | 5 | 20 | Critical |
| Ransomware | 3 | 5 | 15 | High |
| Weak or reused passwords | 4 | 4 | 16 | High |
| Insider misuse / accidental exposure | 2 | 5 | 10 | High |
| Unpatched software | 3 | 4 | 12 | High |
| Laptop loss or theft | 3 | 3 | 9 | Moderate |

## 6. Mitigation strategy

Prioritize MFA for email and cloud accounts, secure backups with restore testing, timely patching, endpoint protection, firewall configuration, least-privilege access, encryption of portable devices, employee awareness training, and a documented incident-response process. Controls should be selected based on business context, cost, and residual risk.

## 7. Validation plan and current evidence

The automated tests check score calculation, rating boundaries, invalid input rejection, descending risk ranking, and JSON/CSV export. Run them with:

```bash
python -m unittest discover -s tests -v
```

The included scenarios are illustrative. A real case study requires a consenting business, an agreed scope, evidence collection, stakeholder interviews, and documented findings. No real-business validation is claimed in this version.

## 8. Limitations

- Likelihood and impact values are illustrative and subjective.
- The tool does not discover assets or vulnerabilities automatically.
- The scoring model does not calculate residual risk or financial loss.
- NIST CSF mapping is a high-level categorization, not a certification or compliance assessment.

## 9. Conclusion

The project demonstrates a simple, repeatable SME risk-register workflow. It translates identified threats into prioritized actions and exportable records. Further work can add asset criticality, control effectiveness, residual-risk scoring, and a user interface.

## 10. References

1. NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, 2024, https://www.nist.gov/cyberframework
2. NIST, *Small Business Cybersecurity Corner*, https://www.nist.gov/itl/smallbusinesscyber
3. CISA, *Secure Our World*, https://www.cisa.gov/secure-our-world

---
**Academic note:** Replace illustrative assumptions with verified evidence and add genuine screenshots and approved case-study observations before final submission.
