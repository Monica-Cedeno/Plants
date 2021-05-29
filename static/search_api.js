const searchForm = document.getElementById('searchForm');

searchForm.addEventListener('submit',(e) => {
    e.preventDefault();
    const result= document.getElementById('displayResults');
    const attemptOne=document.querySelector('ul');
    const testing=document.getElementById("searchBar");
    // const plants = await loadPlants();
    loadPlants().then(plants => displayPlants(plants));
});

async function plantClickHandler (evt){

    let plant= (evt.target.innerHTML);
    // console.log(plant);
    // console.log(evt.target.children[0])
    hiddenDiv = (evt.target.children[0])
    hiddenDiv.toggleAttribute("hidden")

}

function displayPlants (plants){

    Unordered = document.querySelector('ul');
    Unordered.innerHTML='';

    let i = 0;

    for (let p of plants.data){

        // console.log(p.attributes.name);
        i = i + 1;
        Unordered.innerHTML+=(`<li id=${i}>${p.attributes.name}<div hidden>${p.attributes.binomial_name}</div></li>`);
        let results = document.getElementById(`${i}`);
    }

    i = 0;

    for (let p of plants.data){
        i = i + 1;
        let results = document.getElementById(`${i}`);
        results.addEventListener("click", plantClickHandler);
        console.log(results);
    }
}

const loadPlants = async () => {
    const testing=document.getElementById("searchBar");
    const newItem = (testing.value);
    const res = await fetch(`https://openfarm.cc/api/v1/crops/?filter=${newItem}`);
    allCrops = await res.json();
    console.log(allCrops);
    return allCrops;
};



