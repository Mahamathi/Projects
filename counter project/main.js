const counter=document.querySelector('#counter')
const btns=document.querySelectorAll('.btn')
console.log(btns);

//initialize the count=0
 let count=0;

 btns.forEach((btn)=>{
     btn.addEventListener('click',(e)=>{
         const styles=e.currentTarget.classList
         if(styles.contains('increase')){
             count++
         }else if(styles.contains('decrease')){
             count--
         }else{
             count=0
         }

         if(count>0){
             counter.style.color="green"
             
         }

         if(count<0){
             counter.style.color="red"
         }
         if(count==0){
             counter.style.color="gray"
         }
         counter.textContent=count
     })
 })