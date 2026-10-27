import { stdin, stdout } from "node:process";
import { createInterface } from "node:readline/promises";
const readline = createInterface({ input: stdin, output: stdout });
export function ask(question) {
    return readline.question(question);
}
export function closeInput() {
    readline.close();
}
//# sourceMappingURL=input.js.map