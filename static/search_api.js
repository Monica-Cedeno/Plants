const searchForm = document.getElementById('searchForm');

searchForm.addEventListener('submit',(e) => {
    e.preventDefault();

    loadPlants().then(plants => displayPlants(plants));

});

///AllCrops is now called plants 

async function plantClickHandler (evt){

    let plant= (evt.target.innerHTML);
    // console.log(plant);
    // console.log(evt.target.children[0])
    hiddenDiv = (evt.target.children[0])
    hiddenDiv.toggleAttribute("hidden")

}

async function displayPlants (plants){

    Unordered = document.querySelector('#target');
    Unordered.innerHTML='';

    console.log(plants);

    let promises = [];

    for (let p of plants.data){
        //we have p, we do the fetch request
        //the response promise is the result of doing the fetch
        let responsePromise = fetch(`https://openfarm.cc/${p.links.self.api}`);
        //the parsedJsonPromise is the result of calling .json() on the response received from responsePromise
        let parsedJsonPromise = responsePromise.then(result => result.json());
        promises.push(parsedJsonPromise);
    }

    const parsedResults = await Promise.all(promises);

    const crops = {};

    const cropPhotos = {};

    const cropCompanions = {};

    for (let data of parsedResults){

        companion_ids = [];

        for (let companion of data.data.relationships.companions.data){
            let c = companion.id;
            companion_ids.push(c);
        };

        cropCompanions[data.data.id] = companion_ids



        for (let obj of data.included){
            if (obj.type === "crops"){
                crops[obj.id] = obj;
            }
            else if (obj.type === "crops-pictures"){
                cropPhotos[data.data.id] = obj.attributes.image_url
            }
        }
    }

    let i = 0;

    let newHtml= ''

    for (let p of plants.data){
        console.log (p.id)


        i = i + 1;

        const x = []

        for (let companionId of cropCompanions[p.id]){
            x.push(crops[companionId]['attributes']['name'])
        }

        if (cropPhotos[p.id]){   
            newHtml += (`<li id=${i}><img src=${cropPhotos[p.id]} height=200px width=200px><form action="/favourite_plant" method="POST">${p.attributes.name}<div hidden>${x} <input type=hidden name="plant_id" value=${p.id} /><input type=hidden name="name" value="${p.attributes.name}" /><input type="submit" /></div></form></li>`);
        }

        let results = document.getElementById(`${i}`);

    }

    Unordered.innerHTML = newHtml

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
