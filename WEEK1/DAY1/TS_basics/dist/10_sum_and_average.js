import { ask, closeInput } from "./input.js";
async function main() {
    const entry = await ask("Enter numbers separated by commas: ");
    if (!entry.trim()) {
        console.log("Enter one or more numbers.");
        return;
    }
    const numbers = entry.split(",").map((value) => Number(value.trim()));
    if (!numbers.every(Number.isFinite)) {
        console.log("Enter one or more valid numbers separated by commas.");
        return;
    }
    const total = numbers.reduce((sum, number) => sum + number, 0);
    const average = total / numbers.length;
    console.log(`Sum: ${total}`);
    console.log(`Average: ${average}`);
}
void main().finally(closeInput);
//# sourceMappingURL=10_sum_and_average.js.map