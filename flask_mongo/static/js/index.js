const tabBtns = document.querySelectorAll('.btn-tab') //?
const tabContent = document.querySelectorAll('.tab-content') //?
const regex = /tab-\d/i;


tabBtns.forEach(item => { 
    item.addEventListener('click', event => {
        event.preventDefault()
        tabBtns.forEach(tabs => {tabs.classList.remove('active')})
        tabContent.forEach(content => content.classList.remove('isActive'))

        event.target.classList.add('active')    
        const el = String(event.target.classList).match(regex)[0] 
        document.getElementById(el).classList.add('isActive')
    })
})
