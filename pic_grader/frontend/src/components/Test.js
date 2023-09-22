import Grid from "@mui/material/Grid"
import React, { useState } from 'react';

export default function Test() {

    const [ct,setCt] = useState(1);

    const dod1 = () => {
        setCt(ct+1);
    }


  return (
    <div>
        <div className='text'>
            {ct}
        </div>
        
        <button onClick={dod1}>
            Dodaj 1
        </button>
    </div>
  )
  
}
