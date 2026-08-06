# 生图提示词模板

每张图单独生成。根据正文内容替换变量，不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art. Slightly wobbly pen lines. Lots of empty white space. Sparse red/orange/blue handwritten Chinese annotations. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required:
仓老师 (Cang Laoshi), a hand-drawn stylized human character with long straight hair and side-swept bangs, big expressive eyes, exaggerated theatrical expressions, expressive large hand gestures. Simple line-art accessories only: a wide belt line and a necklace line as identity markers, no realistic rendering. Natural adult body proportions; NOT chibi, NOT big-head, NOT childish, not glamorous or photorealistic. In 16:9 body illustrations show full body by default; in cover mode chest-up to hip is correct. 仓老师 must perform the core conceptual action, not decorate the scene.

Identity references:
Use `assets/character-halfbody-expressions.png` for face, hair, expression, and near-camera hand gestures; use `assets/character-fullbody-poses.png` for full-body proportion, stance, and action guidance. Use a single suitable pose or expression as inspiration; never paste or reproduce the nine-panel sheet as a collage.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：仓老师在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Black for main line art and 仓老师. Orange for main flow/path/arrows. Red only for key warnings/problems/results. Blue only for secondary notes or feedback/system state.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve at least 35% blank white space. Use at most 5-8 short handwritten Chinese labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, or dense explainer. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. It should be clear but not instructional, interesting but not childish, strange but clean.

Anatomy hard constraint:
The character has exactly two arms and exactly two hands. Each arm must visibly connect from one shoulder through one elbow and one wrist to one hand. No extra arms, duplicate hands, fused limbs, detached hands, impossible joints, or malformed fingers. Keep the forearms and shoulder connections simple and unobscured when the character holds an object. If the pose is ambiguous, simplify the pose rather than hiding the anatomy behind the object.
```

## 公众号封面提示词模板（2.35:1，封面模式专用）

封面模式使用这个模板，不要套用上面的 16:9 正文配图模板（比例、构图、用色规则都不同）。

```text
Generate one standalone WeChat official-account cover illustration. Exact aspect ratio 2.35:1 (width = height × 2.35) — not 2.15:1, not 16:9.

Visual DNA:
Pure white background. Minimalist black hand-drawn line art, with thicker brush-style strokes for the title. Slightly wobbly pen lines. Sparse red handwritten Chinese for the supporting line, orange only for a single pointing/connector line. Clean absurd product-sketch feeling. No gradients, no shadows, no paper texture, no complex background, no commercial vector style, no PPT infographic look, no cute mascot poster, no children's illustration, no realistic UI.

Recurring IP character required (right side, roughly 35%-45% of canvas width):
仓老师 (Cang Laoshi), a hand-drawn stylized human character with long hair and side-swept bangs, big expressive eyes, exaggerated theatrical expression, one hand pointing toward the title, the other hand raised open with spread fingers. Simple line-art accessories: a wide black belt and a necklace as identity markers. Top/blouse color fixed to brand green #69b076. Shown from roughly chest-up to hip — this chest-up crop is correct for cover mode and does NOT need the full-body-from-head-to-feet rule used in 16:9 body-illustration mode.

Title block (left ~55%-60% of canvas):
Large bold black hand-brushed Chinese title, at most 14 characters: {主标题}
Below it, a shorter line in red handwritten Chinese, at most 12 characters: {补充信息}

Core metaphor element:
{一个与本篇文章主题相关的小物件或小角色}，用橙色线条从它指向标题或补充信息。每篇文章重新发明这个小元素，不要固定成同一种物件。

Composition:
Left ~55%-60%: title + red supporting line. Right ~35%-45%: 仓老师 chest-up pointing gesture. Optional small metaphor element near the boundary between the two halves, connected by exactly one orange line.

Centered square safe-area:
Keep the title, avatar, and core metaphor inside a centered square safe-area (square side = canvas height, horizontally centered), so the cover still reads when cropped to a square for sharing. This is best-effort — if it conflicts with the 2.35:1 composition, prioritize the full-width cover's readability.

Color use:
Black for line art, title, and 仓老师. Red only for the supporting subtitle line. Orange only for the single connector/pointing line. No blue in cover mode.

Constraints:
Exact 2.35:1 canvas. Keep it clean, sparse, hand-drawn. No extra UI chrome, logos, or borders. The avatar must be chest-up to hip, not full body.

Anatomy hard constraint:
The avatar has exactly two arms and exactly two hands. Each arm must visibly connect from one shoulder through one elbow and one wrist to one hand. No extra arms, duplicate hands, fused limbs, detached hands, impossible joints, or malformed fingers. Keep any pointing or holding gesture simple and unobscured.
```

如果手上有一张已发布的旧封面可以做构图参考，把它作为第二张图连同上面的提示词一起传给生图工具，并在提示词末尾追加：

```text
Use the attached reference image only for composition and character-gesture guidance (title-left/avatar-right layout, pointing gesture, brush-title style). Do not copy its exact colors, exact wording, or exact metaphor object — reinterpret for this new article, and always use the fixed brand green #69b076 top.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean white background, matching the surrounding blank paper. Preserve everything else exactly: characters, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强怪诞感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make 仓老师 more central to the conceptual action, with a bigger expression or gesture. 仓老师 should be doing the strange work that explains the idea, not standing beside the diagram. Keep it clean, sparse, hand-drawn, and not cute.
```
