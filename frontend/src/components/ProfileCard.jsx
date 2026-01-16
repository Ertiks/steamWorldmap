import "./profileCard.css";

export default function ProfileCard( {profile} ){
    
    if (profile == null) return <p>Loading...</p>

    return (
        <article className="profile-card">
            <h3> {profile.name}</h3>
            <img className="profile-picture"
                    src={profile.avatarfull}
                    alt="profil icon"
            />
        </article>
    )
}