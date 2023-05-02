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

	@AfterClass
	public static void tearDownClass() {
		// This code is executed after all test methods have been completed in this test
		// class.
		// This is where you'd want to remove stubs / close any connections.
		System.out.println("@AfterClass: I'm something that happens after everything.");

	}
}