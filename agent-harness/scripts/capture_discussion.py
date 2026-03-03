#!/usr/bin/env python3
"""
Enhanced discussion capture script - helps quickly log brainstorm sessions
and design conclusions from any skill interaction.
"""

import argparse
import os
import sys
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(
        description='Quickly capture a discussion and log it to the harness',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Quick capture with minimal info
  python capture_discussion.py --title "API Design Brainstorm" --type design

  # Full capture with participants
  python capture_discussion.py --title "API Design Brainstorm" --type design --participants "Alice, Bob, Code Agent"

  # Open in editor after creation
  python capture_discussion.py --title "API Design Brainstorm" --type design --edit
        """
    )
    parser.add_argument('--title', '-t', required=True, help='Short title for the discussion')
    parser.add_argument('--type', '-y', required=True, 
                       choices=['requirements', 'design', 'execution-plan'],
                       help='Type of discussion')
    parser.add_argument('--participants', '-p', default='Code Agent, User', 
                       help='Participants involved (default: "Code Agent, User")')
    parser.add_argument('--harness-dir', default='.harness', 
                       help='Harness directory path (default: .harness)')
    parser.add_argument('--edit', '-e', action='store_true',
                       help='Open the file in editor after creation')
    args = parser.parse_args()

    discussions_dir = os.path.join(args.harness_dir, 'discussions')
    
    if not os.path.exists(discussions_dir):
        print(f"⚠️  Harness discussions directory not found at {discussions_dir}")
        print("Setting up harness first...")
        
        harness_parent = os.path.dirname(discussions_dir)
        if not os.path.exists(harness_parent):
            os.makedirs(harness_parent, exist_ok=True)
        
        os.makedirs(discussions_dir, exist_ok=True)
        
        index_path = os.path.join(discussions_dir, 'README.md')
        with open(index_path, 'w') as f:
            f.write("""# Discussions Index

## Recent Discussions

## By Category
### Requirements

### Design

### Execution Plans
""")
        print(f"✅ Created discussions directory and index")

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d-%H%M")
    date_str = now.strftime("%Y-%m-%d %H:%M")
    
    safe_title = args.title.lower().replace(' ', '-').replace('/', '-')
    filename = f"{timestamp}-{safe_title}.md"
    filepath = os.path.join(discussions_dir, filename)
    
    template = f"""# {args.title}

**Date**: {date_str}
**Participants**: {args.participants}
**Type**: {args.type}
**Captured with**: capture_discussion.py

---

## ⚡ Quick Capture Section

> Fill this in immediately after your brainstorm!
> You can refine and add more details later.

### Key Points from Discussion
- Point 1:
- Point 2:
- Point 3:

### Decisions Made
- Decision 1:
  - Rationale:
  - Alternatives considered:

### Open Questions
- Question 1:
- Question 2:

### Action Items
- [ ] Action 1 - [Owner]
- [ ] Action 2 - [Owner]

---

## Context
What prompted this discussion? What was the background?

## Discussion Summary
More detailed summary of the conversation.

## Detailed Decisions
Expand on the decisions with more context.

## Related
- Links to other discussions:
- Related files:
- References:

## Next Steps
What happens next?

---
📝 **Reminder**: 
- Commit this file with git!
- Consider creating an ADR if this led to architectural decisions
- Update progress.md to reference this discussion
"""

    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"\n✅ Discussion log created: {filepath}")
    print(f"\n📋 Next steps:")
    print(f"   1. Fill in the Quick Capture section NOW!")
    print(f"   2. Refine details later if needed")
    print(f"   3. Commit: git add {filepath} && git commit -m \"Log discussion: {args.title}\"")
    
    if args.edit:
        print(f"\n🖊️  Opening in editor...")
        editor = os.environ.get('EDITOR', 'vim')
        os.system(f"{editor} {filepath}")
    
    print(f"\n💡 Remember: If it's not in the harness, it didn't happen!")

if __name__ == '__main__':
    main()
