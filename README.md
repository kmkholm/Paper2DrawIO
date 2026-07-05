# Paper2DrawIO 🎨📄

**Turn any research paper into a publication-quality, fully editable draw.io architecture figure — automatically.**

A [Claude Skill](https://docs.claude.com) that reads a research paper (PDF, LaTeX, Word, or plain text), extracts the model/system architecture, and generates a professional `.drawio` figure ready for journal and conference submissions (IEEE, PLOS, Springer, Elsevier, MDPI, …).

<p align="center">
  <em>Upload paper → "draw the architecture" → get an editable .drawio figure</em>
</p>

---

## ✨ Features

- **Any architecture, any paper** — CNN, RNN, Transformer, Mamba, KAN, GAN, encoder–decoder, U-Net, diffusion, federated learning, RL, IDS pipelines, IoT/blockchain frameworks, multimodal systems.
- **9 adaptive layout patterns** — the figure layout follows the paper's real topology (single pipeline, multi-branch → fusion, encoder–decoder, ×N Transformer stacks, client–server FL, adversarial pairs, closed RL loops, layered system bands, diffusion chains). No forced templates.
- **Publication-grade design system** — consistent role-based color palette, lettered block badges (A1, B1, F1, H1…), hyperparameter subtitles, tensor-shape dimension pills, decorative glyphs (feature-map stacks, neuron columns, spline panels, SHAP force plots, locks, clouds, Σ aggregation nodes).
- **Novelty highlighting** — the paper's core contribution module gets a visually distinctive treatment so reviewers see it instantly.
- **Programmatic generation** — a tested Python helper library (`drawio_lib.py`) builds the XML in code, validates it, and guarantees editable vector shapes (no embedded images).
- **Shape-consistency checks** — tensor shapes are traced end-to-end; ambiguous dimensions are computed from stated hyperparameters, and any assumption is reported.

## 📦 Repository Structure

```
paper-architecture-drawio/
├── SKILL.md                        # Skill workflow (extract → layout → style → generate → validate)
├── references/
│   ├── style-guide.md              # Exact mxGraph styles, palette, glyphs, typography, spacing
│   └── layout-patterns.md          # 9 layout recipes for every architecture topology
└── scripts/
    └── drawio_lib.py               # Python library: containers, blocks, badges, pills, strips,
                                    # neuron columns, spline panels, waveforms, brackets, charts
```

## 🚀 Installation

### Option A — Claude.ai (recommended)
1. Download `paper-architecture-drawio.skill` from the [Releases](../../releases) page.
2. In Claude.ai, upload the file to a chat — click **Save skill** on the file card.
3. Done. In any conversation, upload a paper and say **"draw the architecture figure"**.

### Option B — Claude Code / custom agents
Copy the `paper-architecture-drawio/` folder into your skills directory (e.g. `~/.claude/skills/`).

## 🖊️ Usage

```
[upload your paper PDF]
"Draw the architecture figure for this paper."
```

Optional refinements:
- `"...as a landscape figure"` / `"...IEEE single-column width"`
- `"...this is a federated setup — show clients, server, and communication rounds"`
- `"...highlight the attention module as the novelty"`

Output: a validated `.drawio` file you open at [app.diagrams.net](https://app.diagrams.net) (**File → Open From → Device**) or in the draw.io desktop app. Every shape is editable.

## 🧩 Standalone use of the library

`scripts/drawio_lib.py` works without Claude too:

```python
from drawio_lib import Diagram

d = Diagram(page_w=1100, page_h=1600)
path = d.container(30, 100, 470, 600, "Feature Extraction", "#1c56b8")
b1 = d.block(42, 150, 446, 90, "A1", "Conv Block 1",
             sub="Conv1d(64→96, k=5) → BN → ReLU", color="#1c56b8",
             badge_color="#123f8f")
d.dim_pill(265, 245, "(B, 96, 250)")
d.save("figure.drawio")
```

## 🖼️ Design language

| Role | Color |
|---|---|
| Deep / signal path | `#1c56b8` |
| Handcrafted features | `#0e7c7b` |
| Selection / attention | `#e07a1f` |
| Novel modules (Mamba, KAN…) | `#5b2d8e` |
| Classifier head | `#d81b60` |
| Output / decision | `#2e7d32` |
| Explainability | `#6a1b9a` |

## 📄 License

MIT — see [LICENSE](LICENSE).

## 👤 Author

**Mohammed Tawfik** — Assistant Professor, Cybersecurity & Cloud Computing
Sana'a University · [GitHub @kmkholm](https://github.com/kmkholm) · [kmkholm.github.io](https://kmkholm.github.io) · ORCID [0000-0002-1227-387X](https://orcid.org/0000-0002-1227-387X)

## ⭐ Citation

If this tool helped your paper's figures, a star ⭐ on the repo is appreciated!
