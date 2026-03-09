# Resume Project — Conversation Summary for Claude Code

## Owner
Iaroslav "Rick" Postovalov, 21, compiler/JVM developer based in Hannover, Germany. EU Blue Card holder.

## What this is
A Python script (`resume.py`) using ReportLab to generate a 2-page A4 PDF resume targeting **compiler engineer / JVM / blockchain / performance optimization** roles.

## How to run
```bash
pip install reportlab
python resume.py
# Outputs: resume.pdf in the same directory
```

## Key design decisions made during conversation

### Voice & style
- **Shipilëv-style**: Plain, human voice. No corporate action verbs ("Engineered", "Overhauled", "Spearheaded", "Leveraged" are all banned). Just direct statements of what was done.
- **No AI slop**. No excessive bold. No emojis. Conservative formatting appropriate for compiler engineering hiring.
- Font sizes were bumped ~1pt from initial values for readability.

### Factual corrections applied
- Rick was on JetBrains Kotlin/JVM team from **age 17**, not 18
- He is **not** a "core contributor" to Kotlin — he was a team member who shipped real work
- Rell is an **interpreted** language (tree-walk interpreter with SQL generation), NOT compiled
- The arXiv paper is a **preprint**, not a peer-reviewed publication (SEIM submission was rejected)
- NTO result was **2nd degree** (prizewinner), not winner — verified from nkj.ru coverage
- KMath has **700+ stars** (verified from GitHub, was showing ~657 on releases page)
- The "5 citations" claim was from Nozik's separate paper, not Rick's — removed
- SSA, dead code elimination, escape analysis — removed from skills (not hands-on)
- Constant folding, inlining, GraalVM — kept (confirmed hands-on)
- Education: **BSc Applied Computer Science**, not just "Computer Science"
- Constructor University graduation: **Aug 2027**

### Content sources used
- Original resume PDF (Jan 2026)
- LinkedIn profile (scraped via web search) — detailed bullet points, recommendations, lab context
- arXiv paper + Semantic Scholar + ResearchGate — paper details, ORCID, affiliations
- Medium blog post — ObjectWeb ASM implementation details
- GitHub profile — README bio with accomplishments list
- Chromia docs — platform context
- Personal site (commandertvis.github.io) — ITMM-2020 publication, school contests, Ashborn advisory
- nkj.ru article — NTO prizewinner verification
- YouTube — SnowOne 2022 talk confirmation
- GitLab CI pipeline data — JUnit 5 migration metrics (695s → 405s, ~42%)
- Compiler job postings (Apple, AMD, Meta, Qualcomm, MathWorks, LLVM Dev Meeting) — ATS keywords

### Structure
1. **Header**: Name, location, email, LinkedIn, GitHub, personal site
2. **Summary**: Age-forward (21 years old, JetBrains from 17), sole maintainer signal
3. **Languages/Legal**: Native Russian, fluent English, EU Blue Card
4. **Experience** (5 entries):
   - ChromaWay (full-time, concurrent with online education) — Rell language maintainer
   - JetBrains Kotlin Team (part-time, concurrent with full-time education) — K2 transition
   - MiLaboratories (SF-based biotech startup, intern) — 2 months
   - JetBrains Research — KMath, expression compiler, kmath-gsl
   - Lavrentiev Lyceum — Monte Carlo system with DSL, C++ interpreters, REST API
5. **Technical Skills** (6 categories, ATS-optimized for compiler roles):
   - Languages, Compiler Design, JVM & Runtime, Performance & Quality, Tools & Infrastructure, Domain
6. **Education**: Constructor University (BSc Applied CS), Lomonosov MSU Yerevan branch
7. **Publications & Honors**: arXiv preprint, ITMM-2020 paper, SnowOne talk, NTO 2nd degree, TWB volunteering

### Things explicitly excluded by Rick's request
- University activities (Tea Club, Bouldering Club)
- ORCID number
- "Open Source" as a separate line (star count moved to job bullet)
- Blog post link
- YouTube link (talk was in Russian)
- Elementary German (removed from languages)
- Seconds in CI metrics
- Line count in docs bullet

### ATS keywords present (verified against 2026 job postings)
Compiler Design, Language Design, IR, Code Generation, Instruction Selection, JIT, Parsing, ANTLR, Semantic Analysis, Type Inference, Bytecode Generation, ASM Framework, Constant Folding, Inlining, JVM, Invokedynamic, Boxing/Unboxing, Inline/Value Classes, JNI/FFI, GraalVM, Memory Management, JMH, Profiling, Performance Regression Analysis, Test Automation, Code Review, REST APIs, CI/CD, GitLab CI, Gradle, Docker, JUnit 5, PostgreSQL, Kotlin Multiplatform, Open Source, SQL Codegen, Blockchain Smart Contract Compilers, AI-assisted Development, Scientific Computing, Automatic Differentiation

### What could still be added (discussed but not included)
- More school contests from the personal site (Vysshaya Proba, Future of Siberia chemistry olympiads)
- Ashborn advisory role
- Conference talk at age 11
- Specific LLM/AI keywords if applying to AI-adjacent roles
