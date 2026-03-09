#!/usr/bin/env python3
# /// script
# requires-python = ">=3.12"
# dependencies = ["reportlab"]
# ///
"""Generate an ATS-optimized resume PDF for Iaroslav Postovalov.

Enriched from: LinkedIn, GitHub, arXiv paper, Medium blog post,
Semantic Scholar, Chromia docs, and compiler job keyword research.
"""

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import (
    HRFlowable,
    KeepTogether,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

# ── Colors ──────────────────────────────────────────────────────────────
DARK = HexColor("#1a1a2e")
GRAY = HexColor("#555555")
RULE = HexColor("#bbbbbb")
LINK = "#1565c0"

# ── Styles ──────────────────────────────────────────────────────────────
s_name = ParagraphStyle(
    "Name",
    fontSize=22,
    fontName="Helvetica-Bold",
    textColor=DARK,
    spaceAfter=2,
    leading=26,
)

s_contact = ParagraphStyle(
    "Contact",
    fontSize=9,
    fontName="Helvetica",
    textColor=GRAY,
    spaceAfter=1,
    leading=12,
)

s_summary = ParagraphStyle(
    "Summary",
    fontSize=10,
    fontName="Helvetica",
    textColor=DARK,
    leading=14,
    spaceAfter=2,
    alignment=TA_JUSTIFY,
)

s_section = ParagraphStyle(
    "Section",
    fontSize=11,
    fontName="Helvetica-Bold",
    textColor=DARK,
    spaceBefore=7,
    spaceAfter=3,
    leading=14,
)

s_job = ParagraphStyle(
    "Job",
    fontSize=10,
    fontName="Helvetica-Bold",
    textColor=DARK,
    spaceBefore=5,
    spaceAfter=0,
    leading=13,
)

s_meta = ParagraphStyle(
    "Meta", fontSize=9, fontName="Helvetica", textColor=GRAY, spaceAfter=2, leading=12
)

s_bullet = ParagraphStyle(
    "Bullet",
    fontSize=9.5,
    fontName="Helvetica",
    textColor=DARK,
    leading=13,
    leftIndent=10,
    spaceAfter=1.5,
    bulletIndent=0,
    alignment=TA_JUSTIFY,
)

s_small = ParagraphStyle(
    "Small", fontSize=9, fontName="Helvetica", textColor=DARK, leading=12, spaceAfter=1
)

s_edu = ParagraphStyle(
    "Edu",
    fontSize=10,
    fontName="Helvetica-Bold",
    textColor=DARK,
    spaceBefore=4,
    spaceAfter=0,
    leading=13,
)

s_edu_meta = ParagraphStyle(
    "EduMeta",
    fontSize=9,
    fontName="Helvetica",
    textColor=GRAY,
    spaceAfter=1,
    leading=12,
)


def B(text):
    return Paragraph(f"<bullet>&bull;</bullet> {text}", s_bullet)


def rule():
    return HRFlowable(
        width="100%", thickness=0.5, color=RULE, spaceBefore=1, spaceAfter=4
    )


def lnk(url, label=None):
    return f'<a href="{url}" color="{LINK}">{label or url}</a>'


def build():
    doc = SimpleDocTemplate(
        "resume.pdf",
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=14 * mm,
        bottomMargin=12 * mm,
    )

    story = []

    # ═══════════════════════════════════════════════════════════════════
    # HEADER
    # ═══════════════════════════════════════════════════════════════════
    story.append(Paragraph("Iaroslav Postovalov", s_name))
    story.append(
        Paragraph(
            f"Hannover, Germany &nbsp;&middot;&nbsp; "
            f"{lnk('mailto:postovalovya@gmail.com', 'postovalovya@gmail.com')} &nbsp;&middot;&nbsp; "
            f"{lnk('https://linkedin.com/in/iaroslav-postovalov', 'linkedin.com/in/iaroslav-postovalov')} &nbsp;&middot;&nbsp; "
            f"{lnk('https://github.com/commandertvis', 'github.com/commandertvis')} &nbsp;&middot;&nbsp; "
            f"{lnk('https://commandertvis.github.io', 'commandertvis.github.io')}",
            s_contact,
        )
    )
    story.append(Spacer(1, 3))

    # ═══════════════════════════════════════════════════════════════════
    # SUMMARY — ATS keyword-packed
    # ═══════════════════════════════════════════════════════════════════
    story.append(
        Paragraph(
            "Compiler and JVM developer, 21 years old. "
            "Sole maintainer of a production blockchain language (~156K LOC Kotlin). "
            "On the Kotlin/JVM compiler team at JetBrains from age 17, part-time through university: "
            "IR backend, bytecode optimizations, inline class interop. "
            "Published research on JIT compilation targeting JVM, JavaScript, and WebAssembly.",
            s_summary,
        )
    )
    story.append(
        Paragraph(
            "<b>Languages:</b> native Russian, fluent English &nbsp;&nbsp;&nbsp;"
            "<b>Legal status:</b> Russian citizenship, EU Blue Card (Germany)",
            s_small,
        )
    )

    # ═══════════════════════════════════════════════════════════════════
    # EXPERIENCE
    # ═══════════════════════════════════════════════════════════════════
    story.append(Paragraph("EXPERIENCE", s_section))
    story.append(rule())

    # ── ChromaWay ───────────────────────────────────────────────────
    story.append(
        KeepTogether(
            [
                Paragraph(
                    f"Software Engineer &mdash; ChromaWay ({lnk('https://chromaway.com/')})",
                    s_job,
                ),
                Paragraph(
                    "Remote &nbsp;&middot;&nbsp; Apr 2025 &ndash; Present &nbsp;&middot;&nbsp; Full-time (concurrent with online education)",
                    s_meta,
                ),
                B(
                    f"Sole maintainer of Rell ({lnk('https://gitlab.com/chromaway/rell')}), "
                    "the primary language for the Chromia relational blockchain. "
                    "Tree-walk interpreter with SQL generation, ~156K LOC Kotlin."
                ),
                B(
                    "New language features: struct.copy() for immutable updates, "
                    "try_call_catch with automatic database rollback and typed error results "
                    "(try_call_result&lt;T&gt;), @disabled test annotation."
                ),
                B(
                    "Migrated build from Maven to Gradle (~22% faster incremental builds). "
                    "Migrated tests from JUnit 4 to JUnit 5 with parallel execution, "
                    "cutting CI pipeline times by ~42%. "
                    "Refactored SQL connection and schema handling "
                    "to support parallelism and eliminate leaked connections."
                ),
                B(
                    "PostgreSQL backend work: query cancellation, migration tooling. "
                    "Resolved non-deterministic behaviors across platforms."
                ),
                B(
                    "Adopted Kotlin immutable collections throughout the codebase. "
                    "Refined the binary compatibility checker."
                ),
                B(
                    "Restructured and consolidated Rell language documentation, "
                    "merging fragmented pages and trimming verbose reference content."
                ),
            ]
        )
    )

    # ── JetBrains ──────────────────────────────────────────────────
    story.append(
        KeepTogether(
            [
                Paragraph("Software Developer &mdash; JetBrains (Kotlin Team)", s_job),
                Paragraph(
                    "Yerevan, then Bremen (Germany) &nbsp;&middot;&nbsp; Sep 2022 &ndash; Dec 2024 &nbsp;&middot;&nbsp; Part-time (concurrent with full-time education)",
                    s_meta,
                ),
                B(
                    "Kotlin/JVM compiler team, working through the K2 compiler transition. "
                    "IR backend, performance work, language features."
                ),
                B(
                    "Reduced memory allocations in compiler frontend and IR lowering passes. "
                    "Bytecode-level optimizations to reduce boxing conversions in generated code."
                ),
                B(
                    "Designed and implemented @JvmExposeBoxed annotation for seamless integration "
                    "of inline/value classes with Java callers."
                ),
                B(
                    "Migrated Android testing infrastructure to the official Android Gradle Plugin framework. "
                    "Participated in renovating compiler tests for the new K2 frontend, "
                    "including running test suites on Android platform."
                ),
                B(
                    "Fixed bugs in IR serialization and lazy declaration deserialization "
                    "that caused production compiler crashes."
                ),
            ]
        )
    )

    # ── MiLaboratories ─────────────────────────────────────────────
    story.append(
        KeepTogether(
            [
                Paragraph(
                    f"Software Developer (Intern) &mdash; MiLaboratories ({lnk('https://milaboratories.com')})",
                    s_job,
                ),
                Paragraph("Remote &nbsp;&middot;&nbsp; Jul &ndash; Aug 2022", s_meta),
                B(
                    "Kotlin DSL with statistical and serialization features "
                    "for an internal data plotting library (based on lets-plot-kotlin)."
                ),
            ]
        )
    )

    # ── JetBrains Research ─────────────────────────────────────────
    story.append(
        KeepTogether(
            [
                Paragraph(
                    "Researcher &mdash; JetBrains Research, Nuclear Physics Methods Lab",
                    s_job,
                ),
                Paragraph(
                    "Dolgoprudny (Russia), then Remote &nbsp;&middot;&nbsp; Sep 2020 &ndash; Apr 2022",
                    s_meta,
                ),
                B(
                    "The group's research covered non-accelerator particle physics, numerical simulations, "
                    "and software development for experimental physics."
                ),
                B(
                    f"Key developer of KMath ({lnk('https://github.com/SciProgCentre/kmath')}, 700+ stars), "
                    "a cross-platform mathematical library for Kotlin. "
                    "Contributed to the core design of the abstract algebra API, "
                    "which separates operations from data structures. "
                    "Added N-dimensional array support, automatic differentiation, "
                    "and integrations with math libraries (EJML, ND4J, Commons Math)."
                ),
                B(
                    "Cross-platform expression compiler targeting JVM bytecode (ObjectWeb ASM), "
                    "JavaScript, and WebAssembly from a single AST. "
                    "Boxing/unboxing optimization pass with bytecode type state tracking. "
                    f'Paper: <i>"Compilation of mathematical expressions in Kotlin"</i> '
                    f"({lnk('https://arxiv.org/abs/2102.07924', 'arXiv:2102.07924')})."
                ),
                B(
                    "kmath-gsl: Kotlin/Native bindings to the GNU Scientific Library "
                    "via C interop, implementing matrices and vectors. "
                    "Native build/toolchain setup, CI, documentation, performance benchmarking."
                ),
                B(
                    "KMath-to-LaTeX renderer for computable expressions in Jupyter notebooks."
                ),
            ]
        )
    )

    # ── Lavrentiev Lyceum ──────────────────────────────────────────
    story.append(
        KeepTogether(
            [
                Paragraph(
                    "Research Intern &mdash; Lab. Math. Modeling, Lavrentiev Lyceum No. 130",
                    s_job,
                ),
                Paragraph(
                    "Novosibirsk (Russia) &nbsp;&middot;&nbsp; Sep 2019 &ndash; Apr 2021",
                    s_meta,
                ),
                B(
                    "Interactive system for selecting and studying probability distributions "
                    "used in Monte Carlo methods."
                ),
                B(
                    "Custom DSL for defining formulas. C++ tree interpreter "
                    "and simple bytecode interpreter for performance research."
                ),
                B(
                    "HTTP server in Kotlin/Ktor exposing REST API "
                    "for plot generation, histogram computation, and function evaluation."
                ),
                B("Cross-platform bindings: Python via ctypes, Java/Kotlin via JNI."),
                B(
                    "Diploma at the 58th International Scientific Student Conference (MNSK-2020)."
                ),
            ]
        )
    )

    # ═══════════════════════════════════════════════════════════════════
    # TECHNICAL SKILLS — ATS keyword maximized
    # ═══════════════════════════════════════════════════════════════════
    story.append(Paragraph("TECHNICAL SKILLS", s_section))
    story.append(rule())

    skills = [
        ("Languages", "Kotlin (expert), Java, C, Python, C#, SQL"),
        (
            "Compiler Design",
            "Language design, lexical analysis, parsing (ANTLR), semantic analysis, type inference, "
            "IR design &amp; lowering, code generation, instruction selection, "
            "compiler optimization passes, JIT compilation, "
            "cross-platform compilation (JVM, JavaScript, WebAssembly), "
            "compiler testing (end-to-end)",
        ),
        (
            "JVM &amp; Runtime",
            "JVM bytecode generation (ASM framework), invokedynamic, "
            "boxing/unboxing optimization, inline/value classes, "
            "memory allocation profiling, memory management, "
            "class loading, JNI/FFI, GraalVM",
        ),
        (
            "Performance &amp; Quality",
            "Microbenchmarking (JMH), profiling, "
            "compiler backend optimization, "
            "constant folding, inlining, performance regression analysis, "
            "test automation, code review",
        ),
        (
            "Tools &amp; Infrastructure",
            "Git, Gradle, CI/CD (GitLab CI), PostgreSQL, Docker, REST APIs, "
            "JUnit 5, Linux, Kotlin Multiplatform, open source development",
        ),
        (
            "Domain",
            "Blockchain smart contract languages, SQL codegen, "
            "scientific computing, mathematical library design, "
            "automatic differentiation, AI-assisted development",
        ),
    ]

    for cat, val in skills:
        story.append(Paragraph(f"<b>{cat}:</b> &nbsp;{val}", s_small))

    # ═══════════════════════════════════════════════════════════════════
    # EDUCATION
    # ═══════════════════════════════════════════════════════════════════
    story.append(Paragraph("EDUCATION", s_section))
    story.append(rule())

    story.append(
        Paragraph("BSc Applied Computer Science &mdash; Constructor University", s_edu)
    )
    story.append(
        Paragraph(
            "Bremen, Germany &nbsp;&middot;&nbsp; Sep 2023 &ndash; Aug 2027", s_edu_meta
        )
    )

    story.append(Spacer(1, 2))
    story.append(
        Paragraph(
            "Applied Mathematics &amp; CS &mdash; Lomonosov Moscow State University, Yerevan Branch",
            s_edu,
        )
    )
    story.append(Paragraph("Sep 2022 &ndash; Jun 2023", s_edu_meta))

    # ═══════════════════════════════════════════════════════════════════
    # PUBLICATIONS & HONORS
    # ═══════════════════════════════════════════════════════════════════
    story.append(Paragraph("PUBLICATIONS &amp; HONORS", s_section))
    story.append(rule())

    story.append(
        Paragraph(
            f"<b>Preprint:</b> &nbsp;<i>Compilation of mathematical expressions in Kotlin</i> "
            f"&mdash; arXiv, Feb 2021 "
            f"({lnk('https://arxiv.org/abs/2102.07924', 'arXiv:2102.07924')}).",
            s_small,
        )
    )
    story.append(
        Paragraph(
            "<b>Paper:</b> &nbsp;<i>NMPUD: a computer system for sampling and examining "
            "probability distributions</i> &mdash; ITMM-2020 proceedings, Tomsk, 2021. "
            "Co-authored with Prof. A. Voytishek.",
            s_small,
        )
    )
    story.append(
        Paragraph(
            "<b>Talk:</b> &nbsp;<i>Dynamic compilation of mathematical expressions with Kotlin</i> "
            "&mdash; SnowOne 2022 (JUGNsk), Novosibirsk.",
            s_small,
        )
    )
    story.append(
        Paragraph(
            "<b>Winner, National Technology Olympiad</b> &mdash; "
            '"Automation of Business Processes" track (1C partner case). '
            "HSE University, Moscow &middot; Mar 2022",
            s_small,
        )
    )
    story.append(
        Paragraph(
            "<b>Volunteering:</b> &nbsp;Translator at Translators without Borders "
            "(Apr 2022 &ndash; Feb 2023, 11 months).",
            s_small,
        )
    )

    doc.build(story)
    print("Done: resume.pdf")


if __name__ == "__main__":
    build()
