---
categories: ["Creative & Media"]
date: '2025-10-06'
description: "transferring the ideas in my head to sketches on paper went really well-"
image: "/assets/images/sa.JPG"
slug: archie-page-40
tags: []
title: 'Student Assist: Part 2'
---


### Student Assist: Part 2




##### IDEation


Transferring the ideas in my head to sketches on paper went really well- i did the sketch up of the idea for a proper “Multi-Page” system to help me get a better idea of what sections will link to other section (fig 1)- i did the sketch up of the idea for the course planner UX/UI to help me get a better idea of what i will need to have in the CSS and what kind of rendering processes i will need to program  (fig 2)




![Mobirise Website BUIlder](/assets/images/scan0412.JPEG)


![Mobirise Website BUIlder](/assets/images/scan0411.JPEG)




### Step 15: Multi-Page Testing Locally


Photo of the basic local host version


I coded up the basics of the “multi-page” system and got it working great on a locally hosted copy og the site with some very basic CSS. Transferring some basic CSS from the old site (background color, font, lunch button etc) into the locally hosted home page to help get a general idea of what the final homepage could look like relative to my sketch. I ran into some problems when trying to integrate SVG image files that are open to the public into the application but eventually found my own detailed work around that allowed them to display correctly. I also ran into some problems with links and sub-URLs but was able to fix after finding a thread discussing the common issue within the React library


![Mobirise Website BUIlder](/assets/images/home-test.JPG)




### Step 16: Multi-Page Testing Hosted


Photo of the basic hosted version


I worked hard on getting the system hosted, it initially didn’t work but after researching online i found out that due to using Azure as the hosting system, i had to add both a web configuration file and a “staticwebapp. Config. JSON” file on top of the BrowserRouter system for React. After making those changes the multipage system was properly hosted.


![Mobirise Website BUIlder](/assets/images/hosted.JPEG)




### Step 17: Basic DND


One thing that was really hard was finding and implementing a Drag and drop (DND) system. I eventually decided on DNDKIT because it works well with React and has a lot of internal documentation from the organization that made it and external documentation and gUIdes from the larger online community.


![Mobirise Website BUIlder](/assets/images/dnd.JPG)




### Step 18: Skipper Log


Screenshot of the raw HTML


One thing that went really well was getting the raw HTML from the Skipper Log ( a site that contains all course information). I didn't have access to the backend of this website as it is controlled by the school. So I will need to get the Raw HTML and slowly turn it into a JSON class through a lot of Python scripts that i will need to write.


![Mobirise Website BUIlder](/assets/images/raw-HTML.JPG)




### Step 19: Basic Div Sort


Another thing I accomplished was getting a basic div sorting system working by following an online gUIde on how to do so. This allows the next step of combining it with DND to get sortable objects that can be dragged and dropped with properties that I can sort by.


![Mobirise Website BUIlder](/assets/images/div-sort.JPG)




### Step 20: Tv Sign


The page made for the sign as discussed


I also noticed that the school's library was displaying the site on one of the many sign TVs throughout the school. And noticed right away that the formatting looked wrong and it didn't display the lunch, after a 30 minute meeting with person running the TV sign system, I found out that it is using Raspberry Pi's running a Yo-Duck system. After the meeting he recommended that I use the new multipage system to create a much more basic subpage of the site specifically for the tv signs. That is exactly what I did over about a week. I'm happy with how it turned out


![Mobirise Website BUIlder](/assets/images/sign.JPG)




Image of the current Draggable Div Sort demo


![Mobirise Website BUIlder](/assets/images/demo2.JPG)




#### Step 21: Draggable Div Sort


As previously mentioned I started to combine the draggable system with sortable Divs alongside replaced the old JSON with the proper JSON of the courses. That I made from the skipper log I created using the data from the raw HTML of the skipper log. Still has a lot of bugs within the JSON and with the draggable system system interacting with the sorting system. Over time I believe I should be able to slowly fix all the bugs and get a reliable system




### Step 22: Touch controls


Photo of the 3 sections that allow for touch controls


I researched online to find the correct way to add touch control for the drag and drop system. I then implemented it using the code shown here


![Mobirise Website BUIlder](/assets/images/codedemo.JPG)




#### End of Year Meeting


I Booked the end of year for May 29 as the entire team was able to make it to the meeting. Though due to the date's proximity to the end of the year we were only able to get a 30 minute time slot. Fortunately we were able to cover everything on the meeting outline (in picture shown below). Results of the meeting and general discussion:- Discussed general ideas for the course planner and set out clear gUIdelines to ensure student privacy - Plans for a mobile app version of the site that can be pushed to all student devices through the school- Having all new students be instructed to add the app to their home-screen during freshman orientation- Planned for a meeting during the summer to further discuss progress more towards the end of the school year




Group photo of: Me, Dris, Zeen and Ren

(left to right)


![Mobirise Website BUIlder](/assets/images/meeting.JPG)




Me pictured in front of one of the school's TV signs now running the student assist tv sign software


Screenshot of the full document I had made of what was to be discussed at the meeting


![Mobirise Website BUIlder](/assets/images/meeting2.JPEG)


![Mobirise Website BUIlder](/assets/images/meeting3.JPG)




#### Comp Sci Presentation


I used a lot of new updates to student assist for my end of year project for IB Computer science HL, it went very well and it was interesting to answer fellow student's questions and listen to their suggestions for further improvements. They also seemed to enjoy the demos I had created for testing the DND and sorting systems. Below is the slide deck I made and used for my presentation.




![Mobirise Website BUIlder](/assets/images/student-assist-page-1.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-2.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-3.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-4.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-5.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-6.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-7.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-8.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-9.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-10.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-11.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-12.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-13.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-14.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-15.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-16.JPG)


![Mobirise Website BUIlder](/assets/images/student-assist-page-17.JPG)




### New UI IDEas




![Mobirise Website BUIlder](/assets/images/UI3.PNG)


![Mobirise Website BUIlder](/assets/images/UI.PNG)


![Mobirise Website BUIlder](/assets/images/UI2.PNG)




### Step 23: Popup Alert


After reviewing a lot of the old bug reports i found out that the most common issue (which we had fixed) was not having the lunch period saved locally. The fix for this is to click on what lunch they have before they save to home-screen as that we mean they never have to reselect their lunch as it's saved in the URL data. To Inform users of this product feature and increase usage overall, we integrated a popup for new users. We were able to this as a local device var displays the number of times the app has been used (displayed in part 1). Then we just apply the HTML popup when the Var is less than 3 sessions. This feature was coded up by Dris.


![Mobirise Website BUIlder](/assets/images/screen-shot-2024-09-03-at-7.18.27-pm.PNG)




### Step 24: Course Planner Updates


Screenshot of current version


After about a month of discussion and development with Ren over the summer, he bUIlt up a Frontend mockup of the skipper log based on my initial sketch and proposal. After that I converted it into a React function and then deployed it to the /planner of the site. Since them i have added new color scheme and a scroll bar so the mock courses can be scrolled through.


![Mobirise Website BUIlder](/assets/images/screen-shot-2024-09-06-at-12.28.37-pm.PNG)




### Start of School Meeting


During the start of year meeting we discussed the start of year launch, work done regarding the course planner, and the possibility of using the Schoology API to safely leverage student data in the near future.


![Mobirise Website BUIlder](/assets/images/img-1675.PNG)




Page two: Showing a data diagram for possible token system


Page one: Showing of overview of the meeting topics (same as to end of year meeting)


![Mobirise Website BUIlder](/assets/images/screen-shot-2024-09-16-at-8.10.52-am.PNG)


![Mobirise Website BUIlder](/assets/images/screen-shot-2024-09-16-at-8.10.45-am.PNG)


