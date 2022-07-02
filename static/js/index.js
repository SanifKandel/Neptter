//SIDEBAR
const menuItems = document.querySelectorAll('.menu-item');


//remove active
const changeActiveItem =() => {
    menuItems.forEach(item => {
        item.classList.remove('active');
    })
}

//Notifications Popup erase

menuItems.forEach(item =>{
    item.addEventListener('click', ()=>{
        changeActiveItem();
        item.classList.add('active');
        if(item.id != 'notifications'){
            document.querySelector(' .notifications-popup').
            style.display = 'none';
        } else {
            document.querySelector(' .notifications-popup').
            style.display = 'block';
            document.querySelector('#notifications .notification-count').
            style.display = 'none';

        }
    })
})

//---------------------DARK_THEME--------------------
var root = document.querySelector(':root');
var button = document.getElementById('theme');
var text = document.getElementById('mode');
const icon = document.querySelector(' .uil-moon');


let lightColorLightness;
let whiteColorLightness;
let darkColorLightness;

//change background color 

const changeBG= () => {
    root.style.setProperty('--light-color-lightness', lightColorLightness);
    root.style.setProperty('--white-color-lightness', whiteColorLightness);
    root.style.setProperty('--dark-color-lightness', darkColorLightness);
}

// button.addEventListener('click', ()=>{
//     // function darkmode{
//     if (icon.classList.contains('uil-moon')){
//     darkColorLightness='95%';
//     whiteColorLightness='0%';
//     lightColorLightness= '10%';
//     icon.classList.remove('uil-moon');
//     icon.classList.add('uil-sun');
//     mode.innerHTML='Light Mode';
//     localStorage.setItem("mode", "Light Mode");
    
//     changeBG();
//     }
//     else{
//     darkColorLightness='17%';
//     whiteColorLightness='95%';
//     lightColorLightness= '100%';
//     icon.classList.remove('uil-sun');
//     icon.classList.add('uil-moon');
//     mode.innerHTML='Dark Mode';
//     localStorage.setItem("mode", "Dark Mode");
    
//     changeBG();
//     }  
// });


//We're going to use "check" to get the ckeckbox element
const check =document.getElementById("theme")

//If darkMode doesn’t exist in the LocalStorage, create it. False by default
if (localStorage.getItem('darkMode')===null){
    localStorage.setItem('darkMode', "true");
}

//checkStatus is only called one time in the program, when you reload the page
//It gives the page it's default look, depening on waht darkMode is set to

button.addEventListener('click', ()=>{  
    if (localStorage.getItem('darkMode')=="true"){
        // checked = true;                                       //the checkbox is checked (if you load the page by default it isn’t)
       Dark();
        
    }else{
        // checked = false;
        White();

    }
});

function Dark (){                                   //This function gets called every time the checkbox is clicked
    // localStorage.getItem('darkMode')==="true"             //if darkMode was active and this function is called it means the user now wants light
        localStorage.setItem('darkMode', "false");                  //so we set it to false, to indicate we are in light mode
        darkColorLightness='95%';
        whiteColorLightness='0%';
        lightColorLightness= '10%';
        icon.classList.remove('uil-moon');
        icon.classList.add('uil-sun');
        mode.innerHTML='Light Mode';
        changeBG();
    } 
    
function White(){
        localStorage.setItem('darkMode', "true");                   //same code but adapted for dark theme
        darkColorLightness='17%';
        whiteColorLightness='100%';
        lightColorLightness= '95%';
        icon.classList.remove('uil-sun');
        icon.classList.add('uil-moon');
        mode.innerHTML='Dark Mode';
        changeBG();
    }




// function darkmode(){
//     darkColorLightness='95%';
//     whiteColorLightness='0%';
//     lightColorLightness= '10%';
//     icon.classList.remove('uil-moon');
//     icon.classList.add('uil-sun');
//     mode.innerHTML='Light Mode';
//     localStorage.setItem("mode", "light");
    
//     changeBG();
// }
// function lightmode(){
//     darkColorLightness='17%';
//     whiteColorLightness='95%';
//     lightColorLightness= '100%';
//     icon.classList.remove('uil-sun');
//     icon.classList.add('uil-moon');
//     mode.innerHTML='Dark Mode';
//     localStorage.setItem("mode", "dark");
//     changeBG();
// }

// if(localStorage.getItem("mode")=="dark")
//     darkmode();
// else
//     nodark();

// $('#theme').change(function(){   

//     if ($(this).prop('checked'))
//     {
//     darkmode();
//     }
//     else
//     {
//     nodark();
//     }

// });


// Search feature of post

const feeds = document.querySelector(' .feeds');
const feed = document.querySelectorAll(' .feed');
const postsearch = document.querySelector('#post-searchbar');
 
const searchpost =()=>{
    const val = postsearch.value.toLowerCase();

    console.log(val);
    feed.forEach((post) => {
        let name = post.textContent;
        if(name.toLowerCase().includes(val.toLowerCase())){
            post.style.display ='block';
        }
        else{
            post.style.display = 'none';
        }
    })
}

postsearch.addEventListener('keyup', searchpost);





//Profile Update Frontend

const section = document.querySelector(".profile-main"),
      hireBtn = document.querySelector(".profile-details .buttons");
      cancelBtn = document.querySelectorAll("#close");
      

hireBtn.addEventListener("click", ()=>{
    section.classList.add("active");
})
cancelBtn.forEach(cBtn => {
    cBtn.addEventListener("click", () =>{
        section.classList.remove("active");
    })
});
console.log(cancelBtn);





const id = document.getElementById('postid');
const like = document.getElementById('like');

like.addEventListener("click", ()=>{
// $(document).on("click",function(e){
    // e.preventDefault();

    $.ajax({
        type: "GET",
        url:'/likepost',
        data:{
            post_id: id
        },
        
        success:function(){

    }

    });

});
