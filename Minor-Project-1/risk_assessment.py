#!/usr/bin/env python3
"""SME cybersecurity risk assessment tool (educational project; standard library only)."""
from __future__ import annotations

import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any

RISK_REGISTER: list[dict[str, Any]] = [
    {
        "id": "R001",
        "threat": "Phishing and business email compromise",
        "asset": "Employee email and business accounts",
        "likelihood": 4,
        "impact": 5,
        "nist_functions": ["Protect", "Detect"],
        "mitigations": ["Enable MFA", "Deploy email filtering and domain authentication", "Conduct phishing-awareness training", "Provide a simple report-phishing process"],
    },
    {
        "id": "R002",
        "threat": "Ransomware or destructive malware",
        "asset": "Business files, endpoints, and servers",
        "likelihood": 3,
        "impact": 5,
        "nist_functions": ["Protect", "Detect", "Respond", "Recover"],
        "mitigations": ["Maintain offline or immutable backups", "Patch operating systems and applications", "Use endpoint protection", "Test incident-response and restore procedures"],
    },
    {
        "id": "R003",
        "threat": "Weak or reused passwords",
        "asset": "Cloud services and employee accounts",
        "likelihood": 4,
        "impact": 4,
        "nist_functions": ["Protect", "Detect"],
        "mitigations": ["Require MFA", "Use a password manager", "Block known-compromised passwords", "Review authentication logs"],
    },
    {
        "id": "R004",
        "threat": "Insider misuse or accidental data exposure",
        "asset": "Customer and financial records",
        "likelihood": 2,
        "impact": 5,
        "nist_functions": ["Govern", "Protect", "Detect"],
        "mitigations": ["Apply least privilege and role-based access", "Review access regularly", "Log access to sensitive data", "Train staff on data handling and offboarding"],
    },
    {
        "id": "R005",
        "threat": "Unpatched software and exposed services",
        "asset": "Workstations, routers, and public-facing systems",
        "likelihood": 3,
        "impact": 4,
        "nist_functions": ["Identify", "Protect", "Detect"],
        "mitigations": ["Maintain an asset and software inventory", "Apply security updates promptly", "Disable unnecessary services", "Use firewalls and vulnerability scanning"],
    },
    {
        "id": "R006",
        "threat": "Loss or theft of a laptop",
        "asset": "Portable devices and locally stored data",
        "likelihood": 3,
        "impact": 3,
        "nist_functions": ["Identify", "Protect", "Respond"],
        "mitigations": ["Enable full-disk encryption", "Use screen locks and device management", "Back up business data", "Have a device-loss reporting procedure"],
    },
]

def risk_level(score: int) -> str:
    """Map a 1–25 score to the project's documented qualitative band."""
    if not 1 <= score <= 25:
        raise ValueError("Risk score must be between 1 and 25.")
    if score <= 4:
        return "Low"
    if score <= 9:
        return "Moderate"
    if score <= 16:
        return "High"
    return "Critical"

def assess_risk(item: dict[str, Any]) -> dict[str, Any]:
    likelihood = int(item["likelihood"])
    impact = int(item["impact"])
    if not 1 <= likelihood <= 5 or not 1 <= impact <= 5:
        raise ValueError(f"{item.get('id', 'Risk')}: likelihood and impact must each be 1–5.")
    score = likelihood * impact
    return {
        **item,
        "risk_score": score,
        "risk_level": risk_level(score),
    }

def build_assessment(items: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    """Return assessed risks ordered from highest to lowest score."""
    source = RISK_REGISTER if items is None else items
    return sorted((assess_risk(item) for item in source),
                  key=lambda row: (-row["risk_score"], row["id"]))

def export_json(rows: list[dict[str, Any]], destination: Path) -> None:
    destination.write_text(json.dumps(rows, indent=2), encoding="utf-8")

def export_csv(rows: list[dict[str, Any]], destination: Path) -> None:
    fields = ["id", "threat", "asset", "likelihood", "impact", "risk_score",
              "risk_level", "nist_functions", "mitigations"]
    with destination.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({**row,
                "nist_functions": "; ".join(row["nist_functions"]),
                "mitigations": "; ".join(row["mitigations"])})

def print_report(rows: list[dict[str, Any]]) -> None:
    print("SME CYBERSECURITY RISK REGISTER")
    print("=" * 78)
    for row in rows:
        print(f'{row["id"]} | {row["risk_level"]:<8} | {row["risk_score"]:>2}/25 | {row["threat"]}')
        print(f'     Asset: {row["asset"]}')
        print(f'     NIST CSF 2.0: {", ".join(row["nist_functions"])}')
        print(f'     Mitigations: {"; ".join(row["mitigations"])}')
    print("\nNote: sample scores are illustrative; validate likelihood and impact with the organization.")

def main() -> int:
    parser = argparse.ArgumentParser(description="Assess and rank illustrative SME cyber risks.")
    parser.add_argument("--format", choices=("text", "json", "csv"), default="text")
    parser.add_argument("--output", type=Path, help="Output path for JSON or CSV.")
    parser.add_argument("--list", action="store_true", help="List risk IDs and titles.")
    args = parser.parse_args()

    if args.list:
        for item in RISK_REGISTER:
            print(f'{item["id"]}: {item["threat"]}')
        return 0

    rows = build_assessment()
    if args.format == "text":
        print_report(rows)
    else:
        if args.output is None:
            parser.error("--output is required when --format is json or csv")
        if args.format == "json":
            export_json(rows, args.output)
        else:
            export_csv(rows, args.output)
        print(f"Exported {len(rows)} assessed risks to {args.output}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
