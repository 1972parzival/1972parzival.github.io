---
categories: ["Chemistry & Materials"]
date: '2025-10-06'
description: "This is a project i"
image: "/assets/images/image-3.png"
slug: archie-page-59
tags: []
title: The Extruder
---


### The Extruder


#### no further description.




### Background


Variety of extruder idea images


This is a project i've been wanting to do since near the end of last year (2023), but only now after a lot of research and smaller projects do i feel comfortable to pursue it. This project is create a mass market 3d filament recycling system prototype. I'm sure that this will be BY FAR the hardest project i've ever done with issues i can't even fathom at this point in the process.


![Mobirise Website Builder](/assets/images/untitled-design-1.png)




### Recycling? Really?


Economics notebook page


That's your big idea? Is what i would assume you are thinking at this point, and it's a fair critic. So let me break down the economics of a system like this and why is doesn't already exist. Economics: Why now:


![Mobirise Website Builder](/assets/images/5.jpg)




### The general idea


I've written tens of sketches for the system all with conflicting details, but i will try and convey the general idea. This Plastic extruders will work by taking a large sample of plastic (of un-uniform shape). then a grinder mechanism plastic is melted and ground into a certain size and general shape referred to as pellets. These pellets then fall between the groves of a rotating screw and are then heated and rotated to the end tip with a specific diameter. It exit's as a line of plastic which is then rapidly cooled repeatedly along a spool until the initial sample is fully processed or the spool is full. Once it has fully cooled it is referred to as filament and is able to be used in various commercially available 3D printers. In review there are 4 general "sections":1. The "Hotbox" (heat it and crush it)2. The "Screw" (make it a line)3. The "Cooler" (keep it that way)4. The "Spooler" (wrap it up for storage)


![Mobirise Website Builder](/assets/images/image-3.png)




### The "hotbox" notes


Scan of notebook page


I started by coming up with a lot of ideas on how to melt the plastic. After a lot of testing i decided on thin nichrome wire. Next was thinking about how i could support the metal wire with cheap material that i could use and without shorting it. One of these which showed promise was the nail idea, but as stated in the notes it would only work if: -Heat at the intersection of the print and nail is less then the heat required over a long period that would deform plastic -No "hot spots" or (electrical) shorts form due to the wounding of the nail


![Mobirise Website Builder](/assets/images/img-129.JPEG)




#### Small scale testing




### 3D modeling


After a lot of planning and modeling i decided on this general configuration: Two bases: Each with 25 screw holes for a total of 50 and shifted by 90 degrees so that the nichrome wires cut different sections each level 4 support rods: Hold the bottom base and also provides general support 4 rod holders: Support the top layer of the base from the tops of the support rods


![Mobirise Website Builder](/assets/images/screen-shot-2024-10-07-at-1.09.12-pm-1.png)




### basic model


Printed out this model but then figured out it was much too small, still provided a good visual aid for planning and increased my confidence in the general plan.


![Mobirise Website Builder](/assets/images/img-20241008.JPEG)




### IT WORKS. Kinda


Photo of the "hotbox" with the nichrome wire on a smoking


With a 600W power dissipation and the length of 1540 mm, the Nichrome wire could reach temperatures in the estimated range of 800°C to 1000°C. During these tests it did actually "slice" several items perfectly, and once slightly cooled they were extremely Brittle and broke into pieces (hopefully) easily processed by the grinderSome issues did certainly arise that can be adjusted for: Such as the wires slipping due to the physical expansion of the wire from great heat.(fix with wounding every nail point not just the ending terminals)alongside the issue of ambient heat leading to the plastic bed of the hotbox melting and bending inwards.(will be reduced with less slipping and also by reinforcing the bed in general with more material and support)Finally the issue of smoking from plastic residue left over. (will be resolved through air extraction and filters)


![Mobirise Website Builder](/assets/images/img-2279.jpg)




![Mobirise Website Builder](/assets/images/img-2277.jpg)


![Mobirise Website Builder](/assets/images/img-2276.jpg)


![Mobirise Website Builder](/assets/images/img-2275.jpg)


![Mobirise Website Builder](/assets/images/img-2278.jpg)


![Mobirise Website Builder](/assets/images/img-2279.jpg)




### New Model


The new model includes:- Thicker bottom along screw lines - "v shaped" supports on both sides to provide better stability - areas at the top of v supports to hold the screw in place and reduce the bending during prolonged heating


![Mobirise Website Builder](/assets/images/screen-shot-2024-10-17-at-1.05.26-pm.png)




### New sketchs


Scan of notebook pages


Page one showsPage two showsPage three shows


![Mobirise Website Builder](/assets/images/untitled-design-5.png)




#### New Model Video test




#### Video Test Notes


Fire! But before we get to that let's look at the good stuff. So why the fire?




### Let's Talk About Not Dying


Yes while safety is not as exciting as designing and testing seeming that most of the obvious issues with the hotbox have been solved or highly reduced. Now is a good time to discuss it with it being on of the more openly dangerous parts of the Extruder.1. Nichrome wire: 2. Material buildup: 3. Particulates: HEPA filters are designed to capture at least 99.97% of airborne particles that are 0.3 microns in diameter, which covers most of the particulate matter produced when PLA burns or melts. This would remove the tiny solid particles suspended in the smoke.2. Gases and VOCs: Activated carbon filters are excellent at adsorbing gaseous pollutants like the volatile organic compounds (VOCs) that can be released when PLA plastic is burned. This includes fumes like formaldehyde and other organic gases.


![Mobirise Website Builder](/assets/images/7ba8ded63dfc6ebd993e4b90e37389b9.JPEG)




#### Additional recorded test




### Grind it or Blend it?


Notebook scan (tape contains plastic sample)


![Mobirise Website Builder](/assets/images/scan0445.JPEG)




![Mobirise Website Builder](/assets/images/img-2327.jpg)


![Mobirise Website Builder](/assets/images/img-2328.jpg)


![Mobirise Website Builder](/assets/images/img-2329.jpg)


![Mobirise Website Builder](/assets/images/img-2330.jpg)


![Mobirise Website Builder](/assets/images/img-2331.jpg)


![Mobirise Website Builder](/assets/images/img-2334.jpg)


![Mobirise Website Builder](/assets/images/img-2335.jpg)


![Mobirise Website Builder](/assets/images/img-2336.jpg)


![Mobirise Website Builder](/assets/images/img-2338.jpg)


![Mobirise Website Builder](/assets/images/img-2341.jpg)




Hotbox + blender example workflow shown1. Raw part -> 2. Sliced and Melted -> 3. Cool then Blended


![Mobirise Website Builder](/assets/images/img-2341.JPEG)




### Grinder Funnel modeling


Screenshot of 3d model


After the general "workflow" of the blender seemed feasible, I began to model up the blender funnel concept as outlined on the previous notebook scan. The model has a maximum diameter of 187.045 mm and contains a blender screw in the center. This leads to plastic bits being broken and thrown repeatedly until they're the right size to fall through the gaps provided. The size of the gap is the also roughly the maximum size of a part that can flow through it or the rough "pellet size". After falling through the filter they fall into a the dish below, which exists to capture the plastic (only for the initial testing).


![Mobirise Website Builder](/assets/images/screen-shot-2024-10-30-at-10.11.16-am.png)




#### Grinder Funnel Testing




### Buying extruder materials


Photo of some parts in the order of assembly use


It was at this point where i felt that the blender and hotbox were both proven as a general concept and had been tested. So i felt comfortable with investing more so i could build out the "Screw" part of the extruder where the small bits of plastic are melted down into a line of filament. Over the course of 2 days i biked down to my lower hardware store with my caliper and measured a bunch of parts 3d printed parts for reference and wrote down all prices and items i might need, on the second day i had all those parts printed out so i could test everything to make sure it was the best i could get before spending a single cent. Now it was off to the metals shop to work on it.


![Mobirise Website Builder](/assets/images/462539463-526746057001740-4894787199600369959-n.JPEG)




![Mobirise Website Builder](/assets/images/att. Ozhmofeuxq-aqrrxilszs04efjyfdzei-tpwfrrp2se.jpg)


![Mobirise Website Builder](/assets/images/att. F16yi7y5jcgwo6pglrlgs5d6q1ess0bftafy-ga5v3a.jpg)


![Mobirise Website Builder](/assets/images/462540918-1085193753085514-4468653704278786118-n.jpg)


![Mobirise Website Builder](/assets/images/462539463-526746057001740-4894787199600369959-n.jpg)




![Mobirise Website Builder](/assets/images/att. Kke6pmjoqcbur9bwajj97tcq-aqsszuxp4c6-4pz8nw.jpg)


![Mobirise Website Builder](/assets/images/att. Yih8l4tdycwobfkxm-22i1cr-jxj7mdusaaanjop2k4.jpg)


![Mobirise Website Builder](/assets/images/att.-cccynzaitlg16bmlvyvfcehdi8veunylcebfxio1cs.jpg)




#### Shop work




#### Shop work 2




#### Shop work 3


##### (friend helped out with angle grinder)




![Mobirise Website Builder](/assets/images/img-2378.jpg)


![Mobirise Website Builder](/assets/images/img-2380.jpg)


![Mobirise Website Builder](/assets/images/img-2381.jpg)


![Mobirise Website Builder](/assets/images/img-2382.jpg)


![Mobirise Website Builder](/assets/images/img-2383.jpg)




### Water "Cooler" + Puller system


Photo of the system


I also moved on to testing a the cooling system after the filament had been extruded and a potential pulling system for once the filament had been cooled. The cooling system did not have the right valve size for the pump i wanted to use. The pulling system did not have enough torque with the motor i wanted to use so i will gear it down and try again. So will both require further modeling and can only be really tested after Hotbox, Blender and Screw are all in a functional state.


![Mobirise Website Builder](/assets/images/img-2399.jpg)




#### Over-Voltage (240v) Test


##### (point of failure not captured)




Over-voltage results after point of failure (note several points of nichrome wire breakage)


![Mobirise Website Builder](/assets/images/screen-shot-2024-11-10-at-5.40.13-pm.png)




### Wiring improvements


Burned out aligator clip (from 240v test)


Ever since the start of the hotbox i have been burning through my aligator clips and the thin copper that connects them. I know they're not rated for anything even close to 120 volts but they were all i had that suited the task at the time. Finally after the 240v test i knew that i really needed to upgrade, but with no wire on hand that would handle mains voltage i had to get creative. I found a data wire that contained 8 copper leads and separated them in two at both ends, then soldered them and added old aligator clips. Giving it just enough wiring in total that it should be able to handle mains voltage.


![Mobirise Website Builder](/assets/images/img-2406.jpg)




![Mobirise Website Builder](/assets/images/img-2406.jpg)


![Mobirise Website Builder](/assets/images/img-2408.jpg)


![Mobirise Website Builder](/assets/images/img-2410.jpg)


![Mobirise Website Builder](/assets/images/img-2412.jpg)




### hotbox redesign


Photo of the updated model


Additions include:-added a lip on all corners so the the frame is more snug-increased the width of the top support so nails can fit better


![Mobirise Website Builder](/assets/images/screen-shot-2024-11-10-at-5.03.07-pm.png)




### Blender Cup redesign


Photo of the improved model


To fix the "overflow" issue and take advantage of "jitter" from the blending motion i modeled a funnel around the bottom of the Blender cup. This will allow for all the material to slowly slide down into a much smaller point that will make it easier to be extruded.


![Mobirise Website Builder](/assets/images/screen-shot-2024-11-10-at-5.28.58-pm.png)




#### Failed blender cup print




#### Blender cup testing




![Mobirise Website Builder](/assets/images/img-2437.jpg)


![Mobirise Website Builder](/assets/images/img-2438.jpg)


![Mobirise Website Builder](/assets/images/img-2440.jpg)




### Initial cooler design


Photo of the system


I Started off with a design whereby there are two pipe running, one running to the top platform, and the other to the base of the bottom. Each connected to their respective area of the pump. The goal was to create a consistent    "overflow" effect off of the platform. This effect allows cooling in a straight line without warping the shape of the final plastic. Unfortunately the design didn't function as intended. With the output valve being on the same level as the input the pump didn't have enough force even at a stable 12 volts to properly pump the water. Leaks were also frequent due to loose valves.


![Mobirise Website Builder](/assets/images/img-2453.jpg)




#### Cooler test




### Cooler with improvements


Photo of the new design


While not perfect, large strides were made with this new version. Instead of having a output valve on the bottom it is shifted to the top over the center of the top platform and also prints better and seals tighter as a result. While some splash and minor leaks do occur it is far reduced from previous tests and can be improved with better power control of the motor and further iterations of the valve designs until they all have a tight fit.


![Mobirise Website Builder](/assets/images/img-2481.jpg)




#### New Cooler test




### A "duck tape" extruder test


Top: Test setupBottom: View of the tube at the end of the test


For heating i plan on using two proper band heater elements that have yet to arrive, i also have yet to assemble the stand for the extruder but i wanted to do a simple test to get a idea of things. So i used some "Kapton" tape i had bought for this project and made a simple winding of nichrome between two layers of it around the pipe. Then to act as a "motor" as used a simple drill with it's chuck attached to the extruder screw. Of course i knew this was unlikely to work but wanted to do anyways to observe results. Here is what i found:1. As i had expected the one coil of nichrome was not nearly enough to fully melt the plastic2. The rotational force on the pipe enabled by friction is actually much higher then i had expected even removing the wire leads at times. So it's important to make a strong stand and account for this properly.3. The 1-2 mm difference in diameter between the pipe and the extruder didn't seem to be a core issue faced by the extruder as i had so deeply feared, but it will still remain a worry to keep in mind throughout later testing


![Mobirise Website Builder](/assets/images/screen-shot-2024-11-15-at-4.41.02-pm-1.png)




### SRR testing


Photo of the ssr controling the mains voltage of the hotbox


The SRR or "solid state relay" is a device that acts as a intermediate allowing for the control of mains voltage from a low power device similar to a common MOSFET. By inputting the positive and negatives of a dc power source we can allow for power to flow through the hotbox and provide the required heat. This power source can be anything but in my case will be controlled by a microcontroller (like an ardunio) such that we can control the temperature automatically using PWM or "pulse width modulation"


![Mobirise Website Builder](/assets/images/img-2484.jpg)




#### SSR test video




### Cooling peltiar


The thing i will be using for the cooling of the water is a peltiar device, which when voltage is applied across it, cools once face of it and heats the others, when used in combination with a small amount of thermal paste and a heat sink and fan to remove heat from the hot side. It will allow for cooling of at most 30 degrees less then ambient (20 degree room, gets cooled to -10)


![Mobirise Website Builder](/assets/images/4.jpg)




#### peltiar demo




### building out the "shell"


Whiteboard drawing


Now that i seemed to have a basic setup for many of the core components of the extruder i decided to shift my focus into that of the areas that connect them together. Such as, The shell which lays on top of the covering of the blender cup and contains within it both of the outtake fans and the main hotbox area alongside with the lid covering it all.  I also decided to add arc like under-hangs onto both of the outtake fans to provide a easy grip point when doing general maintenance or a home repair


![Mobirise Website Builder](/assets/images/img-2498.jpg)




### Modeling general improvements


Altered screenshot of the exploded view


- modeling of the shell - modeling of the intake fan assembly - modeling of the outtake fan assembly - added holes to the blender cup such that the intakes can fit- model rods such that they tightly fit along the lid, hotbox, and cup lid- modeled a lid that includes a fully print in place hinge and a fully print in place clasp


![Mobirise Website Builder](/assets/images/image-5.png)




#### Filter fan (out-take) testing




### Spool holder (Drill chuck)


Typically when using filament a spool merely sits on a loose rod where it PULLED by a stepper motor and therefore slowly unwound by like one wheel of a old cassette tape. So all we have to do is that in reverse right? Have a stepper motor PUSH the filament forward and therefore it'll wrap around a empty spool. Well no, for a lot of reasons: 1. Filament is still soft, even after the water cooling and being exposed to the air it is still likely to be soft enough that it couldn't just be pulled by gears2. Shape is memory, and things just want to be. When you pick up a roll of filament and mess around with it you'll see that it wants to remain curved, if you pulled it right off the spool yourself you'd see that it wants to shoot right back to shape like a Spring of a slinky toy. This is because when it was cooled it was cooled on the spool so it naturally has an arcing shape that we want to slowly introduce. If you were to "just push" a line of filament that is attached at some point it was just fall right off the spool and collect as a mass at the bottom. So in a perfect world we'd have a spool itself rotating slowly so that slightly filament collects onto the spool and then slowly fully cools over a longer period leading to a proper spool of filament that keeps it's arcing shape. My idea to achieve this? A Drill chuck of some kind.


![Mobirise Website Builder](/assets/images/untitled-design-2.png)




### Spool holder's eternal series of model adjustment


Photo of some of the modeling process for the spool holder


Starting from a simple drill chuck there was a LOT that had to be done to make it work how i wanted. So much so that i even considered not calling it a chuck mechanism at all as it's function and purpose is just so different. The three main goals were to make something that allows you to easily and automatically swap in and out spools, make it hold at least 1kg for it's lifetime, and make it work with as many spools as possible. The simplest way to think about how the chuck achieves this is think of a typical drill chuck as the 2nd ring rotates the 3 rails rotate inward and apply force evenly onto a drill bit. On my design i am doing them same only apply the force outwards instead of inwards, sadly while this sounds easy there is no magic "inverse mechanism" button so it took a lot of trial and error in the modeling process very reminiscent of Spray Assist project i did a while back. Finally i got it working and evenly applying force with no bending from the 1kg load. I think this is by far one of the coolest things to watch work and also just generally look at that i've made. I also could see it being applied to other stuff like rope/coil winding and the like in companies or my own future projects.


![Mobirise Website Builder](/assets/images/screen-shot-2025-01-19-at-1.52.00-pm.png)




Current Version


Original chuck


![Mobirise Website Builder](/assets/images/img-2513.jpg)


![Mobirise Website Builder](/assets/images/screen-shot-2025-01-14-at-10.17.02-am.png)




#### Spool holder's Drill chuck demo




![Mobirise Website Builder](/assets/images/img-2507.jpg)


![Mobirise Website Builder](/assets/images/img-2510.jpg)


![Mobirise Website Builder](/assets/images/img-2513.jpg)




### YES! FINALLY!


Photo of the moment right before first extrusion.


I'm been thinking about the first moment i ever produced some filament from the end of extruder for about a year now ever since i started and today WAS THAT DAY. It worked and man was it a sight to behold forget xmas just do really hard engineering for a year and wait for the payoff. It feels really good, still a long way to go of course but everything from here is essentially refinement of stuff i've already tested or common stuff that i won't (hopefully) have to reinvent the wheel to use.(no video sorry my camera was glitching out)


![Mobirise Website Builder](/assets/images/472888776-2486871558326557-2628943443205828915-n.JPEG)




![Mobirise Website Builder](/assets/images/470805436-626018406480880-7481670470792383872-n.jpg)


![Mobirise Website Builder](/assets/images/472821627-904808808303509-5646964069695914104-n.jpg)


![Mobirise Website Builder](/assets/images/472888776-2486871558326557-2628943443205828915-n.jpg)


![Mobirise Website Builder](/assets/images/472933596-1282163366420047-2291555244438923830-n.jpg)


![Mobirise Website Builder](/assets/images/473254856-1143744533776649-4836493582007264689-n.jpg)


![Mobirise Website Builder](/assets/images/473329843-639574345184983-4078217687092683196-n.jpg)


![Mobirise Website Builder](/assets/images/473522707-1224661882616746-7065925845537224163-n.jpg)


![Mobirise Website Builder](/assets/images/473524930-8998383740255731-1567929277613096163-n.jpg)


![Mobirise Website Builder](/assets/images/473689387-1126865562314066-1105434323274184405-n.jpg)




### Main Assembly Testing


Use Mobirise website building software to create multiple sites for commercial and non-profit projects. CLIck on the image in this block to replace it. You can add a description below your image, or on the side. If you want to hide some of the text fields, open the Block parameters, and uncheck relevant options.


![Mobirise Website Builder](/assets/images/img-2518.JPEG)




![Mobirise Website Builder](/assets/images/img-2525.jpg)


![Mobirise Website Builder](/assets/images/img-2526.jpg)


![Mobirise Website Builder](/assets/images/img-2527.jpg)


![Mobirise Website Builder](/assets/images/img-2528.jpg)


![Mobirise Website Builder](/assets/images/img-2529.jpg)


![Mobirise Website Builder](/assets/images/img-2523.jpg)


![Mobirise Website Builder](/assets/images/img-2524.jpg)




![Mobirise Website Builder](/assets/images/img-2530.jpg)


![Mobirise Website Builder](/assets/images/img-2531.jpg)


![Mobirise Website Builder](/assets/images/img-2532.jpg)




#### Two extruder test (with stand)




![Mobirise Website Builder](/assets/images/img-2540.jpg)


![Mobirise Website Builder](/assets/images/img-2541.jpg)


![Mobirise Website Builder](/assets/images/img-2542.jpg)


![Mobirise Website Builder](/assets/images/img-2543.jpg)




### Thermocouple


Thermocouple i am using (MAX6675)


The reason for the puddle of plastic seen in the two extruder test is simply, heating the nozzle above the temp that it needs to be. Of course i planned for this and so we need something to "check and balance" the output of the band heaters, i decided to use a Thermocouple. The one i used was rated to up too 1 thousand degrees but as we will only be using it need roughly 200 degrees that limit shouldn't matter. Once again it's job is simple to keep the temp of the nozzle (not exactly of the entire system or the band heater itself) at roughly "X" degrees. We don't know what "X" is exactly but it's going to likely be within the 150-250 degree range for most plastics and it will also be software defined so we can change it if needed. When the Thermocouple reads the temp at above "x" it will turn the band heater off and when below it will turn it on, leading to a cycle of states and a roughly consistent temp for the plastic.


![Mobirise Website Builder](/assets/images/screen-shot-2025-02-22-at-4.34.02-pm.png)




#### Thermocouple + SSR testing




Unscaled temp data


Scaled temp data


![Mobirise Website Builder](/assets/images/screen-shot-2025-02-22-at-4.13.23-pm.png)


![Mobirise Website Builder](/assets/images/screen-shot-2025-02-22-at-4.13.10-pm.png)




### Thermocouple upgrade


Photo of the new nozzle with the welded nut


Using a 1 ended nut i welded the end near the nozzle such that the thermocouple can screw into the 1 ended nut and accurately read the temperature at the nozzle. The next thing to achieve is now that we have a more accurate reading then just taping the thermocouple to the nozzle. We need to work on a proper system that will able to keep a consistent temp at the nozzle by controlling the band heater through use of the SSR.


![Mobirise Website Builder](/assets/images/snapchat-1959016579.JPEG)




![Mobirise Website Builder](/assets/images/snapchat-819906141.JPEG)


![Mobirise Website Builder](/assets/images/snapchat-1879175453.JPEG)




#### Blender motor testing


