# Section B routing baseline

Frozen: 2026-08-30 (Asia/Hong_Kong)

Repository commit at freeze: `cf9e9ab3451e096f77906c4a0b9088c4703334a3`

The byte-for-byte snapshots are in `routing-tests/baseline/operational/`. The live
Section B workflow at freeze time was `AGENTS.md` -> `CLAUDE.md` -> `Content.md` and
`section-b.md`. `content-test.md` existed as an untracked additive test index but was
not connected to the live workflow. It is frozen separately so later work cannot
silently rewrite its starting point. `Syllabus.md` is included as the existing
secondary routing aid.

## SHA-256 hashes

| Frozen file | SHA-256 |
|---|---|
| `AGENTS.md` | `1cc89f60975b14f2708386cb9937272b3ad2131b43c7b605c0b29e2243fa7f46` |
| `CLAUDE.md` | `511e564e9f6f3c40be76582ccfe2f2ee24beae00aac2dbc8d7ab2386ec74aa58` |
| `Content.md` | `24b08234f7a29266d6d199d5f5bc8c721253f4b23a53757fc370473bd677416b` |
| `section-b.md` | `2f80861e1fd8f23dfa50b181216c4eb96899aefdc01213884ab409df51473d75` |
| `Syllabus.md` | `6d6b24a63f8e08203660b90b675a6405060d144dc59046672b2d906184a3a519` |
| `content-test.md` | `c90286879ff00772590811bf794840c693c4a55caef6da0ebd40d7d301fd4e7b` |
| Specimen Paper 1 PDF | `06dc9ab27f0bad1ffad543f84ee645a0af07aa0095075ff43b5cba90d7c11f66` |
| Specimen Paper 1 KAP PDF | `c753d14298f585f2d434a64676ba986df306cb527283fd7720dd65ede32392c2` |

The hashes of every operational snapshot were recomputed after copying and matched
the corresponding live file exactly.

## Pre-existing worktree state

The following entries pre-dated this routing task and are outside its edit scope:

- modified `../../.DS_Store`
- modified `../../Materials/.DS_Store`
- untracked `../.DS_Store`
- untracked `../../Markdown/.DS_Store`
- untracked `../../Past Papers/.DS_Store`

The following task-adjacent entries also pre-dated the freeze and are preserved:

- untracked `content-test.md`
- untracked `tmp/`, containing `tmp/pdfs/specimen-q2-page3.png`

No pre-existing file was deleted, renamed, reverted or committed during the freeze.

## Baseline-agent boundary

The blind Baseline Agent must use only the frozen live workflow files, the specimen
question paper (including examination Appendix 1), and the course materials. It must
not open `content-test.md`, any candidate routing prompt, any gold route, any other
agent output, the KAP, or the existing `Past Papers/.../Answers/` files.
