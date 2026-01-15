import { useEffect, useState } from "react";

export default function Test(){

    const [message, setMessage] = useState("")

    useEffect(() => {
        fetch("http://localhost:5000/games")
        
        .then((res) => res.text()) //on transforme en text
        .then((data) => setMessage(data)) //on récupère la data et on l'affiche

        .catch((err) => {
            console.error("erreur lors du fetch.")
            setMessage("Erreur de connexion")
        });
    }, []);


    return (
        <div>

            message récupéré du backend : <br />
            {message}

        </div>
    )
}