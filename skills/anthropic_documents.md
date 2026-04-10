---
name: "Anthropic Documents Expert"
description: "Rules for parsing and extracting knowledge from DOCX, PDF, PPTX, and XLSX."
---

# Precision Extraction
1. **XLSX Logic:** Always process wide spreadsheets by streaming rows instead of loading an entire massive matrix into context. Evaluate column data types stringently before outputting schemas.
2. **PPTX Analysis:** Do not hallucinate chart data. If parsing images or slides within a PPTX, declare explicitly standard structural points (Slide 1: Title, Slide 2: Bullet points).
3. **PDF OCR:** Treat raw PDF text extraction as potentially prone to bad spacing. Never match exact string comparisons across multi-line breaks. Use regex `/[\s\S]*/` matching cautiously.

# Document Editing
- When co-authoring or restructuring, maintain the exact tone of the input document explicitly unless specified to rewrite. 
- Return final edits as clean Markdown mapping strictly to Word Headers (H1, H2, H3).

---
⚡ Smart AI Skills Library | v2.2.7 | Active
