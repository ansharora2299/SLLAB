function double()
{
var x;
x=document.getElementById("num").value;
if(x=="")
{
	alert("can't be empty")
}
else if(isNaN(x)){
document.getElementById("res").innerHTML='not valid data type';
}
else{
	document.getElementById("res").innerHTML=2*x;
}}
function square()
{
var x;
x=document.getElementById("num").value;
if(x=="")
{
	alert("can't be empty")
}
else if(isNaN(x)){
document.getElementById("res").innerHTML='not valid data type';
}
else{
	document.getElementById("res").innerHTML=x*x;
}
}
