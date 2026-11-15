import unittest
from zero_trust_simulator import AccessRequest, evaluate

class ZeroTrustTests(unittest.TestCase):
    def test_valid_authorized_request_allowed(self):
        result = evaluate(AccessRequest("alex", "analyst", "customer_records"))
        self.assertEqual(result["decision"], "ALLOW")

    def test_mfa_required(self):
        result = evaluate(AccessRequest("alex", "analyst", "customer_records", mfa_verified=False))
        self.assertEqual(result["decision"], "DENY")
        self.assertTrue(any("MFA" in reason for reason in result["reasons"]))

    def test_untrusted_device_denied(self):
        result = evaluate(AccessRequest("alex", "analyst", "customer_records", device_trusted=False))
        self.assertEqual(result["decision"], "DENY")

    def test_role_mismatch_denied(self):
        result = evaluate(AccessRequest("alex", "employee", "finance_dashboard"))
        self.assertEqual(result["decision"], "DENY")

    def test_inactive_account_denied(self):
        result = evaluate(AccessRequest("alex", "manager", "finance_dashboard", active=False))
        self.assertEqual(result["decision"], "DENY")

    def test_unknown_resource_default_deny(self):
        result = evaluate(AccessRequest("alex", "manager", "unknown"))
        self.assertEqual(result["decision"], "DENY")

    def test_sensitive_resource_requires_secure_channel(self):
        result = evaluate(AccessRequest("alex", "manager", "finance_dashboard", secure_channel=False))
        self.assertEqual(result["decision"], "DENY")

if __name__ == "__main__":
    unittest.main()
