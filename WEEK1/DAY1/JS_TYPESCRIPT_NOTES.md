# JavaScript and TypeScript Fundamentals

Beginner-friendly notes for the topics in `JS_Basics` and `TS_basics`.

## 1. What are JavaScript and TypeScript?

- **JavaScript (JS)** is a programming language used in web browsers and in environments such as Node.js.
- **TypeScript (TS)** builds on JavaScript by adding optional static types. A TypeScript compiler checks the types and converts `.ts` files into JavaScript that can run in Node.js or a browser.
- Most JavaScript is valid TypeScript, but TypeScript-only annotations must be removed by compiling before running in a regular JavaScript runtime.

## 2. Requirements and packages

Install **Node.js** (which includes npm) to run JavaScript and manage TypeScript packages. Check that they are available in PowerShell:

```powershell
node --version
npm --version
```

### JavaScript packages

The examples in this guide need **no additional packages**. Node.js can run a `.js` file directly.

### TypeScript package

The TypeScript compiler (`tsc`) is a development dependency. In the TypeScript project folder, install it once:

```powershell
cd E:\Ivoyant\WEEK1\DAY1\TS_basics
npm init -y
npm install --save-dev typescript
```

`npm init -y` creates `package.json`; `npm install` adds TypeScript to the project. The installed compiler can then be run with `npx tsc`.

## 3. Run the existing starter projects

### Run the JavaScript starter

From `E:\Ivoyant\WEEK1\DAY1`:

```powershell
node .\JS_Basics\index.js
```

### Compile and run the TypeScript starter

From `E:\Ivoyant\WEEK1\DAY1\TS_basics`:

```powershell
npx tsc
node .\dist\index.js
```

The TypeScript configuration uses `src` as its source folder and `dist` as its output folder. Run the generated `dist\index.js`, not `index.js` from the project root.

## 4. Basic program structure and output

`console.log()` prints a value to the terminal or browser developer console.

```js
console.log("Hello, world!");
console.log(2 + 3);
```

Save JavaScript examples in a `.js` file and run them with `node .\filename.js`.

## 5. Variables: `let` and `const`

A **variable** is a named place to store a value.

- Use `const` when you will not assign a different value to the variable.
- Use `let` when you need to assign a different value later.
- Avoid `var` in new code; `let` and `const` have clearer block scope.

```js
const studentName = "Maya";
let score = 80;

score = score + 5;
console.log(studentName, score); // Maya 85
```

`const` prevents reassignment, but it does not make an object or array immutable:

```js
const colors = ["blue"];
colors.push("green"); // Allowed: the array contents changed.
// colors = [];       // Not allowed: assigning a new array to a const.
```

### TypeScript variable annotations

TypeScript can infer a variable's type from its initial value. You can also write the type explicitly:

```ts
const studentName: string = "Maya";
let score: number = 80;

score += 5;
```

## 6. Data types

Common JavaScript types:

| Type | Meaning | Example |
|---|---|---|
| `string` | Text | `"hello"` |
| `number` | Integer or decimal number | `42`, `3.14` |
| `boolean` | True or false | `true` |
| `undefined` | A value has not been assigned | `let result;` |
| `null` | An intentional absence of a value | `const selected = null;` |
| `object` | Structured data, including objects and arrays | `{ name: "Maya" }`, `[1, 2]` |

JavaScript is **dynamically typed**: a variable can hold values of different types at different times. TypeScript can check declared or inferred types before the program runs.

```js
let value = 10;
value = "ten"; // JavaScript allows this.
```

```ts
let value: number = 10;
// value = "ten"; // TypeScript reports a type error.
```

Use `typeof` to check many values at runtime:

```js
console.log(typeof "hello"); // "string"
console.log(typeof 42);      // "number"
console.log(typeof true);    // "boolean"
```

Note: `typeof null` returns `"object"` in JavaScript, a historical quirk.

## 7. Operators

### Arithmetic

```js
const total = 10 + 3;       // 13: addition
const difference = 10 - 3;  // 7: subtraction
const product = 10 * 3;     // 30: multiplication
const quotient = 10 / 3;    // division
const remainder = 10 % 3;   // 1: remainder
const power = 2 ** 3;       // 8: exponent
```

### Assignment

```js
let count = 4;
count += 2; // count = count + 2
count -= 1;
count *= 3;
```

### Comparison

Comparison operators return a boolean:

```js
console.log(5 > 3);        // true
console.log(5 <= 3);       // false
console.log(5 === 5);      // true: strict equality
console.log(5 !== "5");    // true: different type and value
```

Prefer `===` and `!==` to `==` and `!=`, which can convert values before comparing them.

### Logical and nullish operators

```js
const isAdult = true;
const hasTicket = false;

console.log(isAdult && hasTicket); // AND: true only when both are true
console.log(isAdult || hasTicket); // OR: true when either is true
console.log(!isAdult);             // NOT: reverses a boolean
```

`??` supplies a fallback only for `null` or `undefined`; `||` supplies one for any falsy value, including `0` and `""`.

```js
const suppliedName = "";
console.log(suppliedName ?? "Guest"); // ""
console.log(suppliedName || "Guest"); // "Guest"
```

## 8. Conditional statements

Use `if`, `else if`, and `else` to choose which code to run:

```js
const temperature = 24;

if (temperature >= 30) {
  console.log("Hot");
} else if (temperature >= 18) {
  console.log("Comfortable");
} else {
  console.log("Cool");
}
```

Use `switch` when comparing one value with several specific options:

```js
const day = "Monday";

switch (day) {
  case "Monday":
    console.log("Start of the week");
    break;
  case "Friday":
    console.log("Nearly the weekend");
    break;
  default:
    console.log("Another day");
}
```

The `break` statements prevent execution from falling through to the next case.

## 9. Loops

Loops repeat code. Use the loop that makes the intent easiest to understand.

### `for`

Use when you know how many times to repeat:

```js
for (let i = 0; i < 3; i++) {
  console.log(i); // 0, then 1, then 2
}
```

### `while`

Use when repetition depends on a condition:

```js
let countdown = 3;

while (countdown > 0) {
  console.log(countdown);
  countdown--;
}
```

### `for...of`

Use to visit each value in an array:

```js
const fruits = ["apple", "pear", "plum"];

for (const fruit of fruits) {
  console.log(fruit);
}
```

`break` exits a loop early. `continue` skips the rest of the current iteration and moves to the next one.

## 10. Arrays

An **array** stores an ordered list of values. Array indexes start at `0`.

```js
const fruits = ["apple", "pear", "plum"];

console.log(fruits[0]);    // "apple"
console.log(fruits.length); // 3

fruits.push("orange"); // Add to the end
fruits.pop();          // Remove the last item
```

Useful array methods:

```js
const numbers = [1, 2, 3, 4];

const doubled = numbers.map((number) => number * 2); // [2, 4, 6, 8]
const large = numbers.filter((number) => number > 2); // [3, 4]
const found = numbers.find((number) => number === 3); // 3
```

### TypeScript arrays

Use `type[]` or `Array<type>` to describe the element type:

```ts
const fruits: string[] = ["apple", "pear"];
const scores: Array<number> = [80, 95, 100];
```

## 11. Objects

An **object** groups related information into named properties:

```js
const student = {
  name: "Maya",
  age: 20,
  isEnrolled: true,
};

console.log(student.name);       // Dot notation
console.log(student["age"]);     // Bracket notation
student.age = 21;                // Update a property
student.course = "JavaScript";   // Add a property
```

### TypeScript object types

Describe the expected properties and their types:

```ts
type Student = {
  name: string;
  age: number;
  isEnrolled: boolean;
  course?: string; // Optional property
};

const student: Student = {
  name: "Maya",
  age: 20,
  isEnrolled: true,
};
```

The `?` means the property may be omitted.

## 12. Functions

A **function** is a reusable block of code. It can accept inputs (parameters) and return a result.

```js
function add(a, b) {
  return a + b;
}

console.log(add(2, 3)); // 5
```

If a function has no `return`, its result is `undefined`.

### TypeScript function types

Annotate parameters and, when useful, the return type:

```ts
function add(a: number, b: number): number {
  return a + b;
}
```

## 13. Arrow functions

An **arrow function** is a shorter function expression, often used for callbacks:

```js
const multiply = (a, b) => {
  return a * b;
};

const square = (number) => number * number;
console.log(square(4)); // 16
```

When an arrow function has one expression, the braces and `return` can be omitted. Parentheses around a single parameter are optional in JavaScript, but keeping them is often clearer.

### TypeScript arrow function

```ts
const multiply = (a: number, b: number): number => a * b;
```

## 14. A small combined example

This JavaScript example uses variables, an array, a function, a loop, and a conditional:

```js
const scores = [72, 91, 85];

function average(values) {
  let total = 0;

  for (const value of values) {
    total += value;
  }

  return values.length === 0 ? 0 : total / values.length;
}

const result = average(scores);
console.log(`Average: ${result}`);

if (result >= 80) {
  console.log("Good work!");
} else {
  console.log("Keep practicing!");
}
```

The TypeScript equivalent can make the expected array and return types explicit:

```ts
const scores: number[] = [72, 91, 85];

function average(values: number[]): number {
  let total = 0;

  for (const value of values) {
    total += value;
  }

  return values.length === 0 ? 0 : total / values.length;
}

const result: number = average(scores);
console.log(`Average: ${result}`);
```

## 15. Steps to create and run your own files

### JavaScript

1. Open PowerShell and go to the Day 1 folder:

   ```powershell
   cd E:\Ivoyant\WEEK1\DAY1
   ```
2. Create a file such as `practice.js` in that folder.
3. Add JavaScript code and save the file.
4. Run it:

   ```powershell
   node .\practice.js
   ```
5. Read the output or error in the terminal, edit the file, and run it again.

### TypeScript

1. Open PowerShell and go to the TypeScript project:

   ```powershell
   cd E:\Ivoyant\WEEK1\DAY1\TS_basics
   ```
2. If not already installed in this project, set up TypeScript:

   ```powershell
   npm init -y
   npm install --save-dev typescript
   ```
3. Create or edit a `.ts` file inside `src`, for example `src\index.ts`.
4. Compile the project:

   ```powershell
   npx tsc
   ```
5. Fix any type or syntax errors printed by the compiler, then compile again.
6. Run the generated JavaScript:

   ```powershell
   node .\dist\index.js
   ```

`npx tsc` uses the project's `tsconfig.json`. In this project, compiled JavaScript is written to `dist`.
