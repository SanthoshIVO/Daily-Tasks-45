import { ask, closeInput } from "./input.js";
async function main() {
    const number = Number(await ask("Enter an integer from 0 to 18: "));
    if (!Number.isInteger(number) || number < 0 || number > 18) {
        console.log("Enter a whole number from 0 to 18.");
        return;
    }
    let factorial = 1;
    for (let value = 1; value <= number; value++) {
        factorial *= value;
    }
    console.log(`${number}! = ${factorial}`);
}
void main().finally(closeInput);
//# sourceMappingURL=08_factorial.js.map