---
categories: ["Chemistry & Materials", "Experimental"]
date: '2025-10-06'
description: "The point of this project is to finally build a proper website for AII3,"
image: "/assets/images/aii3.JPG"
slug: archie-page-48
tags: []
title: AII3. org
---


### AII3. Org




#### Intro


The point of this project is to finally build a proper website for AII3, one that i can eventually transfer a lot of my work to and customize a entire website without relying on a external organization or tool (like Mobirise)




### Current page


At the moment the context shown when going to AII3. Org looks like this (see image). I set this up several months ago to simply show that i own the page and that i was planning to build a proper page in the near future. The basic page features a black and white scheme with a slowly appearing ASCII artwork and basic contact info. This work in progress page can still be found on my GitHub


![Mobirise Website Builder](/assets/images/screen-shot-2024-06-23-at-7.38.21-pm.PNG)




### IDEation


Site and layout sketch up


For the AII3 website i wanted to go with a black and white, color scheme. With black being the background and white being used for the highlights for a "terminal" like look. For the layout i decided on 3 key areas: Logo, Projects and Frame. The Logo is a section displaying the AII3 logoProjects is a section that appears like a file system in a computer, with Named folders that contain items that when clicked link to other pages. This will act in place of more tradition methods like a hamburger bar link system. Frame is a section that displays a 3d model wireframe, this changes depending on the item selected


![Mobirise Website Builder](/assets/images/scan0418.JPEG)




### Frame system


Screenshot of plotter vision system


The frame system needs to be able to:1. Display a STL model2. Do so in black and white3. Change the selected model4. Work within React. JSAfter a lot of research i found a open source project that would act as a perfect base that i could Reactor and build up into the frame system i need. Called Plotter-Vision it is based upon the P5. JS JavaScript library. Plotter-Vision: Web GitHub BlogMade by Trammell Hudson


![Mobirise Website Builder](/assets/images/screen-shot-2024-06-23-at-8.00.17-pm.PNG)




##### What is P5. JS?


P5. JS is a JavaScript library for creating interactive, web-based art and design projects. It includes a variety of built-in functions and tools for working with graphics, animation, and input events, as well as support for WebGL, which allows developers to create high-performance 3D graphics and animations. Some examples of what you can do with P5. JS include:* Creating interactive animations and graphics using JavaScript* Implementing input events, such as mouse and keyboard interactions, to create interactive experiences




### Adding P5. JS Into React. JS


Screenshot of the React-p5 library


To do this I used the React-p5 library (Link), installed through the npm command. And leveraging the example sketch while referring back to demos from the P5. JS website i was able to get a basic P5. JS app working within React. JS (shown in the image below)


![Mobirise Website Builder](/assets/images/screen-shot-2024-06-24-at-12.30.09-pm.PNG)




Basic p5. Js app running within React


![Mobirise Website Builder](/assets/images/screen-shot-2024-06-24-at-12.40.14-pm.PNG)




### Getting used to the differences


"pong" app and the code


I've used p5. Js before using their online editor, messing with demos for a bit of fun but have never applied it to a proper app i plan to deploy. To refresh my memory and just get used to the new syntax needed for p5 in React i made a basic "pong" style app to refamiliarize myself


![Mobirise Website Builder](/assets/images/screen-shot-2024-06-24-at-9.07.04-pm.PNG)




### Rebuilding Plotter-Vision into React. JS


Image Description


![Mobirise Website Builder](/assets/images/5.JPG)


