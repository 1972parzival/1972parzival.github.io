---
categories: ["Academic & Documentation", "Electronics & Arduino"]
date: '2025-10-06'
description: ""
image: "/assets/images/campus-bg-1920x1079.JPG"
slug: archie-page-23
tags: []
title: "murray state"
---


### Murray State Parking project




#### Background


"I was approached by Boaz to collaborate on his college project, which involves creating a parking lot system accessible through a website. The goal is to enable students to check the availability of parking spaces. Acknowledging the complementarity of Boaz's background and my proficiency in Arduino and microcontroller systems, I enthusiastically agreed to contribute. My motivation stems from a genuine interest in gaining collaborative experience, working within a team, and contributing to a project with importance to the college. This collaboration is not driven by financial incentives but rather by the opportunity to enhance my skills and contribute to a meaningful project."




### core concept


The core idea of the project is to setup these systems on either side of the entrance/exit, each side will have 2 long range ultrasonic sensor for detecting the passing of cars on that side. Each side will also includes a IR beam and a IR receiver. All the data from the i receivers and the ultrasonic sensors will be fed back to the microcontroller that will then send relative updates over LoRa to a WiFi connected server that will publish new infomation to the public website


![Mobirise Website Builder](/assets/images/blank-diagram-1076x598.PNG)




##### Why Have Both Ultrasonic Sensors And IR Beams?


The effectiveness of ultrasonic technology lies in its sensitivity to all physical materials, which makes it a valuable asset. However, this sensitivity also introduces a potential vulnerability. Elements such as water, leaves, or mud can obscure the sensor, causing issues in accurate readings.


To addressss this concern, we incorporate an infrared (IR) system into our setup. The IR system plays a crucial role in ensuring that when the ultrasonic sensor detects a spike, the reading is reliable and not influenced by external factors. Moreover, this dual-system approach allows us to quickly identify any buildup of physical materials. In the event of such buildup, we can promptly report it, enabling swift deployment of personnel to remove the obstruction and maintain the system's optimal functionality.




### demo


I was able to build a basic short range sensor version using part i had on hand alongside with ultrasonic sensors bought by Boaz for this testing. I made a basic program for receiving the two signals that can be found here: CODE


![Mobirise Website Builder](/assets/images/murray-1076x2511.JPEG)




#### basic demo


##### sorry for poor quality




#### The End


Soon after showing the progress in the MVP above, Boaz decided that it would be better to focus on a mobile app (using swift) using a Machine Learning approach instead of using ultrasonic and IR beam break sensors. Due to my of experience in those areas i told him i would not be able to help further, he understood and we are still in contact and in good standing. Overall i am glad i was able to help with this college level project at all and i'm happy with the ideas i contributed.


