const searchForm = document.getElementById('searchForm');

searchForm.addEventListener('submit',(e) => {
    e.preventDefault();
    const result= document.getElementById('displayResults');
    const attemptOne=document.querySelector('ul');
    const testing=document.getElementById("searchBar");
    loadPlants().then(plants => displayPlants(plants));
});

async function plantClickHandler (evt){

    let plant= (evt.target.innerHTML);
    // console.log(plant);
    // console.log(evt.target.children[0])
    hiddenDiv = (evt.target.children[0])
    hiddenDiv.toggleAttribute("hidden")

}

async function displayPlants (plants){

    Unordered = document.querySelector('ul');
    Unordered.innerHTML='';

    console.log(plants);

    for (let p of plants.data){
    
        r = await fetch(`https://openfarm.cc/${p.links.self.api}`)
        data = await r.json()
        // console.log(data)
        companion_ids = []

        for (let companion of data.data.relationships.companions.data){
            // console.log (companion);
            let c = companion.id
            companion_ids.push(c)
        };
        // console.log(companion_ids)

        const crops = {}

        for (let obj of data.included){
            if (obj.type === "crops"){
                crops[obj.id] = obj;
            }
        }

        for ( let id of companion_ids){
            // console.log (crops[id]['attributes']['name']);
        }
    }

    let i = 0;

    //add an array, append all p plants to array, call array in <li>

    for (let p of plants.data){

        i = i + 1;
        // console.log("p = ", p);
        const x = await findCompanions(p.id)
        // console.log(x)
        Unordered.innerHTML+=(`<li id=${i}> <form action="/favourite_plant" method="POST">${p.attributes.name}<div hidden>${x} <input type=hidden name="plant_id" value=${p.id} /><input type=hidden name="name" value="${p.attributes.name}" /><input type="submit" /></div></form></li>`);
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

async function findCompanions(id){
    r = await fetch(`https://openfarm.cc/api/v1/crops/${id}`)
    data = await r.json()
    console.log(data)
    companion_ids = []

    for (let companion of data.data.relationships.companions.data){
        let c = companion.id
        companion_ids.push(c)
    }

    const crops = {}

    for (let obj of data.included){
        if (obj.type === "crops"){
            crops[obj.id] = obj;
        }
    }

    let retrieved_ids = []

    for ( let id of companion_ids){
        console.log (crops[id]['attributes']['name']);
        retrieved_ids.push((crops[id]['attributes']['name']))
    }
    console.log(retrieved_ids)
    return retrieved_ids
}

const loadPlants = async () => {
    const testing=document.getElementById("searchBar");
    const newItem = (testing.value);
    const res = await fetch(`https://openfarm.cc/api/v1/crops/?filter=${newItem}`);
    allCrops = await res.json();
    // console.log(allCrops);
    return allCrops;
};

