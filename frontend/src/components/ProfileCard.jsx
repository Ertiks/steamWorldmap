import { useEffect, useState } from "react";
import "./profileCard.css";

export default function ProfileCard(){

    const [message, setMessage] = useState("")

    useEffect(() => {
        fetch("http://localhost:5000/steam/profile")

        .then((res) => res.json())
        .then((data) => setMessage(data))

        .catch((err) => {
            console.error("erreur lors du fetch.")
            setMessage("Erreur de connexion")
        });
    })


    return (
        <article className="profile-card">
            <h3> {message.name}</h3>
            <img className="profile-picture"
                    src={message.avatar}
                    alt="profil icon"
            />
        </article>
    )
}