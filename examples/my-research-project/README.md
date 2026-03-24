# Image Captioning Benchmark

Status: active
Mission: Evaluate how accurately vision-language models caption natural images across diverse categories.
Done when: Published benchmark with caption quality scores for 5+ models, correlation metrics against human ratings on 200+ images, and a recommended evaluation protocol.

## Context

Automated image captioning is widely used but poorly benchmarked for fine-grained accuracy. This project measures how well different VLMs describe image content — factual accuracy, detail coverage, and hallucination rates — and compares model outputs against human-written reference captions.

The goal is to answer: which models produce the most accurate and detailed captions, and what evaluation protocol best captures caption quality?

## Log

### 2026-03-01

Project created. Initial data audit completed — found 500 images with 3 human-written reference captions each in `data/captions.csv`. Images span 10 categories (animals, architecture, food, landscapes, people, sports, vehicles, art, indoor scenes, street photography). Each category has 50 images.

Sources: `data/captions.csv`, `data/categories.json`

### 2026-03-23T16:03:40Z

Autonomous session attempted Phase 1 baseline execution for the 50-image pilot task and stopped at prerequisite validation.

Findings:
1. The example project directory currently contains only `README.md`, `TASKS.md`, and `budget.yaml`.
   - Provenance: `list_files("examples/my-research-project", recursive=true)`.
2. The paths referenced by the project description and task (`data/captions.csv`, `data/categories.json`, `experiments/baseline-pilot/results/`) are not present in the repository copy used for this session.
   - Provenance: `search_text("data/captions.csv|categories.json|experiments/baseline-pilot|caption", path="examples/my-research-project")` returned no matches.
3. No configured Gemini or Claude model integrations were found in this repository, so the named 3-model baseline cannot be launched from the current environment.
   - Provenance: `search_text("anthropic|gemini|google.generativeai|vertexai", path=".")` returned no matches; `runner/openai_backend.py` shows only an OpenAI client integration.
4. Because the task requires external model APIs and missing local data assets, it was re-tagged as blocked pending tool/data availability rather than marked complete.
   - Provenance: `examples/my-research-project/TASKS.md` updated in this session.

Session-type: autonomous
Duration: <10 minutes
Task-selected: Run baseline captioning with 3 models on 50-image pilot set
Task-completed: no
Approvals-created: 1
Files-changed: 3
Commits: 0
Compound-actions: none
Resources-consumed: none
Budget-remaining: llm_api_calls 5000/5000 remaining, gpu_hours 50/50 remaining

## Open questions

- Which automated metric (BLEU, METEOR, CIDEr, CLIPScore) best correlates with human quality judgments for single-image captioning?
- How should we handle subjective captions where multiple valid descriptions exist? Human agreement on caption quality may be low for ambiguous images.
- Does caption quality vary systematically by image category? Models may excel at concrete objects (animals, vehicles) but struggle with abstract scenes (art, street photography).
- Where should the example project's referenced pilot assets live in this repository (`data/captions.csv`, `data/categories.json`, pilot image files), and are they intentionally omitted from the bootstrap example?
- Which approved runtime path should be used for the non-OpenAI models named in the task (Gemini 2.0 Flash and Claude Sonnet): new integrations in-repo, a gateway service, or task reformulation to available models only?
