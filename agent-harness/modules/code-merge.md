# Module 6: Code Merge Strategy

## Cost Function Inversion Explained
**Traditional World:**
- Fixing expensive, waiting cheap
- More checks, more approvals, rather slow than wrong

**Agent World:**
- Fixing cheap, waiting expensive
- Fast release, fast exposure, fast fix

## Three Key Actions

1. **Minimize Blocking Gates**
   - Keep only minimal blocking gates
   - Rather than waiting at every intersection, let process run first

2. **Keep PR Lifecycle Short**
   - Humans often get used to writing huge PRs over several days, but this often leads to long painful reviews and extremely high merge conflict rates
   - But in agent workflow with extremely low fix cost, PRs keep extremely short lifecycle - high-frequency small-step fast merges, collision probability extremely low
   - Even if error occurs, submitting another short-cycle fix PR is just seconds

3. **Never Let Flaky Tests Block Progress Indefinitely**
   - Flaky Tests are those ghost tests that sometimes pass, sometimes fail on same code
   - Traditional approach: facing this instability, pipeline directly red lights, blocks everyone, stops to investigate
   - Here approach: use subsequent re-run mechanism to solve - never indefinitely block overall progress, because waiting cost too high

Since fix cost extremely low, individual test instability, first auto-re-run, fix, also better than letting 100 agents globally jam.

**Applicability:** Only holds when agent code output far exceeds human attention.
