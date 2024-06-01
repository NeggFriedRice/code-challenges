function superDigit(n, k) {
    // Write your code here
    let concatNumber = ""
    for (let i = 0; i < k; i++) {
        concatNumber += n
    }

    let target = BigInt(concatNumber)
    console.log(target)

    super_digit(target)

    function super_digit(v) {
        let sum = 0
        if (v < 10) {
            return v
        } else {
            for (let j = 0; j < String(v).length; j++) {
                sum += Number((String(v)[j]))
            }
            target = sum
        }
        console.log(target)
        super_digit(target)
    }

    return target
}

console.log(superDigit("9875", 4))