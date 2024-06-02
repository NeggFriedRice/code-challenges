function getEarliestMeetTime(events, k) {
    // Write your code here
    
    let wakeup1 = 0
    for (let i = 0; i < events.length - 1; i++) {
        let split1 = events[i].split("")
        let split2 = events[i + 1].split("")
        


        if (split1[1] == 'sleep') {
            wakeup1 = split1[-1] += 1
        }

        return wakeup1
    }
}

events = ["sam sleep 12:00 18:59"]
