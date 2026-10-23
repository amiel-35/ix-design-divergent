# design-divergent

<p>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-MIT-8f8a7c"></a>
  <img alt="Claude Code" src="https://img.shields.io/badge/Claude%20Code-skill-D97757">
  <img alt="Status" src="https://img.shields.io/badge/status-experimental-e07a3f">
  <a href="README.fr.md"><b>Français</b></a>
</p>

A Claude Code skill to get design proposals that are **really** different,
then decide on visible pieces.

Ask three models for a screen and you get the same screen three times. Ask for
"something bold" and you get the same screen with a gradient. The problem is
not the model: it is the brief. This skill works on the brief.

## What it does

1. **Cleans the brief.** Writes the use instead of the artefact ("three
   seconds and a thumb", not "a dashboard"), runs a noun test to remove the
   design decisions hidden in the request, drops references that would be
   copied, separates hard constraints from taste.
2. **Proposes orthogonal mandates.** Six to eight aesthetic stances, never
   objects to draw, plus one rupture that breaks the category. You pick three
   plus the rupture.
3. **Produces blind.** Four Sonnet agents in parallel, each with its own
   mandate only. Each one first writes the proposal it would make by default,
   then is forbidden to make it.
4. **Reads the defaults.** Side by side, the discarded defaults show the
   *attractor*: what bland looks like on this brief.
5. **You decide**, on visible pieces. Keeping one variant as it is is a
   valid outcome.
6. **Composes, if you ask.** A Sonnet agent proposes a direction made of
   pieces taken from several variants, and says what it refuses to take from
   each. Your rejections are kept word for word as bans for the next round.

## Install

```bash
git clone https://github.com/amiel-35/ix-design-divergent ~/.claude/skills/design-divergent
```

Then, in Claude Code: `/design-divergent` followed by your request, or just
"make it diverge" when proposals all look alike.

Optional: copy `local.example.md` to `local.md` for your own hard constraints
(design system, tools you never want used). `local.md` is ignored by git.

## Cost

About 12 minutes and 185,000 tokens per variant on the one run where it was
measured, so roughly 750,000 tokens for a full round. Use it for deliverables
that matter, not for a touch-up.

## Documentation

- [What we know](docs/en/method.md): ten findings, each with the case it comes
  from.
- [The five cases](docs/en/cases.md): real runs, anonymised.
- [What we do not know yet](docs/en/open-questions.md), including why the
  composition became optional.

## License

MIT.
