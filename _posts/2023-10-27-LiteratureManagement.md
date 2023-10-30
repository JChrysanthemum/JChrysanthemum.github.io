---
layout: post
title: Literature management
description: Workflow of tag, save, local link of literatures (papers, webs and misc)
keywords: paper
date: [2023-10-27]
mermaid: false
sequence: false
flow: false
mathjax: false
mindmap: false
mindmap2: false
---

**Preparation**: Win10+, browser could access academic resources.

Zotero + zutilo + RBTray + Joplin + Texlive with vscode

- Zotero: Literature managemanet
  
  Note: Netdrive like OneDrive are not recommend. Zotero run a local sql service, synchorization may break it dataset. (That is, backup with raw file, crashed when roll back)

- Zutilo: Zotero addons, could give Zotero URI like zotero://select/library/items/HAI4IUAB. Also many amazing tools. 

- RBTray: Tools for Zotero minimize in backgroud. 

  (Zotero could not run in background. We can not add items without Zotero running.)

  First, make RBTray run at start.

  1. Open windows run (WIN + R)
  2. Type `shell:startup`
  3. Put a softlink of RBTray in this folder.
  
  Right click minimize of Zotero, Zotero could run in back ground

- Joplin: Markdone notebook. Colud be replaced by any notebook you like.

- Texlive with vscode:You can use Overleaf of course. Local latex compiler and editor allow me go deeper with latex.