#!/usr/bin/env python3
"""A small, deterministic Zero Trust policy simulator for academic demonstration."""
from __future__ import annotations
import argparse
import json
from dataclasses import asdict, dataclass
from pathlib import Path

@dataclass(frozen=True)
class AccessRequest:
    user: str
    role: str
    resource: str
    active: bool = True
    mfa_verified: bool = True
    device_trusted: bool = True
    secure_channel: bool = True

POLICIES = {
    "customer_records": {"roles": {"analyst", "manager"}, "sensitive": True},
    "finance_dashboard": {"roles": {"finance", "manager"}, "sensitive": True},
    "public_docs": {"roles": {"employee", "analyst", "finance", "manager"}, "sensitive": False},
    "security_admin": {"roles": {"security_admin"}, "sensitive": True},
}

def evaluate(request: AccessRequest) -> dict:
    """Evaluate every request; deny by default and return explicit reasons."""
    reasons = []
    if request.resource not in POLICIES:
        reasons.append("Unknown resource: default-deny policy")
        return {"decision": "DENY", "user": request.user, "resource": request.resource, "reasons": reasons}

    policy = POLICIES[request.resource]
    if not request.active:
        reasons.append("Account is inactive")
    if not request.mfa_verified:
        reasons.append("MFA verification missing")
    if not request.device_trusted:
        reasons.append("Device does not meet trusted-device policy")
    if request.role not in policy["roles"]:
        reasons.append("Role is not authorized for this resource")
    if policy["sensitive"] and not request.secure_channel:
        reasons.append("Sensitive resource requires a secure channel")

    return {
        "decision": "DENY" if reasons else "ALLOW",
        "user": request.user,
        "role": request.role,
        "resource": request.resource,
        "reasons": reasons or ["All configured policy checks passed"],
    }

def demo_requests() -> list[AccessRequest]:
    return [
        AccessRequest("alex", "analyst", "customer_records"),
        AccessRequest("sam", "analyst", "customer_records", mfa_verified=False),
        AccessRequest("lee", "finance", "finance_dashboard", device_trusted=False),
        AccessRequest("jo", "employee", "finance_dashboard"),
        AccessRequest("pat", "manager", "finance_dashboard", active=False),
        AccessRequest("kim", "employee", "public_docs"),
        AccessRequest("unknown", "employee", "unknown_resource"),
    ]

def main() -> None:
    parser = argparse.ArgumentParser(description="Run a Zero Trust policy simulation.")
    parser.add_argument("--demo", action="store_true", help="Run predefined demonstration requests.")
    parser.add_argument("--output", type=Path, help="Optional JSON output file.")
    args = parser.parse_args()
    requests = demo_requests() if args.demo else demo_requests()
    results = [evaluate(item) for item in requests]
    for result in results:
        print(f'{result["decision"]:5} | {result["user"]:8} | {result["resource"]}: {"; ".join(result["reasons"])}')
    if args.output:
        args.output.write_text(json.dumps(results, indent=2), encoding="utf-8")
        print(f"Saved {len(results)} decisions to {args.output}")

if __name__ == "__main__":
    main()
