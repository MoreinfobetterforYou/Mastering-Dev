// Array: An array is a container which is used to store a collection of values. It uses indexes to number elements and access them. The index starts from 0 and end at length of array - 1. In JS arrays are denoted using square brackets.

// There are two main ways to create arrays in js:
    let array = []; // 99% of the time this syntax will be used to create an array. You use this is mostly everything.
    let AnotherArray = new Array(); // This creates an array using the Array Constructor. It is typically only used when you want to initialize an array with a large number of empty slots to store values later.

// Here is an example showing the difference between if you used the typical syntax VS the Array Constructor.
    let number = [5];
    console.log(number); // This creates an array: [5]
    let SameNumber = new Array(5); 
    console.log(SameNumber); // This creates an array with 5 empty items:

// This is because the array constructor takes one value as a parameter which is the length of the empty array or the number of the empty items you want to store.

// You can create an array with multiple elements of the same data type or even the different data type:
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let everyDataType = ["hi", 1, null, undefined, BigInt, 123456789n, {name: "Hassan", age: 16}, Symbol("hi")]
console.log(numbers)
console.log(everyDataType)

// You can also access elements within an array using their index:
console.log(`My age is: ${numbers[0]}${numbers[5]}`)

// You can also replace the value of the item stored at a specific index by using:
let names = ["Bob", "Ben", "Clark"];
names[0] = "Alex";
console.log(names)

// You can also add a new element by the same method earlier:
names[3] = "Devin"
console.log(names)

// You can also find the length of a particular array by using the .length property:
numberOfNumbersInArray = numbers.length;
console.log(numberOfNumbersInArray)

// Accessing the last element using at(): 
    // Most programming languages allow you to access the last element of a list or an array using index -1. But in javascript you can't do that because the indexes are taken literally, if you use -1 as index it would return undefined because there is no index such as -1. So to solve this issue we use the at() method. :
    console.log(names[-1]) // This returns undefined because there is no element at index -1.
    console.log(names.at(-1)) // This solves the issue by using the .at() method in js. 

// Array Methods:
    // push(): The push() method is used to append an element to the end of an array:
    let friendsInvited = ["Alice", "Ben", "Carl"]
    friendsInvited.push("Devin")

    // pop(): The pop() method is used to remove the last element from an array: 
    friendsInvited.pop()

    // shift(): The shift() method is used to remove the first element from an array and return the removed element:
    let friendNotInvited = friendsInvited.shift()

    // unshift(): The unshift() method is used to add multiple elements to the start or beginning of an array:
    let numberOfPeopleInvited = friendsInvited.unshift("Alice", "Alex")
    console.log(numberOfPeopleInvited)
    console.log(friendsInvited)

// Looping over Array: 
    // Old Way: Using the index:
    for (let i = 0; i < friendsInvited.length; i++){
        console.log(friendsInvited[i]);
    }

    // Modern way: Using the for of way:
    for (let friend of friendsInvited){
        console.log(friend);
    }

// Changing the length of an array: You can change the length of an array manually. If you reduce it you can't restore it back to its original size and it permenantly remains the same. This is known as truncation:
    let fruits = ["apple", "banana", "cherry", "mango"];
    console.log(fruits);
    fruits.length = 2;
    console.log(fruits);
    fruits.length = 4;
    console.log(fruits); // Just like in real life you can't reverse the damage you do to people.

// Multidimensional Arrays: You can also have arrays within arrays. You could use them to store matrices.
    let matrixA = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    console.log(matrixA[1][2]) // This will output 6, it first accesses the second array and then the last element of the 2 array.

// .toString() method: The .toString() method is used to convert an array into a comma seperated list of elements in a string form:
    let arrayOfThingsINeed = ["Exercise", "Abs", "Projects", "Money"];
    let stringOfThingsINeed = arrayOfThingsINeed.toString()
    console.log(stringOfThingsINeed)

// ------------------------------------- Important Note --------------------------------------------
// Arrays like objects can have a trailing comma (meaning each element ends with a comma). This helps in inserting or removing items because all lines of the array become alike.

// An important thing to note is that the .push() method and .pop() method are faster than the .shift() and .unshift() method. Which is because they have to perform more operations like first remove or add the item, then update the index of every single element of the array and then update the length property.

// An important thing to note is that the .at() method is a recent addition to the language, it was first added in ECMAScript 2022. The .at() method is an accessor method only you can't use it to change to set a value to a particular index. 