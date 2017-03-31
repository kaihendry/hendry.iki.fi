const feedparser = require('feedparser-promised')

const name = process.argv[2]
const url = process.argv[3]

feedparser.parse(url).then((items) => {
  console.log(`<div id=${name}><ul>`)
  switch (name) {
    case 'youtube':
      console.log('<a href="https://www.youtube.com/user/kaihendry?sub_confirmation=1"><h2>Tech channel</h2></a>')
      break
    case 'youtube2':
      console.log('<a href="https://www.youtube.com/channel/UCE5Au4LfcBHxTQR_yLbncrQ?sub_confirmation=1"><h2>Non-tech channel</h2></a>')
      break
    default:
  }
  items.forEach((item) => {
    // console.log(item)
    console.log(`<li><a href=${item.link}>${item.title}</a></li>`)
  })
  console.log('</ul></div>')
}).catch((error) => {
  console.log('error: ', error)
})
