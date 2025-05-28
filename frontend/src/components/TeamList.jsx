import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';

export default function TeamList() {
    const [teams, setTeams] = useState([]);

    useEffect(() => {
        fetch('/api/teams/')
            .then((res) => res.json())
            .then((data) => setTeams(data));
    }, []);

    return (
        <>
            <header>
                <h1>Team Management</h1>
            </header>

            <div className="container">
                <Link to="/teams/new" className="add-btn">
                    Add New Team
                </Link>
                <ul>
                    {teams.length > 0 ? (
                        teams.map((team) => (
                            <li key={team.id}>
                                <Link to={`/teams/${team.id}`}>
                                    {team.team_name}
                                </Link>
                            </li>
                        ))
                    ) : (
                        <li className="no-teams">No teams available.</li>
                    )}
                </ul>
            </div>
        </>
    );
}
