---
categories: ["Work & Services"]
date: '2025-10-06'
description: "I was approached by Mr. Erickson, the principle of Minnetonka High School"
image: "/assets/images/stage-2-1076x605.JPEG"
slug: archie-page-16
tags: []
title: 'Student Assist: Part 1'
---


# Student Assist: Part 1




#### Intro


I was approached by Mr. Erickson, the principle of Minnetonka High School in early December of 2023. He wanted me to create a website where students were able to see what the current class was. As Minnetonka high school's schedule changes everyday depending on the day of the week and a A/B rotation that students find it hard to keep track of.




### stage 1: Barebones


I approached a fellow classmate, Zeen and he informed me that he had already got a very barebones system he can made to help him personally keep track of classes with the older, less complex school schedule. We decided to further improve his basic HTML into a proper PWA (progressive web application) so it could be easily changed and all students could access it from their school issued iPads and personal devices like phones.


![Mobirise Website Builder](/assets/images/stage-1-1076x886.jpg)




Photo of a part of the code made by Zeem, for the generating schedule data using Python.


![Mobirise Website Builder](/assets/images/zeem-1836x1377.jpg)




Zeem's statement on backend work of this time: I started out working on the project from the initial proposal, throwing together a proof of concept that the website would be technically feasible with the software we planned on using for the website (React js webpage + JSON for storing schedule data). The schedule app needs to be able to store the schedules for every day of the school year, and it would be tedious type it out line by line, so I wrote a quick JSON schedule generator in Python (a language I’m more comfortable with). At a high level, it works by taking a JSON file of inputs (specifying things like which dates have different schedules like early releases, which are days off, what events are happening each day, etc), and outputs a JSON file of every day and it’s corresponding schedule.




### stage 2: Basic idea


I contacted Zeen and we worked extremely hard on the project planning out the basics, we started out by making a basic table design on a whiteboard


![Mobirise Website Builder](/assets/images/img-9971-1076x717.jpg)




### stage 3: CSS tables


We started by fundamentally making the basic CSS boxes to fit the general layout we had planned. He started work on some of the translation of secession start and stop times, and I worked on the CSS of the frontend.


![Mobirise Website Builder](/assets/images/stage-2-1076x605.JPEG)




### Step 4: Adaptive div's


The next step was adding a checkbox system to allow for divs to be adapted depending on what lunch hours the user wants to view. The system defaults to all lunch time divs being viewable, and when no lunch times are checked a message returns in it's place that states "Check a lunch period to view"


![Mobirise Website Builder](/assets/images/stage-5-1076x605.JPEG)




### Step 5: Logo fix


We replaced the logo we used as a place holder to be a proper PNG. This was so it could correctly adapted in size and also fit the entire "item1" div.


![Mobirise Website Builder](/assets/images/step-6-1076x510.png)




### Step 6: Bug report


I added a bug report button that leads to a Google form where users can report a bug and upload a photo of the reported issue if needed. The user's email's are also recorded so we can follow up in person or over email is needed


![Mobirise Website Builder](/assets/images/stage-6-1076x1029.jpg)




My father then assisted me on deploying this application to the Azure server he wrote all about the process in detail here




### Setup basic informational Google doc


I setup a basic Google doc, for showing beta testers how to report bugs, and also the current website URL. Alongside some common errors they might occur and also where to properly submit feedback for the project.


![Mobirise Website Builder](/assets/images/doc-694x759.jpg)




### Feedback Google Form


This Google form collects both short answer and basic numerical data. This allows us to see insights at glance. Then also allowss us to dive deeper into feedback on a per user basis.


![Mobirise Website Builder](/assets/images/feedback-form-632x891.jpg)




### Step 7: Implement feedback


Grammar Errors Fixed:

Corrected punctuation errors (replaced periods with successions).


Case Sensitivity Fixed:

Resolved upper/lowercase inconsistencies.


Bug Button Moved:

Improved usability by relocating the bug button.


Lunch Button Default:

Set default for the lunch button to "all false" for simplified use on small devices.


Improved Main Content Adaptability:

Enhanced adaptability of the main content size.


Note: Still awaiting a higher resolution logo image.


![Mobirise Website Builder](/assets/images/7-1076x508.jpg)




### Step 8: Mobile adapt


Use Mobirise website building software to create multiple sites for commercial and non-profit projects. CLIck on the image in this block to replace it. You can add a description below your image, or on the side. If you want to hide some of the text fields, open the Block parameters, and uncheck relevant options.


![Mobirise Website Builder](/assets/images/mobile-323x698.jpg)




### Step 9: Domain config


After a lot of thinking i decided on the domain "studentassist. App" due to it's low price and potential to be used for other school related applications. The domain was purchased through namecheap, they had the best prices and also had many help tools in later configuration. After buying I used the Azure and namecheap panels to add a TXT and CNAME record so they could correctly connect.


![Mobirise Website Builder](/assets/images/domain-1076x377.jpg)




### Step 10: CSS swhicher


If anchor time is present in the current day it is highlighted in Dark blue. The current class period is also highlighted in a light yellow. This allows the user to easily see the most important infomation right away


![Mobirise Website Builder](/assets/images/swhicher-765x569.jpg)




The site was then announced to the school on Mar 12 in the early morning: Below is a short video that shows the announcement




We were also featured several times on the principle's public Instagram account




![Mobirise Website Builder](/assets/images/insta1-876x1194.jpg)


![Mobirise Website Builder](/assets/images/insta2-876x1245.jpg)


![Mobirise Website Builder](/assets/images/insta3-837x2048.jpg)




### Step 11: Post launch fixes


(Google form full of bug report responses)


We then got to work going through over 50 bug reports that we received over the first 3 weeks. Wereviewed the issue and image they submitted then reached out to the individuals if needed when trying to solve the bug.


![Mobirise Website Builder](/assets/images/sheets-1076x655.jpg)




### Step 12: CSS 2.0 sketch


#### the most common problem that was reported was that the UI and UX needed to by improved. A fellow student, Ren agreed to help with the improvement. He started out by sketching a new layout




![Mobirise Website Builder](/assets/images/CSS-improve-2-1076x1286.jpg)


![Mobirise Website Builder](/assets/images/CSS-improve-1-1076x1230.jpg)




### Step 13: CSS 2.0 shell


Next Ren created a basic version of the site with all the new visuals added. Though it didn't contain the "guts" of the application it allowed us to have a idea of a final product and also the gave us the CSS code to achieve it.


![Mobirise Website Builder](/assets/images/shell-1076x511.jpg)




### Step 14: New Countdown Circle System


Students didn't seem to like the clock and also the removal of the "this class end in X minutes" section. So we fixed both problems by implementing a brand new system that allows a circular timer system. It shows how long is left in class based on the how far it has been since the start of the hour. It also changes color depending on the remaining time left in class and has the previously mentioned rendering of the "this class end in X minutes" section that fits within the circle.


![Mobirise Website Builder](/assets/images/sa.jpg)




CLICK HERE FOR PART 2


