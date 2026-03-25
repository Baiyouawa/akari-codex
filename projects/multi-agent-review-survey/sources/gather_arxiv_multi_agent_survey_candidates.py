#!/usr/bin/env python3
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import OrderedDict

NS = {"atom": "http://www.w3.org/2005/Atom"}

QUERIES = [
    '(all:"multi-agent" OR all:"multi agent") AND (ti:survey OR abs:survey OR ti:review OR abs:review)',
    '(all:"LLM-based multi-agent" OR all:"multi-agent systems") AND (ti:survey OR abs:survey OR ti:review OR abs:review)',
    '(all:"agentic AI" OR all:"LLM agents") AND (ti:survey OR abs:survey OR ti:review OR abs:review)',
    '(all:communication OR all:collaboration OR all:coordination) AND (all:"multi-agent" OR all:"LLM agents") AND (ti:survey OR abs:survey OR ti:review OR abs:review)',
]

YEAR_RE = re.compile(r'^(2024|2025|2026)-')
SURVEY_RE = re.compile(r'\b(survey|review|perspective)\b', re.I)
MULTI_AGENT_RE = re.compile(r'(multi-agent|multi agent|agentic|llm agent|llm-based multi-agent)', re.I)


def fetch(query, max_results=50):
    url = (
        'http://export.arxiv.org/api/query?search_query=' + urllib.parse.quote(query)
        + f'&start=0&max_results={max_results}&sortBy=submittedDate&sortOrder=descending'
    )
    with urllib.request.urlopen(url, timeout=30) as resp:
        return resp.read().decode('utf-8', 'ignore')


def text(node, path):
    x = node.find(path, NS)
    return (x.text or '').strip() if x is not None and x.text else ''


def parse(feed_text):
    root = ET.fromstring(feed_text)
    rows = []
    for entry in root.findall('atom:entry', NS):
        title = ' '.join(text(entry, 'atom:title').split())
        summary = ' '.join(text(entry, 'atom:summary').split())
        published = text(entry, 'atom:published')
        year = published[:4]
        abs_url = text(entry, 'atom:id')
        pdf_url = abs_url.replace('/abs/', '/pdf/') + '.pdf' if abs_url else ''
        authors = [a.find('atom:name', NS).text.strip() for a in entry.findall('atom:author', NS)]
        rows.append({
            'title': title,
            'summary': summary,
            'published': published,
            'year': year,
            'abs_url': abs_url,
            'pdf_url': pdf_url,
            'authors': authors,
        })
    return rows


def keep(row):
    blob = row['title'] + '\n' + row['summary']
    return row['year'] in {'2024', '2025', '2026'} and SURVEY_RE.search(blob) and MULTI_AGENT_RE.search(blob)


def main():
    seen = OrderedDict()
    provenance = []
    for q in QUERIES:
        feed = fetch(q, max_results=50)
        provenance.append({'query': q, 'feed_prefix': feed[:300]})
        for row in parse(feed):
            if keep(row):
                seen.setdefault(row['abs_url'], row)
        time.sleep(1)
    out = {
        'generated_by': 'projects/multi-agent-review-survey/sources/gather_arxiv_multi_agent_survey_candidates.py',
        'queries': QUERIES,
        'candidate_count': len(seen),
        'candidates': list(seen.values()),
    }
    json.dump(out, sys.stdout, ensure_ascii=False, indent=2)


if __name__ == '__main__':
    main()
