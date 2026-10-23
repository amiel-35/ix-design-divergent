---
name: design-divergent
description: Makes a creative brief truly diverge (screen, visual identity, motion film, visual). Strips the brief of any solution already drawn into it, proposes orthogonal aesthetic mandates for the user to pick, runs 3 Sonnet variants plus one rupture variant, blind, each after writing down and then discarding its default proposal. Opus then composes a direction from the pieces. Use on "/design-divergent", "make it diverge", "I want really different directions", "give me design options", "fais diverger", "propose-moi des pistes de design", or whenever design proposals all look alike.
---

# Design divergent

This skill gets design proposals that are really different from one another,
then composes a direction from the best pieces. It rests on five real runs,
described in `docs/en/cases.md`. Talk to the user in their language.

If a `local.md` file sits next to this `SKILL.md`, read it first: it holds the
user's own hard constraints and conventions, and they override the defaults
below.

## What to know before starting

- **Variance comes from the brief, not from the model.** Three models given
  the same brief return almost the same thing. One model given four briefs
  returns four different things. Do not count on temperature, on the number of
  attempts, or on switching models.
- **Naming an artefact means the design is already decided.** "A compass
  rose", "a map", "a table" are answers, not needs.
- **A cited reference becomes a target.** An "inspiration" mentioned in
  passing is treated as a specification.
- **Asking for boldness produces nothing.** What works: have the model write
  its default proposal, then forbid it.
- **A ban moves convergence, it does not remove it.** It gets you out of a
  rut, it does not create diversity.
- **To diverge, mandates must be orthogonal, not opposite.** A "do the
  opposite" mandate produces a manufactured disagreement that teaches nothing.

## Cost

About 12 minutes and 185,000 tokens per variant (measured on one run), so
roughly 750,000 tokens for four variants, not counting the composition.
Announce it before step 2. This skill is for deliverables that matter, not
for a touch-up.

## Steps

### Step 0 · Clean the brief

From the user's request and the project's context:

1. **Write the use, not the artefact**: who, in what situation, what they
   want to know or feel, in how much time, and how success is judged. The
   model to follow: "he is in his cycling shorts in the hallway, he has three
   seconds and a thumb, he wants to know which way to ride".
2. **Run the noun test**: list every interface object or form noun (map,
   list, table, rose, badge, tab, banner, chart, slider, timeline, matrix).
   Classify each as a **real constraint** (keep it, with its reason) or a
   **decision taken without noticing** (remove it and replace it with the need
   it served).
3. **Remove the references** you do not want copied.
4. **Separate hard constraints from taste.** Examples of hard constraints:
   design system, motion guidelines, brand rules, accessibility, duration,
   format, signature line. If the project has a design system, it is a hard
   constraint: the idea, the composition and the motion diverge, never the
   palette or the type. Do not let a third-party skill generate a design
   system of its own on top of the project's.
5. Carry over the **inherited bans** from previous rounds if any exist (the
   `bans.md` file of the divergence folder). They go into the hard
   constraints. They do not claim to create diversity.

Show the user the cleaned brief and the list of removed nouns, with the
reason for each removal.

### Step 1 · Propose the mandates

1. First write, for yourself, the mandate you would propose by default. Record
   it in one line, under the heading "default mandate, discarded".
2. Propose **6 to 8 orthogonal mandates**: aesthetic stances or points of
   view (for example "Swiss editorial", "mainstream sports", "Japanese
   emptiness"), never objects to draw. No two mandates may be the same one
   with a different setting, nor the opposite of each other.
3. For each, give one line: what it looks at that the others do not.
4. Also propose **one rupture mandate**, which breaks the category of the
   deliverable (example: a screen that is not one, a film with no text).

**Mandatory stop.** The user picks 3 mandates plus the rupture. They may
rewrite one. Then announce the cost and wait for their go-ahead.

### Step 2 · Produce blind

Create the divergence folder in the current project, where the project keeps
its drafts (default: `docs/drafts/divergence-<slug>/`). One subfolder per
variant, `variant-<n>-<mandate>/`.

Launch **4 Agent calls in parallel in a single message**, with
`model: "sonnet"` and `subagent_type: "general-purpose"`. In a code
repository where the variant touches code, add `isolation: "worktree"`.

Each agent receives the cleaned brief, the hard constraints, **its own
mandate only**, and the path of its folder. It receives neither the other
mandates, nor the other variants, nor the existing version of the deliverable
if there is one.

Variant prompt template (write it in the user's language):

```
You are producing a design proposal. You work alone: you read nothing in
docs/drafts/divergence-<slug>/ outside your own folder, and no existing
version of the deliverable.

THE NEED
<cleaned brief>

HARD CONSTRAINTS (non-negotiable)
<constraints, files to read: design system, motion guidelines, brand rules,
bans.md>

YOUR MANDATE
<the mandate, and what it looks at that the others do not>

BEFORE PRODUCING
Write in <folder>/default.md the proposal you would make by default on this
need, without a mandate: form, palette, type, composition, in ten lines at
most. Then do not make it. Your proposal must resemble that default neither
in its form nor in its composition.

WHAT YOU DELIVER in <folder>/
- the piece itself, in a form the user can look at: an HTML page that opens,
  or for motion the MP4 and a contact sheet of 8 frames;
- default.md;
- stance.md: your stance in one sentence, then what your proposal does with
  the need in five lines at most.
Check your piece on screen yourself before handing it in (overflow,
contrast, legibility).

YOUR FINAL ANSWER: only the file paths and your stance in one sentence. Do
not copy the content.
```

### Step 3 · Read the defaults

While you wait or as soon as they come back, put the four `default.md` side
by side and write in `<folder>/attractor.md`:

- what the defaults have in common, that is, where the model lands on its own
  on this brief;
- for each variant, whether it resembles another one's default (if so, it did
  not diverge, and say so).

### Step 4 · Compose

Launch **one Agent call** with `model: "opus"` and
`subagent_type: "general-purpose"`. It receives the path of the divergence
folder, the cleaned brief and the hard constraints. Its job is not to name a
winner but to compose a direction:

```
Read the four variants in <folder> (pieces, stance.md) and attractor.md. Do
not name a winner: compose a direction.

1. Fill <folder>/composition.md with this table:
   | what we take | from which variant | what we refuse to take from it |
2. State the rules of the composed direction (three at most), each with its
   reason.
3. Check the composition against each hard constraint, one line per
   constraint: held or not, and why.
4. Point out what appears in several variants without having been asked for.
   It is often the element most specific to the product.
5. If the composition can be shown, produce it in <folder>/composition/.

Your final answer: the paths, and in three lines what the composed direction
takes from whom.
```

### Step 5 · The user decides

Show them the four variants (open the pages or send the files), the
attractor and the composition. **Their taste decides**, on visible pieces.
There is no scoring between models. Keeping a single variant as it is, or the
version that existed before the divergence, is a valid outcome.

### Step 6 · Keep the trail

In the divergence folder:

- `direction.md`: the chosen direction, its rules and the validated
  composition table;
- `bans.md`: add each of the user's rejections **with their verdict word for
  word**;
- the variants stay where they are: they were used to compose the direction.

Nothing is applied to the real deliverable without the user asking for it.

## What we do not know yet

See `docs/en/open-questions.md`. In short: one run per cell, two variables
changed at once in the founding test, and in the two most recent runs the
user kept one piece as it was rather than the composition.
