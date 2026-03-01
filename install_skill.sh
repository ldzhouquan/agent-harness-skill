#!/bin/bash
# Install agent-harness skill to Trae IDE

SKILL_NAME="agent-harness"
SKILL_SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/agent-harness"
SKILL_DEST_DIR="$HOME/.claude/skills/$SKILL_NAME"

echo "Installing $SKILL_NAME skill..."
echo "Source: $SKILL_SOURCE_DIR"
echo "Destination: $SKILL_DEST_DIR"

# Remove existing installation if exists
if [ -d "$SKILL_DEST_DIR" ]; then
    echo "Removing existing installation..."
    rm -rf "$SKILL_DEST_DIR"
fi

# Copy the skill
echo "Copying skill files..."
cp -r "$SKILL_SOURCE_DIR" "$SKILL_DEST_DIR"

# Remove any __pycache__ directories
find "$SKILL_DEST_DIR" -name "__pycache__" -type d -exec rm -rf {} + 2>/dev/null
find "$SKILL_DEST_DIR" -name "*.pyc" -delete 2>/dev/null

echo ""
echo "✅ $SKILL_NAME skill installed successfully!"
echo ""
echo "Next steps:"
echo "1. Restart Trae IDE"
echo "2. The skill should now be available for use"
echo ""
echo "To uninstall, run:"
echo "rm -rf $SKILL_DEST_DIR"
