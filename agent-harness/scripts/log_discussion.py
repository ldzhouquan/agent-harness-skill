#!/usr/bin/env python3
"""
Helper script to log discussions with Code Agent.
Creates structured discussion log files in .harness/discussions/
"""

import argparse
import os
from datetime import datetime

def main():
    parser = argparse.ArgumentParser(description='Log a discussion with Code Agent')
    parser.add_argument('--type', required=True, 
                       choices=['requirements', 'design', 'execution-plan'],
                       help='Type of discussion')
    parser.add_argument('--title', required=True, help='Short title for the discussion')
    parser.add_argument('--participants', default='Code Agent, User', 
                       help='Participants involved (default: "Code Agent, User")')
    parser.add_argument('--harness-dir', default='.harness', 
                       help='Harness directory path (default: .harness)')
    args = parser.parse_args()

    discussions_dir = os.path.join(args.harness_dir, 'discussions')
    
    if not os.path.exists(discussions_dir):
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
        print(f"Created discussions directory and index at {discussions_dir}")

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

## Context
[Add context about what prompted this discussion]

## Discussion Summary
[Key points from the conversation. Use bullet points for clarity.]

## Decisions Made
- Decision 1: [What was decided]
  - Rationale: [Why this choice]
  - Alternatives considered: [Other options]

## Action Items
- [ ] Action 1 - [Owner] - [Deadline]
- [ ] Action 2 - [Owner] - [Deadline]

## Next Steps
[What needs to happen next?]

## References
- Related files: [file paths]
- Related discussions: [links to other logs]
- External resources: [links]
"""

    with open(filepath, 'w') as f:
        f.write(template)
    
    print(f"\n✅ Created discussion log: {filepath}")
    print(f"\nNext steps:")
    print(f"1. Edit the file to add your discussion notes")
    print(f"2. Commit the file with git: git add {filepath} && git commit -m \"Log discussion: {args.title}\"")
    print(f"3. Update .harness/progress.md to reference this discussion")

if __name__ == '__main__':
    main()
