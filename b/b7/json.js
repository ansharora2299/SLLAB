document.getElementById("car1").addEventListener("mouseover",func1);
document.getElementById("car2").addEventListener("mouseover",func2);
document.getElementById("car3").addEventListener("mouseover",func3);
function func1()
{
var myobj1,i,x="",y="";
document.getElementById("menutable").removeAttribute('hidden');
myobj1={
"name":"ferrari",
"ingredients":["NAME:ABC","MODEL:123","PRICE:1234567"]
};
y=myobj1.name;
for(i in myobj1.ingredients){
 x+=myobj1.ingredients[i]+"&nbsp";
 }
 document.getElementById("item1").innerHTML=y;
  document.getElementById("item2").innerHTML=x;
  }
function func2()
{
var myobj1,i,x="",y="";
document.getElementById("menutable").removeAttribute('hidden');
myobj1={
"name":"fbmw",
"ingredients":["NAME:xyz","MODEL:456","PRICE:123456789"]
};
y=myobj1.name;
for(i in myobj1.ingredients){
 x+=myobj1.ingredients[i]+"&nbsp";
 }
 document.getElementById("item1").innerHTML=y;
 document.getElementById("item2").innerHTML=x;
  }
function func3()
{
var myobj1,i,x="",y="";
document.getElementById("menutable").removeAttribute('hidden');
myobj1={
"name":"porche",
"ingredients":["NAME:pqr","MODEL:123456","PRICE:1234567905"]
};
y=myobj1.name;
for(i in myobj1.ingredients){
 x+=myobj1.ingredients[i]+"&nbsp";
 }
 document.getElementById("item1").innerHTML=y;
 document.getElementById("item2").innerHTML=x;
  }