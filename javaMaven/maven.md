# Maven && JUnit

Maven is a package manager for Java. It acts as a build tool, which helps us build our code. It helps genereate reports, do dependency management, etc. 



What does maven do as a build tool? 

- Multiple Jars:
  -  If you're using a lot of frameworks (like spring or hibernate) - to use these frameworks, you need to download a ton of jars. 
  - You need to properly bundle them during compile time, you need to send them out on distribution. 
- Dependencies / Versioning: 
  - Jars have different dependencies and  versions, and it's not always the case that you'll download the right version  of a jar (unless you're incredibly vigiliant). 
  - Often times, one jar requires a number of other jars to work.  
- Project Structure
  - Most projects need to have a proper structures and libraries to follow proper standards. 



Maven helps us do these things (and a ton of others)!. 



## Installation: 

To download maven, go to the [maven website](https://maven.apache.org) and click the download button under the `Get Maven` header. 

Downlaod either the installer or download the binaries and store them somewhere you'll know where they go. 

#### Environment Variables: 

Make sure that you have the proper environment variables set (remember setting up `JAVA_HOME` - it's similar to that). 

Set `M2_HOME` to the path of where your binaries live (whatever maven version you're using). This is so that you can use the maven executable from anywhere (e.g. eclipse). 

Add your maven directory  to your existing  path as well (be sure not to override your actual path). 

**install note:** if you're using a package manager, you can use homebrew (mac) or apt-get (linux). 



## Creating a Maven Project

First and foremost Maven needs to be connected to the internet to work, so make sure you're connected. 

Create a directory: 

```bash
mkdir testApp
cd testApp
```

Now, to generate a project type: 

```bash
mvn archetype:generate
```

This initial run will take a moment to load all of the maven dependencies, so it may take a minute depending on your connection speed. 

Once the dependencies are all installed, maven will prompt you to choose a number. There are a number of predefined archetypes (if you scroll up, you can look through all of the archetypes). By selecting any one of those archetypes, Maven will download all of the required jars. 

**Hit enter for the default maven quickstart**

Maven will then ask us to choose a version. 

**Choose the latest.**

You will then be prompted for a group id. Enter: 

**com.matthewlane** 

Then you'll be prompted for an artifact id (that is, what's your application's name):

**example-app**

Define value for property "version". The default value is fine. 

Define value for property "package". The default is also fine. 

At the end, **hit y**. 



## Working with the project: 

If you're using eclipse, just open the project via the file structure. If you're using intelli-j, open the file by selecting the `pom.xml`. 

Notice in your file structure you have a whole lot of directories, along with your pom.xml. 

#### src

Inside your src folder, you have both a **main** and a **test** folder. 

- **main**: Inside of your main folder, you'll place all of your actual code. This is where your project files live. 
  - By default Maven has a default main file that prints out hello world to the console. 
  - When you flesh your projects out, right inside of your main directory, you can add a resources folder where you can store properties (such as secret keys), sql code, etc. 
- **src**: Inside of this folder, you'll have all of your tests! (We'll get to this later). 
  - By default maven adds a test that assert that true equals true. 

#### pom.xml

This file describes your project. This is what maven uses to account for dependencies and what jars to use. 

- **Group ID and Artifact ID** version that we set up. 
- **Property section:**
  - **Project build source encoding**: utf-8: When you build the project. Maven will read in the files in your `src/main/resources` and copy them to the jar file, reading them in with a platform dependent character encoding (i.e. it'll read it in agnostic of whether you're on windows/Mac/linux/etc.). 
  - **Maven compiler**: Java jdk source number.
  - **Target version:** the lowest version of java support. If you're using lambdas - make sure your lowest version is java 8! 
- **Dependency Section:** These are the dependencies you have in your project from imported jars.
- **Build Section** - remove - don't need that now (really for production builds). 
  - If you change the pom.xml file - you'll possibly need to refresh your project (unless you have a auto-import turned on, which eclipse should have). 

#### Building your maven project: 

In eclipse, make sure your project is in scope, and go to `Run >> Run As >> Maven Build`. In the goals section, write 'clean verify' and hit run. 

Notice in the run section, maven also runs our unit tests. This is to make sure we don't actually break our app before we actually build it for production!  

Try building your app after changing your test to `assertTrue( false );`





## Testing! 

Testing is hands down one of the best things you can know coming out of this class. Up until now, all of our projects have been apps that you've built and tested entirely by trial and error. Trial and error works great, but the larger and larger our apps get, the more likely we are to run into problems / edge cases that we never entirely anticipated. This is why having a test to know whether or not our functions work the way we want is incredibly useful. 

For our tests we're going to use what was already supplied: **JUnit**. We're using JUnit 4 in this example. Most all IDEs support JUnit. It's one of the most popular packages for unit testing in the world of Java. 

### How does it work? 

Let's assume we have a class: 

```java
public class DoMath {
  public int doAddition(int x, int y){
    return x + y; 
  }
  
  public int doMultiplication(int x, int y){
    return x * y; 
  }
}
```

Though this is a somewhat trivial class, it's also hopefully very straightforward. To make sure our class's functions are working properly, we create a test: 

```java
import org.junit.Test; 

public class DoMathTest {
  
  @Test         // test annotation decorator
  public void testDoAddition(){
    DoMath mathematical = new DoMath(); 
    int a = 25; 
    int b = 52; 
    int result = mathematical.doAddition(a,b); 
    
    int expected = 77; 
    
    assertEquals(expected, result);   // this is what's doing the checking
  }
}
```



If the tests fail, then an exception is thrown, and our test fails (and if we're trying to actually build our app, then it won't actually build until our tests pass)! 



This is the first time we've seen any real decorators other than `@override`. What do JUnit's annotations do? 

- ` @BeforeClass / @BeforeAll`: This runs before all tests are run. 
- `@Before / @BeforeEach`: Runs before each specific test. If you have a whole suite of tests, it gets tedious to rewrite code, so you can reset specific variables to a given value. This is great for what is called `mocking` or `stubbing`. 
- `@Test`: Defines the actual test method. 
- `@After / @AfterEach`: Works just like beforeEach, but does work afterward. 
- `@Ignore / @Disabled`: Disables a specific test. 
- `@AfterClass / @AfterAll`: This runs after all tests are finished. 
- Many more! 

**Note: ** You see there are differences in the befores and afters. These are differences between JUnit4 and JUnit5. 

Typically, setting up a test class looks like: 

```java
import org.junit.*; 

public class DoMathTest {
  @BeforeAll
  public static void setupClass() {
    // Setup code to execute before all test methods
    // This is where we want to prepare our test environment.
    // Something like creating a database environment stubs / open connections
  }
  
  @BeforeEach
  public void setup(){
    // Execute code before each test method
  }
  
  @Test
  public void testDoAddition(){
    DoMath mathematical = new DoMath(); 
    int a = 25; 
    int b = 52; 
    int result = mathematical.doAddition(a,b); 
    
    int expected = 77; 
    
    assertEquals(expected, result);   // this is what's doing the checking
  }
  
  @Test
  public void testDoMultiplacation(){
    DoMath mathematical = new DoMath(); 
    int a = 25; 
    int b = 52; 
    int result = mathematical.doMultiplication(a,b); 
    
    int expected = 1300; 
    
    assertEquals(expected, result);   // this is what's doing the checking
  }
  
  @AfterEach
  public void tearDown() {
    // Code executes after every test. 
  }
  
  @AfterAll
  public static void tearDownClass(){
    // This code is executed after all test methods have been completed in this test class.
    // This is where you'd want to remove stubs / close any connections. 
  }
}
```



### Assertion Methods: 

So far we've seen `assertEquals(expected, actual)`. There are other assertions. Here are a list of a few: 

- `fail()`: This makes a test method fail immediately to force our method to fail (suppose you're not finished writing. a specific method and you want to make sure you don't forget). 
- `assertEquals(expected, actual)` : This asserts that there is an equality between the expected and result. 
- `assertNotEquals(expected, actual)`: Same as above, but asserts that they're different. 
- `assertTrue(bool condition)`: takes in a boolean that must be true. 
- `assertFalse(bool condition)`: asserts that the boolean it takes in must be false. 
- `assertNull(Object)`: takes in an object, and asserts that it must be null. 
- `assertNotNull(Object)`: takes in an object and asserts that it must not be null. 
- `assertSame(Object expected, Object actual)`: asserts that two objects must have the same reference. 
- `assertNotSame(Object unexpected, Object actual)`: asserts two objects do not have the same reference. 



### Implementation: 

Go to your project, and in your test files, create a new test class. If you're using an IDE, right click your test directory and create a new JUnit test. You ought to be prompted what kind of JUnit you'd like to use. JUnit3, JUnit4, or JUnit Jupiter Test (JUnit 5). Make sure to choose the version you're actually using. To make sure you know which JUnit version you have in your project, check your pom.xml for which JUnit version you have (if your decorators like `@Before` don't work, try changing what type of JUnit class you're using). 

If you're using JUnit 4, your pom.xml will have the dependency: 

```xml
<dependency>
  <groupId>junit</groupId>
  <artifactId>junit</artifactId>
  <version>4.*.*</version>
  <scope>test</scope>
</dependency>
```



If you're using JUnit 5, your pom.xml will have the dependency: 

```xml
<dependency>
  <groupId>org.junit.jupiter</groupId>
  <artifactId>junit-jupiter-engine</artifactId>
  <version>5.*.*</version>
  <scope>test</scope>
</dependency>
```



Upon creating a new test (called TestDoMath), you'll see that it looks like: 

```java
// path -> src/test/java/com/matthewlane/
package com.matthewlane;

import static org.junit.Assert.*;

import org.junit.Test;

public class TestDoMath {

	@Test
	public void test() {
		fail("Not yet implemented");
	}

}

```

This fails intentionally to ensure that we don't just create an empty test and move about our way. If you try to run the test, it will fail. 

Before we move on, we need to actually create our `DoMath.java` class. Go to your src, and create a new class called `DoMath.java` right next to your `App.java` file. In this file, let's do some math (though because we're doing this test driven, our math will be intentionally bad). We know that we want to have two functions that do addition and multiplication. Let's have them both return 0:  

```java
// path -> src/main/java/com/matthewlane/
package com.matthewlane;

public class DoMath {
	public int doAddition(int x, int y) {
		return 0;
	}

	public int doMultiplication(int x, int y) {
		return 0;
	}
}
```



Now that we have our DoMath class set up, let's go back to our 

```java
package com.matthewlane;

import static org.junit.Assert.assertEquals;
import org.junit.*;

import org.junit.Test;

public class TestDoMath {  
	  @Test
	  public void testDoAddition(){
	   	System.out.println("I'm going to do some testing"); 
	  }
	  
  	@Ignore // NOTICE WE'RE USING THAT IGNORE DECORATOR - Because let's ignore this for now
	  @Test
	  public void testDoMultiplacation(){
	    System.out.println("I'm also going to do some testing! "); 
	  }

	}
```



We now have our initial test case set up, let's test our addition function. 

```java
package com.matthewlane;

import static org.junit.Assert.assertEquals;
import org.junit.*;

import org.junit.Test;

public class TestDoMath {  
	  @Test
	  public void testDoAddition(){
			DoMath mathematical = new DoMath();
      
      int a = 25; 
      int b = 52; 
      int result = mathematical.doAddition(a,b);
      
      int expected = 77; 
      
      assertEquals(expected, result); 
	  }
	  
  	@Ignore // NOTICE WE'RE USING THAT IGNORE DECORATOR - Because let's ignore this for now
	  @Test
	  public void testDoMultiplacation(){
	    System.out.println("I'm also going to do some testing! "); 
	  }
	}
```



When we run this test, it will fail (which was expected!). If you look at the stack trace, we'll see: 

```bash
java.lang.AssertionError: expected:<77> but was:<0>
	at org.junit.Assert.fail(Assert.java:88)
	at org.junit.Assert.failNotEquals(Assert.java:743)
	at org.junit.Assert.assertEquals(Assert.java:118)
	at org.junit.Assert.assertEquals(Assert.java:555)
	at org.junit.Assert.assertEquals(Assert.java:542)
	at com.matthewlane.TestDoMath.testDoAddition(TestDoMath.java:19)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
	at java.base/jdk.internal.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
	at java.base/jdk.internal.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
	at java.base/java.lang.reflect.Method.invoke(Method.java:567)
	at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:47)
	at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
	at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:44)
	at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
	at org.junit.runners.ParentRunner.runLeaf(ParentRunner.java:271)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:70)
	at org.junit.runners.BlockJUnit4ClassRunner.runChild(BlockJUnit4ClassRunner.java:50)
	at org.junit.runners.ParentRunner$3.run(ParentRunner.java:238)
	at org.junit.runners.ParentRunner$1.schedule(ParentRunner.java:63)
	at org.junit.runners.ParentRunner.runChildren(ParentRunner.java:236)
	at org.junit.runners.ParentRunner.access$000(ParentRunner.java:53)
	at org.junit.runners.ParentRunner$2.evaluate(ParentRunner.java:229)
	at org.junit.runners.ParentRunner.run(ParentRunner.java:309)
	at org.eclipse.jdt.internal.junit4.runner.JUnit4TestReference.run(JUnit4TestReference.java:89)
	at org.eclipse.jdt.internal.junit.runner.TestExecution.run(TestExecution.java:41)
	at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:541)
	at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.runTests(RemoteTestRunner.java:763)
	at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.run(RemoteTestRunner.java:463)
	at org.eclipse.jdt.internal.junit.runner.RemoteTestRunner.main(RemoteTestRunner.java:209)
```

This stack trace, like many, is exceptionally long, but if you look at the very top line, we'll see: 

```bash
java.lang.AssertionError: expected:<77> but was:<0>
```

That right there tells us exactly why our test failed. Now, to make sure we do this right, let's go back to our actual code, and get our method to do what we want it to do (in this case, simple addition): 

```java
// path -> src/main/java/com/matthewlane/
package com.matthewlane;

public class DoMath {
	public int doAddition(int x, int y) {
		return x + y;
	}

	public int doMultiplication(int x, int y) {
		return 0;
	}
}
```



Now, when we run our tests, we get a passing clean bill of health!



#### Don't forget ignored tests!: 

Don't forget about that ignored test. Let's try that one out: 

```java
package com.matthewlane;

import static org.junit.Assert.assertEquals;

import org.junit.*;

import org.junit.Test;

public class TestDoMath {
	  @Test
	  public void testDoAddition(){
	    DoMath mathematical = new DoMath(); 
	    int a = 25; 
	    int b = 52; 
	    int result = mathematical.doAddition(a,b); 
	    
	    int expected = 77; 
	    
	    assertEquals(expected, result);   // this is what's doing the checking
	  }
	  
  	// REMOVE THAT IGNORE! We want to pay attention to our tests.
	  @Test
	  public void testDoMultiplacation(){
	    DoMath mathematical = new DoMath(); 
	    int a = 3; 
	    int b = 5; 
	    int result = mathematical.doMultiplication(a,b); 
	    
      // I don't know how multiplication works off the top of my head
      // but I do know that 3 * 5 is really just 3 5's added together
	    int expected = 5 + 5 + 5; 
	    
	    assertEquals(expected, result);   // this is what's doing the checking
	  }

	}
```



Again, when we run this, we get another failure: 

```bash
java.lang.AssertionError: expected:<15> but was:<0>  ...
```

So let's go change our codebase to properly pass the test: 

```java
// path -> src/main/java/com/matthewlane/
package com.matthewlane;

public class DoMath {
	public int doAddition(int x, int y) {
		return x + y;
	}

	public int doMultiplication(int x, int y) {
		return x*y;
	}
}
```

Now, when we test again, our tests pass! 



#### Test Cleanup: 

Up until now, we've just been doing everything we needed for our tests inside of each specific test function. That's great, though the more we test, the more code we'll need to put in, so let's clean up our code a little bit. Remember those other methods using the `before` and `after` decorators? Let's take a quick look at what they do: 

```java
package com.matthewlane;

import static org.junit.Assert.assertEquals;

//import static org.junit.Assert.*;

import org.junit.*;

import org.junit.Test;

public class TestDoMath {
	@BeforeClass
	public static void setupClass() {
		// Setup code to execute before all test methods
		// This is where we want to prepare our test environment.
		// Something like creating a database environment stubs / open connections
		System.out.println("@BeforeClass: I'm something that happens before everything.");
	}

	@Before
	public void setup() {
		// Execute code before each test method
		System.out.println("@Before I'm something that happens before each specific test.");

	}

	@Test
	public void testDoAddition() {
		System.out.println("I'm a test. I test addition");

		DoMath mathematical = new DoMath();
		int a = 25;
		int b = 52;
		int result = mathematical.doAddition(a, b);

		int expected = 77;

		assertEquals(expected, result); // this is what's doing the checking
	}

	@Test
	public void testDoMultiplacation() {
		System.out.println("I'm a test. I test multiplication");
		DoMath mathematical = new DoMath();
		int a = 3;
		int b = 5;
		int result = mathematical.doMultiplication(a, b);

		int expected = 15;

		assertEquals(expected, result); // this is what's doing the checking
	}

	@After
	public void tearDown() {
		// Code executes after every test.
		System.out.println("@After: I'm something that happens after each specific test.");

	}

	@AfterClass
	public static void tearDownClass() {
		// This code is executed after all test methods have been completed in this test
		// class.
		// This is where you'd want to remove stubs / close any connections.
		System.out.println("@AfterClass: I'm something that happens after everything.");

	}
}
```



So, we now get the output to our console: 

```
@BeforeClass: I'm something that happens before everything.
@Before I'm something that happens before each specific test.
I'm a test. I test multiplication
@After: I'm something that happens after each specific test.
@Before I'm something that happens before each specific test.
I'm a test. I test addition
@After: I'm something that happens after each specific test.
@AfterClass: I'm something that happens after everything.
```



SO, what repeated code can we rid ourselves of? Let's stop creating new `DoMath` objects. 

```java
package com.matthewlane;

import static org.junit.Assert.assertEquals;

//import static org.junit.Assert.*;

import org.junit.*;

import org.junit.Test;

public class TestDoMath {
  static DoMath mathematical;
  
  
	@BeforeClass
	public static void setupClass() {
    mathematical = new DoMath(); 					// INSTANTIATE DO MATH IS THE SETUP CLASS
	}

	@Before
	public void setup() {
		// Execute code before each test method
		System.out.println("@Before I'm something that happens before each specific test.");

	}

	@Test
	public void testDoAddition() {  
		System.out.println("I'm a test. I test addition");
    
    // REMOVED DO MATH INSTANTION OF MATHEMATICAL
		int a = 25;
		int b = 52;
		int result = mathematical.doAddition(a, b);

		int expected = 77;

		assertEquals(expected, result); // this is what's doing the checking
	}

	@Test
	public void testDoMultiplacation() {
		System.out.println("I'm a test. I test multiplication");

    // REMOVED DO MATH INSTANTION OF MATHEMATICAL
		int a = 3;
		int b = 5;
		int result = mathematical.doMultiplication(a, b);

		int expected = 15;

		assertEquals(expected, result); // this is what's doing the checking
	}

	@After
	public void tearDown() {
		// Code executes after every test.
		System.out.println("@After: I'm something that happens after each specific test.");

	}

  
  // We don't really need to do this - but why not. Force that garbage collectionra
  
	@AfterClass
	public static void tearDownClass() {
		mathematical = null; 
    	
	}
}
```

