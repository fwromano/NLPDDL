# PDDL ↔ Natural‑Language Round‑Trip Toolkit

> *Generate NL descriptions for any collection of PDDL problem files, re‑compile
> them back to PDDL with an LLM, and measure semantic fidelity. Designed for
> large corpora such as **Plan‑Bench**.*

---

## 1 · Key Features

| Stage         | Command        | Result                                                            |
| ------------- | -------------- | ----------------------------------------------------------------- |
| **Fetch**     | `cli fetch`    | Shallow‑clone a Git repo that contains PDDL instances             |
| **PDDL → NL** | `cli pddl2nl`  | Produce `*.nl.txt` next to each instance + copy the original PDDL |
| **NL → PDDL** | `cli nl2pddl`  | Re‑generate PDDL under `pairs/nl2pddl/<tag>/`                     |
| **Validate**  | `cli validate` | Compare originals vs regenerated, write human + machine reports   |

*Variant tags* (e.g. model name, prompt version) keep multiple experiment runs isolated.

---

## 2 · Directory Layout

```
instances/                 # original corpus (read‑only)

pairs/                     # generated artefacts
├─ blocksworld/...         # copies of originals + NL files
└─ nl2pddl/
   └─ <tag>/               # regen PDDL for a specific variant
      └─ .../*.regen.pddl

pairs/results/
└─ <tag>/                  # reports for that variant
   ├─ summary.txt          # aligned PASS/FAIL list with diffs for errors
   ├─ summary.csv          # quick spreadsheet import
   └─ summary.jsonl        # one‑line JSON per file (automated analysis)
```

---

## 3 · Quick Start

```bash
# 0)   Put OPENAI_API_KEY in a .env file (python‑dotenv is auto‑loaded)

# 1)   Clone the benchmark repo once (Plan‑Bench example)
python -m cli fetch \
       --repo https://github.com/karthikv792/LLMs-Planning \
       --subdir plan-bench/instances \
       --dest ./instances

# 2)   Generate NL descriptions (skips existing)
python -m cli pddl2nl \
       --repo _skip_ --dest ./instances --subdir . \
       --out pairs

# 3)   Round‑trip with a variant tag
python -m cli nl2pddl \
       --repo _skip_ --dest ./instances --subdir . \
       --out pairs --tag gpt4o_v1 --model gpt-4o-mini

# 4)   Validate and inspect human report
python -m cli validate \
       --repo _skip_ --dest ./instances --subdir . \
       --out pairs --tag gpt4o_v1

less pairs/results/gpt4o_v1/summary.txt
```

Pass `--max 10` to any stage for a quick smoke test and `--force` to overwrite artefacts.

---

## 4 · Customising

### 4.1 Change the LLM or prompt

* Pick any `--model` recognised by OpenAI account.
* Edit **`utils.PROMPT_PDDL2NL`** or **`utils.PROMPT_NL2PDDL`** then use a new
  `--tag` when you re‑run `nl2pddl` & `validate`.


---

## 5 · Dependencies

* Python 3.9+
* `openai>=1.0`   – LLM access
* `python-dotenv` – optional `.env` support

Install:

```bash
pip install -r requirements.txt 
```

---


