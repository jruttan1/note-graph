import Note from '../components/Note.jsx'

const note = {
    title: "My first note",                                                                                                              
    content: "This is some content"                                                                                                      
  }   

function Notes() {

    return (
    <Note title={note.title} content={note.content}/>
    )

}

export default Notes
