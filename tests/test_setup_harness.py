import sys
import os
import json
import pytest
from datetime import datetime

# Add the project root to sys.path to import setup_harness
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Import from the specific file path to avoid package issues
import importlib.util
spec = importlib.util.spec_from_file_location("setup_harness", os.path.join(project_root, "agent-harness", "scripts", "setup_harness.py"))
setup_harness = importlib.util.module_from_spec(spec)
spec.loader.exec_module(setup_harness)
create_features_json = setup_harness.create_features_json

def test_create_features_json():
    """Test that features.json is created with the correct structure."""
    project_name = "Test Project"
    features = create_features_json(project_name)
    
    # Check basic fields
    assert features["project"] == project_name
    assert "created" in features
    assert isinstance(features["agents"], list)
    assert len(features["agents"]) == 3
    
    # Check agents
    roles = [agent["role"] for agent in features["agents"]]
    assert "implementer" in roles
    assert "tester" in roles
    assert "observer" in roles
    
    # Check observability
    assert "observability" in features
    assert features["observability"]["metrics_enabled"] is True
    assert features["observability"]["logging_enabled"] is True
    
    # Check features list
    assert isinstance(features["features"], list)
    assert len(features["features"]) >= 3
    
    # Check specific features exist
    feature_ids = [f["id"] for f in features["features"]]
    assert "setup-001" in feature_ids
    assert "observability-001" in feature_ids
    assert "testing-001" in feature_ids
    
    # Check default state
    for feature in features["features"]:
        assert feature["passes"] is False
