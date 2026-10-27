import { ask, closeInput } from "./input.js";

async function main(): Promise<void> {
  const score = Number(await ask("Enter a score from 0 to 100: "));
  if (!Number.isFinite(score) || score < 0 || score > 100) {
    console.log("Enter a valid score between 0 and 100.");
  } else if (score >= 90) {
    console.log("Grade: A");
  } else if (score >= 80) {
    console.log("Grade: B");
  } else if (score >= 70) {
    console.log("Grade: C");
  } else if (score >= 60) {
    console.log("Grade: D");
  } else {
    console.log("Grade: F");
  }
}

void main().finally(closeInput);
