
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


## Bugs

### Integration fault
**Input**:  
**Time**: 60, **Depth**: 5  
  
**Expected output**: **no risk**  
**Real output**: **high risk**  

### Off by one fault 1
**Input**:  
**Time**: 60, **Depth**: 10  
  
**Expected output**: **low risk**  
**Real output**: **no risk**  

### Off by one fault 2
**Input**:  
**Time**: 60, **Depth**: 15  
  
**Expected output**: **high risk**  
**Real output**: **no risk**  

### Typing error
**Input**:  
**Time**: 50, **Depth**: 10  
  
**Expected output**: **no risk**  
**Real output**: **low risk**  