import Note from '../components/Note.jsx'

const note = {
    title: "My first note",                                                                                                              
    content: "This is some content rfonrevfkwjer viwrkjt vwkjrt vwkrjt vkjrefv;kjrt vwk;rjt v;krjt vw;kjrt v;kjrt v;krjt vb;3krtj v;krjtg vw;kedf nv;wkrgj v;kwjrt vk;wjrfgv;kwjrt v;kwjrt vk;wjrtv"                                                                                                      
  }   

function Notes() {

    return (
    <Note title={note.title} content={note.content}/>
    )

}

export default Notes
