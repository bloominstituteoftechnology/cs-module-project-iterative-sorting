let myFirstPromise = new Promise((resolve, reject) => {
    // We call resolve(...) when what we were doing asynchronously was successful, and reject(...) when it failed.
    // In this example, we use setTimeout(...) to simulate async code.
    // In reality, you will probably be using something like XHR or an HTML5 API.
    setTimeout( function() {
      resolve("Success!")  // Yay! Everything went well!
    }, 250)
  })
  
  myFirstPromise.then((successMessage) => {
    // successMessage is whatever we passed in the resolve(...) function above.
    // It doesn't have to be a string, but if it is only a succeed message, it probably will be.
    console.log("Yay! " + successMessage)
  });

const getData = new Promise((resolve, reject) => {
    setTimeout(function() {
        resolve({data: 2, picture: 3})
    },250)
})

getData.then(data => {
    data.data = 56
    return data
}).then(data => {
    data['news'] = 9
    console.log({data})
})

const getData2 = async()  => {
    try{
        console.log('in getData2')
        let result = await(getData)
        console.log('22222',result)
    }catch(err){
        return err
    }
}

getData2()