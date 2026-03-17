#!/bin/bash
# Add a new feature to feature_list.json
# Usage: ./add-feature.sh <feature-name> <description> <verification>
# Can run from any directory -会自动定位项目根目录

set -e

# Find project root (look for package.json, feature_list.json, or .git)
find_project_root() {
    local dir="$PWD"
    while [ "$dir" != "/" ]; do
        if [ -f "$dir/package.json" ] || [ -f "$dir/feature_list.json" ] || [ -d "$dir/.git" ]; then
            echo "$dir"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    # Fallback: use current directory
    echo "$PWD"
}

PROJECT_ROOT="$(find_project_root)"
cd "$PROJECT_ROOT"

FEATURE_NAME="$1"
FEATURE_DESC="$2"
FEATURE_VERIFICATION="$3"

if [ -z "$FEATURE_NAME" ]; then
    echo "Usage: ./add-feature.sh <feature-name> <description> <verification>"
    echo ""
    echo "Arguments:"
    echo "  feature-name    : Feature name (required)"
    echo "  description     : Feature description (required)"
    echo "  verification    : How to verify this feature works (required)"
    echo ""
    echo "Example: ./add-feature.sh \"Calculator\" \"Basic math operations\" \"Run calc.test.js and verify all tests pass\""
    exit 1
fi

# Validation: verification is required
if [ -z "$FEATURE_VERIFICATION" ]; then
    echo "❌ Error: verification is required!"
    echo ""
    echo "Before adding a feature, you MUST define how to verify it works."
    echo "Think about: What tests? What manual checks? What success criteria?"
    echo ""
    echo "Usage: ./add-feature.sh <feature-name> <description> <verification>"
    exit 1
fi

# Create feature_list.json if it doesn't exist
if [ ! -f "feature_list.json" ]; then
    echo '{"features": []}' > feature_list.json
fi

# Generate new ID
FEATURE_COUNT=$(jq '.features | length' feature_list.json 2>/dev/null || echo "0")
FEATURE_ID="F$((FEATURE_COUNT + 1))"
TIMESTAMP=$(date +%Y-%m-%d)

# Create temp file and update
jq --arg id "$FEATURE_ID" \
   --arg name "$FEATURE_NAME" \
   --arg desc "$FEATURE_DESC" \
   --arg verif "$FEATURE_VERIFICATION" \
   --arg date "$TIMESTAMP" \
   '.features += [{"id": $id, "name": $name, "description": $desc, "verification_plan": $verif, "status": "pending", "pass": false, "started_at": $date, "completed_at": null}]' \
   feature_list.json > feature_list.json.tmp && mv feature_list.json.tmp feature_list.json

echo "✅ Added feature: $FEATURE_NAME (ID: $FEATURE_ID)"
echo ""
echo "📋 Verification: $FEATURE_VERIFICATION"

# Show updated list
echo ""
echo "Current features:"
jq -r '.features[] | "  - [\(.status)] \(.name)"' feature_list.json
