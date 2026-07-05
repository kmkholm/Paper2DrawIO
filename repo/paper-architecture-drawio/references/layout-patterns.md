# Layout Patterns — one recipe per architecture topology

Pick the pattern matching the paper's real topology (from the Step-1 inventory).
Combine patterns when papers are hybrids (e.g., federated + two-branch model:
draw the model with Pattern B *inside* one client of Pattern E).

---

## A. Single pipeline
Vertical column, top→bottom: Input box → stage blocks → output → optional
XAI/eval panel. One container per logical stage group (preprocessing, backbone,
head) if there are >6 blocks; otherwise blocks float directly on the page.
Badges: S1, S2, … or P1…/M1…/H1… per stage group.

## B. Multi-branch → fusion (2–3 parallel paths)
- Input box centered at top, arrows split to N side-by-side path containers.
- Each container: banner + vertical chain of badged blocks (A1…, B1…, C1…).
- Fusion bar (F1) below spanning the paths, showing concatenation/attention
  fusion with mixed-color cell strips indicating provenance.
- Head container (H1…) → output → XAI.
- Balance container heights; extend the shorter path's container to align
  bottoms, or route its exit arrow down a corridor.

## C. Encoder–decoder / U-Net / autoencoder
Landscape page. Encoder stack on the left (blocks E1…En, shapes shrinking),
bottleneck/latent block centered, decoder stack on the right (D1…Dn, shapes
growing). Skip connections: dashed gray orthogonal arrows arcing over the top
from Ei to D(n−i+1). Latent shape pill under the bottleneck. For VAEs add μ/σ
blocks + sampling ⊙ node.

## D. Transformer / stack of N
One container for the repeated block: its internal sub-blocks (MHSA, Add&Norm,
FFN, Add&Norm) drawn once, with a right-side "× N" bracket. Embedding +
positional encoding blocks above; head below. For encoder-decoder Transformers
use two such containers side by side with cross-attention arrows.

## E. Federated learning
- Bottom row: 2–3 client boxes + a "… Client K" ghost box (dashed border).
  Each client contains a mini model icon (or the full Pattern-A/B model in
  client 1 with "same model" notes in others), local data cylinder, and local
  training loop arrow.
- Top center: server container with aggregation block (Σ/FedAvg/median, exact
  rule from the paper), global model block, and any defense/DP module.
- Up arrows (solid) = model updates w_k; down arrows (dashed) = global broadcast
  w^(t+1). Label communication rounds "t = 1…T" on a loop arc.
- Privacy modules (DP noise, secure aggregation) drawn as lock-badged blocks on
  the up arrows.

## F. GAN / adversarial
Generator container (left, blue) and discriminator container (right, pink).
Noise z / condition input → G → fake sample; real data cylinder → D alongside
fake. D output → real/fake decision diamond. Dashed pink gradient arrows back
to G and D labeled with the loss terms from the paper.

## G. RL / closed loop
Agent container (policy/value blocks) and Environment box, connected in a cycle:
action a_t →, state s_{t+1} + reward r_t ←. Replay buffer as a cylinder if
present; target networks as dashed twin boxes.

## H. Layered system / framework (IoT, blockchain, cloud, IDS deployments)
Full-width horizontal bands stacked vertically (e.g., Perception → Network →
Edge/Fog → Cloud → Application), each band a container with its components as
badged blocks arranged horizontally inside. Cross-band arrows vertical. Use
device/cloud/lock glyphs generously; this pattern is about the system, not
tensors, so dimension pills are optional — use protocol/data-type labels
instead.

## I. Diffusion
Forward process arrow (x₀ → x_T, adding noise, light-to-dark gradient strip)
on top; reverse denoising chain with the U-Net/DiT block (Pattern C or D inside)
below; timestep embedding block feeding in from the side.

---

## Universal tail sections (append when the paper has them)
- **Output/decision block** (green): softmax/regressor/detector + class labels
  + class dots + output shape.
- **Explainability panel** (purple): SHAP/LIME/Grad-CAM/attention-map mini
  visuals (bar chart, force plot, heat-grid).
- **Training/objective note**: dashed side note with the loss function and
  optimizer if the paper emphasizes them.
- **Parameters/complexity note**: dashed pink side note (≈ counts) linked with a
  dashed arrow.

## Numbering conventions
Letters follow the drawing order of major sections: paths get A/B/C…, fusion F,
head H, server S, clients C, generator G, discriminator D, encoder E, decoder D
(rename one if it collides). Numbers restart at 1 within each letter. Keep IDs
short — they exist so the caption and the running text can reference blocks.
