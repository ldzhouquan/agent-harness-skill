#!/bin/bash
# Install Superpowers skills to Trae IDE

echo "Installing Superpowers skills..."
echo ""

SKILLS_SOURCE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/superpowers-skills"
SKILLS_DEST="$HOME/.claude/skills"

echo "Source: $SKILLS_SOURCE"
echo "Destination: $SKILLS_DEST"
echo ""

if [ ! -d "$SKILLS_SOURCE" ]; then
    echo "Error: Superpowers skills source directory not found: $SKILLS_SOURCE"
    exit 1
fi

# Copy each skill
for skill_dir in "$SKILLS_SOURCE"/*; do
    if [ -d "$skill_dir" ]; then
        skill_name=$(basename "$skill_dir")
        echo "Installing skill: $skill_name"
        
        # Remove existing if exists
        if [ -d "$SKILLS_DEST/$skill_name" ]; then
            echo "  - Removing existing installation..."
            rm -rf "$SKILLS_DEST/$skill_name"
        fi
        
        # Copy the skill
        cp -r "$skill_dir" "$SKILLS_DEST/"
        echo "  ✓ Installed"
    fi
done

echo ""
echo "✅ Superpowers skills installed successfully!"
echo ""
echo "Next steps:"
echo "1. Restart Trae IDE"
echo "2. The skills should now be available"
echo ""
echo "Available skills:"
ls -1 "$SKILLS_SOURCE" | while read skill; do echo "  - $skill"; done
echo ""
echo "To uninstall, run:"
echo "for skill in $(ls -1 "$SKILLS_SOURCE"); do rm -rf \"$SKILLS_DEST/\$skill\"; done"
