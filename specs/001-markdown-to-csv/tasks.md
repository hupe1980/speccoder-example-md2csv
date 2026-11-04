---
description: "Task list for Markdown to CSV CLI"
---

# Tasks: Markdown to CSV CLI

**Input**: Design documents from `/specs/001-markdown-to-csv/`

**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Evidence (speccoder)**: each story's acceptance tests are written by speccoder from the story's acceptance scenarios before its tasks run; a task is verified when it turns some of them from failing to passing.

**Who does it (speccoder)**: every task is code for the implementer unless it says otherwise.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [X] T001 Confirm package layout and entrypoint targets in `pyproject.toml` and `src/md2csv/`
- [X] T002 Review existing feature decisions in `specs/001-markdown-to-csv/research.md` and align task scope to them

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [X] T003 Create the CLI parsing and command dispatch skeleton in `src/md2csv/__init__.py` and `src/md2csv/__main__.py`
- [X] T004 Create shared Markdown table parsing and CSV emission helpers in `src/md2csv/parser.py` and `src/md2csv/csv_writer.py`
- [X] T005 Define shared error types and exit handling for invalid input in `src/md2csv/errors.py`

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Convert a table from standard input (Priority: P1) 🎯 MVP

**Goal**: A user pipes Markdown table text into the CLI and receives equivalent CSV output.

**Independent Test**: Pipe a valid Markdown table into `md2csv` with no file argument and verify stdout contains the expected CSV rows in the same order.

### Implementation for User Story 1

- [X] T006 [P] [US1] Add stdin reading and command-line default input handling in `src/md2csv/cli.py` (scenarios US1-1, US1-2)
- [X] T007 [US1] Implement conversion of one Markdown table from stdin to CSV using the shared helpers in `src/md2csv/parser.py` and `src/md2csv/csv_writer.py` (scenarios US1-1, US1-2)
- [X] T008 [US1] Wire CLI output and user-facing success/error messages for stdin conversion in `src/md2csv/__main__.py` and `src/md2csv/errors.py` (scenarios US1-1, US1-2)

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - Convert a table from a file (Priority: P2)

**Goal**: A user passes a Markdown file path and receives CSV output for the table content it contains.

**Independent Test**: Run the CLI against a sample Markdown file and verify it emits CSV for the table found in that file, or a clear no-table message when none exists.

### Implementation for User Story 2

- [X] T009 [P] [US2] Add file path argument parsing and file loading in `src/md2csv/cli.py` (scenarios US2-1, US2-2)
- [X] T010 [US2] Extend table discovery to read Markdown content from files and report missing tables in `src/md2csv/parser.py` (scenarios US2-1, US2-2)
- [X] T011 [US2] Route file-based conversion through the same CSV output path in `src/md2csv/__main__.py` and `src/md2csv/csv_writer.py` (scenarios US2-1, US2-2)

**Checkpoint**: At this point, User Story 1 and User Story 2 should both work independently

---

## Phase 5: User Story 3 - Handle common table formatting issues (Priority: P3)

**Goal**: Markdown tables with spacing noise, empty cells, or escaped pipe characters still convert to usable CSV.

**Independent Test**: Convert sample tables that include uneven spacing, empty cells, and escaped pipes, and verify the CSV preserves intended values and column counts.

### Implementation for User Story 3

- [X] T012 [P] [US3] Add normalization for spacing noise and empty cells in `src/md2csv/parser.py` (scenarios US3-1, US3-2)
- [X] T013 [P] [US3] Add escaped pipe handling and CSV-safe escaping for commas, quotes, and line breaks in `src/md2csv/csv_writer.py` (scenarios US3-1, US3-2)
- [X] T014 [US3] Add table-shape validation and malformed-table errors in `src/md2csv/errors.py` and `src/md2csv/parser.py` (scenarios US3-1, US3-2)

**Checkpoint**: All user stories should now be independently functional

---

## Phase 6: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [X] T015 [P] Validate CLI behavior against `specs/001-markdown-to-csv/quickstart.md`
- [X] T016 Clean up module exports and documentation comments in `src/md2csv/__init__.py` and `src/md2csv/cli.py`
- [ ] T017 Run the full pytest suite using `uv run --locked --offline python -m pytest -q --junitxml=.speccoder/junit.xml`

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable

### Within Each User Story

- speccoder writes the story's acceptance tests first; they fail before the story's tasks and pass after
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- Setup tasks T002 can run in parallel with T001 if review scope is independent
- Foundational tasks T003-T005 can be worked in parallel after T001-T002
- US1 tasks T006 can start in parallel with other story tasks once foundation is ready; T007 depends on T006
- US2 tasks T009 can start in parallel with US1 completion if desired; T010-T011 depend on T009
- US3 tasks T012-T013 can run in parallel; T014 depends on both

---

## Parallel Example: User Story 1

```bash
Task: "Add stdin reading and command-line default input handling in `src/md2csv/cli.py`"
Task: "Implement conversion of one Markdown table from stdin to CSV using the shared helpers in `src/md2csv/parser.py` and `src/md2csv/csv_writer.py`"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- speccoder verifies each story's acceptance tests fail before its tasks and pass after
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence
