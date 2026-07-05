# Visual Design System — draw.io style reference

All style strings are mxGraph styles. Append `fontFamily=Helvetica;` to everything.

## Page
- `pageWidth="1100" pageHeight="1600"` (extend height freely; go landscape
  2200×1200 for encoder-decoder / federated / layered-system layouts).
- Grid 10, white background, no shadow by default.

## Role-based color palette
Assign by *function*, adapting to whatever modules the paper has. Stay internally
consistent (banner/border = main color, badge = darker shade, fills = light tints).

| Role | Main | Badge (dark) | Light fills |
|---|---|---|---|
| Deep/signal/backbone path | `#1c56b8` | `#123f8f` | `#cfe0ff`, `#dbe7ff` |
| Handcrafted features / 2nd branch | `#0e7c7b` | `#0b6463` | `#cfe7e7`, `#e8f4f4` |
| Selection / attention / gating | `#e07a1f` | `#c96a12` | `#fbe3cc` |
| Novel sequence / SSM / KAN / custom | `#5b2d8e` | `#4a2378` | `#f6f0fc`, `#e3d0f7` |
| Classifier / head | `#d81b60` | `#b3124d` | `#fff5f8`, `#f8bbd0`, `#f48fb1` |
| Output / softmax / decision | `#2e7d32` | — | `#f0faf0`, dots `#66bb6a` |
| Explainability / evaluation | `#6a1b9a` | — | accents `#8e24aa` |
| Fusion / utility / neutral | `#555555` | `#333333` | `#fafafa`, `#f5f5f5` |
| Server / aggregation (FL) | `#1c56b8` | `#123f8f` | `#e3f2fd` |
| Clients / edge devices (FL) | `#0e7c7b` | `#0b6463` | `#e0f2f1` |
| Generator (GAN) | `#1c56b8` | `#123f8f` | `#cfe0ff` |
| Discriminator (GAN) | `#d81b60` | `#b3124d` | `#fff5f8` |

If a paper needs more roles, extend with harmonious dark-bordered hues; never
use pure red/yellow fills (journal print issues).

## Components (exact styles)

**Path/stage container** (one per branch/major stage):
```
rounded=1;arcSize=6;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=<MAIN>;strokeWidth=2;
```
**Container banner** (full-width, on top edge of container):
```
rounded=1;arcSize=20;whiteSpace=wrap;html=1;fillColor=<MAIN>;strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=19;
```
**Ribbon banner** (small centered label overlapping a container's top border,
used for heads/classifiers): same as banner but `arcSize=30;fontSize=15`,
width ≈ 160, y = container_y − 12.

**Inner block**:
```
rounded=1;arcSize=8;whiteSpace=wrap;html=1;fillColor=#ffffff;strokeColor=<MAIN>;strokeWidth=1.5;
```
Novel modules use a light-tint fill (e.g. `#f6f0fc`) instead of white.

**Badge** (44×30, letter+number ID, top-left inside block):
```
rounded=1;arcSize=25;whiteSpace=wrap;html=1;fillColor=<DARK>;strokeColor=none;fontColor=#ffffff;fontStyle=1;fontSize=15;
```

**Block title**: `text;html=1;align=left;fontSize=15;fontStyle=1;`
**Block subtitle** (hyperparameters): `text;html=1;align=left;fontSize=12;`
Use `&#8594;` for →, `&#10;` for line breaks inside values.

**Dimension pill** (centered under the block content, 120×22):
```
rounded=1;arcSize=50;whiteSpace=wrap;html=1;fillColor=#f5f5f5;strokeColor=#666666;fontSize=11;fontStyle=1;
```
Text like `(B, 128, 62)` — always the paper's real shapes.

**Data-flow arrow**:
```
edgeStyle=orthogonalEdgeStyle;rounded=0;html=1;strokeColor=#000000;strokeWidth=2;endArrow=block;endFill=1;
```
**Dashed side-note arrow / control signal**: same + `dashed=1;strokeWidth=1.5`.
**Gradient / loss arrows (GAN, backprop)**: `strokeColor=#d81b60;dashed=1;`.

**Side note** (parameters count, complexity):
```
rounded=1;arcSize=15;whiteSpace=wrap;html=1;fillColor=#fff0f5;strokeColor=#d81b60;dashed=1;fontColor=#d81b60;fontStyle=1;fontSize=12;
```

## Decorative glyphs (pick per operation)
- **Conv / feature maps**: 3–7 overlapping cards, offset ~10px diagonal, style
  `fillColor=<light>;gradientColor=<mid>;gradientDirection=south;strokeColor=<MAIN>`.
- **Feature vector**: row of small squares 17×15 (`fillColor=<light tint>`), with
  a bold `...` text break for long vectors, e.g. 10 cells + … + 6 cells.
- **Dense / KAN / MLP**: vertical neuron columns (ellipses r≈11, gap 4, `⋮`
  below), joined by small straight arrows; add a mini curve panel (white rounded
  rect + curved pink polyline + dot markers) for spline/activation functions.
- **Residual**: small `+` circle (26×26, white, black border) with an orthogonal
  bypass arrow over the block.
- **Attention**: small Q/K/V labeled squares feeding a `⊗` circle.
- **Waveform**: black polyline zig-zag over a double-headed axis arrow.
- **Image input**: 3×3 grid of small squares.
- **Cloud/server**: `shape=cloud` or a rounded rect with a small DB cylinder
  (`shape=cylinder3`).
- **Device/client**: rounded rect with tiny screen rect inside.
- **Lock (privacy/DP)**: `shape=mxgraph.basic.lock` or a padlock built from a
  rect + arc.
- **Aggregation (FedAvg)**: circle labeled `Σ` or `⊕`.
- **Repeat bracket (× N)**: right-side curly text `× N` in bold fontSize 16 with
  a thin bracket line spanning the repeated blocks.
- **Bar chart (XAI)**: left-aligned labels + gradient bars
  (`fillColor=#8e24aa;gradientColor=#d81b60`), axis text below.
- **Force plot (SHAP)**: row of `shape=step` chevrons in a pink→blue ramp with
  base value / f(x) labels and a dashed divider.

## Typography scale
19 banner / 17 input title / 15 block titles & badges / 13 input subtitle /
12 block subtitles / 11 dim pills / 10–9 fine print. Bold = `fontStyle=1`.

## Spacing rules
- ≥ 12 px between blocks inside a container; ≥ 20 px between containers.
- Arrows enter top-center, exit bottom-center (`exitX=0.5;exitY=1;entryX=0.5;entryY=0`)
  unless topology requires side entry.
- Route inter-container arrows through clear corridors; add waypoints so lines
  never cross a block.
