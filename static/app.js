

const $cupcakeList = $('#cupcake-list');
const $addButton = $('#add-button');

// function to get list of cupcakes from API and add to the page
async function getCupcakes() {
    
    const cupcakes = await axios.get('http://127.0.0.1:5000/api/cupcakes')
    items = cupcakes.data.cupcakes

    for(let i = 0; i < items.length; i++) {
        console.log(items[i].flavor); 
        $cupcakeList.append(`<li>${items[i].flavor}</li>`);
    }
    // returns an array of two objects
    return cupcakes.data.cupcakes
}

getCupcakes();

// handle clicks to the button
$addButton.on("click", function (event) {
    event.preventDefault();
    console.log("You clicked!")

// capture the form data
    flavor = $('#flavor').val()
    size = $('#size').val()
    rating = $('#rating').val()
    image = $('#image').val()

// make an API call to add the cupcake
    


// update the DOM

})

