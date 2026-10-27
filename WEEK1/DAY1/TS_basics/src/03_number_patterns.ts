import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const rows = Number(await ask("Enter the number of rows: "));
  if (!Number.isInteger(rows) || rows < 1) {
    console.log("Enter a positive whole number of rows.");
    return;
  }

  console.log("\nStar pattern:");
  for (let row = 1; row <= rows; row++) {
    console.log("* ".repeat(row));
  }

  console.log("\nNumber pattern:");
  for (let row = 1; row <= rows; row++) {
    const numbers: number[] = [];
    for (let number = 1; number <= row; number++) {
      numbers.push(number);
    }
    console.log(numbers.join(" "));
  }
}

void main().finally(closeInput);
