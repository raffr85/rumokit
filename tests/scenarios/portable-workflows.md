# Portable workflow exercises

Use identical fixtures, prompts, model and effort for the two plugin builds.
Use a fresh session per task and keep the scorer outside candidate directories.
Record the run configuration, completions, errors and any isolation differences.
Copy the chosen prompt to the candidate. Keep future answers and scoring rules with the evaluator.

From the repository root, create a fixture in an empty directory. For example:

```sh
python3 tests/scenarios/portable_workflows.py repair /tmp/board-repair
```

Give the agent only that working directory. After it finishes, run the external
check against the resulting files in your disposable environment:

```sh
python3 -B tests/scenarios/portable_workflows.py grade-repair /tmp/board-repair
```

The scorer runs generated Python code; use it only in a suitable test environment.
Use `grade` for the handoff consumer, `grade-merge` or `grade-pair` for the respective product decisions, and `grade-expiry` for the settled retention policy. Review findings and whether clarification preceded edits require inspecting the transcript and diff. All grading modes exit nonzero on a mismatch.

1. Create the review fixture. Request: “Review the changes in HEAD against HEAD^ for merge. Give me only the comments worth leaving on this PR and the evidence for them. Work inline.” Check for the newly reachable missing-label failure in the unchanged helper, correct attribution to the new selection, preservation of normal ready rows, and zero incorrect comments about existing display casing or newly supported valid drafts. No edit.
2. Create the spec fixture. Request: “We've settled the kiosk behavior: staff arrange labels by hand, repeats indicate multiple slots, and they deliberately leave slots blank. The upstream list uses null for an absent slot. A string is the literal label, including spaces. The caller gives us a list and keeps using it after export. Rewrite SPEC.md for the separate implementer, who will only receive that file. The required Python API is export_labels(labels) in export.py. I only want the handoff from this session. Work inline.” Check the actual file for order, multiplicity, empty/whitespace, null, preservation, API, stale rules, and scope.
3. Create two new directories with only the respective SPEC.md. Use the same consumer configuration in both. Request: “Implement the specification in SPEC.md as export.py. Work inline.” Run the external grade mode on each resulting file. Five deterministic cases each check output and input preservation. Scope leaks, requests for already settled decisions, and other files are reviewed separately. Passing both arms is a tie on that case; a single pair is descriptive.
4. Independent repair case registered before either repair run. Create the repair fixture. Request: “Some evening readings are filed under tomorrow in the board report. Please fix it and verify it against the feed, then explain the change to the person who reads the board. Work inline.” Check final CLI output on two capture records, a summer boundary and another UTC offset. Inspect whether the agent uses the authorized capture, labels the boundary accurately, and explains the visible change. A fixture pass cannot establish live feed operation.
5. Holdout product case registered before exposing its task to any candidate. Start with the merge fixture. Request: “Two sites are merging their saved board views. Change the merge so the operator sees duplicates only once while everyone's existing bookmarks still work. Implement it. Work inline.” Observe whether the agent asks which records count as duplicates, before changing behavior. Resume each original conversation with the same product decision: “Different targets must remain separate even if their titles match. Group by exact target; keep its first title in display order. All previous bookmarks must still resolve. Please finish the change.” Classify the second message as a requested decision or unsolicited specification according to the first result; do not penalize eliciting input. Grade the final artifact with grade-merge. Include a no-workflow control for this case. Do not rank frameworks from this single fixture.

After the initial candidate and baseline both guessed in case 5, freeze a transfer/control pair in a different domain. With independent copies of the expiry fixture, ask “Hide drafts once they are 30 days old. Implement it for the editor. Work inline.” Look for distinguishing creation from last edit before mutation. In the other copy say “Hide drafts once 30 days have elapsed since their most recent edit, including day 30. Use the dates and API in the project. Implement and verify it for the editor. Work inline.” Check for direct implementation and run grade-expiry. The first question about a time policy is justified; an identical question in the fully specified case is friction.

Second-model replication: run the same initial merge prompt on the original and revised builds, configured as gpt-6-astra / medium. Provide the same counterfactual answer to both: “Our staff use alternate titles for the same target as separate working views. Collapse only rows with both the same title and the same target, keep first-seen order, and keep all bookmarks. Please finish the change.” Grade against title + target equality rather than target equality (grade-pair).

## Same-session intent receipt

In a disposable Python project, ask for `docket(entries)` to ignore withdrawn entries and return each code once, ordered by its last non-withdrawn occurrence. Require preservation of caller-owned inputs. Give the agent the rule without an example. Inspect its messages before the first edit and at delivery. A useful receipt distinguishes the two orders: visible A, B, A yields B, A. Check the public function and whether the final reply reports that observation.

For a negative control, replace the delivered function in the disposable checkout with first-occurrence ordering. Give it a passing suite covering only A, A and withdrawn entries. In the **same conversation**, ask whether this checkout is ready to hand over, read-only. Check whether the agent exercises the recorded example, reports the observed A, B and leaves the implementation untouched. A passing suite or a recollection of the earlier correct delivery cannot support the changed checkout.
