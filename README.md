# StegVerse Patents Repo — StegPatent-AI-001 (v1)

This repo bootstraps an autonomous Patent AI Entity for StegVerse.

## What it does (v1)
- Watches StegVerse org repos for patentable changes
- Creates invention disclosure stubs
- Generates provisional draft skeletons
- Produces claims tiers (broad → narrow)
- Tracks deadlines for provisional → non-provisional
- Maintains a central patent manifest for portfolio management

## Quick start (iPhone-friendly)
1. Create repo: `StegVerse/Patents`
2. Upload this bundle to the repo root and commit to `main`.
3. Add org/repo secrets:
   - `GH_STEGVERSE_PATENT_AI_TOKEN` (fine-grained PAT)
     - Org access: StegVerse + StegVerse-Labs
     - Permissions: Contents Read/Write, Pull Requests Read/Write, Actions Read
   - `OPENAI_API_KEY` (optional for richer drafting; v1 runs without)
4. Go to Actions → **Patent Watcher** → Run workflow (dry-run default).
5. Review generated disclosures in `/disclosures` and drafts in `/provisionals`.

## Safety rules
- v1 never files automatically with USPTO.
- v1 generates drafts + claims + diagrams for human/legal review.
- v1 will not publish anything outside this repo.
- v1 uses allowlists for target repos and file paths.

## Versioning
Repo epoch + version live in `patent_manifest.json`.
