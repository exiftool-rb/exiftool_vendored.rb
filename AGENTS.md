# AGENTS.md

## Project Overview

- **Project:** exiftool_vendored — a vendored version of Phil Harvey's excellent [exiftool](http://www.sno.phy.queensu.ca/~phil/exiftool) library, and
- a dependency on the [exiftool](https://github.com/exiftool-rb/exiftool.rb) rubygem
- **Target user:** developers
- **My skill level:** intermediate
- **Stack:** Ruby

## Commands

- **Install:** `bundle install`
- **Build:** `bundle exec rake build`
- **Test:** `bundle exec rake test`
- **Lint:** `bundle exec rake rubocop`

## Do

- Read existing code before modifying anything
- Match existing patterns, naming, and style
- Handle errors gracefully — no silent failures
- Keep changes small and scoped to what was asked
- Ask clarifying questions before guessing

## Don't

- Install new dependencies without asking
- Delete or overwrite files without confirming
- Hardcode secrets, API keys, or credentials
- Rewrite working code unless explicitly asked
- Push, deploy, or force-push without permission
- Make changes outside the scope of the request

## When Stuck

- If a task is large, break it into steps and confirm the plan first
- If you can't fix an error in 2 attempts, stop and explain the issue

## Testing

- Run existing tests after any change
- Run lint after any change
- Add at least one test for new features
- Never skip or delete tests to make things pass

## Git

- Small, focused commits with descriptive messages
- Never force push

## Response Style

- always respond with clear & concise messages
- use plain English when explaining to the User
- avoid long sentences, complex words, or long paragraphs
