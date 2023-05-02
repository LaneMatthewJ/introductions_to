## Testing in Python Introduction: 

1. **Unit tests** are quite literally just lines of code that test "units of functionality"
   1. By writing unit tests as you go, you can be sure that your code is doing what you think it is. 
2. **Regression Testing** is ultimately the processes of keeping up with your unit tests as you flesh out your program, so that when you change your code (and rerun your tests) you'll know if you accidentally broke something and "regress" to a broken state.
3. The strategy **Red Green Refactor:**:
   ![rgr](https://content.codecademy.com/programs/tdd-js/articles/red-green-refactor-tdd.png) 
   1. **Red**
      1. Implement the skeleton of a function with: 
         1. Parameters: (name, params, return type)
         2. Return value: Nonsense dummy value (that satisfies the return type)
      2. Once the skeleton function is implemented, we go to write our test. 
         1. Think of examples of input you think your function will likely get and what you'd expect to return those values with. 
         2. Write a test that inputs these values and then expects to see what you expect to see. 
   2. **Green**
      1. Fix the code skeleton to actually pass the test you've written (and get green text*). 
   3. **Refactor**
      1. Clean up your code. 
   4. Repeat ad nauseam for all functional units. 

 **Red, Green, Refactor**  is the process for **Test Driven Development**.  Naturally, this takes time to get into the habit, but it's good to know this methodology exists. 



## Examples: 

We'll be using `pytest`. To install pytest, copy into the command line: 

```
pip install pytest
```



Create a new project directory with the  structure (all with empty files): 

```
.
├── conftest.py
├── lib
│   ├── __init__.py
│   └── dataframe_helpers.py
└── tests
    └── test_dataframe_helpers.py

```

### Red

Now that we've created our empty files, we can start our **red** development: 

1. > Implement the skeleton of a function with parameters and return values


   In `dataframe_helpers.py` we will create a function `remove_variance` with two parameters, their datatypes, and their return values. Additionally we'll want a doc string to define what our function does (self documenting code seems fine, but what's self documenting now likely won't mean anything to you in 6 months)

   1. Note: The data types and return values aren't absolutely necessary, however, they're good for documenting your function so that when you return to your code months later, you'll have an easier time of understanding what's going on with your own material. 

   2. ```python
      import pandas as pd
      
      def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
      	"""
      	This function removes the low variance values from a dataframe
      	determined by some threshold
      	"""
      	low_variance_dataframe = pd.DataFrame()
      
      	return low_variance_dataframe
      ```

2. > Write our test. Think of examples of input you think your function will likely get and what you'd expect to return those values with. 
   >
   > and
   >
   > Write a test that inputs these values and then expects to see what you expect to see. 

   Now that we have a function skeleton, we continue our **red** development by writing our test: 

   1. We first start by writing a class container to cordon off our tests specific to the function we're testing (you don't need to do this specifically, but it keeps your code clean). 

   2. Next we write our expected input and expected output. 

   3. Finally, we write our `assert` statement. There exists a basic `assert` in python:
      ```
      assert(2 + 3 == 5)
      ```

      Which fails when the values are not true: 
      ```
      assert(2 + 3 == 4)
      > Traceback (most recent call last):
      >  File "<stdin>", line 1, in <module>
      > AssertionError
      ```

      Many libraries have their own assertion libraries for us to make use of as well, such as the pandas library, so we'll be using the `pd.testing` module. 
      ```python
      import pytest
      import numpy as np 
      import pandas as pd
      from lib import dataframe_helpers
      
      class TestRemoveLowVariance:
      	"""
      	This class tests the remove low variance function
      	""" 
      
      	def test_remove_low_variance(self): 
      		"""
      		This function tests 'remove_low_var' with ideal parameters.
      		"""
      		data = {
      					"a": [0, 1, 2, 3, 2, 1, 3, 0, 3], # sum = 15  
      					"b": [0, 0, 0, 0, 0, 0, 0, 0, 0], # sum =  0
      					"c": [2, 1, 2, 3, 1, 3, 2, 3, 3], # sum = 20 
      					"d": [1, 0, 0, 1, 0, 1, 1, 0, 1]  # sum =  5
      				}
      		dataframe = pd.DataFrame(data= data)
      
      		expected_output_columns = ['a','c','d']
      		expected_output = dataframe[ expected_output_columns ]
      
      		actual_output = dataframe_helpers.remove_low_variance(dataframe, 0.1)
      
      		pd.testing.assert_frame_equal(expected_output, actual_output)
      		
      ```

   4. Now we test our code at the project head: 
      ```bash
      pytest
      ```

      > ============================== test session starts ==============================
      > platform darwin -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
      > rootdir: /Users/96v/Documents/projects/test/basic_testing
      > plugins: anyio-3.5.0, cov-4.0.0
      > collected 1 item                                                                
      >
      > tests/test_greeting.py F                                                  [100%]
      >
      > =================================== FAILURES ====================================
      > _______________________ TestRemoveLowVariance.test_greet ________________________
      >
      > self = <test_greeting.TestRemoveLowVariance object at 0x7f8050216bb0>
      >
      >     def test_greet(self):
      >         """
      >         This function tests 'remove_low_var' with ideal parameters.
      >         """
      >         data = {
      >                                 "a": [0, 1, 2, 3, 2, 1, 3, 0, 3], # sum = 15
      >                                 "b": [0, 0, 0, 0, 0, 0, 0, 0, 0], # sum =  0
      >                                 "c": [2, 1, 2, 3, 1, 3, 2, 3, 3], # sum = 20
      >                                 "d": [1, 0, 0, 1, 0, 1, 1, 0, 1]  # sum =  5
      >                         }
      >         dataframe = pd.DataFrame(data= data)
      >     
      >         expected_output_columns = ['a','c','d']
      >         expected_output = dataframe[ expected_output_columns ]
      >     
      >         actual_output = dataframe_helpers.remove_variance(dataframe, 0.1)
      >
      > >       pd.testing.assert_frame_equal(expected_output, actual_output)
      > >       E    AssertionError: DataFrame are different
      > >       E    
      > >       E    DataFrame shape mismatch
      > >       E    [left]:  (9, 3)
      > >       E    [right]: (0, 0)
      >
      > tests/test_greeting.py:28: AssertionError
      > ============================ short test summary info ============================
      > FAILED tests/test_greeting.py::TestRemoveLowVariance::test_greet - AssertionEr...
      > =============================== 1 failed in 1.01s ===============================

### Green

1. > Fix the code skeleton to actually pass the test you've written. 

   1. To fix our code, we're going to need to actually implement what it is that we're trying to do: 
      ```python
      import pandas as pd
      
      def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
      	"""
      	This function removes the low variance values from a dataframe
      	determined by some threshold
      	"""
      
      	low_variance_dataframe = df[ df.columns[(df.var() > threshold)] ] 
      
      	return low_variance_dataframe
      ```

   2. Now when we run our test: 

      > ============================== test session starts ==============================
      > platform darwin -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
      > rootdir: /Users/96v/Documents/projects/test/basic_testing
      > plugins: anyio-3.5.0, cov-4.0.0
      > collected 1 item                                                                
      >
      > tests/test_greeting.py .                                                  [100%]
      >
      > =============================== 1 passed in 0.76s ===============================

   ### Refactor

   Our code within the `remove_variance` function is a little gross. Let's refactor it to make it a little more readable: 

   ```python
   import pandas as pd
   
   def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
   	"""
   	This function removes the low variance values from a dataframe
   	determined by some threshold
   	"""
   	
     # Create mask and extract desired columns
     high_variance_mask = df.var() > threshold
     high_variance_columns = df.columns[high_variance_mask]
     
     # Extract desired columns from actual dataframe
   	low_variance_dataframe = df[ high_variance_columns ] 
    
   	return low_variance_dataframe
   ```

   Now we rerun pytest to make sure we didn't *regress*: 

   ```
   pytest
   ```

   > ============================== test session starts ==============================
   > platform darwin -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
   > rootdir: /Users/96v/Documents/projects/test/basic_testing
   > plugins: anyio-3.5.0, cov-4.0.0
   > collected 1 item                                                                
   >
   > tests/test_greeting.py .                                                  [100%]
   >
   > =============================== 1 passed in 0.76s ===============================



## Testing for Expected Failures

Now that we've written our first function and unit test that pass, let's add to our function. First, let's think of additional functionality that we want our `remove_low_variance` function to have. Perhaps we wish for it to throw an error if _all_ columns are removed due to low variance?  Let's do it. 

### Red

Because we've already written our base function, we don't need to write any additional skeletons, we can move straight to writing our test function within our class. We'll do so by using a feature from pytest that captures thrown errors for assertions:

```python
	def test_remove_low_variance_throws_error(self): 
		"""
		This test asserts that remove_low_var throws an error
		when there exist no columns within the low variance dataframe
		"""
		
		data = {
			"a": [ 0, 0, 0, 0, 0],
			"b": [ 0, 0, 0, 0, 0],
			"c": [ 0, 0, 0, 0, 0],
			"d": [ 0, 0, 0, 0, 0]
		}

		dataframe = pd.DataFrame(data=data)

		with pytest.raises(RuntimeError, match="remove_low_variance removed all features from dataframe."):
			dataframe_helpers.remove_low_variance(dataframe, 0.1)
```

Now, instead of  writing the _same_ variables over and over again, we can refactor our code a smidge to use previously defined variables (i.e. the threshold parameter).  So let's move `threshold` to be a class level variable for this test block: 

```python
import pytest
import numpy as np 
import pandas as pd
from lib import dataframe_helpers

class TestRemoveLowVariance:
	"""
	This class tests the remove low variance function
	""" 

	threshold = 0.1


	def test_remove_low_variance(self): 
		"""
		This function tests 'remove_low_var' with ideal parameters.
		"""
		data = {
					"a": [0, 1, 2, 3, 2, 1, 3, 0, 3], # sum = 15  
					"b": [0, 0, 0, 0, 0, 0, 0, 0, 0], # sum =  0
					"c": [2, 1, 2, 3, 1, 3, 2, 3, 3], # sum = 20 
					"d": [1, 0, 0, 1, 0, 1, 1, 0, 1]  # sum =  5
				}
		dataframe = pd.DataFrame(data= data)

		expected_output_columns = ['a','c','d']
		expected_output = dataframe[ expected_output_columns ]

		actual_output = dataframe_helpers.remove_low_variance(dataframe, self.threshold)

		pd.testing.assert_frame_equal(expected_output, actual_output)
		

	def test_remove_low_variance_throws_error(self): 
		"""
		This test asserts that remove_low_var throws an error
		when there exist no columns within the low variance dataframe
		"""
		
		data = {
			"a": [ 0, 0, 0, 0, 0],
			"b": [ 0, 0, 0, 0, 0],
			"c": [ 0, 0, 0, 0, 0],
			"d": [ 0, 0, 0, 0, 0]
		}

		dataframe = pd.DataFrame(data=data)

		with pytest.raises(RuntimeError, match="remove_low_variance removed all features from dataframe."):
			dataframe_helpers.remove_low_variance(dataframe, self.threshold)
```

Now when we run our test, we see: 

```
pytest
```

>collected 2 items                                                               
>
>tests/test_dataframe_helpers.py .F                                        [100%]
>
>=================================== FAILURES ====================================
>__________ TestRemoveLowVariance.test_remove_low_variance_throws_error __________
>
>self = <test_dataframe_helpers.TestRemoveLowVariance object at 0x7ff3f4217f40>
>
>    def test_remove_low_variance_throws_error(self):
>        """
>        This test asserts that remove_low_var throws an error
>        when there exist no columns within the low variance dataframe
>        """
>    
>        data = {
>                "a": [ 0, 0, 0, 0, 0],
>                "b": [ 0, 0, 0, 0, 0],
>                "c": [ 0, 0, 0, 0, 0],
>                "d": [ 0, 0, 0, 0, 0]
>        }
>    
>        dataframe = pd.DataFrame(data=data)
>    
>        with pytest.raises(RuntimeError, match="remove_low_variance removed all features from dataframe."):
>>               dataframe_helpers.remove_variance(dataframe, self.threshold)
>>               E     Failed: DID NOT RAISE <class 'RuntimeError'>
>
>tests/test_dataframe_helpers.py:50: Failed
>============================ short test summary info ============================
>FAILED tests/test_dataframe_helpers.py::TestRemoveLowVariance::test_remove_low_variance_throws_error
>========================== 1 failed, 1 passed in 1.10s ==========================

### Green

Now let's fix our code!  To do so, we need only to check if we have no columns left in our dataframe before we return it to the user. 

```python
import pandas as pd

def remove_low_variance(df: pd.DataFrame, threshold: float) -> pd.DataFrame:
	"""
	This function removes the low variance values from a dataframe
	determined by some threshold
	"""
	
	# Create mask and extract desired columns
	high_variance_mask = df.var() > threshold
	high_variance_columns = df.columns[high_variance_mask]

	# Extract desired columns from actual dataframe
	low_variance_dataframe = df[ high_variance_columns ] 

	if len(low_variance_dataframe.columns) == 0: 
		raise RuntimeError("remove_low_variance removed all features from dataframe.")
	return low_variance_dataframe
```

And we check our code: 
```
pytest
```

>collected 2 items                                                               
>
>tests/test_dataframe_helpers.py ..                                        [100%]
>
>=============================== 2 passed in 0.83s ===============================

Golden. 



Could we add even more tests? Such as ones to make sure we account for empty data frames entering the function? Absolutely! But let's move onto another type of testing: 



## Mocking:

Let's expand our work. We're now relatively certain we've got some good ground to stand on with respect to the `remove_low_variance`funciton. Let's add a function that calls low variance and then adds it to file. 

Let's write our skeleton: 
```python
def remove_variance_and_write_to_file(df: pd.DataFrame, threshold: float, outfile: str) -> None: 
	"""
	This function calls remove_variance and saves the output to file. 
	"""

	return None
```

We've written a basic skeleton of our function. Let's write our test class and base:

```python
class TestRemoveLowVarianceAndWriteToFile: 
	"""
	This test class tests the remove_low_variance_and_write_to_file function. 
	"""

	def test_remove_low_variance_and_write_to_file(self):
		"""
		This function tests remove_low_variance_and_write_to_file. 
		"""
		print("hello")

```

Before we go any further: 

- We have data that we've already written above. There's no need to copy paste when we can just refactor a smidge and reuse it. 
- With this class we don't want to test everything we've already done again. We've already written tests for `remove_low_var`, and we certainly don't want to start saving test files all over the place, so what we would like to do is create a **"mock"** for our functions that sit in for the actual functions (so we can be sure they're called). 

Let's first refactor our code: 

```python
import numpy as np 
import pandas as pd
import pytest
import pytest_mock

from lib import dataframe_helpers

data_all_zero = {
	"a": [ 0, 0, 0, 0, 0],
	"b": [ 0, 0, 0, 0, 0],
	"c": [ 0, 0, 0, 0, 0],
	"d": [ 0, 0, 0, 0, 0]
}

dataframe_no_var = pd.DataFrame(data=data_all_zero)
threshold = 0.1


class TestRemoveLowVariance:
	"""
	This class tests the remove low variance function
	""" 

	def test_remove_low_variance(self): 
		"""
		This function tests 'remove_low_var' with ideal parameters.
		"""
		data = {
					"a": [0, 1, 2, 3, 2, 1, 3, 0, 3], # sum = 15  
					"b": [0, 0, 0, 0, 0, 0, 0, 0, 0], # sum =  0
					"c": [2, 1, 2, 3, 1, 3, 2, 3, 3], # sum = 20 
					"d": [1, 0, 0, 1, 0, 1, 1, 0, 1]  # sum =  5
				}
		dataframe = pd.DataFrame(data= data)

		expected_output_columns = ['a','c','d']
		expected_output = dataframe[ expected_output_columns ]

		actual_output = dataframe_helpers.remove_low_variance(dataframe, self.threshold)

		pd.testing.assert_frame_equal(expected_output, actual_output)
		

	def test_remove_low_variance_throws_error(self):
		"""
		This test asserts that remove_low_var throws an error
		when there exist no columns within the low variance dataframe
		"""

		with pytest.raises(RuntimeError, match="remove_low_variance removed all features from dataframe."):
			dataframe_helpers.remove_low_variance(dataframe_no_var, self.threshold)


class TestRemoveLowVarianceAndWriteToFile: 
	"""
	This test class tests the remove_low_variance_and_write_to_file function. 
	"""

	def test_remove_low_variance_and_write_to_file(self):
		"""
		This function tests remove_low_variance_and_write_to_file. 
		"""
		print('hello')

```

Now, for our mocking, what we want to do is write a "mock" that overwrites two functions: 

- `remove_low_variance`: since we've already tested it
- `.to_csv(outfile)`: since we don't actually want to write our test data to csv

We can do this with mocks: 

```python
class TestRemoveLowVarianceAndWriteToFile: 
	"""
	This test class tests the remove_low_variance_and_write_to_file function. 
	"""

	def test_remove_low_variance_and_write_to_file(self, mocker):
		"""
		This function tests remove_low_variance_and_write_to_file. 
		"""
		
		output_file = "testout.tsv"

		rlv_mock = mocker.patch("lib.dataframe_helpers.remove_low_variance", return_value=dataframe)
		to_csv_mock = mocker.patch.object(dataframe, "to_csv")
		
		dataframe_helpers.remove_low_variance_and_write_to_file(dataframe, threshold, output_file)

		rlv_mock.assert_called_once_with(dataframe, threshold)
		to_csv_mock.assert_called_once_with(output_file)

```

Now, when we run our tests, we'll naturally fail as we haven't fleshed out our actual code: 
```
pytest
```

> ===================== test session starts =====================
> platform darwin -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
> rootdir: /Users/96v/Documents/projects/test/basic_testing
> plugins: anyio-3.5.0, mock-3.10.0, cov-4.0.0
> collected 3 items                                             
>
> tests/test_dataframe_helpers.py ..F                     [100%]
>
> ========================== FAILURES ===========================
> _ TestRemoveLowVarianceAndWriteToFile.test_remove_low_variance_and_write_to_file _
>
> __wrapped_mock_method__ = <function NonCallableMock.assert_called_once_with at 0x7f7b849fb550>
> args = (<MagicMock name='remove_low_variance' id='140168509078208'>,    a  b  c  d
> 0  0  0  2  1
> 1  1  0  1  0
> 2  2  0  2  0
> 3  3  0  3  1
> 4  2  0  1  0
> 5  1  0  3  1
> 6  3  0  2  1
> 7  0  0  3  0
> 8  3  0  3  1, 0.1)
> kwargs = {}, __tracebackhide__ = True
> msg = "Expected 'remove_low_variance' to be called once. Called 0 times."
> __mock_self = <MagicMock name='remove_low_variance' id='140168509078208'>
>
>     def assert_wrapper(
>         __wrapped_mock_method__: Callable[..., Any], *args: Any, **kwargs: Any
>     ) -> None:
>         __tracebackhide__ = True
>         try:
> >           __wrapped_mock_method__(*args, **kwargs)
>
> /Users/96v/opt/anaconda3/lib/python3.8/site-packages/pytest_mock/plugin.py:444: 
> _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
>
> self = <MagicMock name='remove_low_variance' id='140168509078208'>
> args = (   a  b  c  d
> 0  0  0  2  1
> 1  1  0  1  0
> 2  2  0  2  0
> 3  3  0  3  1
> 4  2  0  1  0
> 5  1  0  3  1
> 6  3  0  2  1
> 7  0  0  3  0
> 8  3  0  3  1, 0.1)
> kwargs = {}
> msg = "Expected 'remove_low_variance' to be called once. Called 0 times."
>
>     def assert_called_once_with(self, /, *args, **kwargs):
>         """assert that the mock was called exactly once and that that call was
>         with the specified arguments."""
>         if not self.call_count == 1:
>             msg = ("Expected '%s' to be called once. Called %s times.%s"
>                    % (self._mock_name or 'mock',
>                       self.call_count,
>                       self._calls_repr()))
> >           raise AssertionError(msg)
> >           E           AssertionError: Expected 'remove_low_variance' to be called once. Called 0 times.
>
> /Users/96v/opt/anaconda3/lib/python3.8/unittest/mock.py:924: AssertionError
>
> During handling of the above exception, another exception occurred:
>
> self = <test_dataframe_helpers.TestRemoveLowVarianceAndWriteToFile object at 0x7f7b86313700>
> mocker = <pytest_mock.plugin.MockerFixture object at 0x7f7b863134f0>
>
>     def test_remove_low_variance_and_write_to_file(self, mocker):
>         """
>         This function tests remove_low_variance_and_write_to_file.
>         """
>     
>         output_file = "testout.tsv"
>     
>         rlv_mock = mocker.patch("lib.dataframe_helpers.remove_low_variance", return_value=dataframe)
>         to_csv_mock = mocker.patch.object(dataframe, "to_csv")
>     
>         dataframe_helpers.remove_low_variance_and_write_to_file(dataframe, threshold, output_file)
>
> >       rlv_mock.assert_called_once_with(dataframe, threshold)
> >       E    AssertionError: Expected 'remove_low_variance' to be called once. Called 0 times.
>
> tests/test_dataframe_helpers.py:78: AssertionError
> =================== short test summary info ===================
> FAILED tests/test_dataframe_helpers.py::TestRemoveLowVarianceAndWriteToFile::test_remove_low_variance_and_write_to_file
> ================= 1 failed, 2 passed in 1.32s =================



### Green:

Mock outputs are exceptionally detailed when they fail. Let's write our code to actually call `remove_low_var` and save it to a csv: 

```python
def remove_low_variance_and_write_to_file(df: pd.DataFrame, threshold: float, outfile: str) -> None: 
	"""
	This function calls remove_variance and saves the output to file. 
	"""

	low_variance_df = remove_low_variance(df, threshold)
	low_variance_df.to_csv(outfile)

	return None
```

Now when we run our pytest, we substitute in the `mock` objects for the actual functions: 

```
pytest
```

>===================== test session starts =====================
>platform darwin -- Python 3.8.12, pytest-6.2.5, py-1.11.0, pluggy-1.0.0
>rootdir: /Users/96v/Documents/projects/test/basic_testing
>plugins: anyio-3.5.0, mock-3.10.0, cov-4.0.0
>collected 3 items                                             
>
>tests/test_dataframe_helpers.py ...                     [100%]
>
>====================== 3 passed in 0.96s ======================



Huzzah! Now we've written tests and even mocked data! 

