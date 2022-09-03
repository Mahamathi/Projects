var msg1=document.querySelector("#msg1");
var msg2=document.querySelector("#msg2");
var msg3=document.querySelector("#msg3");
var msg4=document.querySelector("#msg4");
var no_of_guesses= 0;
var guessed_num=[];

function play(){
    var result= Math.floor(Math.random() * 10) -1;
    var user_guess = document.querySelector("#guess").value ;
    if(user_guess <1 || user_guess > 10){
        alert("Enter the number between 1 - 10")
    }else{
        guessed_num.push(user_guess);
        no_of_guesses=no_of_guesses + 1;
        if(user_guess < result){
        msg1.innerHTML="Your guess is low!!";
        msg2.innerHTML="Number of Guesses " + no_of_guesses;
        msg3.innerHTML="Guessed numbers are " + guessed_num;
        msg4.innerHTML="The Correct answer is " +result;
        }
        else if(user_guess > result){
            msg1.innerHTML="Your guess is high!!";
            msg2.innerHTML="Number of Guesses " + no_of_guesses;
            msg3.innerHTML="Guessed numbers are " + guessed_num;
            msg4.innerHTML="The Correct answer is " +result;
        }
        else if(user_guess == result){
            msg1.innerHTML="Your Won!!";
            msg2.innerHTML="The number is " + result;
            msg3.innerHTML=" You Guessed " + no_of_guesses + " guesses";
            
        }
    } 
}