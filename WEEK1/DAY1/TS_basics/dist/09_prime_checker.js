import { ask, closeInput } from "./input.js";
async function main() {
    const number = Number(await ask("Enter an integer: "));
    if (!Number.isInteger(number)) {
        console.log("Enter a valid integer.");
        return;
    }
    if (number < 2) {
        console.log(`${number} is not a prime number.`);
        return;
    }
    let isPrime = true;
    for (let divisor = 2; divisor <= Math.sqrt(number); divisor++) {
        if (number % divisor === 0) {
            isPrime = false;
            break;
        }
    }
    console.log(`${number} is ${isPrime ? "" : "not "}a prime number.`);
}
void main().finally(closeInput);
//# sourceMappingURL=09_prime_checker.js.map