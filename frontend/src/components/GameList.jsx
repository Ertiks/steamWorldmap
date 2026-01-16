import GameCard from "./GameCard"

export default function GameList({ games }){

    if (games == null){
        return <p>Loading games ...</p>
    }

    return (
        <div>

            {games.map((game) => (
                <GameCard game = {game} />
            ))}
        </div>
    )
}