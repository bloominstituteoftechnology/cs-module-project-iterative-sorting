//Write a JavaScript program to find 1st January is being a Sunday between 2025 and 2050 (Answer year 2034)

const date = () => {
    // find day Sunday
    for(let i=2025; i<2050; i++ ){
        let year = `January 1, ${i}`
        const d = new Date(year);
        let day = d.getDay();
        if(day === 0) return i
    }
}
console.log(date())