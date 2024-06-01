function minimumBribes(q) {
    // Write your code here
    let bribes = 0
    for (let i = q.length - 1; i >= 0; i--) {
        if (q[i] != i + 1) {
            if (q[i-1] == i + 1) {
                bribes += 1
                let tmp = q[i]
                q[i] = q[i-1]
                q[i-1] = tmp
            } else if (q[i-2] == i + 1) {
                bribes += 2
                let tmp2 = q[i-2]
                q[i-2] = q[i-1]
                q[i-1] = q[i]
                q[i] = tmp2
            } else {
                console.log("Too chaotic")
                return
            }
        }
    }
    console.log(bribes)
}

minimumBribes([ 1, 3, 2 ])