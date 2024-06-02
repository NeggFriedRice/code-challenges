function findLowestPrice(products, discounts) {
    // Write your code here

    let total = 0

    for (let i = 0; i < products.length; i++) {
        let price1 = products[i][0]
        let productPrice = products[i][0]

        if (discounts.length == 0) {
            price1 = productPrice
        }

        for (let j = 0; j < discounts.length; j++) {
            if(discounts[j][0].includes(products[i][1])) {
                if (discounts[j][1] == "0") {
                    let price2 = discounts[j][2]
                    if (price2 <= price1) {
                        price1 = price2
                    }
                } else if (discounts[j][1] == "1") {
                    let price2 = productPrice - (productPrice * (1 / discounts[j][2]))
                    if (price2 <= price1) {
                        price1 = price2
                    }
                } else if (discounts[j][1] == "2") {
                    let price2 = productPrice - discounts[j][2]
                    if (price2 <= price1) {
                        price1 = price2
                    }
                }
            } else {
                price1 = productPrice
            }
            
        }
        total += Math.floor(Number(price1))
    }

    return total
}

products = [["50","dcoupon1"]]
discounts = [["dcoupon1","1","30"]]

console.log(findLowestPrice(products, discounts))