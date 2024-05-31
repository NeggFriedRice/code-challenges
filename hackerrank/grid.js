function gridChallenge(grid) {
    // Write your code here

    let newGrid = []

    for (let i = 0; i < grid.length; i++) {
        let sorted = grid[i].split("").sort().join("")
        newGrid.push(sorted)
    }

    let column = newGrid[0].length
    for (let j = 0; j < newGrid.length - 1; j++) {
        for (let z = 0; z < column; z++) {
            if (newGrid[j][z] > newGrid[j + 1][z]) {
                return "NO"
            }
        }
    }

    return "YES"

}

const grid = ['mpxz', 'abcd', 'wlmf']

console.log(gridChallenge(grid))

