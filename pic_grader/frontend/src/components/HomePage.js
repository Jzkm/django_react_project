import React, { Component } from 'react'
import Grid from "@mui/material/Grid"
import { useNavigate } from "react-router-dom";
import { responsiveFontSizes } from '@mui/material';
import sec from "secrets.json"


export default function HomePage() {
  
  const navigate = useNavigate();

    const handleclick = () => {
      fetch("/api/get_two_random_codes", {
        headers: {
            'X-API-Key': sec.SECRET_KEY  
        }
    }).then((response) => 
        response.json()
      ).then( (data) => {
        navigate(`/PicGrader/${data}`)
      }
      )
    }

    return (
      <div className='git-home'>
         {/* <h1 className='home-text'>
            This is a home page
        </h1>  */}
        <Grid container spacing={1}>
          <Grid item xs={12} align = "center"> 
            <h1 className='text'>Welcome to PicGrader</h1>
          </Grid>
          <Grid item xs={12} align = "center"> 
            <button className='start-button' onClick={handleclick}>
              START!
            </button>
          </Grid>
          

        </Grid>
      </div>
    )
  }

