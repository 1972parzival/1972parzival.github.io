---
categories: ["Engineering & Mechanical"]
date: '2025-10-06'
description: "i was merely sitting down thinking about gears, specially circular gears and wondering how they came into being and how they were first modeled. so the purpose of this post is to try and recreate a."
image: "/assets/images/4.jpg"
slug: archie-page-65
tags: []
title: Understanding Gears
---


### Understanding Gears


#### Through the lens of math




### Initial thoughts


Notebook Scan


I was merely sitting down thinking about gears, specially circular gears and wondering how they came into being and how they were first modeled. So the purpose of this post is to try and recreate a way to create gears using only simple programming tools like arrays and basic mathematics. I am not going to do any research on how they were made in the past or leverage AI in questioning as that would ruin the spirt of the challenge. Now to break down my thoughts on the subject. A gear in the most simple sense is just a function of gaps and material that link together. Shown in the top left where there is a roughly half section of 0 height and the second half with a linear rise flat top and linear fall, I have termed this as a "gearic cycle" on way to think of this is as the default state like in a straight gear where this gearic cycle just repeats along it's length. When we are thinking in terms of a circle the gearic cycle is the result of a infinite radius with that cycle applied. At infinite radius the distance between A and B is at it's maximum value, and as radius decreases from infinity the distance between A and B decreases as it's affected by the arc. This is of course assuming the size of the gearic cycle is constant and doesn't directly scale as we decrease from an infinite radius.  as far as equations go we know that the distance around a circle is C = 2(pi)R. We can also gather through logical thought that length of arc (for a gearic cycle) divided by the distance around a circle is the maximum number of possible cycles C/L=N (or C/N=L)Thereforen= (2(pi)R)/L and R = (NL)/2(pi)So we can now gather that the ratio between gears is fundamentally determined by the difference in the number of cycles consumed. Allowing us to estimate the radius of two circles with a cycle length of 1 that would result in a 20:1 ratio (shown in picture)


![Mobirise Website Builder](/assets/images/4.jpg)




### But how do i apply a gearic function to a circle?


Circle Properties Visualizer


Use Mobirise website building software to create multiple sites for commercial and non-profit projects. CLIck on the image in this block to replace it. You can add a description below your image, or on the side. If you want to hide some of the text fields, open the Block parameters, and uncheck relevant options.


![Mobirise Website Builder](/assets/images/screen-shot-2025-01-23-at-10.23.56-am.png)




### Resulting code


Use Mobirise website building software to create multiple sites for commercial and non-profit projects. CLIck on the image in this block to replace it. You can add a description below your image, or on the side. If you want to hide some of the text fields, open the Block parameters, and uncheck relevant options.


![Mobirise Website Builder](/assets/images/4.jpg)


