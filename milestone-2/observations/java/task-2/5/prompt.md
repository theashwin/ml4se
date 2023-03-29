## Prompt - 1
```
For the java function with comments given in the variable 'code' below, write unit test for testing the function. Import all the required packages.
code: static double truncate(double v) {
		if (v >= 0)
			return Math.floor(v);
		else
			return -Math.floor(-v);
	}
```

## Output - 1
Sure! Here's a JUnit test for the truncate function:

```
import static org.junit.Assert.assertEquals;
import org.junit.Test;

public class TruncateTest {

    @Test
    public void testTruncatePositive() {
        double input = 3.6;
        double expected = 3.0;
        double result = Truncate.truncate(input);
        assertEquals(expected, result, 0.0);
    }
    
    @Test
    public void testTruncateNegative() {
        double input = -3.6;
        double expected = -3.0;
        double result = Truncate.truncate(input);
        assertEquals(expected, result, 0.0);
    }
}
```
Note: I have assumed that the class name for the truncate function is Truncate. Please replace it with the appropriate class name before running the test.

### Generated Test Output

## Prompt - 2
Refactor the unit test produced, make sure it's runnable and efficient.

## Output - 2
Sure, here's a refactored version of the TruncateTest that uses parameterized tests to reduce code duplication:

```
import static org.junit.Assert.assertEquals;
import java.util.Arrays;
import java.util.Collection;
import org.junit.Test;
import org.junit.runner.RunWith;
import org.junit.runners.Parameterized;
import org.junit.runners.Parameterized.Parameters;

@RunWith(Parameterized.class)
public class TruncateTest {

    private double input;
    private double expected;

    public TruncateTest(double input, double expected) {
        this.input = input;
        this.expected = expected;
    }

    @Parameters
    public static Collection<Object[]> data() {
        Object[][] data = new Object[][] { 
            { 3.6, 3.0 }, 
            { 3.1, 3.0 },
            { -3.6, -3.0 },
            { -3.1, -3.0 } 
        };
        return Arrays.asList(data);
    }

    @Test
    public void testTruncate() {
        double result = Truncate.truncate(input);
        assertEquals(expected, result, 0.0);
    }
}
```
This version of the test uses the @RunWith(Parameterized.class) annotation to enable parameterized testing, and the @Parameters annotation to specify the test data. The test method testTruncate is called once for each row in the test data, and the input and expected values are passed in as arguments to the constructor. This reduces code duplication and makes the test more efficient.
### Generated Test Output