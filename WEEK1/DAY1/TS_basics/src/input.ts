import { stdin, stdout } from "node:process";
import { createInterface } from "node:readline/promises";

const readline = createInterface({ input: stdin, output: stdout });

export function ask(question: string): Promise<string> {
  return readline.question(question);
}

export function closeInput(): void {
  readline.close();
}
