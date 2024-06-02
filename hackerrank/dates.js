function preprocessDate(dates) {
    // Write your code here
    let formatted = []

    for (let i = 0; i < dates.length; i++) {
        let day, month, year
        let splitDates = dates[i].split(" ")
        console.log(splitDates)
        day = splitDates[0]
        month = splitDates[1]
        year = splitDates[2]
        let formattedDay = ""
        const numbers = ["1","2","3","4","5","6","7","8",'9', "0"]
        for (let j = 0; j < day.length; j++) {
            if (numbers.includes(String(day[j])))
                formattedDay += day[j]
        }

        if (formattedDay.length == 1) {
            formattedDay = "0" + formattedDay
        }

        const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

        let formattedMonth = String((months.indexOf(month)) + 1)
        let newFormattedMonth = ""
        
        if (formattedMonth.length == 1) {
            newFormattedMonth = "0" + String(formattedMonth)
        } else {
            newFormattedMonth = formattedMonth
        }

        formatted.push(String(year + "-" + newFormattedMonth + "-" + formattedDay))
    }

    return formatted

}

dates =["1st Jun 2052"]

console.log(preprocessDate(dates))