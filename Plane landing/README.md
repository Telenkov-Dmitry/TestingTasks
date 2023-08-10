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

## Bugs

### Integration fault
**Input**:  
**Wind**: 1, **Pressure**: 7  
  
**Expected output**: **land**  
**Real output**: **stay in the air**  

### Off by one fault 1
**Input**:  
**Wind**: 6, **Pressure**: 4   
  
**Expected output**: **fly to another airport**  
**Real output**: **land**  

### Off by one fault 2
**Input**:  
**Wind**: 5, **Pressure**: 3  
  
**Expected output**: **land**  
**Real output**: **stay in the air**  

### Typing error
**Input**:  
**Wind**: 6, **Pressure**: 3  
  
**Expected output**: **stay in the air**  
**Real output**: **land**  