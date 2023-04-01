## Prompt - 1
```
For the java function with comments given in the variable 'code' below, write unit test for testing the function. Import all the required packages.
code: public static BigDecimal add(Number... values) {
    if (ArrayUtil.isEmpty(values)) {
        return BigDecimal.ZERO;
    }

    Number value = values[0];
    BigDecimal result = toBigDecimal(value);
    for (int i = 1; i < values.length; i++) {
        value = values[i];
        if (null != value) {
            result = result.add(toBigDecimal(value));
        }
    }
    return result;
}
```

## Output - 1
Here's an example unit test for the add function:

```
import static org.junit.Assert.assertEquals;

import java.math.BigDecimal;
import org.junit.Test;

public class AddTest {
  
  @Test
  public void testAddition() {
    // Test adding two integers
    assertEquals(new BigDecimal("5"), add(2, 3));
    
    // Test adding a double and an integer
    assertEquals(new BigDecimal("6.7"), add(2.2, 4.5));
    
    // Test adding a mix of integers, doubles, and null values
    assertEquals(new BigDecimal("6.0"), add(2, 4.0, null, 0, -1.5));
  }
  
  private BigDecimal toBigDecimal(Number num) {
    return num == null ? BigDecimal.ZERO : new BigDecimal(num.toString());
  }
  
  private BigDecimal add(Number... values) {
    if (ArrayUtil.isEmpty(values)) {
      return BigDecimal.ZERO;
    }

    Number value = values[0];
    BigDecimal result = toBigDecimal(value);
    for (int i = 1; i < values.length; i++) {
      value = values[i];
      if (null != value) {
        result = result.add(toBigDecimal(value));
      }
    }
    return result;
  }
}
```
Note that the test cases cover various scenarios such as adding two integers, adding a double and an integer, and adding a mix of integers, doubles, and null values. The toBigDecimal helper method is used to convert the input values to BigDecimal objects, while the add method is a copy of the original add function.

## Observation - 1
Out of three generated tests, the third test has wrong expected output. For other two tests, the ChatGPT generated correct tests.
This could've caused due to involvement of negative numbers in the calculation.
![alt text](observation-1.PNG "Test-Execution")

## Prompt - 2
The third test in testAddition has the wrong expected output. Can you please rectify that?
## Output - 2
Certainly, here is the updated testAddition method with the corrected expected output for the third test case:
```
@Test
public void testAddition() {
    assertEquals(BigDecimal.ZERO, MathUtil.add());
    assertEquals(BigDecimal.valueOf(5), MathUtil.add(2, 3));
    assertEquals(BigDecimal.valueOf(15), MathUtil.add(1, 2.5, 3, 4.5, 4));
    assertEquals(BigDecimal.valueOf(10.7), MathUtil.add(2.3, 3.4, 5, 0, 0, 0, 0, -1));
}
```
Note that the third test case now expects the result to be BigDecimal.valueOf(15), which is the correct sum of the input values.
## Observation - 2
When we explicitly asked ChatGPT to rectify the 3rd test, it changed the inputs and all were positive.

## Prompt - 3
The expected output is incorrect when one of the numbers is negative. Consider negative numbers as well while generating tests.
## Output - 3
Sure! Here are the updated tests that also cover negative numbers:
```
@Test
public void testAddition() {
    assertEquals(BigDecimal.ZERO, AdditionUtil.add());
    assertEquals(new BigDecimal("10"), AdditionUtil.add(2, 3, 5));
    assertEquals(new BigDecimal("-5"), AdditionUtil.add(10, -15));
    assertEquals(new BigDecimal("0.5"), AdditionUtil.add(0.1, 0.2, 0.2));
}
```
These tests check the function with different types of inputs, including an empty input array, positive numbers, negative numbers, and decimal numbers.
## Observation - 3
When explicitly asked to generate tests with negative number as inputs, the ChatGPT generated the correct tests.
Error - The first test is giving compile time error - as the method needs atleast one parameter as input.
Other tests are running successfully.
![alt text](observation-3.PNG "Test-Execution")

## Prompt - 4
Give few more examples involving negative numbers
## Output - 4
Sure, here are a few more examples involving negative numbers for the add function:
```
@Test
public void testAddition() {
    assertEquals(BigDecimal.ZERO, Calculator.add());
    assertEquals(BigDecimal.valueOf(5), Calculator.add(2, 3));
    assertEquals(BigDecimal.valueOf(-5), Calculator.add(-2, -3));
    assertEquals(BigDecimal.valueOf(0), Calculator.add(5, -5));
    assertEquals(BigDecimal.valueOf(5), Calculator.add(2.5, 2.5, 0, -0.5));
    assertEquals(BigDecimal.valueOf(10.55), Calculator.add(5.25, -3.75, 8.05, 1));
}
```
These tests cover different combinations of positive and negative numbers as well as decimal values.
## Observation - 4
When explicitly asked to generate more tests with negative number as inputs, the ChatGPT generated the correct tests.
Error - The first test is giving compile time error - as the method needs atleast one parameter as input.
For 5th test - the expected output is incorrect as it involves negative number.
Other tests are running successfully.
![alt text](observation-4.PNG "Test-Execution")
