import { useEffect, useState } from "react";
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Test from './components/Test'



import Cardgame from './components/GameCard'

import ProfileCard from './components/ProfileCard'
import GameCard from "./components/GameCard";
import GameList from "./components/GameList";



function App() {
  const [profile, setProfile] = useState(null)
  const [games, setGames] = useState(null)

  useEffect(() => {
      fetch("http://localhost:5000/steam/profile")

      .then((res) => {
      if (!res.ok) throw new Error("HTTP error");
        return res.json();
      })

      .then(
        (data) => {
          setProfile(data); 
        })

      .catch((err) => {
          console.error("erreur lors du fetch.")
      });
  }, [])

  useEffect(() => {
    fetch("http://localhost:5000/steam/games")

    .then((res) => {
    if (!res.ok) throw new Error("HTTP error");
      return res.json();
    })

    .then(
      (data) => {
        setGames(data)
      })

    .catch((err) => {
        console.error("erreur lors du fetch.")
    });
  }, []);

  return (
    <>
      <ProfileCard profile={profile}/> 
      <GameList games={games}/>
    </>
  )
}

export default App
