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
        console.log("p = ", p);
        // console.log(`p.relationships.companions.links.related = ${p.relationships.companions.links.related}`)
        Unordered.innerHTML+=(`<li id=${i}> <form action="/favourite_plant" method="POST">${p.attributes.name}<div hidden>${p.attributes.binomial_name} <input type=hidden name="plant_id" value=${p.id}/><input type=hidden name="name" value=${p.attributes.name}/><input type="submit"/> </div></form></li>`);
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
    // console.log(allCrops);
    return allCrops;
};



