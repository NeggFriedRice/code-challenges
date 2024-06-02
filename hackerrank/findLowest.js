function findLowestPrice(products, discounts) {
    // Write your code here
    let total = 0

    for (let i = 0; i < products.length; i++) {
        let productPrice = products[i][0]

        let price1 = 0
        let price2 = 0

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



        if (products[i][1] != 'EMPTY') {
            if (products[i][1] == d1Name && d1Type == '0') {
                price1 += Number(d1Discount)
            } else if (products[i][1] == d1Name && d1Type == '1') {
                price1 += Number(productPrice - (productPrice * 1 / d1Discount))
            } else if (products[i][1] == d1Name && d1Type == '2') {
                price1 += Number(productPrice - d1Discount)
            } else if (products[i][1] == d1Name && d1Type == '0') {
                price1 += Number(d1Discount)
            } else if (products[i][1] == d1Name && d1Type == '1') {
                price1 += Number(productPrice - (productPrice * 1 / d1Discount))
            } else if (products[i][1] == d1Name && d1Type == '2') {
                price1 += Number(productPrice - d1Discount)
            }
        } else {
            price1 = productPrice
        }
        if (products[i][2] != 'EMPTY') {
            if (products[i][2] == d2Name && d2Type == '0') {
                price2 += Number(d2Discount)
            } else if (products[i][2] == d2Name && d2Type == '1') {
                price2 += Number(productPrice - (productPrice * 1 / d2Discount))
            } else if (products[i][2] == d2Name && d2Type == '2') {
                price2 += Number(productPrice - d2Discount)
            } else if (products[i][2] == d2Name && d2Type == '0') {
                price2 += Number(d2Discount)
            } else if (products[i][2] == d2Name && d2Type == '1') {
                price2 += Number(productPrice - (productPrice * 1 / d2Discount))
            } else if (products[i][2] == d2Name && d2Type == '2') {
                price2 += Number(productPrice - d2Discount)
            }
        } else {
            price2 = productPrice
        }

        if (price1 <= price2) {
            total += Number(price1)
        } else {
            total += Number(price2)
        }

    }

    return total

}

products = [["10","sale","january-sale"],["200","sale","EMPTY"]]
discounts = [["sale","0","10"],["january-sale","1","10"]]

console.log(findLowestPrice(products, discounts))





    // for (let i = 0; i < products.length; i++) {
    //     for (let j = 0; j < discounts.length; j++) {
    //         let price1 = 0
    //         let price2 = 0
    
    //         if (products[i][1] != "EMPTY") {
    //             price1 = products[i][0] - (products[i][0] * (1 / discounts[0][2]))
    //         } else {
    //             price1 = products[i][0]
    //         }
    
    //         if (products[i][2] != "EMPTY") {
    //             price2 = products[i][0] - (products[i][0] * (1 / discounts[1][2]))
    //         } else {
    //             price2 = products[i][0]
    //         }
    
    //         if (price1 <= price2) {
    //             total += price1
    //         } else if (price2 <= price1) {
    //             total += price2
    //         }
    //     }
    // }
    // return total