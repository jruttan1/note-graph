import { Maximize2 } from 'lucide-react'

function ExpandButton({onExpandClick}) { // destructure function prop


    return ( 
        <button className = 'expandContent' onClick = {onExpandClick}> {/* pass function from note as onclick */}
            <Maximize2/>
        </button>
    )
 
}

export default ExpandButton