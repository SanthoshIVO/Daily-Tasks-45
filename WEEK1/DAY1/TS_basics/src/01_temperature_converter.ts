import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const celsius = Number(await ask("Enter temperature in Celsius: "));
  if (!Number.isFinite(celsius)) {
    console.log("Enter a valid number.");
    return;
  }

  const fahrenheit = (celsius * 9) / 5 + 32;
  console.log(`${celsius.toFixed(2)}°C = ${fahrenheit.toFixed(2)}°F`);
}

void main().finally(closeInput);
