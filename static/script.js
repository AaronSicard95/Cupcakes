$list = $('#cakeList').get(0)
$form = $('#cakeForm').get(0)

async function getCakes(){
    let cakes = await axios.get('/api/cupcakes');
    $list.innerhtml = "";
    for (let cake of cakes.data['cakes']){
        $newli = $(`<li>${'Kill Me LMAO'}${cake.flavor} ${cake.rating} ${cake.size}</li>`);
        console.log($newli.get(0));
        $list.append($newli.get(0));
    }
    return cakes.data['cakes'];
}

$form.addEventListener('submit', async function(evt){
    evt.preventDefault();
    let newCake = await axios.post('/api/cupcakes', new FormData($form));
    await getCakes();
    return newCake;
})

getCakes()