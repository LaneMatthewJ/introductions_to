package com.matthewlane;

import static org.junit.Assert.*;

import org.junit.Test;
import org.junit.*; 

public class DoMathTest {
	static DoMath totallyMath; 
	static int a; 
	static int b; 
	
	@BeforeClass
	public static void setupClass() {
		System.out.println("BEFORE CLASS I run before everything");
		totallyMath = new DoMath();
		a = 10; 
		b = 10;
	}
	
	@Before
	public void preTest() {
		System.out.println("BEFORE I come before each test"); 
	}
	
	@Test
	public void testAddition() {

		int result = totallyMath.doAddition(a, b);
		
		int expected = 20; 
		
		assertEquals(expected, result);
	}
	
	@Test
	public void testMultiplication() {
		
		int result = totallyMath.doMulitplication(a, b);
		int expected = 100; 
		
		assertEquals(expected, result); 
	}
	
	@After
	public void postTest() {
		System.out.println("AFTER I go after each"); 
	}
	
	@AfterClass
	public static void tearDownClass() {
		System.out.println("AFTER CLASS I'm the last!");
	}
	
	
	
	
	
	
	
	
	
	
	
	

}
