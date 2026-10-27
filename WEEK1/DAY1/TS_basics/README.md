# TypeScript Exercises

The `src` folder contains ten interactive beginner exercises. They match the programs in `..\python`:

1. Temperature converter
2. Simple calculator
3. Star and number patterns
4. Grade calculator with conditionals
5. Even or odd
6. Largest of three numbers
7. Multiplication table
8. Factorial
9. Prime checker
10. Sum and average

## Requirements

- Node.js and npm.
- Visual Studio Code with the **JavaScript and TypeScript** language support (included with VS Code).
- TypeScript and Node.js type definitions as development dependencies.

From this folder, install the development dependencies once:

```powershell
cd E:\Ivoyant\WEEK1\DAY1\TS_basics
npm install --save-dev typescript @types/node
```

## Compile and run one exercise

Compile the TypeScript files:

```powershell
npm run build
```

Then run an exercise's generated JavaScript with Node.js. For example:

```powershell
node .\dist\01_temperature_converter.js
```

Replace the filename with the matching numbered file in `dist` to run a different exercise. Each program asks for its values in the terminal. The shared `src\input.ts` helper uses Node.js built-ins; no additional runtime packages are needed.
