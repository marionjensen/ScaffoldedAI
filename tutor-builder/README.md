# Tutor Builder

The Tutor Builder is a Claude **skill**. You give it your source material (documentation, guides, textbooks) or just describe what you know, and it interviews you, designs the learning path, and hands you one finished file. Paste that file into a Claude Project and you have your own tutor.

No instructional design experience needed. The builder handles the pedagogy; you bring the subject matter knowledge.

---

## Set It Up (about 2 minutes, one time)

1. **Download [`tutor-builder.zip`](tutor-builder.zip)** from this folder. Don't unzip it.
2. In Claude, go to **Customize > Skills**, click **+**, choose **Create skill**, then **Upload a skill**, and select the ZIP.
3. Make sure the skill is toggled **on**.

**Requirements:** Skills need **Code execution and file creation** turned on (Settings > Capabilities). If you're on a Team or Enterprise plan, your organization's admin has to allow code execution and skills first.

---

## Use It

Start a new chat and type:

> **I want to make a tutor.**

That's the whole trick. The builder will ask what you want to teach and walk you through it from there. Not sure what it does yet? Say **"I'd like a practice run"** and it will guide you through building a tutor from a sample article.

If it doesn't start on its own, click the **+** button in the message box and pick **tutor-builder** from your skills.

---

## What Happens

The builder works with you in five short steps, and checks with you at each one:

1. **Review your content** and agree on scope.
2. **Write learning objectives**: what your learner will be able to *do*.
3. **Outline the learning path** in a sensible order.
4. **Check the teaching style** and adjust it if your subject needs something different (safety training, for example, might want a firmer voice).
5. **Build your tutor file.**

At the end you'll get a single file. Then:

1. Create a new Claude Project.
2. Open the file, copy everything, and paste it into the Project's instructions.
3. Start a chat in that Project and say hello.

---

## Under the Hood

A ScaffoldedAI tutor has two layers: **Layer 1** (how to teach, the same for every tutor) and **Layer 2** (what to teach, unique to your subject). The builder writes Layer 2 and joins it to Layer 1 for you, so you never have to handle them separately.

If you want to read or modify the skill itself, it's in [`source/tutor-builder/`](source/tutor-builder/):

| File | What It Is |
|---|---|
| `SKILL.md` | The builder's instructions: the five-stage process. |
| `references/layer-1.md` | The universal pedagogical foundation, copied into every tutor. |
| `references/layer-2-template.md` | The structure of a Layer 2 document. |
| `examples/starter-kit.md` | The sample article used for the practice run. |
| `scripts/assemble_tutor.py` | Joins Layer 1 and your Layer 2 into the finished file. |

To rebuild the ZIP after editing, zip the `tutor-builder` folder itself (not just its contents):

```
cd source && zip -r ../tutor-builder.zip tutor-builder
```

---

**Want to see what a finished tutor looks like first?** Check out the [Sample Tutors](../samples/).
