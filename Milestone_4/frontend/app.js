async function runWorkflow(){

let topic=document.getElementById("topic").value

resetSteps()

let response=await fetch(

"http://127.0.0.1:8000/workflow?topic="+topic,

{method:"POST"}

)

let data=await response.json()

activate("research")

setTimeout(()=>activate("analysis"),500)

setTimeout(()=>activate("summary"),1000)

setTimeout(()=>activate("email"),1500)

setTimeout(()=>activate("evaluation"),2000)

document.getElementById("summaryText")
.innerText=data.summary

document.getElementById("emailText")
.innerText=data.email

document.getElementById("metrics")
.innerText=

JSON.stringify(data.metrics,null,2)

}

function activate(id){

document.getElementById(id)
.classList.add("active")

}

function resetSteps(){

let steps=["research","analysis","summary","email","evaluation"]

steps.forEach(s=>{

document.getElementById(s)
.classList.remove("active")

})

}