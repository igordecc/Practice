let pets = ["dog", "cat", "fly", "bug", "oxs"]
console.log("original array 'pets': ", pets)
pets.push("cow") 
console.log("pets.push('cow')", pets)
pets.pop()
console.log("pets.pop()", pets)
let pet = pets.shift()
console.log("pets.shit()", pets)
pets.unshift(pet)
console.log(`pets.unshift(${pet})`, pets)
pets.splice(2, 2, "pig", "duck", "emu")
console.log("splice(2, 2, 'pig', 'duck', 'emu') - delete two elements and add three starting next to element pets[1]  ", pets)
