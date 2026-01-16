import { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Test from './components/Test'



import Cardgame from './components/GameCard'

import ProfileCard from './components/ProfileCard'



function App() {
  const [profile, setProfile] = useState(null)

  useEffect(() => {
      fetch("http://localhost:5000/steam/profile")

      .then((res) => {
      if (!res.ok) throw new Error("HTTP error");
        return res.json();
      })

      .then(
        (data) => {
          console.log(data.name)
          setProfile(data); 
        })

      .catch((err) => {
          console.error("erreur lors du fetch.")
          setMessage("Erreur de connexion")
      });
  }, [])

  return (
    <>
      <ProfileCard profile={profile}/> 
    </>
  )
}

export default App
