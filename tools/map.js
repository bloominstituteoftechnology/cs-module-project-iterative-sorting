const contacts = new Map()
contacts.set('Jessie', {phone: "213-555-1234", address: "123 N 1st Ave"})
contacts.has('Jessie') // true
contacts.get('Hilary') // undefined
contacts.set('Hilary', {phone: "617-555-4321", address: "321 S 2nd St"})
contacts.get('Jessie') // {phone: "213-555-1234", address: "123 N 1st Ave"}
contacts.delete('Raymond') // false
contacts.delete('Jessie') // true
console.log(contacts.size) // 1


const teams = new Map()
teams.set('Steelers', {record: '11-7-1'})
console.log(teams.has('Steelers'))
console.log(teams.get('Cheifs'))
teams.set('Cheifs')
console.log(teams.size)

teams.set('Steelers', {...teams, result: 'winners'})
console.log(teams.get('Steelers'))
