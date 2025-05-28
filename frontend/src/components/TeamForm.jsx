import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';

export default function TeamForm() {
    const { id } = useParams();
    const navigate = useNavigate();
    const isEdit = Boolean(id);

    const [team, setTeam] = useState({ team_name: '', city: '', stadium: '' });

    useEffect(() => {
        if (isEdit) {
            fetch(`/api/teams/${id}/`)
                .then((res) => res.json())
                .then((data) => setTeam(data));
        }
    }, [id, isEdit]);

    const handleChange = (e) => {
        setTeam({ ...team, [e.target.name]: e.target.value });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        fetch(`/api/teams/${isEdit ? `${id}/` : ''}`, {
            method: isEdit ? 'PUT' : 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(team),
        }).then((res) => res.ok && navigate('/'));
    };

    const handleDelete = () => {
        fetch(`/api/teams/${id}/`, {
            method: 'DELETE',
        }).then(() => navigate('/'));
    };

    return (
        <>
            <header>
                <h1>{isEdit ? 'Edit' : 'Add'} Team</h1>
            </header>
            <div className="container">
                <form onSubmit={handleSubmit}>
                    <label htmlFor="team_name">
                        Team Name:
                        <input
                            type="text"
                            id="team_name"
                            name="team_name"
                            value={team.team_name}
                            onChange={handleChange}
                            required
                        />
                    </label>

                    <label htmlFor="city">
                        City:
                        <input
                            type="text"
                            id="city"
                            name="city"
                            value={team.city}
                            onChange={handleChange}
                            required
                        />
                    </label>

                    <label htmlFor="stadium">
                        Stadium:
                        <input
                            type="text"
                            id="stadium"
                            name="stadium"
                            value={team.stadium}
                            onChange={handleChange}
                            required
                        />
                    </label>

                    <button type="submit">
                        {isEdit ? 'Save Changes' : 'Add Team'}
                    </button>
                </form>

                {isEdit && (
                    <button
                        type="button"
                        className="delete-btn"
                        onClick={handleDelete}
                    >
                        Delete Team
                    </button>
                )}

                <div className="back-btn">
                    <a href="/">Back to Team List</a>
                </div>
            </div>
        </>
    );
}
