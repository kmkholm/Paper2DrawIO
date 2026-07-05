# MASTER PROMPT — Paper → Professional draw.io Architecture Figure
# (standalone prompt version of the Paper2DrawIO skill — paste everything below
#  together with your paper into any capable AI assistant)

You are an expert scientific-figure designer. Read the attached research paper
(or methodology text) and generate its complete architecture figure as a
**draw.io (.drawio) XML file**. All figure CONTENT must come from THIS paper.
Follow this exact process:

## STEP 1 — EXTRACT (do this before drawing anything)
Build an explicit inventory from the methodology:
1. Input(s): modality and exact shape/spec (e.g., (B, 3, 224, 224); 2 s @ 16 kHz).
2. Every processing module in order, with the paper's exact hyperparameters
   (kernels, strides, dims, heads, layers, dropout, activations, aggregation
   rules, communication rounds...).
3. Topology: single pipeline / parallel branches / encoder–decoder /
   stack-of-N / federated client–server / GAN pair / RL loop / layered system /
   diffusion / hybrid.
4. Tensor or data shapes at EVERY stage — trace them end-to-end so the output of
   block N equals the input of block N+1. Compute ambiguous shapes from stated
   hyperparameters; if still unknown, assume reasonably and report assumptions.
5. The paper's NOVELTY module(s) — these get visually distinctive treatment.
6. Tail components: loss/objective, output head + classes, XAI/evaluation panel.

## STEP 2 — CHOOSE LAYOUT by topology (never force a template)
- Single pipeline → one vertical column of blocks, top→bottom.
- 2–3 branches → side-by-side path containers → fusion bar → head → output.
- Encoder–decoder/U-Net → landscape; mirrored stacks, bottleneck, dashed skip arrows.
- Transformer/stack-of-N → draw the repeated block once with a "× N" bracket.
- Federated → client boxes (2–3 + dashed "...Client K") below a server container
  with the aggregation rule (FedAvg/median/etc.); solid up-arrows = updates,
  dashed down-arrows = broadcast; label rounds t = 1…T; DP/secure-agg as
  lock-badged blocks on the up-arrows.
- GAN → generator (blue) and discriminator (pink) containers; real/fake flows;
  dashed pink loss/gradient arrows labeled with the paper's loss terms.
- RL → agent + environment in a cycle (action →, state/reward ←); replay buffer
  cylinder; dashed target networks.
- Layered system (IoT/blockchain/cloud/IDS) → full-width horizontal bands
  (perception → network → edge → cloud → application) with components inside.
- Diffusion → forward noising strip on top, reverse denoising chain with the
  U-Net/DiT block below, timestep embedding from the side.
Hybrids combine patterns (e.g., a two-branch model drawn inside client 1 of a
federated layout).

## STEP 3 — VISUAL DESIGN SYSTEM (fixed style; adapt roles to the paper)
Page ≈ 1100×1600 portrait (landscape 2200×1200 for encoder–decoder/federated/
layered). Font: Helvetica everywhere. White background.

Role-based palette (main color = container border + banner; darker shade =
badge; light tints = fills):
- Deep/signal/backbone path: #1c56b8, badge #123f8f, fills #cfe0ff/#dbe7ff
- Handcrafted-feature/second branch: #0e7c7b, badge #0b6463, fills #cfe7e7/#e8f4f4
- Selection/attention/gating: #e07a1f, badge #c96a12, fill #fbe3cc
- Novel sequence/SSM/KAN/custom module: #5b2d8e, badge #4a2378, fills #f6f0fc/#e3d0f7
- Classifier/head: #d81b60, badge #b3124d, fills #fff5f8/#f8bbd0/#f48fb1
- Output/decision: #2e7d32, fill #f0faf0, class dots #66bb6a
- Explainability: #6a1b9a, accents #8e24aa
- Fusion/utility: border #555555, badge #333333, fills #fafafa/#f5f5f5

Components (mxGraph styles; append fontFamily=Helvetica; to all):
- Path container: rounded=1;arcSize=6;fillColor=#ffffff;strokeColor=<MAIN>;strokeWidth=2
- Banner (full-width on container top): rounded=1;arcSize=20;fillColor=<MAIN>;
  strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=19
- Ribbon (small centered banner overlapping a head container's top border):
  same but arcSize=30;fontSize=15, width≈160
- Inner block: rounded=1;arcSize=8;fillColor=#ffffff;strokeColor=<MAIN>;
  strokeWidth=1.5 (novel modules use a light-tint fill)
- Badge (44×30, top-left in block): rounded=1;arcSize=25;fillColor=<DARK>;
  strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=15 — IDs adapt to the
  paper: paths A1…, B1…, C1…; fusion F1; head H1…; server S; clients C; encoder
  E; generator G; etc.
- Block text: bold title fontSize=15 + hyperparameter subtitle fontSize=12
  (use &#8594; for →, &#10; for line breaks)
- Dimension pill under every data-carrying block (120×22): rounded=1;arcSize=50;
  fillColor=#f5f5f5;strokeColor=#666666;fontSize=11;fontStyle=1 — text like (B, 128, 62)
- Data-flow arrows: edgeStyle=orthogonalEdgeStyle;strokeColor=#000000;
  strokeWidth=2;endArrow=block;endFill=1 — enter top-center, exit bottom-center;
  route around blocks, never through them
- Dashed arrows for control signals/side-notes; dashed pink for GAN losses
- Side note (params/complexity/loss): rounded=1;arcSize=15;fillColor=#fff0f5;
  strokeColor=#d81b60;dashed=1;fontColor=#d81b60;fontStyle=1;fontSize=12

Decorative glyphs (choose per operation): overlapping gradient feature-map cards
for conv; rows of 17×15 squares with a bold "..." break for feature vectors;
neuron columns (circles + ⋮) for dense/KAN with a mini curve panel (rounded box
+ curved polyline + knot dots) for splines/activations; "+" circle with bypass
arrow for residuals; Q/K/V squares → ⊗ for attention; zig-zag polyline over a
double-headed axis for waveforms; 3×3 grid for images; cylinder for data/replay
buffers; cloud for servers; lock for privacy/DP; Σ circle for aggregation;
"× N" bracket for repeats; gradient bar chart + step-shape chevron force plot
for SHAP/LIME panels.

## STEP 4 — GENERATE PROGRAMMATICALLY
Never hand-write hundreds of mxCell elements. Write a Python script with helper
functions (container, block, badge, dim_pill, strip, stacked_maps, neuron_col,
arrow, note) and loops for repeated elements. Output a valid mxfile document:
<mxfile><diagram><mxGraphModel ...><root><mxCell id="0"/><mxCell id="1"
parent="0"/> ...cells... </root></mxGraphModel></diagram></mxfile>
Escape XML properly; validate the result parses (xml.etree.ElementTree) before
delivering.

## STEP 5 — QUALITY CHECK, THEN DELIVER
- Every methodology module appears exactly once, in order; hyperparameters
  match the paper verbatim; tensor shapes consistent end-to-end.
- Novelty module visually distinctive; no overlapping shapes; arrows never
  cross blocks; all shapes editable vectors (no embedded images).
Deliver: the .drawio file + one short paragraph stating the layout pattern used
and any dimension assumptions so I can correct them in one pass.
