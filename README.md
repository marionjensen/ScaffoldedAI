# ScaffoldedAI

**A two-layer framework for building AI tutors that actually teach.**

---

## The Problem

Most AI-powered learning tools do one of two things: they answer questions like a search engine, or they deliver scripted content like a slideshow with a chatbot bolted on. Neither one *teaches*. They give you information and hope learning happens on its own.

That's like handing someone a textbook and calling it a teacher. Information is not instruction.

## What ScaffoldedAI Does Differently

ScaffoldedAI is a framework for building AI tutors grounded in established learning science — tutors that guide learners through understanding rather than handing them answers. These tutors use Socratic questioning, check for misconceptions, adapt to what the learner already knows, and build knowledge step by step.

The framework is built on a two-layer architecture:

- **Layer 1: Pedagogy.** A universal set of instructional principles that govern *how* the tutor teaches — things like Socratic dialogue, scaffolded complexity, formative assessment, and productive struggle. This layer stays the same no matter what you're teaching.

- **Layer 2: Domain Content.** The subject matter, learning objectives, learning path, common misconceptions, and key concepts for a specific topic. This is the layer you swap out to create a new tutor.

The result: you can build a tutor for *any* subject by writing a Layer 2 document and pairing it with the universal Layer 1. No coding. No AI expertise. Just clear thinking about what you want to teach and how learners typically struggle with it.

## What You'll Need

- A **Claude Pro, Max, Team, or Enterprise account** with access to [Claude Projects](https://support.anthropic.com/en/articles/9517075-what-are-projects)
- **Code execution and file creation** turned on (Settings > Capabilities). This is only needed for the Tutor Builder in Path 2.
- About **15 minutes** to set up your first tutor
- Curiosity about how AI can do more than answer questions

## Two Paths: Choose Your Starting Point

### 🎓 Path 1: Experience a Sample Tutor

If you want to see what a ScaffoldedAI tutor feels like before building anything, start here. We've built three sample tutors that demonstrate the framework across different types of learning:

| Sample Tutor | What It Teaches | What It Demonstrates |
|---|---|---|
| **Impressionism & Post-Impressionism** | Key movements, artists, techniques, and the historical shifts between them | Teaching *conceptual knowledge* — how the tutor builds understanding of ideas and connections |
| **Photography Exposure Basics** | Aperture, shutter speed, ISO, and depth of field | Teaching an *applied skill* — how the tutor helps you learn settings that interact with each other |
| **Logical Fallacies** | Common reasoning errors and how to spot them in real arguments | Teaching *analytical reasoning* — how the tutor presents flawed arguments and guides you to find the problem |

Each sample includes everything you need: setup instructions, the Layer 1 and Layer 2 files, and suggested first prompts to get started.

👉 **[Try a Sample Tutor →](samples/)**

---

### 🛠️ Path 2: Build Your Own Tutor

Ready to create a tutor for your own subject? The **Tutor Builder** is a Claude skill. Install it once, then start any chat with:

> **I want to make a tutor.**

It asks what you want to teach (you can bring documentation, guides, training manuals, textbooks, or just your own expertise), walks you through learning objectives and an outline, and hands you one finished file. Paste that file into a new Claude Project and your tutor is ready.

Not sure what to expect? Tell the builder you'd like a **practice run** and it will guide you through a full build using a sample article before you use your own content.

👉 **[Build Your Own Tutor →](tutor-builder/)**

---

## How It Works (The Short Version)

1. **Start with Layer 1.** This file contains the pedagogical instructions that tell Claude *how to be a tutor*. You add it to a Claude Project as part of the project instructions. You never need to modify this file.

2. **Add a Layer 2.** This file contains your subject matter — the learning objectives and path, key concepts, common misconceptions, and anything else the tutor needs to know about your topic. You add this to the same Claude Project.

3. **Start a conversation.** Open a new chat within the project and begin learning. The tutor will assess where you are, guide you through the material, and adapt to your responses.

That's it. Two layers in one Claude Project. No code, no plugins, no platform to learn. (If you use the Tutor Builder, it joins the two layers into a single file for you.)

---

## Who Made This

ScaffoldedAI was created by **Marion Jensen**, an author and instructional designer with 25+ years of experience building learning programs at companies like American Express, Discover, Brex, and Milliman. Marion's work sits at the intersection of instructional design and AI — exploring how large language models can move beyond content delivery into genuine, adaptive teaching.

This framework grew out of real-world deployment: AI tutors built using this architecture have been used for employee onboarding, professional development, and skills training in live corporate environments.

Marion is currently pursuing a PhD in Instructional Technology & Learning Sciences at Utah State University, with a research focus on AI-facilitated learning.

- 🔗 [LinkedIn](https://www.linkedin.com/in/marionjensen/)
- 🌐 [marionjensen.com](https://marionjensen.com)

---

## License

This project is licensed under the [Creative Commons Attribution 4.0 International License](LICENSE). You are free to use, adapt, and share this framework for any purpose, including commercially, as long as you provide attribution.
