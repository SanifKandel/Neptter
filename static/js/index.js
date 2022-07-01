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

button.addEventListener('click', ()=>{
    // function darkmode{
    if (icon.classList.contains('uil-moon')){
    darkColorLightness='95%';
    whiteColorLightness='0%';
    lightColorLightness= '10%';
    icon.classList.remove('uil-moon');
    icon.classList.add('uil-sun');
    mode.innerHTML='Light Mode';
    localStorage.setItem("mode", "Light Mode");
    
    changeBG();
    }
    else{
    darkColorLightness='17%';
    whiteColorLightness='95%';
    lightColorLightness= '100%';
    icon.classList.remove('uil-sun');
    icon.classList.add('uil-moon');
    mode.innerHTML='Dark Mode';
    localStorage.setItem("mode", "Dark Mode");
    
    changeBG();
    }  
});




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


//Display Image URL
var url = document.getElementById('imageurl');

function getImage (imagename){
    $.url.html(imagename);
}

//Toggle Image URL

function menuToggle(){
    const toggleMenu = document.querySelector('.menu');
    toggleMenu.classList.toggle('active');
}



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


