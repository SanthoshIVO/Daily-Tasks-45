import { ask, closeInput } from "./input.js";
async function main() {
    const first = Number(await ask("Enter the first number: "));
    const operation = (await ask("Choose an operation (+, -, *, /): ")).trim();
    const second = Number(await ask("Enter the second number: "));
    if (!Number.isFinite(first) || !Number.isFinite(second)) {
        console.log("Enter valid numbers.");
        return;
    }
    let result;
    if (operation === "+") {
        result = first + second;
    }
    else if (operation === "-") {
        result = first - second;
    }
    else if (operation === "*") {
        result = first * second;
    }
    else if (operation === "/") {
        if (second === 0) {
            console.log("Cannot divide by zero.");
            return;
        }
        result = first / second;
    }
    else {
        console.log("Unknown operation. Choose +, -, *, or /.");
        return;
    }
    console.log(`Result: ${result}`);
}
void main().finally(closeInput);
//# sourceMappingURL=02_simple_calculator.js.map