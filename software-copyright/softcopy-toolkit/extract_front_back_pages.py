#!/usr/bin/env python3
"""Extract the first N and last M pages from a PDF without duplicating overlap."""

from __future__ import annotations

import argparse
from pathlib import Path

from pypdf import PdfReader, PdfWriter


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Extract front/back pages from a PDF while keeping cover/TOC at the beginning."
    )
    parser.add_argument("input_pdf", type=Path, help="Input PDF")
    parser.add_argument("output_pdf", type=Path, nargs="?", help="Output PDF")
    parser.add_argument("--front-pages", type=int, default=30, help="Pages kept from the start")
    parser.add_argument("--back-pages", type=int, default=30, help="Pages kept from the end")
    args = parser.parse_args()

    input_pdf = args.input_pdf
    if not input_pdf.exists():
        raise SystemExit(f"Input PDF not found: {input_pdf}")

    output_pdf = args.output_pdf
    if output_pdf is None:
        output_pdf = input_pdf.with_name(
            f"{input_pdf.stem}_front{args.front_pages}_back{args.back_pages}{input_pdf.suffix}"
        )

    reader = PdfReader(str(input_pdf))
    total_pages = len(reader.pages)
    front_end = min(max(args.front_pages, 0), total_pages)
    back_start = max(total_pages - max(args.back_pages, 0) + 1, 1)

    pages = list(range(1, front_end + 1))
    pages.extend(range(max(back_start, front_end + 1), total_pages + 1))

    if not pages:
        raise SystemExit("No pages selected")

    writer = PdfWriter()
    for page in pages:
        writer.add_page(reader.pages[page - 1])

    with output_pdf.open("wb") as handle:
        writer.write(handle)

    output_pages = len(writer.pages)
    print(f"Input PDF: {input_pdf}")
    print(f"Total pages: {total_pages}")
    print(f"Extracted pages: {output_pages}")
    print(f"Output PDF: {output_pdf}")


if __name__ == "__main__":
    main()
