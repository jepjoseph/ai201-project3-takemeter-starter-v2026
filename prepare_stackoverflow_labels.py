
import csv
import html
import json
import re
from html.parser import HTMLParser
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCE = ROOT / "data" / "stackoverflow_200.json"
OUTPUT = ROOT / "labels.csv"
REVIEW = ROOT / "data" / "stackoverflow_labeling_review.csv"

FIELDNAMES = ["text", "label", "note"]


class QuestionHTMLParser(HTMLParser):
    """Convert Stack Overflow HTML to readable text without dropping code."""

    BLOCK_TAGS = {
        "p", "div", "pre", "blockquote", "ul", "ol",
        "li", "h1", "h2", "h3", "h4", "table", "tr"
    }

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.parts = []

    def handle_starttag(self, tag, attrs):
        if tag in self.BLOCK_TAGS or tag == "br":
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in self.BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        self.parts.append(data)

    def get_text(self):
        result = "".join(self.parts)
        result = result.replace("\xa0", " ")
        result = re.sub(r"\n{3,}", "\n\n", result)
        return result.strip()


def clean_html(value):
    parser = QuestionHTMLParser()
    parser.feed(value or "")
    parser.close()
    return html.unescape(parser.get_text())


def main():
    if not SOURCE.exists():
        raise FileNotFoundError(f"Missing source: {SOURCE}")

    with SOURCE.open("r", encoding="utf-8-sig") as file:
        questions = json.load(file)

    if isinstance(questions, dict):
        questions = questions.get("items", [])

    if not isinstance(questions, list):
        raise ValueError("Expected a list of Stack Overflow questions.")

    if OUTPUT.exists():
        raise FileExistsError(
            f"{OUTPUT} already exists. Review it before replacing it."
        )

    seen_ids = set()
    prepared = []
    review_rows = []

    for question in questions:
        question_id = question["question_id"]

        if question_id in seen_ids:
            raise ValueError(f"Duplicate question ID: {question_id}")

        seen_ids.add(question_id)

        title = clean_html(question.get("title", ""))
        body = clean_html(question.get("body", ""))

        if not title or not body:
            raise ValueError(
                f"Missing title or body for question {question_id}"
            )

        text = f"{title}\n\n{body}"

        prepared.append({
            "text": text,
            "label": "",
            "note": "",
        })

        review_rows.append({
            "question_id": question_id,
            "url": question.get(
                "link",
                f"https://stackoverflow.com/questions/{question_id}"
            ),
            "text": text,
            "label": "",
            "note": "",
        })

    REVIEW.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(prepared)

    with REVIEW.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=["question_id", "url", *FIELDNAMES]
        )
        writer.writeheader()
        writer.writerows(review_rows)

    print(f"Questions prepared: {len(prepared)}")
    print(f"Unique question IDs: {len(seen_ids)}")
    print(f"Dataset created: {OUTPUT}")
    print(f"Labeling review created: {REVIEW}")
    print("All labels are blank. No classification has been performed.")


if __name__ == "__main__":
    main()
