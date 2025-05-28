import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';

export default function TeamDetail() {
    const { id } = useParams();
    const [team, setTeam] = useState(null);

    useEffect(() => {
        fetch(`/api/teams/${id}/`)
            .then((res) => res.json())
            .then((data) => setTeam(data));
    }, [id]);

    if (!team) return <p>Loading...</p>;

    return (
        <>
            <header>
                <h1>{team.team_name}</h1>
            </header>
            <div className="container">
                <div className="team-info">
                    <p>
                        <strong>Team:</strong> {team.team_name}
                    </p>
                    <p>
                        <strong>City:</strong> {team.city}
                    </p>
                    <p>
                        <strong>Stadium:</strong> {team.stadium}
                    </p>
                </div>
                <div className="actions">
                    <Link to={`/teams/${team.id}/edit`} className="action-btn">
                        Edit Team
                    </Link>
                    <Link to="/" className="action-btn back-btn">
                        Back to Team List
                    </Link>
                </div>
            </div>
        </>
    );
}
