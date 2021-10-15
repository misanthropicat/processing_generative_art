---
name: Release template
about: Used by release workflow
title: "[RELEASE]"
labels: ''
assignees: ''

---

## Issue title

Issue {{ payload.repository.full_name }}/{{ payload.issue.number }}
Release {{ payload.ref }}

## Issue statement

Release CSI version {{ payload.ref }}
