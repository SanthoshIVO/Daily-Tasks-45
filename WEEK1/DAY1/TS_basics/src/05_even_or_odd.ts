import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const number = Number(await ask("Enter an integer: "));
  if (!Number.isInteger(number)) {
    console.log("Enter a valid integer.");
    return;
  }

  console.log(`${number} is ${number % 2 === 0 ? "even" : "odd"}.`);
}

void main().finally(closeInput);
