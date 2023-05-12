// animate items on scroll====================
const cards = document.querySelectorAll('.animate');
const callback = (elements) => {
    elements.forEach(ele => {
        if(ele.isIntersecting  && !ele.target.classList.contains('show')){
            ele.target.classList.add('show');
        }else{
            ele.target.classList.remove('show');
        }
    });
}
const observer = new IntersectionObserver(callback);
cards.forEach(card => observer.observe(card));


// // scroll the quicklinks to the left and right using the buttons
function leftScroll() {
    const left = document.querySelector(".job-section > .quick-links > .quick-links-container");
    left.scrollBy(200, 0);
}
function rightScroll() {
    const right = document.querySelector(".job-section > .quick-links > .quick-links-container ");
    right.scrollBy(-200, 0);
}

let userJobLocationDescription = document.querySelector("input[name='job_location']:checked").value;
let jobLocationDisplay = document.querySelector('.location');

console.log(userJobLocationDescription);

userJobLocationDescription.onchange = () => {
        if (userJobLocationDescription == 'remote'){
            jobLocationDisplay.style.display = 'none';
            console.log('display = block');
        } else if (userJobLocationDescription == 'fulltime'){
            jobLocationDisplay.style.display = 'flex';
            console.log('display = flex');
        }
};

// form step in the admin dashboard and in the register page

// const nextButton = document.querySelector(".btn-next");
// const prevButton = document.querySelector(".btn-prev");
// const steps = document.querySelectorAll(".step");
// const form_steps = document.querySelectorAll(".form-step");

// let active = 1;
// nextButton.addEventListener("click", () => {
//     active++;
//     if(active > steps.length){
//         active = steps.length;
//     }
//     updateProgress();
// });

// prevButton.addEventListener("click", () => {
//     active--;
//     if(active < 1){
//         active = 1;
//     }
//     updateProgress();
// });

// const updateProgress = () =>{
//     console.log("steps.length =>" + steps.length);
//     console.log("active => " + active);

//     // toggle active class for each item

//     steps.forEach((step, i) => {
//         if (i == (active-1)) {
//             step.classList.add('active');
//             form_steps[i].classList.add('active');
//             console.log('i =>' + i);
//         } else{
//             step.classList.remove("active");
//             form_steps[i].classList.remove('active')
//         }
//     });
    
//     //enable to disable prev and next button
//     if (active === 1){
//         prevButton.disabled = true;
//     } else if (active === steps.length) {
//         nextButton.disabled = true;
//     } else{
//         prevButton.disabled = false;
//         nextButton.disabled = false;
//     }
// };


//tags input and output======================================
//====================================================================

// const ul = document.querySelector(".content ul");
// const tagInput = ul.querySelector("input");
// const countNumb = document.querySelector(".details span");
// const removeBtn = document.querySelector(".details button");

// let tags = [];
// let maxTags = 10;

// countTag();

// function countTag(){
//   tagInput.focus();
//   countNumb.innerText = maxTags - tags.length; // subtracting max tag from tag length
// };

// function createTag(){
//   //removing all li tags so there will be no duplicate tags
//   ul.querySelectorAll('li').forEach(li => li.remove());
//   tags.slice().reverse().forEach(tag => {
//     let liTag = `<li>${tag}<i class="ri-close-line" title="Remove tag" onclick= "remove(this, '${tag}')"></i></li>`;
//     ul.insertAdjacentHTML("afterbegin", liTag); // inserting or adding li inside ul tag
//   });
//   countTag();
// };

// function remove(element, tag){
//   let index = tags.indexOf(tag);  // getting removing tag index
//   tags = [...tags.slice(0, index), ...tags.slice(index + 1)]; //removing  or excluding selected tag from a array
//   element.parentElement.remove(); //removing li of removed tag
//   countTag();
// };

// function addTag(e){
//   if(e.key == "Enter"){
//     let tag = e.target.value.replace(/\s+/g, " "); //removing unwanted space from user tag
//     if(tag.length > 1 && !tags.includes(tag)){  //if tag is greater than 1 and doesn't exist
//       if (tags.length < 10){
//             tag.split(",").forEach(tag =>{    //splitting tag form comma
//                   tags.push(tag); //adding each tag inside array
//                   createTag();
//             });
//       }
//     }
//     e.target.value = "";
//   }
// };

// tagInput.addEventListener("keyup", addTag);

// removeBtn.addEventListener("click", () => {
//   tags.length = 0; //making array empty
//   ul.querySelectorAll('li').forEach(li => li.remove());
//   countTag();
// });


// Trending job slider srcipt ===========================================
//========================================================================

// const container = document.querySelector('.trending-jobs-container');
// const jobs = document.querySelector('.trending-inner');

// // keep track of user's mouse up and down
// let isPressedDown = false;
// // x horizontal space of cursor from inner container
// let cursorXspace;

// container.addEventListener('mousedown', (e) => { 
//     isPressedDown = true;
//     cursorXspace = e.offsetX - jobs.offsetLeft;
//     container.style.cursor = 'grabbing';
// });

// container.addEventListener('mouseup', () => {
//     container.style.cursor = 'grab';
// });

// window.addEventListener('mouseup', () => {
//     isPressedDown = false;
// });

// container.addEventListener('mousemove', (e) => {
//     if(!isPressedDown) return;
//     e.preventDefault();
//     jobs.style.left = `${e.offsetX - cursorXspace}px`;
//     boundCards();
// });

// function boundCards(){
//     const container_rect = container.getBoundingClientRect();
//     const jobs_rect = jobs.getBoundingClientRect();

//     if (parseInt(jobs.style.left) > 0) {
//             jobs.style.left = 0;
//     } else if (jobs_rect.right < container_rect.right) {
//             jobs.style.left = `-${jobs_rect.width - container_rect.width}px`;
//     }
// }