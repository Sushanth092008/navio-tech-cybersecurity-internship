# Minor Project 2: Zero Trust Architecture for Enterprise Security

Educational Zero Trust access-control simulator implementing identity verification, MFA checks, role-based access control (RBAC), device posture, resource segmentation, and encrypted-channel requirements.

## Requirements
- Python 3.10+
- Standard library only

## Run
```bash
python zero_trust_simulator.py
python zero_trust_simulator.py --demo
python -m unittest discover -s tests -v
```

## Model
The policy engine denies access by default. Access is granted only when the user is active, MFA is verified, the device is trusted, the user's role is authorized for the requested resource, and the session uses the required secure channel. This is a simplified teaching model, not a production identity provider or cryptographic implementation.

## Demonstration scenarios
The included demo covers an authorized employee, a missing MFA factor, an untrusted device, a role mismatch, and an inactive account. Results are simulated policy decisions and do not represent a penetration test.

## Safety and limitations
No real accounts, enterprise directory, network, or cloud tenant are accessed. Passwords and authentication secrets are not collected. For production, use a mature IAM/IdP, phishing-resistant MFA, managed device posture, audited policy enforcement, and tested key management.
