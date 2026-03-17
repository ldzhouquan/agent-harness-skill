#!/bin/bash
# Update progress.txt with a new entry
# Usage: ./update-progress.sh <message>
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

MESSAGE="$1"

if [ -z "$MESSAGE" ]; then
    echo "Usage: ./update-progress.sh <message>"
    echo ""
    echo "Examples:"
    echo '  ./update-progress.sh "Started working on Calculator"'
    echo '  ./update-progress.sh "Completed Calculator - all tests passing"'
    echo '  ./update-progress.sh "Blocked: Token refresh bug"'
    exit 1
fi

TIMESTAMP=$(date +%Y-%m-%d\ %H:%M)

# Create progress.txt if it doesn't exist
if [ ! -f "progress.txt" ]; then
    echo "# Progress Log" > progress.txt
    echo "" >> progress.txt
fi

# Add new entry with timestamp
echo "[$TIMESTAMP] $MESSAGE" >> progress.txt

echo "✅ Updated progress.txt"
echo ""
echo "Recent entries:"
tail -10 progress.txt
