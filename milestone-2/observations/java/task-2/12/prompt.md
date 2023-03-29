## Prompt - 1
```
For the java function with comments given in the variable 'code' below, write unit test for testing the function. Import all the required packages.
code: public static String functionDescriptionHTML(GeometryFunction func)
  {
    String txt = "<b>" + func.getSignature() + "</b>";
    String desc = func.getDescription();
    if (desc != null) {
      txt += "<br><br>" + desc;
    }
    return "<html>" + txt + "</html>";
  }
```

## Output - 1
Here is a sample unit test for the given code:

```
import org.junit.Test;
import static org.junit.Assert.assertEquals;

public class GeometryFunctionTest {

  @Test
  public void testFunctionDescriptionHTML() {
    GeometryFunction func = new GeometryFunction("buffer(geometry,distance)", "Computes a buffer around a geometry", 2);
    String expectedOutput = "<html><b>buffer(geometry,distance)</b><br><br>Computes a buffer around a geometry</html>";
    assertEquals(expectedOutput, functionDescriptionHTML(func));
  }
}
```
Note: The GeometryFunction class and its constructor are not provided in the code, so I created a sample constructor with some inputs. You may need to modify the input values according to the actual implementation of GeometryFunction.

### Generated Test Output

## Prompt - 2
Can you please regenerate the tests by using the following data:
getDescription() will return "This is the description"
and getSignature() will return "test signature"

## Output - 2
Certainly, here are two unit tests for the functionDescriptionHTML function:
```
@Test
public void testFunctionDescriptionHTMLWithDescription() {
  GeometryFunction func = new GeometryFunction() {
    @Override
    public String getSignature() {
      return "test signature";
    }
    @Override
    public String getDescription() {
      return "This is the description";
    }
    @Override
    public Object invoke(Geometry geom, Object[] args) {
      return null;
    }
  };
  String expected = "<html><b>test signature</b><br><br>This is the description</html>";
  String actual = functionDescriptionHTML(func);
  assertEquals(expected, actual);
}

@Test
public void testFunctionDescriptionHTMLWithoutDescription() {
  GeometryFunction func = new GeometryFunction() {
    @Override
    public String getSignature() {
      return "test signature";
    }
    @Override
    public String getDescription() {
      return null;
    }
    @Override
    public Object invoke(Geometry geom, Object[] args) {
      return null;
    }
  };
  String expected = "<html><b>test signature</b></html>";
  String actual = functionDescriptionHTML(func);
  assertEquals(expected, actual);
}
```
The first test checks if the description is properly appended to the signature when it exists, while the second test checks if only the signature is returned when there is no description.

### Generated Test Output





