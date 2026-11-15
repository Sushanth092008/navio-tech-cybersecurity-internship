# Project Report
## Zero Trust Architecture for Enterprise Security

**Student:** Sushanth G  
**Internship:** NavioTech Solution  
**Project:** Minor Project 2  
**Status:** Initial policy simulator and illustrative test scenarios

## 1. Introduction

Traditional perimeter-based security assumes that activity inside a corporate network is relatively trustworthy. Zero Trust instead requires explicit verification of each access request and limits access to the minimum required. The project demonstrates a simplified policy decision process for enterprise resources.

## 2. Objectives

- Explain the principle “Never trust, always verify”.
- Demonstrate Multi-Factor Authentication (MFA) and Role-Based Access Control (RBAC).
- Model identity, device trust, secure-channel, and resource-segmentation checks.
- Simulate authorized and unauthorized access attempts.
- Document results and potential improvements.

## 3. Architecture

The demonstration has four conceptual components:

1. **Identity context:** user identity, account status, and assigned role.
2. **Device posture:** whether the requesting device is marked trusted.
3. **Policy decision point:** evaluates the request against access rules.
4. **Protected resources:** customer records, finance dashboard, public documents, and security administration.

The simulator applies default-deny logic. Sensitive resources require a secure channel. Role membership is checked against each resource's allow-list.

## 4. Authentication and authorization

MFA is represented as a boolean verification result; the simulator does not implement or store OTPs, passwords, or secrets. RBAC associates roles with resource permissions. Device trust and account status are additional contextual checks.

## 5. Micro-segmentation and encryption

The resource policy table illustrates logical segmentation: access to one resource does not imply access to another. The secure-channel flag represents a policy requirement for sensitive resources. It is not a TLS implementation and does not encrypt data itself.

## 6. Simulation results

The included demonstration contains seven requests: a valid analyst request, missing MFA, untrusted device, role mismatch, inactive account, a public-document request, and an unknown resource. The program prints ALLOW or DENY plus reasons. These are deterministic simulated outcomes, not results from a live enterprise network.

## 7. Testing

Run:

```bash
python -m unittest discover -s tests -v
python zero_trust_simulator.py --demo
```

Tests cover valid access, missing MFA, device trust, role mismatch, inactive accounts, unknown resources, and secure-channel enforcement.

## 8. Implementation with enterprise tools

A real deployment could integrate an identity provider (IdP), MFA, endpoint management, network access controls, and centralized logging. VMware or Docker can host isolated lab services, but the current version is a local Python simulation and does not claim to have deployed either platform.

## 9. Limitations and future work

The model uses static roles and a fixed policy table. It does not provide real identity proofing, device attestation, dynamic risk scoring, network micro-segmentation, or cryptographic transport. Future work could add a local web interface, policy configuration files, audit logs, and a controlled container lab.

## 10. References

1. NIST SP 800-207, *Zero Trust Architecture*, https://csrc.nist.gov/pubs/sp/800/207/final
2. NIST SP 800-63B, *Digital Identity Guidelines: Authentication and Lifecycle Management*, https://pages.nist.gov/800-63-4/sp800-63b.html
3. CISA, *Zero Trust Maturity Model*, https://www.cisa.gov/zero-trust-maturity-model

---
**Academic note:** This is a conceptual simulator. Do not describe it as a deployed enterprise Zero Trust environment.
