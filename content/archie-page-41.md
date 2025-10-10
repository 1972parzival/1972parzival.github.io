---
categories: ["Software & Programming", "Tutorial"]
date: '2025-10-06'
description: ""
image: "/assets/images/ollama2.JPG"
slug: archie-page-41
tags: []
title: "'Ollama part 1: Setup'"
---


### Ollama part 1: Setup


#### Setting up Ollama and a easy to use Windows shortcut




### What is Ollama?


Image Description


"Ollama is an open-source platform that allows users to run large language models (LLMs) locally on their machines. It's a lightweight framework that bundles model weights, configurations, and data into a single package, and provides a simple API for creating, running, and managing models. Ollama supports a variety of models, including Llama 2, Code Llama, Mistral, and more."


![Mobirise Website Builder](/assets/images/ollama.JPG)




Setup Launcher


![Mobirise Website Builder](/assets/images/ollama4.JPG)


![Mobirise Website Builder](/assets/images/ollama3.JPG)




### Command Line


Screenshot of the command line result


Then enter your command line, for Windows you simply enter "cmd" into the Windows search bar and hit enter. Then type "ollama" into the command line and hit enter. You should get a terminal page similar to this showing the available commands.


![Mobirise Website Builder](/assets/images/ollama5.JPG)




### Downloading models


Use "ollama list" to make sure both models installed properly


Ollama doesn't come with models installed. You can see a list of the newest models here. The format for dowloading or running a model is "ollama run MODEL". I will be using llama2-uncensored: For conversational uses and text generation"ollama run llama2-uncensored"I will also be using codellama for this project: For code review and basic function generation"ollama run codellama"


![Mobirise Website Builder](/assets/images/ollama6.JPG)




### Windows shortcut


Step one and Step two shown


First you need to go onto your Windows desktop and create a new shortcut on your desktop (Step 1)Then a window will pop up asking for a location of the item, enter:"C:\Windows\System32\cmd. Exe /c ollama run MODEL"replace MODEL with the name of the model you downloaded and hit next, then type out a name for this model and hit enter. It will then appear on your home screen with the name you gave it. When you press it will bring up the model right away and you can start prompting.


![Mobirise Website Builder](/assets/images/ollama7.JPG)




### Additional customization


To enter screen above right click on the shortcut and hit properties


Feel free to add your personal touch! I decided to change the color of the font to a dark red and swhiched the font over to a retro one, for that classic terminal look. I would also look online and choose between the hundreds of custom systems and looks people have used for Windows terminals overs the years to really take it to the next levelyou can also uses Nano commands to create sub models for more detailed prompts that are automatically applied, such as roleplaying a certain character


![Mobirise Website Builder](/assets/images/ollama8.JPG)




You could also runs codellama through the command line of VS code and have your own personal Copilot system!


![Mobirise Website Builder](/assets/images/ollama9.JPG)


