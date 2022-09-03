function Time(){
    var date = new Date();
    var hour =date.getHours();
    var min = date.getMinutes();
    var sec= date.getSeconds();
    var period="AM";
    if(hour==0){
        hour=12;
    }
    if(hour<12){
        period="AM";

    }
    if(hour>12){
        hour=hour-12;
        period="PM"
    }
    if(hour<10){
        hour="0" + hour;
    }
    if(min<10){
        min="0" + min;
    }
    if(sec<10){
        sec="0" + sec;
    }
    var time= date.toLocaleTimeString();
    document.getElementById("display").innerHTML=time;
    document.getElementById("box").innerHTML=date;
    setTimeout(Time,1000); //it is used for refreshing the "Time"function for every one second, so we are using setTimeout()
}

Time();