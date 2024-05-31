function caesarCipher(s, k) {
    // Write your code here
    const alphabet = "abcdefghijklmnopqrstuvwxyz"
    let output = ""
    let shift = k % 26
   
    for (let i = 0; i < s.length; i ++) {
        if (s[i].toUpperCase() != s[i].toLowerCase()) {
            if (alphabet.includes(s[i])) {
                output += alphabet[(alphabet.indexOf(s[i]) + shift) % 26]
            } else {
                output += alphabet[(alphabet.indexOf(s[i].toLowerCase()) + shift) % 26].toUpperCase()
            }
        } else {
            output += s[i]
        }
    }

    return output
}

 

// Indexof + shift % 26
console.log(caesarCipher("o-u-t-Z", 2))