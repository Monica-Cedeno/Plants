const searchForm = document.getElementById('searchForm')

searchForm.addEventListener('submit',(e) => {
    e.preventDefault();
    const result= document.getElementById('displayResults');
    attemptOne=document.querySelector('ul')
    const testing=document.getElementById("searchBar")
    // const plants = await loadPlants();
    loadPlants().then(plants => displayPlants(plants.data))
});

function plantClickHandler (evt){

    let filter = (evt.target.innerHTML);
    


};

function displayPlants (plants){

    Unordered = document.querySelector('ul')
    Unordered.innerHTML=''

    let i = 0;

    for (let p of plants){

        // console.log(p.attributes.name);
        i = i + 1;
        Unordered.innerHTML+=(`<li id=${i}>${p.attributes.name}</li>`)
        let results = document.getElementById(`${i}`);
    };

    i = 0;

    for (let p of plants){
        i = i + 1;
        let results = document.getElementById(`${i}`);
        results.addEventListener("click", plantClickHandler);
        console.log(results)
    };
};

const loadPlants = async () => {
    const testing=document.getElementById("searchBar")
    const newItem = (testing.value)
    const res = await fetch(`https://openfarm.cc/api/v1/crops/?filter=${newItem}`);
    allCrops = await res.json();
    return allCrops
};



