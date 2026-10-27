import { ask, closeInput } from "./input.js";
async function main() {
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
//# sourceMappingURL=07_multiplication_table.js.map