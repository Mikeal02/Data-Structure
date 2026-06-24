//Better Solution-XOR
const miss_number = (arr, n) => {
  let xor1 = arr.reduce((acc, current) => acc ^ current, 0);
  let xor2 = 0;
  for (let i = 1; i <= n; i++) {
    xor2 ^= i;
  }
  return xor1 ^ xor2;
};

//Optimal solution - Math function
const missing_number = (arr, n) => {
  let sum = arr.reduce((acc, current) => acc + current, 0);
  console.log(sum);
  let sum2 = (n * (n + 1)) / 2;
  console.log(sum2);
  return sum2 - sum;
};

const arr = [1, 2, 3, 5, 6];
console.log(`The missing number is : ${miss_number(arr, 6)}`);
