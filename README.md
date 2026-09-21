# CodeMedic

> Portable agent for identifying obvious debug-output patterns in source code.

## What it does

CodeMedic scans project source for recognizable debug-print patterns such as `console.log(...)` and debug-style Python prints. It converts those observations into a focused maintainability recommendation.

### Diagnostic fingerprint

**Source pattern → maintainability signal → evidence → cleanup action**

## Why this agent is distinct

CodeMedic is intentionally not a full static-analysis platform. It focuses on one easy-to-understand signal that often survives into production code and makes the project's intent harder to read.

## Workflow

```text
Source files
    ↓
Pattern scanner
    ↓
Debug-output rule
    ↓
Observed evidence
    ↓
Cleanup recommendation
```

## Verification

This repository includes:
- OpenGAP passport metadata
- code-quality fixture data
- explainability and duty contracts
- four framework adapters
- automated verification

OpenGAP validation passed and all four framework exports have been exercised successfully.

## Design principle

**Keep findings concrete.** CodeMedic reports the pattern it can actually see rather than claiming a broad quality score for the entire codebase.

## Medic family

CodeMedic is a focused source-quality agent within a portable family designed around composable diagnostic responsibilities.