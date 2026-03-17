#!/bin/bash
# Mark a feature as complete in feature_list.json
# Usage: ./complete-feature.sh <feature-name>
# Can run from any directory -会自动定位项目根目录

set -e

# Find project root
find_project_root() {
    local dir="$PWD"
    while [ "$dir" != "/" ]; do
        if [ -f "$dir/package.json" ] || [ -f "$dir/feature_list.json" ] || [ -d "$dir/.git" ]; then
            echo "$dir"
            return 0
        fi
        dir="$(dirname "$dir")"
    done
    echo "$PWD"
}

PROJECT_ROOT="$(find_project_root)"
cd "$PROJECT_ROOT"

FEATURE_NAME="$1"

if [ -z "$FEATURE_NAME" ]; then
    echo "Usage: ./complete-feature.sh <feature-name>"
    echo "Example: ./complete-feature.sh \"Calculator\""
    exit 1
fi

if [ ! -f "feature_list.json" ]; then
    echo "Error: feature_list.json not found"
    exit 1
fi

TIMESTAMP=$(date +%Y-%m-%d)

# Check if feature exists
if ! jq -e --arg name "$FEATURE_NAME" '.features[] | select(.name == $name)' feature_list.json > /dev/null 2>&1; then
    echo "Error: Feature '$FEATURE_NAME' not found in feature_list.json"
    echo "Available features:"
    jq -r '.features[] | "  - \(.name)"' feature_list.json
    exit 1
fi

# Update feature as complete
jq --arg name "$FEATURE_NAME" \
   --arg date "$TIMESTAMP" \
   '.features |= map(if .name == $name then .status = "completed" | .pass = true | .completed_at = $date else . end)' \
   feature_list.json > feature_list.json.tmp && mv feature_list.json.tmp feature_list.json

echo "✅ Completed feature: $FEATURE_NAME"

# Show updated list
echo ""
echo "Current features:"
jq -r '.features[] | "  - [\(.status)] \(.name)"' feature_list.json
