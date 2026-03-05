# Module 4: Incremental Development Workflow

## Clean State Principle Explained
- Code standard suitable for merging to main branch
- No major errors, code well-organized, docs complete
- Developers can directly start new feature development without first cleaning up messy code

## Git Rollback Mechanism
- When agent introduces error, after trying to fix without success
- Use version control to roll project back to previous stable commit state
- Provides low-cost fault tolerance, avoids "guessing what happened before"

## Complete Startup Sequence
**MUST strictly follow this order:**

1. **Locate**
   ```bash
   pwd
   ```
   Confirm current working directory

2. **Recall**
   - Read `progress.txt` to see previous round's progress log
   - Read `feature_list.json` to see feature inventory
   - Check Git log: `git log -20` to reconstruct project evolution timeline

3. **Claim Task**
   - Find highest priority feature still not passed
   - Clarify this session's goal

4. **Restore**
   - Check if test scripts exist
   - Start or restart dev server
   - Run basic tests to verify environment

5. **Validate**
   - Confirm core functionality still works
   - Only after confirming system health, start new development work
