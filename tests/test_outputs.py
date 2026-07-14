import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Expected values computed from the fixed environment/access.log (6 lines):
# IPs: 192.168.0.1 x2, 192.168.0.2 x2, 10.0.0.5 x2 -> 3 unique
# Paths: /index.html x3, /about.html x2, /api/login x1 -> top is /index.html
EXPECTED = {"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}


def _load():
    assert REPORT.exists(), "no /app/report.json found"
    return json.loads(REPORT.read_text())


def test_criterion_1_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and contains a single valid JSON object."""
    data = _load()
    assert isinstance(data, dict), "report.json must contain a JSON object"


def test_criterion_2_report_has_exact_keys():
    """Criterion 2: the object has exactly the keys total_requests, unique_ips, top_path."""
    data = _load()
    assert set(data.keys()) == set(EXPECTED.keys()), (
        f"expected exactly keys {sorted(EXPECTED)}, got {sorted(data.keys())}"
    )


def test_criterion_3_total_requests():
    """Criterion 3: total_requests is an integer equal to the number of non-empty log lines."""
    data = _load()
    assert isinstance(data["total_requests"], int), "total_requests must be an integer"
    assert data["total_requests"] == EXPECTED["total_requests"]


def test_criterion_4_unique_ips():
    """Criterion 4: unique_ips is an integer equal to the number of distinct client IPs."""
    data = _load()
    assert isinstance(data["unique_ips"], int), "unique_ips must be an integer"
    assert data["unique_ips"] == EXPECTED["unique_ips"]


def test_criterion_5_top_path():
    """Criterion 5: top_path is a string equal to the most frequently requested path."""
    data = _load()
    assert isinstance(data["top_path"], str), "top_path must be a string"
    assert data["top_path"] == EXPECTED["top_path"]
