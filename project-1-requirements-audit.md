# Project 1 Requirements Audit

**Audit date:** October 15, 2026  
**Materials reviewed:** the Project 1 brief, submission architecture, AI Boundary Card, major-project checklist, annotated exemplar/non-example, Research Evolution / Validation / Decision Memo / Manifest templates, starter README guidance, and Weeks 2, 7, and 8 Project 1 materials in the instructor repository.

This is a requirements audit, not a claim that the project is final or submission-ready.

| Requirement | Current status | Evidence / next action |
|---|---|---|
| Eligible operating-company target | Meets | Apple is an operating company compatible with an FCFF / enterprise-value framework. |
| Unchanged Edition A baseline | Partial | `project-1-edition-a.pdf` exists. Preserve the actual Brightspace receipt/attempt ID and do not edit the submitted version. |
| AI-boundary compliance | Verify with instructor / Brightspace | The published GitHub rule says Edition A is AI-closed, while the student reports different instructor direction. Preserve any written instructor clarification and use truthful AI disclosure; do not make an AI-free attestation if it is not true. |
| Edition B A-to-B evolution | In progress | `project-1-edition-b.md` now contains the required table, disclosed AI assistance, current decision, and ending explanation. |
| Five-year three-statement pro-forma | Missing final version | Existing `apple_proforma.py` is a simplified FCFE model; rebuild to a company-specific, articulating income statement, balance sheet, and cash-flow statement. |
| FCFF DCF, WACC, terminal value, bridge | Partial | `dcf.py` runs an FCFF case, but starting FCFF, WACC, and bridge conventions need full reconciliation and source support. |
| Normalization / historical-input evidence | Partial | Filing facts exist, but the base-year one-time-item / basis-change decision is not documented. |
| Low/base/high cases and sensitivity | Partial | WACC–growth and FCFE driver sensitivities exist; add causal FCFF low/base/high cases linked through the statements. |
| Comparable-company policy and multiples | Partial | P/E cross-check exists. Freeze a peer policy before final selection; add at least one consistent EV multiple and one equity-value multiple. |
| Semi-adjustable analyst product | Missing | Build bounded controls, base reset, live sensitivity results, and visible checks that fail loudly. A notebook with widgets is sufficient. |
| Known-answer / source / changed-input validation | Partial | Existing labs support sensitivity checks. Create the final locked changed-input record with pre-run human prediction, commit, units, result, decision effect, and diagnosis. |
| Cold run and highest-risk failure test | Missing | Run the README-only clean-environment test; preserve first failure, elapsed time, repair/limitation, and highest-risk test. |
| README, environment, visible output | Partial | `README.md`, `requirements.txt`, `.env.example`, `analysis.py`, and generated `visible_output.json` exist; complete the final model and clean-environment cold run. |
| Validation and AI-use record | Partial | Working `docs/validation-and-ai-use.md` exists; freeze a matching `Validation-and-AI-Use.pdf` at final submission. |
| Decision memo/deck | Partial | Working `docs/decision-memo.md` exists; finalize a ≤2-page PDF memo or ≤8-main-slide deck. |
| Videos and transcripts | Missing | Record Video 1 ≤3:00, Video 2 ≤5:00, Video 3 ≤5:00. Video 3 must begin with the live product demo. Correct and submit all transcripts. |
| Submission manifest / access | Missing | Complete all 12 manifest rows, use stable links, verify instructional-team repository/video access, and run the supplied manifest audit. |

## Non-negotiable final package

The final Project 1 package must include the unchanged Edition A plus Edition B, accessible repository and visible executed output, decision memo/deck, frozen validation-and-AI-use PDF, three bounded videos with transcripts, and the 12-row manifest. The repository must also retain content-equivalent `docs/` files and must not contain credentials or private data.

## Priority order

1. Rebuild the model around an articulating three-statement forecast that produces FCFF.
2. Source/reconcile the FCFF starting point, WACC, enterprise-to-equity bridge, normalizations, and peer policy.
3. Build the semi-adjustable interface and the validation/cold-run evidence.
4. Produce the memo/deck, final research-evolution PDF, validation PDF, videos/transcripts, and manifest.
