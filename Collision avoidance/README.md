

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

## Bugs

### Off by one fault 1
**Input**:  
**Distance:**: 50, **Speed**: 60    
  
**Expected output**: **Use brakes**  
**Real output**: **Slow down**  

### Off by one fault 2
**Input**:  
**Distance:**: 100, **Speed**: 70    
  
**Expected output**: **Use brakes**  
**Real output**: **Slow down**  

### Off by one fault 3
**Input**:  
**Distance:**: 50, **Speed**: 30    
  
**Expected output**: **Slow down**  
**Real output**: **Keep current speed**  

### Off by one fault 4
**Input**:  
**Distance:**: 100, **Speed**: 40    
  
**Expected output**: **Slow down**  
**Real output**: **Keep current speed**  

### Typing error
**Input**:  
**Distance:**: 50, **Speed**: 40    
  
**Expected output**: **Slow down**  
**Real output**: **Use brakes**  
