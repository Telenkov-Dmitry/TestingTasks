## Plane landing.

Before going for the landing a plane receives a status report from the airport. The report contains two risk factors, **wind** and **pressure**. Based on them, **total_risk** is calculated with the formula:

$$total\underline{ }risk = 5\cdot wind + 4\cdot pressure$$


1. If **total_risk** is not higher than **37**, the plane can land.
2. If **total_risk** is higher than **37** but less than **46**, the plane will not be able to land safely and therefore should stay in the air, waiting for better conditions. 
3. If **total_risk** is **46** or higher then the plane should fly to another airport. 

You are asked to test the program, which decides whether a plane should land or not.

Input: 

**wind** $\in$ **[0, 10]**

**pressure** $\in$ **[0, 10]**

Output:

**decision** $\in$ **{“land”, “stay in the air”, “fly to another airport”}**


## Collision avoidance.

Nowadays cars with autopilot are becoming more and more popular. You are asked to test a part of a program for such autopilot. The part is responsible for avoiding collisions with objects in front of a car. When car’s sensors spot an object, they send **distance** to the object(meters) and current **speed**(km/h) to the function we are testing. Based on this data the car should either “**Keep current speed**”, “**Slow down**” or “**Use brakes**”. 

During physical tests, it was derived that there can be six different situations in collision avoidance:



1. Distance is lower than **5** - **Use brakes**
2. Distance is higher than **100**, speed is lower than **50** - **Keep current speed**
3. Distance is higher than **100**, speed is not lower than **50** - **Slow down**
4. Distance is $\in$ **[5, 100]**, speed is lower than **30** - **Keep current speed**
5. Distance is $\in$ **[5, 100]**, speed is in **[30, 60)**  - **Slow down**
6. Distance is $\in$ **[5, 100]**, speed is not lower than **60** - **Use brakes**

You need to test whether **collision_avoidance** function outputs the right **action** depending on the **speed & distance** pairs.

Input: 

**distance** $\in$ **[0, 200]**

**speed** $\in$ **[0, 100]**

Output:

**action** $\in$ **{“Keep current speed”, “Slow down”, “Use brakes”}**


## Underwater diving.

Underwater diving is known to be a dangerous activity. One of its many threats is a risk of decompression sickness, which increases the longer and deeper you stay underwater. To help divers, you are asked to test a simple program, which calculates approximate risk of getting a decompression sickness. The program uses **time**(minutes) and **depth**(meters) as input. Based on them it calculates **decompression_risk**:

$$decompression\underline{ }risk = time * (depth)^2 / 60$$



1. If **decompression_risk** is less than **100**, it is considered negligible
2. If **decompression_risk** is $\in$ **[100; 225)**, it is considered low
3. If **decompression_risk** is not less than **225**, it is considered high and the diver in question should return to the surface while performing decompression procedure

Depending on **decompression_risk** and rules 1)-3), the program should output either “**no risk**”, “**low risk**” or “**high risk**”

Input: 

**time** $\in$ **[0, 60]**

**depth** $\in$ **[0, 20]**

Output:

**decision** $\in$ **{“no risk”, “low risk”, “high risk”}**
