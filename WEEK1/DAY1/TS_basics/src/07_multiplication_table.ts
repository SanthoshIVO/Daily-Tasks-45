import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const number = Number(await ask("Enter an integer: "));
  if (!Number.isInteger(number)) {
    console.log("Enter a valid integer.");
    return;
  }

  for (let multiplier = 1; multiplier <= 10; multiplier++) {
    console.log(`${number} x ${multiplier} = ${number * multiplier}`);
  }
}

void main().finally(closeInput);
