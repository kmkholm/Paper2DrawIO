---
name: paper-architecture-drawio
description: Turn ANY research paper, methodology section, or model description into a professional, publication-quality architecture figure as an editable draw.io (.drawio) XML file. Use this skill whenever the user uploads or pastes a paper (PDF, LaTeX, Word, or text) and asks to "draw the architecture", "make a figure", "create a draw.io / diagrams.net diagram", "make the framework figure", "visualize the model/pipeline/methodology", or wants a system diagram for a journal or conference submission. Also trigger when the user asks to reproduce, restyle, or improve an existing architecture figure in draw.io format. Works for ANY architecture type — CNN, RNN, Transformer, Mamba, KAN, GAN, encoder-decoder, diffusion, federated learning, RL, IDS pipelines, multimodal, blockchain, IoT frameworks, etc.
---

# Paper → Professional draw.io Architecture Figure

Convert any research paper's methodology into a polished, fully editable draw.io
architecture figure. The figure content is ALWAYS derived from the paper at hand;
this skill only fixes the *process* and the *visual quality bar*, never the layout
or content of a previous figure.

## Workflow (always in this order)

### Step 1 — Extract the architecture from the paper
Read the methodology/model sections and build an explicit inventory before drawing
anything:

1. **Input(s)**: modality (audio, image, packets, text, graph, tabular, multimodal),
   exact shape/spec (e.g. `(B, 3, 224, 224)`, 2 s @ 16 kHz, flow records).
2. **Processing stages**: every module in order, with the paper's exact
   hyperparameters (kernel sizes, strides, hidden dims, heads, layers, dropout,
   activations, grid sizes, aggregation rules, comm rounds…).
3. **Topology**: single pipeline, parallel branches, encoder–decoder,
   client–server (federated), adversarial pair (GAN), cyclic loop (RL/diffusion),
   stack-of-N (Transformer), or hybrid. This decides the page layout.
4. **Tensor/data shapes at every stage**. Trace them through the whole network so
   every block gets a correct dimension annotation. If a shape is ambiguous,
   compute it from the stated hyperparameters; if still unknown, make a reasonable
   assumption and record it (report assumptions to the user at the end).
5. **The novelty**: identify the paper's core contribution module(s). These get
   visually distinctive treatment (unique color + internal mini-diagram) so the
   contribution is instantly visible to reviewers.
6. **Tail components**: loss/objective, output head, classes, and any
   XAI/evaluation/deployment panel the paper includes.

Write this inventory down (as a comment block or scratch notes) before generating
XML. Do not skip it — figures drawn without the inventory drift from the paper.

### Step 2 — Choose the layout pattern
Pick the pattern that matches the topology from Step 1. Read
`references/layout-patterns.md` for the full recipes. Summary:

| Topology in paper | Layout |
|---|---|
| Single pipeline | One vertical column of blocks, top→bottom |
| 2–3 parallel branches → fusion | Side-by-side path containers → fusion bar → head |
| Encoder–decoder / U-Net | Two mirrored stacks with bottleneck + skip arrows |
| Transformer / stack of N | One container with "× N" bracket on repeated blocks |
| Federated learning | Client boxes (2–3 shown + "…") around/below a server box, aggregation + broadcast arrows, round loop |
| GAN / adversarial | Generator and discriminator containers with real/fake data flows and loss arrows |
| RL / closed loop | Agent + environment boxes with action/state/reward cycle arrows |
| System/framework (IoT, blockchain, cloud) | Layered horizontal bands (perception → network → processing → application) |

Never force a two-path template onto a paper that doesn't have two paths. The
layout serves the paper.

### Step 3 — Apply the visual design system
Read `references/style-guide.md` for exact style strings, colors, and component
specs. Core rules:

- Page ≈ 1100 × 1600 (extend as needed), Helvetica everywhere, white background.
- Each major stage/path lives in a **rounded container** with a colored banner
  title; blocks inside are white rounded rects with a **lettered badge**
  (A1, A2…, B1…, F1 for fusion, H1… for head — letters adapt to THIS paper's
  structure), bold title + hyperparameter subtitle.
- Every data-carrying block gets a **dimension pill** with the exact shape.
- Add small **decorative glyphs** that match each operation (feature-map stacks,
  vector strips, neuron columns, curve panels, gears, clouds, locks…) — details
  in the style guide.
- Black orthogonal arrows (strokeWidth 2) for data flow; dashed arrows for
  side-notes, gradients, or control signals.
- Consistent role-based palette (blue = deep/signal, teal = handcrafted/features,
  orange = selection/attention, purple = novel sequence modules, pink = classifier
  head, green = output, deep purple = explainability, gray = fusion/utility).
  Adapt roles to the paper; keep colors internally consistent.

### Step 4 — Generate the XML programmatically
NEVER hand-write hundreds of mxCell elements. Use the helper library:

```bash
cp /path/to/skill/scripts/drawio_lib.py /home/claude/
```

Then write a short Python script that imports `drawio_lib` and composes the
figure with its helpers (`container`, `block`, `badge`, `dim_pill`, `strip`,
`stacked_maps`, `neuron_col`, `arrow`, `free_arrow`, `note`, `save`). Loops
handle all repeated elements (vector cells, neurons, clients, stacked maps).

### Step 5 — Validate and deliver
1. Run the script; parse the output with `xml.etree.ElementTree` to confirm
   validity.
2. Save the final file to `/mnt/user-data/outputs/<name>.drawio` and present it.
3. Report in one short paragraph: what was drawn, layout pattern used, and any
   dimension assumptions made — so the user can correct them in one pass.

## Quality bar (check before delivering)
- [ ] Every module from the paper's methodology appears exactly once, in order.
- [ ] Every hyperparameter shown matches the paper verbatim.
- [ ] Tensor shapes are consistent end-to-end (output of block N = input of N+1).
- [ ] The novelty module is visually distinctive.
- [ ] No overlapping text/shapes; arrows never cross through blocks.
- [ ] All shapes are editable vectors — no embedded images.
- [ ] XML parses; file opens in app.diagrams.net.

## Handling follow-up edits
When the user asks for changes (colors, IEEE/PLOS-safe fonts, landscape layout,
splitting into sub-figures), edit the generator script and regenerate — never
patch raw XML by hand. Keep the script in the working directory for the whole
conversation.
