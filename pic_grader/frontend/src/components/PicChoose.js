import React, {useState, Component,useEffect } from 'react'
import Grid from "@mui/material/Grid"
import { useLocation, useParams,useNavigate } from "react-router-dom";
import sec from "secrets.json"

export default function PicChoose() {
  const { ppCodes } = useParams();
  let [image1,setImage1] = useState(null);
  let [image2, setImage2] = useState(null);

  const code = [ppCodes.substring(0,6),ppCodes.substring(6,12)];

  const navigate = useNavigate();
  const [count, setCount] = useState(0);

  const randomcos = () => {
    return Math.random()*1000000000+""
  };

  const getimage = (ktory) => {
    fetch("/api/get_person" + "?pcode=" + code[ktory], {
      headers: {
          'X-API-Key': sec.SECRET_KEY  
      }
  })
    .then((response) => 
        response.json()
      ).then( (data) => {
        if(ktory == 0){
          // alert(data.picture+`?dummy=${randomcos()}`)
          setImage1(data.picture+`?dummy=${randomcos()}`)

        }
        else{
          setImage2(data.picture+`?dummy=${randomcos()}xd`)
        }
      })
  }

  const handleclick = (ktory) => {
    fetch("/api/get_person" + "?pcode=" + code[ktory], {
      headers: {
          'X-API-Key': sec.SECRET_KEY
      }
  })
    .then((response) => response.json())
    .then( (data) => {
        //alert(`Wybrales laskę o kodzie: ${data.code}`)
        let ktory2 = 0
        if(ktory == 0)
          ktory2 = 1
        
        


        fetch("/api/get_person" + "?pcode=" + code[ktory2], {
          headers: {
              'X-API-Key': sec.SECRET_KEY
          }
      })
        .then((response2) => response2.json())
        .then( (data2) => {
          fetch('/api/get_token', {
            method: 'GET',
            headers: {
              'Content-Type': 'application/json',
              'X-API-Key': sec.SECRET_KEY
            },
          })
          .then((response5) => response5.json())
          .then((data5) => {
          const csrfToken = data5.csrf_token;
          // alert(data.code)
          const requestOptions = {
            method: "POST",
            headers: {
               "Content-Type": "application/json",
               'X-CSRFToken': csrfToken,
               'X-API-Key': sec.SECRET_KEY
              },
            body: JSON.stringify({
              code: data.code,
              enymycode: data2.code,
              rank: data.rank,
              enymyrank: data2.rank,
            }),
          };
          //tutaj
          fetch("/api/update_rating",requestOptions)
          .then((response3) => response3.json())
          .then((data3) => {
            // pisz tu kod teraz
            fetch("/api/get_two_random_codes", {
              headers: {
                  'X-API-Key': sec.SECRET_KEY
              }
          })
            .then((response4) => response4.json())
            .then( (data4) => {
              
              navigate(`/PicGrader/${data4}`)
              setCount(count+1)
              
            })
            // .then(() =>{
            //   getimage(0)
            // })
            // .then(() =>{
            //   getimage(1)
            // })

          })
        })
        })
      })
    }
  
  // alert("xd")

  // useEffect(() => {
  //   getimage(0)
  //   getimage(1)
  // }, [])

  useEffect(() => {
    getimage(0)
    getimage(1)
  }, [location.pathname]);
  // getimage(0)
  // getimage(1)
  

  return (
    <div className='git-picgrader'>
      <div className='block1'>
        <Grid container spacing={1}>
          <Grid item xs={12} align = "center"> 
            <h1 className='text'>Kto Ci się bardziej podoba?</h1>
          </Grid>
          <Grid item xs={6} align = "center"> 
            <img src={image1} className='pic-box-1'/>
          </Grid> 
          <Grid item xs={6} align = "center"> 
            <img src={image2} className='pic-box-2'/>
          </Grid>
        </Grid>

      </div>
      <div className='block2'>

        <button className='st-button' onClick={() => handleclick(0)}>Laska 1</button>

        <button className='nd-button' onClick={() => handleclick(1)}>Walęga</button>

      </div>

      </div>
  )
  
}
