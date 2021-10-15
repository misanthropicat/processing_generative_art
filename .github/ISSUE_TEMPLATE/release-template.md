---
name: Release template
about: Used by release workflow
title: "[RELEASE]"
labels: ''
assignees: ''

---

Release: {{ payload.release.tag_name }}
{{ payload.release.body }}