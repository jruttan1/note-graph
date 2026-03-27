import './Note.css'
import { useState } from 'react'
import ExpandButton from './ExpandButton'

function Note({title, content}) { // passing in a notes title and content

    const [isExpanded, setIsExpanded] = useState(false) // initialize state for preview vs full content

    function onExpandClick() { // function to manage state
        setIsExpanded(!isExpanded)
        
    }

    return (
        <div className = 'noteCard'>
            <div className = 'header'>
                {title}
            </div>
            <div className = 'content'>
                {isExpanded ? content : content.slice(0, 100)}
            </div>
            <ExpandButton onExpandClick = {onExpandClick}/> {/*uses the expand button component by passing the state function in as a prop*/}
        </div>
    )
}

export default Note