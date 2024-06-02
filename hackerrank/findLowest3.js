function findLowestPrice(products, discounts) {
    // Write your code here

    let total = 0

    for (let i = 0; i < products.length; i++) {
        let price1 = 99999999
        let productPrice = products[i][0]

        let d1Name, d1Type, d1Discount
        let d2Name, d2Type, d2Discount

        if (discounts[0]) {
            d1Name = discounts[0][0]
            d1Type = discounts[0][1]
            d1Discount = discounts[0][2]
        }

        if (discounts[1]) {
            d2Name = discounts[1][0]
            d2Type = discounts[1][1]
            d2Discount = discounts[1][2]
        }



        for (let j = 0; j < discounts.length; j++) {
            
            if(discounts[j][0].includes(products[i][1]) && discounts[j][1] == "0") {
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
        total += Number(price1)
    }

    return total
}

products = [["10","sale","january-sale"],["200","sale","EMPTY"]]
discounts = [["sale","0","10"],["january-sale","1","10"]]

console.log(findLowestPrice(products, discounts))