//CSRFTOKEN

function getToken(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
    }
    const csrftoken = getToken('csrftoken');



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


const check =document.getElementById("theme")


if (localStorage.getItem('darkMode')===null){
    localStorage.setItem('darkMode', "true");
}


button.addEventListener('click', ()=>{  
    if (localStorage.getItem('darkMode')=="true"){
        // checked = true;                                       
       Dark();
        
    }else{
        // checked = false;
        White();

    }
});

function Dark (){                                            
        localStorage.setItem('darkMode', "false");                  
        darkColorLightness='95%';
        whiteColorLightness='0%';
        lightColorLightness= '10%';
        icon.classList.remove('uil-moon');
        icon.classList.add('uil-sun');
        mode.innerHTML='Light Mode';
        changeBG();
    } 
    
function White(){
        localStorage.setItem('darkMode', "true");                  
        darkColorLightness='17%';
        whiteColorLightness='100%';
        lightColorLightness= '95%';
        icon.classList.remove('uil-sun');
        icon.classList.add('uil-moon');
        mode.innerHTML='Dark Mode';
        changeBG();
    }



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

const section = document.querySelector(".profile-main");
const  hireBtn = document.querySelector(".buttons");
      cancelBtn = document.querySelectorAll("#close");
      

hireBtn.addEventListener("click", ()=>{
    section.classList.add("active");
});

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


//Display Image
const middle = document.querySelector(".middle");
const wrapper = middle.querySelector(".lower-part");

const img = wrapper.querySelector("img");
var cancelBtnn = wrapper.querySelector(".cancel");
const defaultbtn = document.querySelector("#imageupload");

function defaultBtnActive(){
    defaultbtn.click();
}


defaultbtn.addEventListener("change", function(){
    console.log("hii");

    const file = this.files[0];
    console.log(file);

    if(file){
      const reader = new FileReader();
      reader.onload = function(){
        const result = reader.result;
        img.src = result;
        console.log(result);
        wrapper.classList.add("active");
      }

     cancelBtnn.addEventListener("click", function(){
     img.src = "";
     wrapper.classList.remove("active");
      })
      reader.readAsDataURL(file);

    }
      });
   

  
