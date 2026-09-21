# Explainability Contract: CodeMedic

## Decision

CodeMedic decides whether readable source contains defined debug-output patterns. When a match is detected, it reports the evidence and recommends replacing or removing the debug output.

## Inputs

It uses source text collected by the scanner and checks for console.log or debug-style print patterns. The decision comes from explicit pattern rules.

## Limits

It does not perform full static analysis or judge overall code quality. Legitimate logging and unusual debug mechanisms may be reported or missed depending on their syntax.
