import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const first = Number(await ask("Enter the first number: "));
  const second = Number(await ask("Enter the second number: "));
  const third = Number(await ask("Enter the third number: "));

  if (![first, second, third].every(Number.isFinite)) {
    console.log("Enter valid numbers.");
    return;
  }

  console.log(`The largest number is ${Math.max(first, second, third)}.`);
}

void main().finally(closeInput);
