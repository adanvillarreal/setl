# Marmoset
Marmoset is a programming language based on SETL (more information here: http://hopl.info/showlanguage.prx?exp=1268). Marmoset is a typed, procedural language that supports functions. It's main characteristic is that it implements sets as the main non-atomic data structure, and supports set operations.

## Compiling
To compile a program, run `python lexer.py filename [quads]` if `quads` is sent as second parameter, it will print the list of quadruples.

## Code layout
Marmoset requires the programmer to adhere to the following code order:
1. Signature `program name;`
2. Global variables
3. Functions
4. Main

Functions and Main follow the order:
1. Local variables
2. Statements

All lines are terminated by a `;`, except for opening and closing braces.

## Variable types and declaration
A variable can be declared in the following way: `datatype varID;`
### Datatypes
Atomic variables can be of type:
* `int`
* `float`
* `char`
* `string`
* `bool`

Non-atomic variables can be of type:
* `set<atomic_datatype>`
* `map<atomic_datatype, atomic_datatype>`

### Declaring a variable
To declare a variable, one must simply type: `datatype varID;` a `varID` must start with a lowercase followed by any letter or `_`.

### Assigning a value to a variable
To assign a value to a variable, one should use the assignator operator `:=`. For instance `x := 3 + 4;`

## Functions 
### Declarations
Function signatures follow the structure: `return_type function_name(param1, param2,..., paramN){...}` The return type can be any of the atomic datatypes or void. If the return type is non-void, the function must return a value. The parameters can be any of the atomic datatypes and a function can have zero or more parameters.

### Calls
Functions can be called with: `function_name(params)`. 

## Operations
### Atomic operations
Marmoset support the arithmetic operations `+, -, *, /`. These operators can be only applied to numeric and string operands of the same datatype (i.e. `int` with `int`, `float` with `float`, etc.). Numeric datatypes can also be compared by using `>, >=, <, <=, ==, !=`

Boolean operands can be manipulated with logical operators such as `||, &&, !`.

### Set operations
Sets of the same datatype support the following operations:
* union: `.+`
* difference: `.-`
* intersection: `.*`
* size: `varID.size()`
* find: `varID.find(value)` returning true or false if element exists
* remove: `varId.remove(value)` 

### Map operations
 Maps are key-value pairs. The operations on maps can be:
 * retrieval: `varID[key]`
 * assignment: `varID[key] = expression`
 * range: `varID.range()` returns a set with the range.
 * domain: `varID.domain()` returns a set with the domain
 
 ## Input/Output
 ### Input
 Input from console can be read with `read(varID, varID2, ...);`, where `varID` must be already declared. Only atomic datatypes can be read from console.
 
 ### Output
 Printing to console can be achieved with `print(expression, varID2,...);`, all data types except maps can be printed.

## Examples
### Fibonacci-primes
The following code calculates the intersection between the fibonacci set and the primes set.
``` 
program aPlusB;

set<int> primes;
map<int, bool> M;
set<int> union, intersection, dif;

set<int> fib;

void fibonacci(int n){
  int first, second, aux;
  first := 0;
  second := 1;

  while(first < n){
    fib.insert(first);
    aux := second + first;
    first := second;
    second := aux;
  }

}

void sieve(int n){
  int i, j;
  i := 0;

  print(M[1]);

  while(i < n){
    M[i] := true;
    i := i + 1;
  }

  i := 2;

  while(i < n){
    j := 2;
    if(M[i] == true){
      primes.insert(i);
    }
    while(i * j < n){
      M[i * j] := false;
      j := j + 1;
    }
    i := i + 1;
  }
}

main {
  int limit;
  int i;
  limit := 100;

  sieve(limit);
  print(primes);

  fibonacci(limit);
  print(fib);

  intersection := primes .* fib;
  print(intersection);

} 
```
